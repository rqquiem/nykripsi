"""Validator kerangka BAB I / Pendahuluan (docs/bab1-framework.md; A1-A8/B1-B3).

Menegakkan aturan berbasis korpus (docs/bab1-framework.md,
docs/bab1-corpus-stats.md) pada content/skripsi/10-bab-01-pendahuluan.md:
  A1 lima subbagian dengan urutan tetap;
  A2 lima baris formula bertag `kamus:f` dengan id tetap;
  A3 Latar Belakang dengan pita panjang dan ambang sitasi;
  A4 Rumusan Masalah = pertanyaan bernomor;
  A5 Batasan Masalah menyebut lima batas;
  A6 Tujuan = butir bernomor yang memetakan 1:1 ke Rumusan Masalah;
  A7 Manfaat memuat bagian teoretis dan praktis;
  B2 formula tujuan kanonik `Penelitian ini bertujuan untuk`.
Angka pita dibaca dari assets/bahasa/kamus-id.yaml §bab1 (fallback bawaan).
"""

import os
import re

from .base import Context, Finding, read, register

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

BAB1 = "content/skripsi/10-bab-01-pendahuluan.md"
KAMUS = "assets/bahasa/kamus-id.yaml"

DEFAULT = {
    "subbagian": ["Latar Belakang", "Rumusan Masalah", "Batasan Masalah", "Tujuan", "Manfaat"],
    "formula_tag": ["latar_belakang", "rumusan_masalah", "batasan_masalah", "tujuan", "manfaat"],
    "latar_belakang_panjang": [700, 1300],
    "latar_belakang_sitasi_min": 15,
    "batasan_lima": ["waktu", "objek", "kerangka", "data", "pengecualian"],
    "manfaat": ["teoretis", "praktis"],
}

BATAS_POLA = {
    "waktu": r"20\d{2}|rentang waktu|periode|tahun",
    "objek": r"objek|diplomasi",
    "kerangka": r"kerangka|soft power|nation branding|analisis kebijakan",
    "data": r"sumber data|dokumen|publikasi|pemberitaan|data",
    "pengecualian": r"tidak menjadi fokus|di luar|dikecualikan|tidak dimaksudkan|kecuali",
}

OBJECTIVE = "Penelitian ini bertujuan untuk"
H2_RE = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)
TAG_F_RE = re.compile(r"<!-- kamus:f id=([a-z0-9_]+) -->")
CITE_RE = re.compile(r"\[@[^\]]+\]")
NUM_RE = re.compile(r"^\s*\d+\.\s+\S", re.MULTILINE)
COMMENT_RE = re.compile(r"<!--.*?-->")


def _kamus(ctx: Context) -> dict:
    if yaml is None:
        return {}
    path = os.path.join(ctx.root, KAMUS)
    try:
        with open(path, encoding="utf-8") as fh:
            return (yaml.safe_load(fh) or {}).get("bab1", {}) or {}
    except OSError:
        return {}


def _sections(text: str) -> dict[str, str]:
    parts = H2_RE.split(text)
    out: dict[str, str] = {}
    for i in range(1, len(parts) - 1, 2):
        out[parts[i].strip()] = parts[i + 1]
    return out


def _words(text: str) -> int:
    return len(COMMENT_RE.sub(" ", text).split())


@register("bab1_framework", "content/skripsi/10-bab-01-pendahuluan.md (A1-A8/B1-B3)")
def run(ctx: Context) -> list[Finding]:
    findings: list[Finding] = []
    text = read(BAB1)
    if text is None:
        return [Finding("warn", f"{BAB1} belum ada")]
    d = {**DEFAULT, **_kamus(ctx)}

    order = tuple(H2_RE.findall(text))
    want = tuple(d["subbagian"])
    if order != want:
        findings.append(Finding("fail", f"A1: subbagian BAB I tidak sesuai/urutan salah: {list(order)}"))

    tags = tuple(TAG_F_RE.findall(text))
    if tags != tuple(d["formula_tag"]):
        findings.append(Finding("fail", f"A2: tag kamus:f tidak sesuai/urutan salah: {list(tags)}"))

    secs = _sections(text)

    lb = secs.get("Latar Belakang", "")
    lo, hi = d["latar_belakang_panjang"]
    n = _words(lb)
    if not (lo <= n <= hi):
        findings.append(Finding("fail", f"A3: Latar Belakang {n} kata (harus {lo}-{hi})"))
    nc = len(CITE_RE.findall(lb))
    if nc < d["latar_belakang_sitasi_min"]:
        findings.append(Finding("fail", f"A3: Latar Belakang {nc} sitasi (min {d['latar_belakang_sitasi_min']})"))

    rm = len(NUM_RE.findall(secs.get("Rumusan Masalah", "")))
    if rm < 2:
        findings.append(Finding("fail", f"A4: Rumusan Masalah punya {rm} butir bernomor (min 2)"))

    bt = secs.get("Batasan Masalah", "").lower()
    missing = [k for k in d["batasan_lima"] if not re.search(BATAS_POLA.get(k, re.escape(k)), bt)]
    if missing:
        findings.append(Finding("fail", f"A5: Batasan Masalah tidak menyebut: {', '.join(missing)}"))

    tj = len(NUM_RE.findall(secs.get("Tujuan", "")))
    if tj < 2 or tj != rm:
        findings.append(Finding("fail", f"A6: Tujuan {tj} butir tidak 1:1 dengan Rumusan Masalah {rm}"))

    mf = secs.get("Manfaat", "").lower()
    miss = [k for k in d["manfaat"] if k not in mf]
    if miss:
        findings.append(Finding("fail", f"A7: Manfaat tidak memuat bagian: {', '.join(miss)}"))

    if OBJECTIVE not in text:
        findings.append(Finding("fail", f"B2: formula tujuan '{OBJECTIVE} ...' tidak ditemukan"))

    if not any(f.level == "fail" for f in findings):
        findings.append(Finding("ok", f"BAB I patuh kerangka A1-A8/B1-B3 ({n} kata Latar Belakang, {nc} sitasi, {rm} rumusan masalah)"))
    return findings
