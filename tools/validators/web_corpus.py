"""Validator korpus web: ``docs/web-corpus/{manifest.tsv,MANIFEST.md,*.html,*.txt}``."""

import os
import re

from .base import Context, Finding, read, register

HEADER = ["slug", "url", "accessed", "mode", "status", "http", "bytes", "sha256", "text_chars"]
MODES = {"curl", "headless-puppeteer", "headless-chrome"}
SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
HEX_RE = re.compile(r"^[a-f0-9]{64}$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
URL_RE = re.compile(r"^(https?|file)://\S+$")
MD_ROW_RE = re.compile(r"^\|\s*\d+\s*\|")
FAILED_RE = re.compile(r"FAILED=(\d+)")


@register("web_corpus", "docs/web-corpus/{manifest.tsv,MANIFEST.md,*.html,*.txt}")
def run(ctx: Context) -> list[Finding]:
    findings: list[Finding] = []

    # --- manifest.tsv ---
    text = read("docs/web-corpus/manifest.tsv")
    if text is None:
        return [Finding("warn", "docs/web-corpus/manifest.tsv belum ada")]
    lines = [ln for ln in text.splitlines() if ln.strip()]
    header = lines[0].split("\t") if lines else []
    if header != HEADER:
        findings.append(Finding("fail", f"header manifest.tsv salah: {header}"))

    rows = [ln.split("\t") for ln in lines[1:]]
    seen: set[str] = set()
    n_ok = 0
    for i, cells in enumerate(rows, start=1):
        if len(cells) != 9:
            findings.append(Finding("fail", f"baris {i} tidak memiliki 9 kolom"))
            continue
        slug, url, accessed, mode, status, http, nbytes, sha256, text_chars = cells
        if slug in seen:
            findings.append(Finding("fail", f"slug duplikat: {slug}"))
        seen.add(slug)
        if not SLUG_RE.match(slug):
            findings.append(Finding("fail", f"slug tidak valid '{slug}' pada baris {i}"))
        if not URL_RE.match(url):
            findings.append(Finding("fail", f"url tidak valid '{url}' pada baris {i}"))
        if not DATE_RE.match(accessed):
            findings.append(Finding("fail", f"accessed tidak valid '{accessed}' pada baris {i}"))
        if mode not in MODES:
            findings.append(Finding("fail", f"mode tidak valid '{mode}' pada baris {i}"))
        if not HEX_RE.match(sha256):
            findings.append(Finding("fail", f"sha256 tidak valid '{sha256}' pada baris {i}"))
        for field, value in (("http", http), ("bytes", nbytes), ("text_chars", text_chars)):
            if not value.lstrip("-").isdigit():
                findings.append(Finding("fail", f"{field} tidak valid '{value}' pada baris {i}"))
        if status == "ok":
            n_ok += 1

    # --- MANIFEST.md ---
    md = read("docs/web-corpus/MANIFEST.md")
    if md is None:
        findings.append(Finding("fail", "MANIFEST.md tidak ditemukan"))
    else:
        for slug in seen:
            if slug not in md:
                findings.append(Finding("fail", f"slug '{slug}' tidak ada di MANIFEST.md"))
        m_failed = FAILED_RE.search(md)
        if not m_failed:
            findings.append(Finding("fail", "MANIFEST.md tidak menyatakan FAILED=<n>"))
        else:
            expected = sum(1 for cells in rows if len(cells) == 9 and cells[4] != "ok")
            if int(m_failed.group(1)) != expected:
                findings.append(Finding("fail", f"FAILED={m_failed.group(1)} != {expected}"))

    # --- berkas lokal (peringatan saja) ---
    for cells in rows:
        if len(cells) != 9 or cells[4] != "ok":
            continue
        slug = cells[0]
        txt = os.path.join(ctx.root, "docs/web-corpus", slug + ".txt")
        raw = any(
            os.path.exists(os.path.join(ctx.root, "docs/web-corpus", slug + ext))
            for ext in (".html", ".json", ".pdf")
        )
        if not os.path.exists(txt) and not raw:
            findings.append(
                Finding("warn", f"{slug} belum terunduh lokal (jalankan 'make webgrab')")
            )

    if not any(f.level == "fail" for f in findings):
        findings.append(Finding("ok", f"{len(rows)} baris, {n_ok} ok, konsisten"))
    return findings
