"""Validator sitasi artikel: ``content/**/*.md`` vs ``assets/refs.bib``."""

import glob
import os
import re

from .base import Context, Finding, read, register

CITE_RE = re.compile(r"\[@([A-Za-z0-9_:\-]+)\]")
ENTRY_RE = re.compile(r"^@(\w+)\{([^,]+),", re.MULTILINE)
FIELD_RE = re.compile(r"^\s*(\w+)\s*=", re.MULTILINE)
ABSTRACT_RE = re.compile(r'::: \{custom-style="Abstract"\}(.*?)\n:::', re.DOTALL)

REQUIRED = {
    "article": ("author", "title", "journal", "year"),
    "book": ("author", "title", "publisher", "year"),
    "inproceedings": ("author", "title", "booktitle", "year"),
}


def _bib_blocks() -> list[tuple[str, str, str]]:
    """Kembalikan ``(type, key, block)`` untuk setiap entri bib (blok seimbang)."""
    text = read("assets/refs.bib") or ""
    blocks: list[tuple[str, str, str]] = []
    for m in ENTRY_RE.finditer(text):
        etype, key = m.group(1), m.group(2).strip()
        start = text.index("{", m.start())  # posisi '{' pembuka entri
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
        blocks.append((etype, key, text[start : i + 1]))
    return blocks


@register("papers", "content/artikel/artikel-sinta.md + content/skripsi/*.md + assets/refs.bib")
def run(ctx: Context) -> list[Finding]:
    findings: list[Finding] = []

    # Kumpulkan kunci sitasi dari seluruh content/**/*.md.
    cited: list[str] = []
    for path in sorted(glob.glob(os.path.join(ctx.root, "content/**/*.md"), recursive=True)):
        if os.path.relpath(path, ctx.root).startswith("content/drafts" + os.sep):
            continue
        with open(path, encoding="utf-8") as fh:
            cited.extend(CITE_RE.findall(fh.read()))
    cited_set = set(cited)

    blocks = _bib_blocks()
    bib_keys = {key for _t, key, _b in blocks}

    # Setiap sitasi harus ada di bib.
    for k in sorted(cited_set - bib_keys):
        findings.append(Finding("fail", f"sitasi [@{k}] tidak ada di refs.bib"))
    # Setiap entri bib harus disitasi.
    for k in sorted(bib_keys - cited_set):
        findings.append(Finding("fail", f"entri bib '{k}' tidak pernah disitasi"))

    # Bidang wajib + keseimbangan kurung per entri.
    for etype, key, block in blocks:
        if block.count("{") != block.count("}"):
            findings.append(Finding("fail", f"entri bib '{key}' kurung tidak seimbang"))
        fields = set(FIELD_RE.findall(block))
        required = REQUIRED.get(etype, ("author", "title", "year"))
        for fld in required:
            if fld not in fields:
                findings.append(Finding("fail", f"entri bib '{key}' ({etype}) tidak punya bidang '{fld}'"))

    # Abstrak tidak boleh memuat sitasi.
    for path in sorted(glob.glob(os.path.join(ctx.root, "content/**/*.md"), recursive=True)):
        if os.path.relpath(path, ctx.root).startswith("content/drafts" + os.sep):
            continue
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        for abstract in ABSTRACT_RE.findall(text):
            if "[@" in abstract:
                findings.append(Finding("fail", f"abstrak memuat sitasi ({os.path.relpath(path, ctx.root)})"))

    if not any(f.level == "fail" for f in findings):
        findings.append(Finding("ok", f"{len(cited_set)} sitasi \u2194 {len(bib_keys)} entri bib, semua terselesaikan"))
    return findings
