"""Kerangka bersama untuk validator alur kerja Nykripsi v2.

Stdlib saja. Setiap validator mendaftar lewat ``@register(name, subject)`` dan
mengembalikan ``list[Finding]`` dengan level ``ok``/``warn``/``fail``.
"""

import os
import re
import shutil
import subprocess
from typing import Callable, NamedTuple

# Akar repositori: tools/validators/base.py -> tools/validators -> tools -> root.
REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

UA = "Mozilla/5.0 (X11; Linux x86_64)"

# Prefiks DOI contoh/placeholder. ``10.1234`` adalah prefiks placeholder yang
# dipakai oleh ``assets/refs.bib``, sehingga dilewati saat daring (menjaga
# ``make check`` tetap hijau).
EXAMPLE_DOI_PREFIXES = ("10.1234", "10.5555", "10.0000")

AGENT_PROMPT = """Baca ulang subjek berikut dan periksa setiap klaim.

SUBJEK:
{subject}

KLAIM:
{claims}

Untuk SETIAP klaim, keluarkan TEPAT dua baris dan tidak ada yang lain:
VERDICT <id> CONFIRMED|REFUTED|UNCLEAR
EVIDENCE <id> <kutipan>
"""


class Finding(NamedTuple):
    level: str  # salah satu dari "ok", "warn", "fail"
    message: str


# Registry: nama -> (subjek, callable). Dict biasa sudah terurut (insertion order).
VALIDATORS: dict[str, tuple[str, Callable[["Context"], list[Finding]]]] = {}


def register(name: str, subject: str):
    """Dekorator: daftarkan validator ``fn`` dengan ``name`` dan ``subject``."""

    def deco(fn: Callable[["Context"], list[Finding]]):
        VALIDATORS[name] = (subject, fn)
        return fn

    return deco


def read(rel: str) -> str | None:
    """Baca berkas relatif-akar repo sebagai utf-8; ``None`` bila tidak ada."""
    path = rel if os.path.isabs(rel) else os.path.join(REPO, rel)
    try:
        with open(path, encoding="utf-8") as fh:
            return fh.read()
    except (OSError, UnicodeDecodeError):
        return None


def exists(rel: str) -> bool:
    """True bila berkas relatif-akar repo ada."""
    path = rel if os.path.isabs(rel) else os.path.join(REPO, rel)
    return os.path.exists(path)


def sh(cmd: list[str]) -> tuple[int, str]:
    """Jalankan ``cmd``; kembalikan ``(returncode, stdout+stderr)``."""
    try:
        proc = subprocess.run(cmd, text=True, capture_output=True)
    except FileNotFoundError:
        return 127, ""
    return proc.returncode, (proc.stdout or "") + (proc.stderr or "")


def run_agent(prompt: str) -> str | None:
    """Panggil CLI ``claude``; ``None`` bila CLI tidak ada atau gagal."""
    if shutil.which("claude") is None:
        return None
    try:
        proc = subprocess.run(
            ["claude", "-p", "--output-format", "text"],
            input=prompt,
            text=True,
            capture_output=True,
            timeout=180,
        )
    except (subprocess.TimeoutExpired, OSError):
        return None
    if proc.returncode != 0:
        return None
    return proc.stdout


_VERDICT_RE = re.compile(r"^VERDICT (\S+) (CONFIRMED|REFUTED|UNCLEAR)$", re.MULTILINE)


def parse_verdicts(text: str) -> dict[str, str]:
    """Petakan ``id -> verdict`` dari baris ``VERDICT <id> <VERDICT>``."""
    return {m.group(1): m.group(2) for m in _VERDICT_RE.finditer(text)}


class Context:
    """Konteks eksekusi yang dibagikan ke setiap validator."""

    def __init__(self, root: str, offline: bool = False, agent: bool = False):
        self.root = root
        self.offline = offline
        self.agent = agent

    def agent_review(self, name: str, claims: list[str], subject: str) -> list[Finding]:
        if not self.agent:
            return []
        ids = {f"c{i}": c for i, c in enumerate(claims, start=1)}
        listing = "\n".join(f"{cid}: {txt}" for cid, txt in ids.items())
        prompt = AGENT_PROMPT.format(claims=listing, subject=subject)
        out = run_agent(prompt)
        if out is None:
            return [Finding("fail", f"GAGAL: {name}: agen tidak dapat dihubungi")]
        verdicts = parse_verdicts(out)
        findings: list[Finding] = []
        for cid in ids:
            verdict = verdicts.get(cid)
            if verdict == "REFUTED":
                findings.append(Finding("fail", f"GAGAL: {name}: klaim {cid} dibantah agen"))
            elif verdict == "UNCLEAR":
                findings.append(Finding("warn", f"PERINGATAN: {name}: klaim {cid} tidak jelas bagi agen"))
            elif verdict == "CONFIRMED":
                findings.append(Finding("ok", f"OK: {name}: klaim {cid} dikonfirmasi agen"))
        return findings
