"""Validator sitasi & catatan kaki (kerangka CT1-CT7).

Menegakkan docs/citation-framework.md:
  CT1 gaya sitasi dalam teks (APA author-date via [@key]; tanpa sitasi
      parentetik/numerik yang ditulis tangan);
  CT2 ketertutupan sitasi <-> daftar pustaka (sadar multi-kunci [@a; @b]);
  CT3 daftar pustaka dirender lewat blok ::: {#refs} :::;
  CT4 catatan kaki hanya penjelas (tanpa sitasi [@key]);
  CT5 abstrak tanpa sitasi dan tanpa catatan kaki;
  CT6 kutipan langsung memakai tanda petik melengkung (EYD) + lokator;
  CT7 tautan daftar pustaka: entri tidak boleh memuat doi dan url sekaligus,
      dan entri bukti (note berkanal Berita/Siaran pers/Artikel/Web) wajib
      memuat url (karya akademik menampilkan DOI, bukan URL).
Berkas final (content/artikel/*.md + content/skripsi/1[0-5]-*.md + 90-*) level
'fail'; content/drafts/*.md level 'warn'.
"""

import glob
import os
import re

from .base import Context, Finding, read, register

BIB = "assets/refs.bib"
ARTIKEL_GLOB = "content/artikel/*.md"
EN_GLOB = "content/artikel-en/*.md"
SKRIPSI_GLOB = "content/skripsi/1[0-5]-*.md"
SKRIPSI_PUSTAKA = "content/skripsi/90-daftar-pustaka.md"
DRAFT_GLOB = "content/drafts/*.md"

ENTRY_RE = re.compile(r"^@\w+\{([^,]+),", re.MULTILINE)
CITE_RE = re.compile(r"\[@([^\]]+)\]")
REF_BLOCK_RE = re.compile(r":::\s*\{#refs\}\s*:::")
ABSTRACT_RE = re.compile(r'::: \{custom-style="Abstract"[^}]*\}(.*?)\n:::', re.DOTALL)
FOOT_DEF_RE = re.compile(r"^\[\^([^\]]+)\]:", re.MULTILINE)
FOOT_REF_RE = re.compile(r"\[\^([^\]]+)\]")
PAREN_CITE_RE = re.compile(r"\(\s*[A-Z][A-Za-z.'’&.\- ]+,\s*(?:19|20)\d{2}[^)]*\)")
NUMERIC_CITE_RE = re.compile(r"\[\s*\d+\s*(?:\]|[-–]\s*\d+\s*\])")
STRAIGHT_QUOTE_RE = re.compile(r'"')
CURLY_QUOTE_RE = re.compile(r"“[^”]*”")
FENCE_RE = re.compile(r"^\s*```")
HEADING_RE = re.compile(r"^#{1,6}\s")
CAPTION_RE = re.compile(r"^(Tabel|Gambar)\b")
KW_RE = re.compile(r"^\*\*(Kata Kunci|Keywords)\b")
COMMENT_RE = re.compile(r"<!--.*?-->")
CODE_RE = re.compile(r"`[^`\n]+`")
BOLD_RE = re.compile(r"\*\*[^*\n]+\*\*")
ITAL_RE = re.compile(r"\*[^*\n]+\*")

DOI_FIELD_RE = re.compile(r"^\s*doi\s*=", re.M)
URL_FIELD_RE = re.compile(r"^\s*url\s*=", re.M)
NOTE_KANAL_RE = re.compile(r"^\s*note\s*=\s*\{[^}]*(Berita|Siaran pers|Artikel|Web)", re.M)


def _kinds(lines: list[str]) -> list[str]:
    kinds: list[str] = []
    fence = div = False
    for raw in lines:
        s = raw.strip()
        if FENCE_RE.match(raw):
            fence = not fence
            kinds.append("fence")
            continue
        if fence:
            kinds.append("fence")
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


def _baca(path: str) -> str:
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def _keys(inner: str) -> list[str]:
    """Kunci dari isi kurung sitasi: pisah ';', buang '@' dan lokator ', …'.

    Menangani `key`, `@a; @b`, dan `key, hlm. 12` sekaligus (sadar multi-kunci).
    """
    out: list[str] = []
    for part in inner.split(";"):
        tok = part.strip().lstrip("@").split(",")[0].strip()
        if tok:
            out.append(tok)
    return out


def _foot_body(text: str, label: str) -> str:
    out: list[str] = []
    inside = False
    for ln in text.splitlines():
        m = FOOT_DEF_RE.match(ln)
        if m:
            if inside:
                break
            if m.group(1) == label:
                inside = True
                out.append(ln)
            continue
        if inside:
            if not ln.strip():
                break
            out.append(ln)
    return "\n".join(out)


def _scan(rel: str, text: str, level: str, findings: list[Finding]) -> None:
    lines = text.splitlines()
    kinds = _kinds(lines)
    for n, (line, kind) in enumerate(zip(lines, kinds), 1):
        if kind != "prose":
            continue
        bersih = _mask(line)
        if PAREN_CITE_RE.search(bersih):
            findings.append(Finding(level, f"{rel}:{n}: sitasi parentetik ditulis tangan; gunakan [@key]"))
        if NUMERIC_CITE_RE.search(bersih):
            findings.append(Finding(level, f"{rel}:{n}: sitasi numerik [n] ditulis tangan; gunakan [@key]"))
        if STRAIGHT_QUOTE_RE.search(bersih):
            findings.append(Finding(level, f"{rel}:{n}: tanda petik lurus; pakai tanda petik melengkung (EYD) “…”"))
        for mq in CURLY_QUOTE_RE.finditer(bersih):
            mc = re.match(r"\s*\[@[^\]]*\]", line[mq.end():])
            if mc and "," not in mc.group(0):
                findings.append(Finding("warn", f"{rel}:{n}: kutipan langsung sebaiknya sertakan lokator ([@key, hlm. N])"))
    for block in ABSTRACT_RE.findall(text):
        if "[@" in block:
            findings.append(Finding(level, f"{rel}: abstrak memuat sitasi"))
        if "[^" in block:
            findings.append(Finding(level, f"{rel}: abstrak memuat catatan kaki"))
    defs = set(FOOT_DEF_RE.findall(text))
    for r in sorted(set(FOOT_REF_RE.findall(text)) - defs):
        findings.append(Finding(level, f"{rel}: catatan kaki [^{r}] tanpa definisi"))
    for d in sorted(defs):
        if "[@" in _foot_body(text, d):
            findings.append(Finding(level, f"{rel}: catatan kaki [^{d}] memuat sitasi (hanya catatan penjelas)"))


def _bib_entry_blocks(bib: str) -> list[tuple[str, str]]:
    """Kembalikan ``(key, block)`` tiap entri bib (blok kurung seimbang)."""
    out: list[tuple[str, str]] = []
    for m in ENTRY_RE.finditer(bib):
        key = m.group(1).strip()
        start = bib.index("{", m.start())
        depth = 0
        i = start
        while i < len(bib):
            if bib[i] == "{":
                depth += 1
            elif bib[i] == "}":
                depth -= 1
                if depth == 0:
                    break
            i += 1
        out.append((key, bib[start : i + 1]))
    return out


@register("citation_framework", "content/{artikel,skripsi,drafts} + assets/refs.bib (CT1-CT7)")
def run(ctx: Context) -> list[Finding]:
    findings: list[Finding] = []
    bib = read(BIB) or ""
    bib_keys = {m.group(1).strip() for m in ENTRY_RE.finditer(bib)}

    final = sorted(glob.glob(os.path.join(ctx.root, ARTIKEL_GLOB))) \
        + sorted(glob.glob(os.path.join(ctx.root, EN_GLOB))) \
        + sorted(glob.glob(os.path.join(ctx.root, SKRIPSI_GLOB)))
    cited: set[str] = set()
    for path in final:
        rel = os.path.relpath(path, ctx.root)
        text = _baca(path)
        _scan(rel, text, "fail", findings)
        for m in CITE_RE.finditer(text):
            cited.update(_keys(m.group(1)))
    for path in sorted(glob.glob(os.path.join(ctx.root, DRAFT_GLOB))):
        rel = os.path.relpath(path, ctx.root)
        _scan(rel, _baca(path), "warn", findings)

    # --- CT2: ketertutupan sitasi <-> daftar pustaka (sadar multi-kunci) ---
    for k in sorted(cited - bib_keys):
        findings.append(Finding("fail", f"sitasi [@{k}] tidak ada di refs.bib"))
    for k in sorted(bib_keys - cited):
        findings.append(Finding("fail", f"entri bib '{k}' tidak pernah disitasi"))

    # --- CT3: blok daftar pustaka dirender ---
    for rel in [SKRIPSI_PUSTAKA] + [
        os.path.relpath(p, ctx.root) for p in sorted(
            glob.glob(os.path.join(ctx.root, ARTIKEL_GLOB))
            + glob.glob(os.path.join(ctx.root, EN_GLOB)))
    ]:
        if REF_BLOCK_RE.search(read(rel) or "") is None:
            findings.append(Finding("fail", f"CT3: {rel} tanpa blok ::: {{#refs}} :::"))

    # --- CT7: tautan daftar pustaka (doi/url & kanal bukti wajib url) ---
    for key, block in _bib_entry_blocks(bib):
        has_doi = bool(DOI_FIELD_RE.search(block))
        has_url = bool(URL_FIELD_RE.search(block))
        if has_doi and has_url:
            findings.append(Finding("fail", f"CT7: entri '{key}' memuat doi dan url sekaligus"))
        if NOTE_KANAL_RE.search(block) and not has_url:
            findings.append(Finding("fail", f"CT7: bukti '{key}' tanpa url"))

    if not any(f.level == "fail" for f in findings):
        findings.append(Finding(
            "ok", f"sitasi & catatan kaki patuh kerangka CT1-CT7 "
                  f"({len(cited)} sitasi <-> {len(bib_keys)} entri bib)"))
    return findings
