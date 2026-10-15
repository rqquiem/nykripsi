"""Validator kebaruan bukti (ER1-ER3): sumber bukti <= 5 tahun & dalam periode sasaran."""
import glob, os, re
import yaml
from .base import Context, Finding, read, register

KAMUS = "assets/bahasa/kamus-id.yaml"
BIB = "assets/refs.bib"
ARTIKEL_META = "templates/artikel-*-meta.yaml"
ARTIKEL_GLOB = "content/artikel/*.md"
EN_GLOB = "content/artikel-en/*.md"
KANAL = ("Berita", "Siaran pers", "Artikel", "Web")
CITE_RE = re.compile(r"\[@([A-Za-z0-9_:\-]+)")
NOTE_RE = re.compile(r"note\s*=\s*\{([^}]*)\}")
YEAR_RE = re.compile(r"year\s*=\s*\{?\s*(\d{4})")
PERIODE_RE = re.compile(r"(\d{4})\s*[–\-]\s*(\d{4})")


def _bib_blocks() -> list[tuple[str, str]]:
    """Kembalikan ``(key, block)`` tiap entri bib (blok kurung seimbang).

    Pindai kurung seimbang yang sama seperti ``tools/validators/papers.py``.
    """
    text = read(BIB) or ""
    entry_re = re.compile(r"^@(\w+)\{([^,]+),", re.MULTILINE)
    blocks: list[tuple[str, str]] = []
    for m in entry_re.finditer(text):
        key = m.group(2).strip()
        start = text.index("{", m.start())
        depth = 0
        i = start
        while i < len(text):
            if text[i] == "{":
                depth += 1
            elif text[i] == "}":
                depth -= 1
                if depth == 0:
                    break
            i += 1
        blocks.append((key, text[start : i + 1]))
    return blocks


def _kanal(note: str) -> str | None:
    """Kanal pertama yang muncul pada ``note`` (urut KANAL), else ``None``."""
    for token in KANAL:
        if token in note:
            return token
    return None


def _meta_path(rel: str) -> str:
    """Petakan ``content/artikel*/artikel-X.md`` -> ``templates/artikel-X-meta.yaml``."""
    stem = os.path.basename(rel)[:-3] if rel.endswith(".md") else os.path.basename(rel)
    return f"templates/{stem}-meta.yaml"


@register("evidence_recency", "content/artikel*/** + assets/refs.bib + templates/artikel-*-meta.yaml")
def run(ctx: Context) -> list[Finding]:
    findings: list[Finding] = []

    # --- Konfigurasi kebaruan dari kamus ---
    kamus = yaml.safe_load(read(KAMUS) or "") or {}
    recency = kamus.get("recency", {}) or {}
    max_tahun = int(recency.get("max_tahun", 5))
    periode_default = recency.get("periode_default", "2020–2025")

    # --- Basis data bib: {key: {"year": int|None, "kanal": str|None}} ---
    bib: dict[str, dict] = {}
    for key, block in _bib_blocks():
        note_m = NOTE_RE.search(block)
        kanal = _kanal(note_m.group(1)) if note_m else None
        year_m = YEAR_RE.search(block)
        year = int(year_m.group(1)) if year_m else None
        bib[key] = {"year": year, "kanal": kanal}

    paths = sorted(glob.glob(os.path.join(ctx.root, ARTIKEL_GLOB))) \
        + sorted(glob.glob(os.path.join(ctx.root, EN_GLOB)))

    for path in paths:
        rel = os.path.relpath(path, ctx.root)
        meta_rel = _meta_path(rel)
        meta = yaml.safe_load(read(meta_rel) or "") or {}
        periode = meta.get("periode") or periode_default
        pm = PERIODE_RE.search(str(periode))
        if not pm:
            findings.append(Finding("warn", f"{rel}: periode '{periode}' tidak dapat diurai; lewati"))
            continue
        start, end = int(pm.group(1)), int(pm.group(2))
        lo = max(start, end - max_tahun)

        with open(path, encoding="utf-8") as fh:
            text = fh.read()

        art_evidence = False
        seen: set[str] = set()
        for key in CITE_RE.findall(text):
            if key in seen or key not in bib:
                continue
            seen.add(key)
            entry = bib[key]
            if entry["kanal"] is None:
                continue  # entri beasiswa (scholarship), bukan bukti
            art_evidence = True
            # ER2: entri bukti tanpa tahun yang dapat diurai.
            if entry["year"] is None:
                findings.append(Finding("fail", f"{rel}: ER2: bukti [@{key}] tanpa tahun"))
                continue
            # ER1: tahun bukti harus di dalam jendela [lo, end].
            year = entry["year"]
            if not (lo <= year <= end):
                findings.append(Finding(
                    "fail", f"{rel}: ER1: bukti [@{key}] tahun {year} di luar jendela {lo}–{end}"))

        # ER3: artikel tanpa sumber bukti (beasiswa saja) tetap lulus (no-op).
        if not art_evidence:
            findings.append(Finding("ok", f"{rel}: ER3: tidak ada sumber bukti (artikel beasiswa)"))

    if not any(f.level == "fail" for f in findings):
        findings.append(Finding(
            "ok", f"kebaruan bukti patuh ER1-ER3 (jendela {max_tahun} tahun; periode {periode_default})"))
    return findings
