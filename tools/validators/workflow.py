"""Validator alur kerja: ``docs/workflow.md`` vs ``Makefile``."""

import os
import re

from .base import Context, Finding, exists, read, register

MAKE_REF_RE = re.compile(r"`make\s+([\w-]+)`")
PATH_REF_RE = re.compile(r"`((?:tools|content|docs|assets|templates)/[^`]*)`")
STEP_RE = re.compile(r"^(\d+)\. ", re.MULTILINE)
TARGET_RE = re.compile(r"^([a-zA-Z][\w-]*):")


def _targets() -> set[str]:
    mk = read("Makefile") or ""
    targets: set[str] = set()
    for line in mk.splitlines():
        m = TARGET_RE.match(line)
        if m and m.group(1) != ".PHONY":
            targets.add(m.group(1))
    return targets


@register("workflow", "docs/workflow.md + Makefile")
def run(ctx: Context) -> list[Finding]:
    text = read("docs/workflow.md")
    if text is None:
        return [Finding("fail", "docs/workflow.md tidak ditemukan")]

    findings: list[Finding] = []
    targets = _targets()

    # Setiap `` `make <t>` `` harus menunjuk target yang ada.
    for t in MAKE_REF_RE.findall(text):
        if t in targets:
            findings.append(Finding("ok", f"menunjuk make {t} (ada)"))
        else:
            findings.append(Finding("fail", f"menunjuk target 'make {t}' yang tidak ada"))

    # ``make check`` wajib dirujuk dan ada.
    if "make check" not in text:
        findings.append(Finding("fail", "tidak merujuk 'make check'"))
    elif "check" not in targets:
        findings.append(Finding("fail", "target 'check' tidak ada di Makefile"))
    else:
        findings.append(Finding("ok", "make check dirujuk dan target ada"))

    # Setiap path repo yang di-backtick harus ada (wildcard dicek via direktori prefiks).
    for p in PATH_REF_RE.findall(text):
        if "*" in p:
            prefix = p.split("*", 1)[0]
            ok = os.path.isdir(os.path.join(ctx.root, prefix))
        else:
            ok = exists(p)
        if ok:
            findings.append(Finding("ok", f"menunjuk {p} (ada)"))
        else:
            findings.append(Finding("fail", f"menunjuk {p} yang tidak ada"))

    # Kontinuitas langkah bernomor: tepat 1..N tanpa celah/duplikat.
    nums = [int(n) for n in STEP_RE.findall(text)]
    if nums and nums != list(range(1, len(nums) + 1)):
        findings.append(Finding("fail", f"langkah bernomor tidak berurutan: {nums}"))
    else:
        findings.append(Finding("ok", f"langkah bernomor berurutan (1..{len(nums)})"))

    return findings
