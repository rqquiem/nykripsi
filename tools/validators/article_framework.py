"""Validator kerangka artikel (abstrak + kepala bagian) untuk artikel KYT.

Menegakkan aturan berbasis korpus Sinta (docs/abstrak-framework.md,
docs/bab1-framework.md, docs/conversion-skripsi-to-article.md) pada
``content/artikel/artikel-kyt.md``:
  1. abstrak dwibahasa 150-250 kata dengan lima komponen (latar belakang ->
     tujuan -> metode -> hasil -> simpulan) dan 3-6 kata kunci;
  2. himpunan + urutan kepala bagian kanonik (enam tag ``kamus:h``);
  3. formula tujuan kanonik ``Penelitian ini bertujuan untuk``;
  4. tidak ada penanda ``TODO`` yang tersisa.
"""

import re

from .base import Context, Finding, read, register

ARTICLE = "content/artikel/artikel-kyt.md"
HEADING_IDS = ("pendahuluan", "metode", "hasil", "simpulan", "ucapan", "pustaka")
TAG_RE = re.compile(r"<!-- kamus:h id=([a-z0-9_]+) -->")
TODO_RE = re.compile(r"<!--\s*TODO")
ABSTRACT_RE = re.compile(r'::: \{custom-style="Abstract"\}(.*?)\n:::', re.DOTALL)
KEYWORD_RE = re.compile(r"\*\*(?:Kata Kunci|Keywords):\*\*\s*(.*)")
LABEL_RE = re.compile(r"^\s*\*\*(?:Abstrak|Abstract)\*\*\s*[—-]\s*", re.MULTILINE)
OBJECTIVE = "Penelitian ini bertujuan untuk"
AB_MIN, AB_MAX = 150, 250
KW_MIN, KW_MAX = 3, 6
COMPONENT_CUES = (
    ("latar belakang", re.compile(r"pasar eropa|industri helm", re.IGNORECASE)),
    ("tujuan", re.compile(r"bertujuan untuk", re.IGNORECASE)),
    ("metode", re.compile(r"menggunakan pendekatan|studi kasus|analisis dokumen", re.IGNORECASE)),
    ("hasil", re.compile(r"hasil penelitian menunjukkan bahwa", re.IGNORECASE)),
    ("simpulan", re.compile(r"dapat disimpulkan|dengan demikian", re.IGNORECASE)),
)

def _abstract_words(block: str) -> int:
    text = KEYWORD_RE.sub("", block)
    text = LABEL_RE.sub("", text)
    return len(text.split())

def _keywords(block: str) -> list[str]:
    m = KEYWORD_RE.search(block)
    if not m:
        return []
    return [k.strip() for k in m.group(1).split(",") if k.strip()]

@register("article_framework", "content/artikel/artikel-kyt.md (abstrak + kepala bagian)")
def run(ctx: Context) -> list[Finding]:
    findings: list[Finding] = []
    text = read(ARTICLE)
    if text is None:
        return [Finding("warn", f"{ARTICLE} belum ada")]

    ids = tuple(TAG_RE.findall(text))
    if ids != HEADING_IDS:
        findings.append(Finding("fail", f"kepala bagian tidak sesuai/urutan salah: {list(ids)}"))

    todos = len(TODO_RE.findall(text))
    if todos:
        findings.append(Finding("fail", f"{todos} penanda TODO tersisa di {ARTICLE}"))

    if OBJECTIVE not in text:
        findings.append(Finding("fail", f"formula tujuan '{OBJECTIVE} ...' tidak ditemukan"))

    blocks = ABSTRACT_RE.findall(text)
    if len(blocks) < 2:
        findings.append(Finding("fail", f"abstrak dwibahasa (ID + EN) tidak lengkap ({len(blocks)} blok)"))
    for i, block in enumerate(blocks):
        n = _abstract_words(block)
        if not (AB_MIN <= n <= AB_MAX):
            findings.append(Finding("fail", f"abstrak #{i + 1} {n} kata (harus {AB_MIN}-{AB_MAX})"))
        kws = _keywords(block)
        if not (KW_MIN <= len(kws) <= KW_MAX):
            findings.append(Finding("fail", f"abstrak #{i + 1} punya {len(kws)} kata kunci (harus {KW_MIN}-{KW_MAX})"))
    if blocks:
        for name, cue in COMPONENT_CUES:
            if not cue.search(blocks[0]):
                findings.append(Finding("fail", f"komponen abstrak '{name}' tidak terdeteksi"))

    if not any(f.level == "fail" for f in findings):
        findings.append(Finding("ok", f"artikel KYT patuh kerangka: {len(blocks)} abstrak, {len(ids)} kepala bagian"))
    return findings
