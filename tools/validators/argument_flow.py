"""Validator alur argumen & kohesi paragraf untuk artikel + bab skripsi.

Menegakkan kerangka alur argumen (docs/argument-framework.md) pada
``content/artikel/*.md`` dan ``content/skripsi/1[0-5]-*.md``:
  K2 setiap transisi antarkalimat punya kaitan leksikal atau pemarkah transisi;
  K3 setiap batas paragraf punya kaitan atau pemarkah transisi;
  K4 paragraf >= 3 kalimat tidak boleh melompat topik tanpa satu pun transisi;
  K5 kepadatan paragraf (maks kalimat per paragraf, paragraf satu kalimat).
K1 (satu gagasan + kalimat topik di awal) bersifat editorial, diperkuat K4/K5.
"""

import glob
import os
import re

from .base import Context, Finding, register

GLOBS = ("content/artikel/*.md", "content/skripsi/1[0-5]-*.md")
TOKEN_RE = re.compile(r"[a-zA-Z\u00c0-\u00ff]+")
CITE_RE = re.compile(r"\[@[^\]]+\]")
PAREN_RE = re.compile(r"\([^)]*\)")
ABSTRACT_RE = re.compile(r'::: \{custom-style="Abstract"\}.*?\n:::', re.DOTALL)
SKIP_PREFIX = ("#", ":::", "|", "-", "*", "<", ">", "`", "1.", "2.", "3.", "4.", "5.")
STOPWORDS = frozenset(
    """yang dan di ke dari untuk dengan pada dalam ini itu adalah sebagai oleh akan tidak
juga dapat telah secara bahwa atau karena sehingga agar namun tetapi serta para suatu satu
dua lebih masih hanya saja sudah belum bila jika maka hal tersebut antara terhadap melalui
maupun yaitu yakni bagi pun mereka kita kami saya anda dia ia nya lah kah se per an ter ber
meng mana saat ketika adanya akan halnya tersendiri berbagai sejumlah beberapa seluruh semua
setiap orang tahun ada ialah merupakan""".split()
)
KONEKTOR = (
    "hal ini", "hal tersebut", "selain itu", "dengan demikian", "namun", "meskipun",
    "sedangkan", "karena", "sehingga", "oleh karena itu", "sementara itu", "akan tetapi",
    "berdasarkan", "adapun", "pertama", "kedua", "ketiga", "di sisi lain", "sejalan dengan",
    "yaitu", "misalnya", "sebagai contoh", "selanjutnya", "kemudian", "sebaliknya",
    "walaupun", "oleh sebab itu", "dengan kata lain", "kajian ini", "penelitian ini",
    "studi ini", "artikel ini", "tulisan ini", "temuan ini", "dengan begitu", "lebih lanjut",
    "guna", "akibatnya", "konsekuensinya", "di samping itu", "maka dari itu",
    "atas dasar tersebut", "sehubungan dengan", "dalam konteks", "pada dasarnya",
    "secara keseluruhan", "oleh karenanya",
)
MAKS_KALIMAT = 14
MAKS_TUNGGAL = 0.50
AMBANG_TRANSISI = 0.30
AMBANG_PARAGRAF = 0.25


def _bersih(text: str) -> str:
    """Buang blok abstrak, sitasi [@key], dan tanda kurung."""
    text = ABSTRACT_RE.sub("", text)
    text = CITE_RE.sub("", text)
    return PAREN_RE.sub("", text)


def _kata_isi(text: str) -> set[str]:
    return {w for w in TOKEN_RE.findall(text.lower()) if len(w) >= 4 and w not in STOPWORDS}


def _stem(w: str) -> str:
    for p in ("meng", "meny", "mem", "men", "me", "di", "ter", "ber", "pe", "per"):
        if w.startswith(p) and len(w) - len(p) >= 3:
            w = w[len(p):]
            break
    for s in ("kan", "an", "nya", "lah"):
        if w.endswith(s) and len(w) - len(s) >= 3:
            w = w[:-len(s)]
            break
    return w


def _lemma(text: str) -> set[str]:
    return {_stem(w) for w in _kata_isi(text)}


def _kalimat(paragraf: str) -> list[str]:
    return [s for s in re.split(r"(?<=[.!?])\s+", paragraf.strip()) if len(s.split()) >= 4]


def _paragraf(text: str) -> list[str]:
    out: list[str] = []
    for blk in re.split(r"\n\s*\n", _bersih(text)):
        blk = blk.strip()
        if not blk or blk.startswith(SKIP_PREFIX):
            continue
        out.append(blk)
    return out


def _konektor(kalimat: str) -> bool:
    s = kalimat.lower().lstrip()
    return any(s.startswith(c) for c in KONEKTOR)


@register("argument_flow", "content/artikel/*.md + content/skripsi/1[0-5]-*.md")
def run(ctx: Context) -> list[Finding]:
    findings: list[Finding] = []
    diperiksa = 0
    for g in GLOBS:
        for path in sorted(glob.glob(os.path.join(ctx.root, g))):
            rel = os.path.relpath(path, ctx.root)
            with open(path, encoding="utf-8") as fh:
                paragraf = _paragraf(fh.read())
            sents = [s for s in (_kalimat(p) for p in paragraf) if s]
            if not sents:
                continue
            diperiksa += 1
            trans_total = trans_gap = batas_total = batas_gap = 0
            tunggal = 0
            for s in sents:
                if len(s) == 1:
                    tunggal += 1
                if len(s) >= 3:
                    terhubung = sum(
                        1 for a, b in zip(s, s[1:])
                        if (_lemma(a) & _lemma(b)) or _konektor(b)
                    )
                    if terhubung == 0:
                        findings.append(Finding(
                            "fail", f"{rel}: paragraf melompat topik (tidak ada transisi terhubung)"))
                for a, b in zip(s, s[1:]):
                    trans_total += 1
                    if not (_lemma(a) & _lemma(b)) and not _konektor(b):
                        trans_gap += 1
            for a, b in zip(sents, sents[1:]):
                batas_total += 1
                if not (_lemma(" ".join(a)) & _lemma(" ".join(b))) and not _konektor(b[0]):
                    batas_gap += 1
            if trans_total and trans_gap / trans_total > AMBANG_TRANSISI:
                findings.append(Finding(
                    "fail", f"{rel}: {trans_gap}/{trans_total} transisi antarkalimat tanpa kaitan "
                    f"(> {AMBANG_TRANSISI:.0%})"))
            if batas_total and batas_gap / batas_total > AMBANG_PARAGRAF:
                findings.append(Finding(
                    "fail", f"{rel}: {batas_gap}/{batas_total} batas paragraf tanpa kaitan "
                    f"(> {AMBANG_PARAGRAF:.0%})"))
            for s in sents:
                if len(s) > MAKS_KALIMAT:
                    findings.append(Finding(
                        "fail", f"{rel}: paragraf {len(s)} kalimat (> {MAKS_KALIMAT})"))
                    break
            if tunggal / len(sents) > MAKS_TUNGGAL:
                findings.append(Finding(
                    "warn", f"{rel}: {tunggal}/{len(sents)} paragraf satu kalimat "
                    f"(> {MAKS_TUNGGAL:.0%})"))
    if not any(f.level == "fail" for f in findings):
        findings.append(Finding(
            "ok", f"alur argumen & kohesi paragraf patuh pada {diperiksa} berkas (K1-K5)"))
    return findings
