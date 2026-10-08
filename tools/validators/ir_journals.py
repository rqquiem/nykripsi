"""Validator korpus jurnal HI/IR: ``docs/ir-corpus/{manifest.tsv,MANIFEST.md,*.pdf}``."""

import glob
import math
import os
import re

from .base import Context, Finding, read, register, sh

HEADER = ["slug", "tier", "venue", "year", "article_url", "pdf_url"]
TIERS = {"national", "international"}
MANIFEST_ROW_RE = re.compile(r"^\|\s*\d+\s*\|")

def _manifest_rows() -> list[list[str]]:
    text = read("docs/ir-corpus/manifest.tsv") or ""
    lines = [ln for ln in text.splitlines() if ln.strip()]
    return [ln.split("\t") for ln in lines[1:]]

def _md_failed_slugs() -> set[str]:
    text = read("docs/ir-corpus/MANIFEST.md") or ""
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

@register("ir_journals", "docs/ir-corpus/{manifest.tsv,MANIFEST.md,*.pdf}")
def run(ctx: Context) -> list[Finding]:
    findings: list[Finding] = []

    # --- manifest.tsv ---
    text = read("docs/ir-corpus/manifest.tsv")
    if text is None:
        return [Finding("fail", "manifest.tsv tidak ditemukan")]
    lines = [ln for ln in text.splitlines() if ln.strip()]
    header = lines[0].split("\t") if lines else []
    if header != HEADER:
        findings.append(Finding("fail", f"header manifest.tsv salah: {header}"))

    rows = _manifest_rows()
    seen: set[str] = set()
    n_intl = 0
    for i, cells in enumerate(rows, start=1):
        if len(cells) != 6:
            findings.append(Finding("fail", f"baris {i} tidak memiliki 6 kolom"))
            continue
        slug, tier, _venue, year, article_url, _pdf_url = cells
        if slug in seen:
            findings.append(Finding("fail", f"slug duplikat '{slug}' pada baris {i}"))
        seen.add(slug)
        if tier not in TIERS:
            findings.append(Finding("fail", f"tier tidak valid '{tier}' pada baris {i}"))
        if tier == "international":
            n_intl += 1
        if not re.match(r"^\d{4}$", year):
            findings.append(Finding("fail", f"year tidak valid '{year}' pada baris {i}"))
        if not re.match(r"^https?://", article_url):
            findings.append(Finding("fail", f"article_url tidak valid '{article_url}' pada baris {i}"))

    # Cakupan korpus: >= 30 baris dan >= 30% tier international.
    n = len(rows)
    if n < 30:
        findings.append(Finding("fail", f"manifest hanya {n} baris (< 30)"))
    need_intl = math.ceil(0.30 * n)
    if n_intl < need_intl:
        findings.append(
            Finding("fail", f"tier international {n_intl}/{n} < {need_intl} (30%)")
        )

    # --- PDF di disk ---
    pdfs = sorted(glob.glob(os.path.join(ctx.root, "docs/ir-corpus/*.pdf")))
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
    md = read("docs/ir-corpus/MANIFEST.md")
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
            Finding("ok", f"{len(rows)} baris manifest, {len(pdf_slugs)} PDF ada, {n_intl} internasional, konsisten")
        )
    return findings
