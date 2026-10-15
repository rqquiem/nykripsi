"""Validator kerangka artikel (abstrak + kepala bagian) — Sinta, KYT, Arai,
Datacenter, dan varian HI/IR dwibahasa (artikel-hi, artikel-hi-en).

Menegakkan aturan berbasis korpus Sinta (docs/abstrak-framework.md,
docs/bab1-framework.md, docs/article-framework.md,
docs/conversion-skripsi-to-article.md):
  1. abstrak dwibahasa 150-250 kata dengan lima komponen (latar belakang ->
     tujuan -> metode -> hasil -> simpulan) dan 3-6 kata kunci;
  2. himpunan + urutan kepala bagian kanonik (enam tag ``kamus:h``);
  3. formula tujuan kanonik ``Penelitian ini bertujuan untuk``;
  4. tidak ada penanda ``TODO`` yang tersisa.

``content/artikel/artikel-kyt.md`` dan ``content/artikel/artikel-arai.md``
diperiksa pada tingkat ``fail``;
``content/artikel/artikel-sinta.md`` (masih berscaffold) pada tingkat ``warn``
sehingga kekurangan naskah draf terlihat tanpa memblokir ``make check``.
"""

import re

from .base import Context, Finding, read, register

ARTICLE = "content/artikel/artikel-kyt.md"
ARTICLE_SINTA = "content/artikel/artikel-sinta.md"
ARTICLE_ARAI = "content/artikel/artikel-arai.md"
ARTICLE_DATACENTER = "content/artikel/artikel-datacenter.md"
HEADING_IDS_6 = ("pendahuluan", "metode", "hasil", "simpulan", "ucapan", "pustaka")
HEADING_IDS_5 = ("pendahuluan", "metode", "hasil", "simpulan", "pustaka")
OBJECTIVE_ID = "Penelitian ini bertujuan untuk"
OBJECTIVE_EN = "This study aims to"
ARTICLE_HI = "content/artikel/artikel-hi.md"
ARTICLE_HI_EN = "content/artikel-en/artikel-hi-en.md"
FILES = (
    (ARTICLE, "fail", HEADING_IDS_6, OBJECTIVE_ID),
    (ARTICLE_ARAI, "fail", HEADING_IDS_6, OBJECTIVE_ID),
    (ARTICLE_DATACENTER, "fail", HEADING_IDS_6, OBJECTIVE_ID),
    (ARTICLE_SINTA, "warn", HEADING_IDS_6, OBJECTIVE_ID),
    (ARTICLE_HI, "fail", HEADING_IDS_5, OBJECTIVE_ID),
    (ARTICLE_HI_EN, "fail", HEADING_IDS_5, OBJECTIVE_EN),
)
TAG_RE = re.compile(r"<!-- kamus:h id=([a-z0-9_]+) -->")
TODO_RE = re.compile(r"<!--\s*TODO")
ABSTRACT_RE = re.compile(r'::: \{custom-style="Abstract"[^}]*\}(.*?)\n:::', re.DOTALL)
KEYWORD_RE = re.compile(r"\*\*(?:Kata Kunci|Keywords):\*\*\s*(.*)")
LABEL_RE = re.compile(r"^\s*\*\*(?:Abstrak|Abstract)\*\*\s*[:—-]\s*", re.MULTILINE)
AB_MIN, AB_MAX = 150, 250
KW_MIN, KW_MAX = 3, 6
COMPONENT_CUES = (
    ("latar belakang", re.compile(r"industri helm|pasar eropa|diplomasi|kebijakan|citra|ekspor|impor|investasi|teknologi|pusat data|import|tariff|policy|market|consumer|brand|trade|regulation", re.IGNORECASE)),
    ("tujuan", re.compile(r"bertujuan|menganalisis|meneliti|mengkaji|this study|this article", re.IGNORECASE)),
    ("metode", re.compile(r"menggunakan|metode|pendekatan|method|kualitatif|qualitative", re.IGNORECASE)),
    ("hasil", re.compile(r"hasil penelitian|menunjukkan|findings|indicate", re.IGNORECASE)),
    ("simpulan", re.compile(r"dapat disimpulkan|simpulan|kesimpulan|conclusion|dengan demikian", re.IGNORECASE)),
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


def _scan(rel: str, text: str, level: str, heading_ids: tuple[str, ...],
          objective: str, findings: list[Finding]) -> None:
    ids = tuple(TAG_RE.findall(text))
    if ids != heading_ids:
        findings.append(Finding(level, f"{rel}: kepala bagian tidak sesuai/urutan salah: {list(ids)}"))

    todos = len(TODO_RE.findall(text))
    if todos:
        findings.append(Finding(level, f"{rel}: {todos} penanda TODO tersisa"))

    if objective not in text:
        findings.append(Finding(level, f"{rel}: formula tujuan '{objective} ...' tidak ditemukan"))

    blocks = ABSTRACT_RE.findall(text)
    if len(blocks) < 2:
        findings.append(Finding(level, f"{rel}: abstrak dwibahasa (ID + EN) tidak lengkap ({len(blocks)} blok)"))
    for i, block in enumerate(blocks):
        n = _abstract_words(block)
        if not (AB_MIN <= n <= AB_MAX):
            findings.append(Finding(level, f"{rel}: abstrak #{i + 1} {n} kata (harus {AB_MIN}-{AB_MAX})"))
        kws = _keywords(block)
        if not (KW_MIN <= len(kws) <= KW_MAX):
            findings.append(Finding(level, f"{rel}: abstrak #{i + 1} punya {len(kws)} kata kunci (harus {KW_MIN}-{KW_MAX})"))
    if blocks:
        for name, cue in COMPONENT_CUES:
            if not cue.search(blocks[0]):
                findings.append(Finding(level, f"{rel}: komponen abstrak '{name}' tidak terdeteksi"))


@register("article_framework", "content/artikel/*.md + content/artikel-en/*.md (abstrak + kepala bagian)")
def run(ctx: Context) -> list[Finding]:
    findings: list[Finding] = []
    for rel, level, heading_ids, objective in FILES:
        text = read(rel)
        if text is None:
            findings.append(Finding("warn", f"{rel} belum ada"))
            continue
        _scan(rel, text, level, heading_ids, objective, findings)
    if not any(f.level == "fail" for f in findings):
        berkas = ", ".join(rel for rel, _lvl, _h, _o in FILES)
        findings.append(Finding("ok", f"artikel patuh kerangka (fail-tier: {berkas}; sinta warn-tier)"))
    return findings
