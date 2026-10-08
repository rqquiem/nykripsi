"""Validator catatan riset HI/IR: ``docs/kamus-riset-korpus-hi.md`` vs korpus di disk."""

import glob
import os
import re

from .base import Context, Finding, read, register

PDF_CLAIM_RE = re.compile(r"\*\*(\d+) PDF\*\*|(\d+) PDF")
TABLE_ROW_RE = re.compile(r"^\|\s*`hi-", re.MULTILINE)
SLUG_RE = re.compile(r"\bhi-[a-z0-9-]+")
FRACTION_RE = re.compile(r"(\d+)/(\d+) (paper|PDF)")

def _manifest_slugs() -> set[str]:
    text = read("docs/ir-corpus/manifest.tsv") or ""
    lines = [ln for ln in text.splitlines() if ln.strip()]
    return {ln.split("\t")[0] for ln in lines[1:]}

@register("ir_research_notes", "docs/kamus-riset-korpus-hi.md + docs/ir-corpus/*")
def run(ctx: Context) -> list[Finding]:
    findings: list[Finding] = []

    text = read("docs/kamus-riset-korpus-hi.md")
    if text is None:
        return [Finding("fail", "docs/kamus-riset-korpus-hi.md tidak ditemukan")]

    pdfs = glob.glob(os.path.join(ctx.root, "docs/ir-corpus/*.pdf"))
    n_pdf = len(pdfs)
    pdf_slugs = {os.path.basename(p)[:-4] for p in pdfs}
    manifest_slugs = _manifest_slugs()
    corpus_slugs = manifest_slugs & pdf_slugs

    # Klaim "<n> PDF" harus sama dengan jumlah berkas PDF.
    for m in PDF_CLAIM_RE.finditer(text):
        n = int(m.group(1) or m.group(2))
        if n != n_pdf:
            findings.append(Finding("fail", f"klaim {n} PDF != {n_pdf} berkas"))

    # Baris tabel per-paper harus sama dengan jumlah PDF.
    row_count = len(TABLE_ROW_RE.findall(text))
    if row_count != n_pdf:
        findings.append(Finding("fail", f"tabel punya {row_count} baris != {n_pdf} PDF"))

    # Setiap slug di catatan harus slug manifest.
    note_slugs = set(SLUG_RE.findall(text))
    unknown = sorted(note_slugs - manifest_slugs)
    if unknown:
        findings.append(Finding("fail", f"slug tak dikenal: {unknown}"))

    # Setiap slug korpus (manifest ber-PDF) harus muncul di catatan.
    missing = sorted(corpus_slugs - note_slugs)
    if missing:
        findings.append(Finding("fail", f"slug korpus tak ada di catatan: {missing}"))

    # Pecahan "<num>/<den> paper|PDF": num <= den; den == n_pdf untuk "paper".
    for m in FRACTION_RE.finditer(text):
        num, den, word = int(m.group(1)), int(m.group(2)), m.group(3)
        if num > den:
            findings.append(Finding("fail", f"pecahan {num}/{den} {word} tidak valid"))
        if word == "paper" and den != n_pdf:
            findings.append(Finding("fail", f"penyebut {den} paper != {n_pdf} PDF"))

    if not any(f.level == "fail" for f in findings):
        findings.append(Finding("ok", f"klaim {n_pdf} PDF == {n_pdf} berkas"))
    return findings
