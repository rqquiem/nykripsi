"""Validator tata letak & tipografi (kerangka LT1-LT9).

Menegakkan docs/layout-framework.md:
  LT1 tata letak skripsi (margin 2,5 cm, spasi 1,5, indent 0,5 cm, font serif,
      penomoran bab Romawi);
  LT2 tata letak artikel/jurnal (margin 2,5 cm, spasi 1,15, Times New Roman);
  LT3 istilah asing ditulis miring (*istilah*);
  LT4 singkatan dijabarkan pada penyebutan pertama: SINGKATAN (Kepanjangan);
  LT5 setiap singkatan terpakai terdaftar di DAFTAR SINGKATAN;
  LT6 tata letak Sinta terpusat (filter sinta_layout.lua, anchor preamble,
      target artikel Makefile terpasang);
  LT7 bahasa dokumen (kamus bahasa.utama, filter bilingual.lua terpasang,
      abstrak artikel ber-atribut lang=id/lang=en);
  LT8 larangan em dash + hyphen berspasi di prosa (dan penindasan hyphenation
      otomatis di kedua preamble);
  LT9 istilah teknis Indonesia wajib berglos Inggris pada penyebutan prosa
      pertama: "istilah (english gloss)".
Berkas final (content/artikel/*.md + content/skripsi/1[0-5]-*.md) level 'fail';
content/drafts/*.md level 'warn'.
"""

import glob
import os
import re
import zipfile

import yaml

from .base import Context, Finding, read, register

KAMUS = "assets/bahasa/kamus-id.yaml"
SKRIPSI_PREAMBLE = "templates/skripsi-preamble.tex"
ARTIKEL_PREAMBLE = "templates/artikel-preamble.tex"
REFERENCE_DOCX = "templates/journal-reference.docx"
SKRIPSI_GLOB = "content/skripsi/1[0-5]-*.md"
ARTIKEL_GLOB = "content/artikel/*.md"
DRAFT_GLOB = "content/drafts/*.md"
DAFTAR_SKRIPSI = "content/skripsi/07-daftar-singkatan.md"

SKRIPSI_ANCHORS = (
    "top=2.5cm", "bottom=2.5cm", "left=2.5cm", "right=2.5cm",
    r"\onehalfspacing", r"\setlength{\parindent}{0.5cm}",
    r"\setmainfont{Liberation Serif}",
    r"\renewcommand{\thechapter}{\Roman{chapter}}",
)
ARTIKEL_ANCHORS = ("margin=2.5cm", r"\setstretch{1.15}")

SINTA_FILTER = "tools/pandoc_filters/sinta_layout.lua"
BILINGUAL_FILTER = "tools/pandoc_filters/bilingual.lua"
ABSTRACT_LANG_RE = re.compile(r':::\s*\{custom-style="Abstract"\s+lang=(id|en)\}')
SINTA_PREAMBLE_ANCHORS = (
    r"\centering", r"\titleformat{\section}",
    r"\renewcommand{\figurename}{Gambar}", r"\renewcommand{\tablename}{Tabel}",
)
MAKEFILE = "Makefile"
ARTIKEL_TARGET_RE = re.compile(r"^artikel(-\w+)?$")

FENCE_RE = re.compile(r"^\s*```")
HEADING_RE = re.compile(r"^#{1,6}\s")
DAFTAR_RE = re.compile(r"^#{1,6}\s+Daftar Singkatan\s*$", re.IGNORECASE)
CAPTION_RE = re.compile(r"^(Tabel|Gambar)\b")
KW_RE = re.compile(r"^\*\*(Kata Kunci|Keywords)\b")
CITE_RE = re.compile(r"\[@[^\]]*\]")
CODE_RE = re.compile(r"`[^`\n]+`")
BOLD_RE = re.compile(r"\*\*[^*\n]+\*\*")
ITAL_RE = re.compile(r"\*[^*\n]+\*")
COMMENT_RE = re.compile(r"<!--.*?-->")


def _kamus(ctx: Context) -> dict:
    with open(os.path.join(ctx.root, KAMUS), encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


def _istilah(d: dict) -> list[str]:
    out = []
    for x in d.get("istilah_asing") or []:
        name = x if isinstance(x, str) else str(x.get("istilah", ""))
        if name:
            out.append(name)
    return out


def _singkatan(d: dict) -> list[dict]:
    return [x for x in (d.get("singkatan") or [])
            if isinstance(x, dict) and x.get("singkatan")]

def _teknis(d: dict) -> list[dict]:
    return [x for x in (d.get("istilah_teknis") or [])
            if isinstance(x, dict) and x.get("istilah") and x.get("inggris")]


def _kinds(lines: list[str]) -> list[str]:
    kinds: list[str] = []
    fence = div = langdiv = False
    for raw in lines:
        s = raw.strip()
        if FENCE_RE.match(raw):
            fence = not fence
            kinds.append("fence")
            continue
        if fence:
            kinds.append("fence")
            continue
        if s.startswith(":::") and "lang=" in s:
            langdiv = s != ":::"
            kinds.append("div")
            continue
        if langdiv:
            if s == ":::":
                langdiv = False
            kinds.append("div")
            continue
        if s.startswith(":::"):
            div = s != ":::"
            kinds.append("div")
            continue
        if div:
            kinds.append("div")
            continue
        if not s:
            kinds.append("blank")
        elif s.startswith("<!--"):
            kinds.append("comment")
        elif HEADING_RE.match(s):
            kinds.append("heading")
        elif s.startswith("|"):
            kinds.append("table")
        elif CAPTION_RE.match(s):
            kinds.append("caption")
        elif KW_RE.match(s):
            kinds.append("kw")
        else:
            kinds.append("prose")
    return kinds


def _mask(text: str) -> str:
    t = COMMENT_RE.sub(lambda m: " " * len(m.group()), text)
    t = CITE_RE.sub(lambda m: " " * len(m.group()), t)
    t = CODE_RE.sub(lambda m: " " * len(m.group()), t)
    t = BOLD_RE.sub(lambda m: " " * len(m.group()), t)
    return ITAL_RE.sub(lambda m: " " * len(m.group()), t)


def _re_token(tok: str) -> re.Pattern:
    return re.compile(r"(?<![A-Za-z0-9*])" + re.escape(tok) + r"(?![A-Za-z0-9*])",
                      re.IGNORECASE)


def _baca(path: str) -> list[str]:
    with open(path, encoding="utf-8") as fh:
        return fh.read().splitlines()


def _rows(rel: str, lines: list[str], kinds: list[str]) -> list[tuple]:
    return [(rel, n, line, kind)
            for n, (line, kind) in enumerate(zip(lines, kinds), 1)]


def _cek_istilah(rows: list[tuple], istilah: list[str], level: str,
                 findings: list[Finding]) -> None:
    for rel, n, line, kind in rows:
        if kind not in ("prose", "heading"):
            continue
        bersih = _mask(line)
        for term in istilah:
            if _re_token(term).search(bersih):
                findings.append(Finding(
                    level, f"{rel}:{n}: istilah asing '{term}' belum miring (*{term}*)"))


def _cek_singkatan(rows: list[tuple], singkatan: list[dict], daftar: str,
                   doc_label: str, level: str, findings: list[Finding]) -> None:
    first: dict[str, tuple] = {}
    used: set[str] = set()
    for rel, n, line, kind in rows:
        if kind not in ("prose", "heading", "table"):
            continue
        bersih = _mask(line)
        for s in singkatan:
            tok = s["singkatan"]
            if _re_token(tok).search(bersih):
                used.add(tok)
                if kind == "prose" and tok not in first:
                    first[tok] = (rel, n, line)
    for s in singkatan:
        tok = s["singkatan"]
        if tok not in first:
            continue
        rel, n, line = first[tok]
        m = _re_token(tok).search(_mask(line))
        after = line[m.end():]
        keps = [s.get("kepanjangan", "")] + list(s.get("varian") or [])
        if not any(k and re.match(r"\s*\(\s*" + re.escape(k) + r"\s*\)", after,
                                  re.IGNORECASE) for k in keps):
            findings.append(Finding(
                level, f"{rel}:{n}: singkatan '{tok}' belum dijabarkan "
                       f"(harus '{tok} (Kepanjangan)')"))
    for tok in sorted(used):
        if not re.search(r"(?<![A-Za-z0-9])" + re.escape(tok) + r"(?![A-Za-z0-9])", daftar):
            findings.append(Finding(
                level, f"{doc_label}: '{tok}' tidak terdaftar di DAFTAR SINGKATAN"))


def _cek_teknis(rows: list[tuple], teknis: list[dict], level: str,
                findings: list[Finding]) -> None:
    first: dict[str, tuple] = {}
    for rel, n, line, kind in rows:
        if kind not in ("prose", "heading"):
            continue
        bersih = _mask(line)
        for t in teknis:
            term = t["istilah"]
            if term in first:
                continue
            m = _re_token(term).search(bersih)
            if m:
                first[term] = (rel, n, line, m.end())
    for t in teknis:
        term = t["istilah"]
        if term not in first:
            continue
        rel, n, line, end = first[term]
        gloss = t["inggris"]
        pat = r"\s*\(\s*\*?" + re.escape(gloss) + r"\*?\s*\)"
        if not re.match(pat, line[end:], re.IGNORECASE):
            findings.append(Finding(
                level, f"{rel}:{n}: istilah teknis '{term}' belum berglos "
                       f"Inggris ('{gloss}')"))

def _daftar_dalam(lines: list[str], kinds: list[str]) -> str:
    out: list[str] = []
    inside = False
    for line, kind in zip(lines, kinds):
        if kind == "heading":
            if DAFTAR_RE.match(line.strip()):
                inside = True
                continue
            if inside:
                break
        if inside:
            out.append(line)
    return "\n".join(out)


@register("layout_typography", "templates/* + content/{artikel,skripsi,drafts} (LT1-LT9)")
def run(ctx: Context) -> list[Finding]:
    findings: list[Finding] = []
    d = _kamus(ctx)
    istilah = _istilah(d)
    singkatan = _singkatan(d)
    teknis = _teknis(d)

    # --- LT1: tata letak skripsi ---
    sp = read(SKRIPSI_PREAMBLE)
    if sp is None:
        findings.append(Finding("fail", f"LT1: {SKRIPSI_PREAMBLE} tidak ditemukan"))
    else:
        for a in SKRIPSI_ANCHORS:
            if a not in sp:
                findings.append(Finding("fail", f"LT1: {SKRIPSI_PREAMBLE} kehilangan '{a}'"))

    # --- LT2: tata letak artikel/jurnal ---
    ap = read(ARTIKEL_PREAMBLE)
    if ap is None:
        findings.append(Finding("fail", f"LT2: {ARTIKEL_PREAMBLE} tidak ditemukan"))
    else:
        for a in ARTIKEL_ANCHORS:
            if a not in ap:
                findings.append(Finding("fail", f"LT2: {ARTIKEL_PREAMBLE} kehilangan '{a}'"))
    docx = os.path.join(ctx.root, REFERENCE_DOCX)
    if not os.path.exists(docx):
        findings.append(Finding("fail", f"LT2: {REFERENCE_DOCX} tidak ditemukan"))
    else:
        try:
            with zipfile.ZipFile(docx) as z:
                styles = z.read("word/styles.xml").decode("utf-8", "ignore")
            if "Times New Roman" not in styles:
                findings.append(Finding("fail", f"LT2: {REFERENCE_DOCX} tanpa 'Times New Roman'"))
        except (KeyError, zipfile.BadZipFile) as exc:  # noqa: BLE001
            findings.append(Finding("fail", f"LT2: {REFERENCE_DOCX} tidak terbaca ({exc})"))

    # --- LT6: tata letak Sinta terpusat ---
    if not os.path.exists(os.path.join(ctx.root, SINTA_FILTER)):
        findings.append(Finding("fail", f"LT6: {SINTA_FILTER} tidak ditemukan"))
    if ap is None:
        findings.append(Finding("fail", f"LT6: {ARTIKEL_PREAMBLE} tidak ditemukan"))
    else:
        for a in SINTA_PREAMBLE_ANCHORS:
            if a not in ap:
                findings.append(Finding(
                    "fail", f"LT6: {ARTIKEL_PREAMBLE} kehilangan '{a}'"))
    mf = read(MAKEFILE)
    if mf is None:
        findings.append(Finding("fail", f"LT6: {MAKEFILE} tidak ditemukan"))
    else:
        wired: set[str] = set()
        target = None
        for line in mf.splitlines():
            m = re.match(r"^([A-Za-z0-9_.-]+)\s*:", line)
            if m:
                target = m.group(1)
                continue
            if target and ARTIKEL_TARGET_RE.match(target) \
                    and "--lua-filter=" + SINTA_FILTER in line:
                wired.add(target)
        for t in ("artikel", "artikel-kyt", "artikel-arai"):
            if t not in wired:
                findings.append(Finding(
                    "fail", f"LT6: target '{t}' di {MAKEFILE} belum memakai "
                            f"--lua-filter={SINTA_FILTER}"))

    # --- LT7: bahasa dokumen (filter bilingual) ---
    utama = (d.get("bahasa") or {}).get("utama")
    if not isinstance(utama, str) or not utama:
        findings.append(Finding(
            "fail", f"LT7: {KAMUS} kehilangan 'bahasa.utama'"))
    if not os.path.exists(os.path.join(ctx.root, BILINGUAL_FILTER)):
        findings.append(Finding("fail", f"LT7: {BILINGUAL_FILTER} tidak ditemukan"))
    if mf is None:
        pass
    else:
        wired_bil: set[str] = set()
        all_targets: set[str] = set()
        target = None
        for line in mf.splitlines():
            m = re.match(r"^([A-Za-z0-9_.-]+)\s*:", line)
            if m:
                target = m.group(1)
                if ARTIKEL_TARGET_RE.match(target) or target == "skripsi":
                    all_targets.add(target)
                continue
            if target and (ARTIKEL_TARGET_RE.match(target) or target == "skripsi") \
                    and "--lua-filter=" + BILINGUAL_FILTER in line:
                wired_bil.add(target)
        for t in sorted(all_targets):
            if t not in wired_bil:
                findings.append(Finding(
                    "fail", f"LT7: target '{t}' di {MAKEFILE} belum memakai "
                            f"--lua-filter={BILINGUAL_FILTER}"))
    for path in sorted(glob.glob(os.path.join(ctx.root, ARTIKEL_GLOB))):
        rel = os.path.relpath(path, ctx.root)
        text = "\n".join(_baca(path))
        found = ABSTRACT_LANG_RE.findall(text)
        if len(found) < 2:
            for want in ("id", "en"):
                if want not in found:
                    findings.append(Finding(
                        "fail", f"LT7: {rel}: abstrak {want} tanpa atribut lang={want}"))
        elif found[0] != "id" or found[1] != "en":
            findings.append(Finding(
                "fail", f"LT7: {rel}: abstrak lang={found[0]} lalu lang={found[1]} "
                        f"(harus id lalu en)"))

    # --- LT8: larangan em dash + hyphen berspasi di prosa ---
    for preamble in (SKRIPSI_PREAMBLE, ARTIKEL_PREAMBLE):
        ptxt = read(preamble)
        if ptxt is None:
            findings.append(Finding("fail", f"LT8: {preamble} tidak ditemukan"))
            continue
        for anchor in (r"\hyphenpenalty=10000", r"\exhyphenpenalty=10000"):
            if anchor not in ptxt:
                findings.append(Finding(
                    "fail", f"LT8: {preamble} kehilangan '{anchor}'"))
    for g, level in ((ARTIKEL_GLOB, "fail"), (SKRIPSI_GLOB, "fail"),
                     (DRAFT_GLOB, "warn")):
        for path in sorted(glob.glob(os.path.join(ctx.root, g))):
            rel = os.path.relpath(path, ctx.root)
            lines = _baca(path)
            for n, (line, kind) in enumerate(zip(lines, _kinds(lines)), 1):
                if kind in ("fence", "div", "comment"):
                    continue
                s = line.strip()
                if s.startswith("- ") or s.startswith("* "):
                    continue
                bersih = _mask(line)
                if "\u2014" in bersih:
                    findings.append(Finding(
                        level, f"LT8: {rel}:{n}: tanda pisah terlarang (\u2014)"))
                if " - " in bersih:
                    findings.append(Finding(
                        level, f"LT8: {rel}:{n}: tanda pisah terlarang ( - )"))

    # --- LT3 + LT9 + LT4/LT5: artikel (per berkas) dan draf ---
    for g, level in ((ARTIKEL_GLOB, "fail"), (DRAFT_GLOB, "warn")):
        for path in sorted(glob.glob(os.path.join(ctx.root, g))):
            rel = os.path.relpath(path, ctx.root)
            lines = _baca(path)
            kinds = _kinds(lines)
            rows = _rows(rel, lines, kinds)
            _cek_istilah(rows, istilah, level, findings)
            _cek_teknis(rows, teknis, level, findings)
            _cek_singkatan(rows, singkatan, _daftar_dalam(lines, kinds),
                           rel, level, findings)

    # --- LT3 (per bab) + LT9 (gabungan) + LT4/LT5 (gabungan skripsi) ---
    sk_rows: list[tuple] = []
    n_bab = 0
    for path in sorted(glob.glob(os.path.join(ctx.root, SKRIPSI_GLOB))):
        rel = os.path.relpath(path, ctx.root)
        lines = _baca(path)
        kinds = _kinds(lines)
        _cek_istilah(_rows(rel, lines, kinds), istilah, "fail", findings)
        sk_rows.extend(_rows(rel, lines, kinds))
        n_bab += 1
    _cek_teknis(sk_rows, teknis, "fail", findings)
    _cek_singkatan(sk_rows, singkatan, read(DAFTAR_SKRIPSI) or "",
                   DAFTAR_SKRIPSI, "fail", findings)

    if not any(f.level == "fail" for f in findings):
        findings.append(Finding(
            "ok", f"tata letak & tipografi patuh kerangka LT1-LT9 "
                  f"({n_bab} bab skripsi + artikel + draf)"))
    return findings
