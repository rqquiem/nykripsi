"""Validator DOI: ``assets/refs.bib`` (struktur + verifikasi daring opsional)."""

import re
import urllib.error
import urllib.request

from .base import EXAMPLE_DOI_PREFIXES, UA, Context, Finding, read, register

DOI_FIELD_RE = re.compile(r"doi\s*=\s*\{([^}]*)\}")
DOI_STRUCT_RE = re.compile(r"^10\.\d{4,9}/\S+$")


def _check_online(doi: str) -> Finding:
    req = urllib.request.Request(
        "https://doi.org/" + doi,
        headers={
            "Accept": "application/vnd.citationstyles.csl+json",
            "User-Agent": UA,
        },
    )
    try:
        resp = urllib.request.urlopen(req, timeout=15)
        code = getattr(resp, "status", 200)
        if 200 <= code < 400:
            return Finding("ok", f"{doi} dapat diverifikasi")
        return Finding("warn", f"{doi} tidak dapat diverifikasi (jaringan)")
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return Finding("fail", f"{doi} tidak ditemukan")
        return Finding("warn", f"{doi} tidak dapat diverifikasi (jaringan)")
    except (urllib.error.URLError, TimeoutError, OSError):
        return Finding("warn", f"{doi} tidak dapat diverifikasi (jaringan)")


@register("doi", "assets/refs.bib")
def run(ctx: Context) -> list[Finding]:
    text = read("assets/refs.bib") or ""
    dois = DOI_FIELD_RE.findall(text)
    if not dois:
        return [Finding("warn", "tidak ada field doi di refs.bib")]

    findings: list[Finding] = []
    seen: set[str] = set()

    # Struktur + duplikat + kosong.
    for d in dois:
        if d.strip() == "":
            findings.append(Finding("fail", "field doi kosong"))
            continue
        if not DOI_STRUCT_RE.match(d):
            findings.append(Finding("fail", f"struktur tidak valid '{d}'"))
        if d in seen:
            findings.append(Finding("fail", f"duplikat '{d}'"))
        seen.add(d)

    # Verifikasi daring (dilewati bila offline).
    checked = 0
    if not ctx.offline:
        for d in dict.fromkeys(dois):
            if not DOI_STRUCT_RE.match(d):
                continue
            if d.startswith(EXAMPLE_DOI_PREFIXES):
                findings.append(Finding("ok", f"{d} (prefix contoh, dilewati)"))
                continue
            checked += 1
            findings.append(_check_online(d))

    if not any(f.level == "fail" for f in findings):
        findings.append(Finding("ok", f"{len(dois)} DOI tervalidasi struktur ({checked} dicek daring)"))
    return findings
