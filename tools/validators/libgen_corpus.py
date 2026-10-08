"""Validator korpus LibGen: ``docs/libgen-corpus/{manifest.tsv,MANIFEST.md,*.pdf}``."""

import glob
import os
import re

from .base import Context, Finding, read, register, sh

HEADER = ["slug", "kind", "title", "year", "md5", "doi"]
KINDS = {"book", "article"}
MD5_RE = re.compile(r"^[a-f0-9]{32}$")
DOI_RE = re.compile(r"^10\.\d{4,9}/\S+$")
MANIFEST_ROW_RE = re.compile(r"^\|\s*\d+\s*\|")

def _manifest_rows() -> list[list[str]]:
    text = read("docs/libgen-corpus/manifest.tsv") or ""
    lines = [ln for ln in text.splitlines() if ln.strip()]
    return [ln.split("\t") for ln in lines[1:]]

def _md_failed_slugs() -> set[str]:
    text = read("docs/libgen-corpus/MANIFEST.md") or ""
    failed: set[str] = set()
    for line in text.splitlines():
        if not MANIFEST_ROW_RE.match(line):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if cells[1]:
            slug = cells[1].strip("`")
            if "FAILED" in cells[-1]:
                failed.add(slug)
    return failed

@register("libgen_corpus", "docs/libgen-corpus/{manifest.tsv,MANIFEST.md,*.pdf}")
def run(ctx: Context) -> list[Finding]:
    findings: list[Finding] = []

    # --- manifest.tsv ---
    text = read("docs/libgen-corpus/manifest.tsv")
    if text is None:
        return [Finding("fail", "manifest.tsv tidak ditemukan")]
    lines = [ln for ln in text.splitlines() if ln.strip()]
    header = lines[0].split("\t") if lines else []
    if header != HEADER:
        findings.append(Finding("fail", f"header manifest.tsv salah: {header}"))

    rows = _manifest_rows()
    seen: set[str] = set()
    seen_md5: set[str] = set()
    n_book = 0
    n_art = 0
    for i, cells in enumerate(rows, start=1):
        if len(cells) != 6:
            findings.append(Finding("fail", f"baris {i} tidak memiliki 6 kolom"))
            continue
        slug, kind, _title, year, md5, doi = cells
        if slug in seen:
            findings.append(Finding("fail", f"slug duplikat '{slug}' pada baris {i}"))
        seen.add(slug)
        if kind not in KINDS:
            findings.append(Finding("fail", f"kind tidak valid '{kind}' pada baris {i}"))
        if kind == "book":
            n_book += 1
        elif kind == "article":
            n_art += 1
        if not re.match(r"^\d{4}$", year):
            findings.append(Finding("fail", f"year tidak valid '{year}' pada baris {i}"))
        if not MD5_RE.match(md5):
            findings.append(Finding("fail", f"md5 tidak valid '{md5}' pada baris {i}"))
        if md5 in seen_md5:
            findings.append(Finding("fail", f"md5 duplikat '{md5}' pada baris {i}"))
        seen_md5.add(md5)
        if doi and not DOI_RE.match(doi):
            findings.append(Finding("fail", f"doi tidak valid '{doi}' pada baris {i}"))

    # --- cakupan ---
    n = len(rows)
    if n < 1:
        findings.append(Finding("fail", "manifest.tsv tidak memiliki baris data"))
    if n_book < 1:
        findings.append(Finding("fail", "tidak ada baris kind='book'"))
    if n_art < 1:
        findings.append(Finding("fail", "tidak ada baris kind='article'"))

    # --- PDF di disk ---
    pdfs = sorted(glob.glob(os.path.join(ctx.root, "docs/libgen-corpus/*.pdf")))
    for p in pdfs:
        rel = os.path.relpath(p, ctx.root)
        rc, out = sh(["file", p])
        if rc != 0 or "PDF" not in out:
            findings.append(Finding("fail", f"{rel} bukan PDF"))

    pdf_slugs = {os.path.basename(p)[:-4] for p in pdfs}
    failed_slugs = _md_failed_slugs()
    ok_slugs = seen - failed_slugs

    # Setiap slug manifest harus punya PDF ATAU baris FAILED; tanpa PDF yatim.
    diff = pdf_slugs ^ ok_slugs
    if diff:
        findings.append(Finding("fail", f"ketidaksesuaian slug/PDF: {sorted(diff)}"))

    # --- MANIFEST.md ---
    md = read("docs/libgen-corpus/MANIFEST.md")
    if md is None:
        findings.append(Finding("fail", "MANIFEST.md tidak ditemukan"))
    else:
        md_rows = [ln for ln in md.splitlines() if MANIFEST_ROW_RE.match(ln)]
        if len(md_rows) != len(rows):
            findings.append(Finding("fail", f"MANIFEST.md {len(md_rows)} baris != manifest.tsv {len(rows)} baris"))
        m_ok = re.search(r"OK=(\d+)", md)
        m_failed = re.search(r"FAILED=(\d+)", md)
        if not m_ok:
            findings.append(Finding("fail", "MANIFEST.md tidak menyatakan OK=<n>"))
        elif int(m_ok.group(1)) != len(pdf_slugs):
            findings.append(Finding("fail", f"OK={m_ok.group(1)} != {len(pdf_slugs)} PDF di disk"))
        if not m_failed:
            findings.append(Finding("fail", "MANIFEST.md tidak menyatakan FAILED=<m>"))
        elif int(m_failed.group(1)) != len(rows) - len(pdf_slugs):
            findings.append(Finding("fail", f"FAILED={m_failed.group(1)} != {len(rows) - len(pdf_slugs)}"))

    if not any(f.level == "fail" for f in findings):
        findings.append(
            Finding("ok", f"{len(rows)} baris, {len(pdf_slugs)} PDF, {n_book} book/{n_art} article, konsisten")
        )
    return findings
