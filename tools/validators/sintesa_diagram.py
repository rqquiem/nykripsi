"""Validator diagram sintesa teori (kerangka TS1-TS6).

Menegakkan docs/sintesa-diagram-framework.md pada blok berkode berkelas
``sintesa`` di ``content/artikel/*.md`` + ``content/skripsi/1[0-5]-*.md``
(level fail) dan ``content/drafts/*.md`` (level warn):
  TS1 blok sintesa ber-YAML sah (mapping dengan kunci wajib);
  TS2 >= 2 teori, tiap teori punya nama + peran;
  TS3 lensa.nama + lensa.gabungan >= 2 yang menunjuk teori yang ada;
  TS4 lintas_tahap (bila ada) punya nama + peran, tidak tumpang-tindih gabungan;
  TS5 tahap >= 2 entri unik;
  TS6 nama lensa disebut di prosa berkas yang sama (di luar fence).
"""

import glob
import os
import re

import yaml

from .base import Context, Finding, register

FINAL_GLOBS = ("content/artikel/*.md", "content/skripsi/1[0-5]-*.md")
DRAFT_GLOBS = ("content/drafts/*.md",)
SINTESA_OPEN_RE = re.compile(r"^```\{\.sintesa\b([^}]*)\}")

def _blok_sintesa(lines: list[str]):
    """Hasilkan (baris_buka, baris_tutup, body) tiap blok sintesa."""
    i = 0
    while i < len(lines):
        if SINTESA_OPEN_RE.match(lines[i].strip()):
            j = i + 1
            while j < len(lines) and lines[j].strip() != "```":
                j += 1
            yield i, j, "\n".join(lines[i + 1:j])
            i = j + 1
        else:
            i += 1

def _periksa(path: str, rel: str, level: str, findings: list[Finding]) -> bool:
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().splitlines()
    blocks = list(_blok_sintesa(lines))
    if not blocks:
        return False
    diuji = True

    def tambah(msg: str) -> None:
        findings.append(Finding(level, f"{rel}: {msg}"))

    tertutup = set()
    for buka, tutup, body in blocks:
        tertutup.update(range(buka, tutup + 1))
        try:
            spec = yaml.safe_load(body)
        except yaml.YAMLError as exc:
            tambah(f"sintesa TS1: YAML tidak sah (baris {buka + 1}): {exc}")
            continue
        if not isinstance(spec, dict):
            tambah(f"sintesa TS1: badan bukan mapping (baris {buka + 1})")
            continue

        teori = spec.get("teori")
        if not isinstance(teori, list) or len(teori) < 2:
            tambah("sintesa TS2: 'teori' harus list >= 2")
            teori = []
        nama_teori = []
        for t in teori:
            if not isinstance(t, dict) or not str(t.get("nama", "")).strip() \
                    or not str(t.get("peran", "")).strip():
                tambah("sintesa TS2: setiap teori butuh 'nama' dan 'peran'")
            else:
                nama_teori.append(str(t["nama"]).strip())

        lensa = spec.get("lensa")
        gabungan: list[str] = []
        if not isinstance(lensa, dict) or not str(lensa.get("nama", "")).strip():
            tambah("sintesa TS3: 'lensa.nama' wajib")
            lensa = {}
        else:
            raw = lensa.get("gabungan")
            if not isinstance(raw, list) or len(raw) < 2:
                tambah("sintesa TS3: 'lensa.gabungan' harus list >= 2")
            else:
                for g in raw:
                    if str(g).strip() not in nama_teori:
                        tambah(f"sintesa TS3: gabungan '{g}' tidak ada di teori")
                    else:
                        gabungan.append(str(g).strip())

        lintas = spec.get("lintas_tahap") or []
        if not isinstance(lintas, list):
            tambah("sintesa TS4: 'lintas_tahap' harus list")
            lintas = []
        for l in lintas:
            if not isinstance(l, dict) or not str(l.get("nama", "")).strip() \
                    or not str(l.get("peran", "")).strip():
                tambah("sintesa TS4: setiap lintas_tahap butuh 'nama' dan 'peran'")
            elif str(l["nama"]).strip() in gabungan:
                tambah(f"sintesa TS4: '{l['nama']}' tumpang-tindih dengan gabungan")

        tahap = spec.get("tahap")
        if not isinstance(tahap, list) or len(tahap) < 2:
            tambah("sintesa TS5: 'tahap' harus list >= 2")
        elif len({str(s).strip() for s in tahap}) != len(tahap):
            tambah("sintesa TS5: 'tahap' memuat entri duplikat")

        nama_lensa = str(lensa.get("nama", "")).strip()
        if nama_lensa:
            prosa = "\n".join(ln for k, ln in enumerate(lines) if k not in tertutup)
            if nama_lensa not in prosa:
                tambah(f"sintesa TS6: nama lensa '{nama_lensa}' tidak disebut di prosa")
    return diuji

@register("sintesa_diagram", "content/{artikel,skripsi}/** + content/drafts (diagram sintesa teori)")
def run(ctx: Context) -> list[Finding]:
    findings: list[Finding] = []
    diperiksa = 0
    for g in FINAL_GLOBS:
        for path in sorted(glob.glob(os.path.join(ctx.root, g))):
            rel = os.path.relpath(path, ctx.root)
            _periksa(path, rel, "fail", findings)
            diperiksa += 1
    for g in DRAFT_GLOBS:
        for path in sorted(glob.glob(os.path.join(ctx.root, g))):
            rel = os.path.relpath(path, ctx.root)
            _periksa(path, rel, "warn", findings)
    if not any(f.level == "fail" for f in findings):
        findings.append(Finding(
            "ok", f"diagram sintesa patuh kerangka TS1-TS6 pada {diperiksa} berkas final"))
    return findings
