"""Validator celah penelitian: ``research/judul.json`` + ``research/index.md``."""

import glob
import json
import os
import re
import unicodedata

from .base import Context, Finding, read, register

STATUSES = {"selected", "candidate", "rejected"}
VERDICTS = {"available", "duplicate", "too-similar"}
ORIGINS = {"auto", "browser", "manual"}
REQUIRED = ("id", "judul", "judul_norm", "status", "verdict", "origin", "checked", "matches")

def _slug(text: str) -> str:
    """Aturan slug yang sama dengan research_gap.py."""
    folded = unicodedata.normalize("NFKD", text or "").encode("ascii", "ignore").decode("ascii")
    folded = folded.lower()
    folded = re.sub(r"[^a-z0-9]+", "-", folded).strip("-")
    return folded or "untitled"

@register("research", "research/judul.json + research/index.md")
def run(ctx: Context) -> list[Finding]:
    findings: list[Finding] = []

    text = read("research/judul.json")
    if text is None:
        return [Finding("warn", "research/judul.json belum ada")]

    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return [Finding("fail", "judul.json bukan JSON valid")]

    if not isinstance(data, list):
        return [Finding("fail", "judul.json bukan array JSON")]

    seen_ids: set[str] = set()
    selected: list[dict] = []

    for index, rec in enumerate(data):
        if not isinstance(rec, dict):
            findings.append(Finding("fail", f"catatan #{index} bukan objek JSON"))
            continue

        rid = rec.get("id")
        label = str(rid) if rid else f"#{index}"

        for key in REQUIRED:
            if key not in rec:
                findings.append(Finding("fail", f"judul '{label}' tidak punya kunci '{key}'"))

        status = rec.get("status")
        if status not in STATUSES:
            findings.append(Finding("fail", f"judul '{label}' punya status tidak dikenal '{status}'"))

        verdict = rec.get("verdict")
        if verdict not in VERDICTS:
            findings.append(Finding("fail", f"judul '{label}' punya verdict tidak dikenal '{verdict}'"))

        origin = rec.get("origin")
        if origin not in ORIGINS:
            findings.append(Finding("fail", f"judul '{label}' punya origin tidak dikenal '{origin}'"))

        if not isinstance(rec.get("matches"), list):
            findings.append(Finding("fail", f"judul '{label}' punya matches bukan array"))

        if rid is not None:
            if rid in seen_ids:
                findings.append(Finding("fail", f"id duplikat '{rid}'"))
            seen_ids.add(rid)

        if status == "selected":
            selected.append(rec)

    if len(selected) > 1:
        ids = ", ".join(str(r.get("id")) for r in selected)
        findings.append(Finding("fail", f"lebih dari satu judul terpilih: {ids}"))

    for rec in selected:
        if rec.get("verdict") != "available":
            findings.append(Finding("fail",
                                    f"judul terpilih '{rec.get('judul')}' tidak tersedia ({rec.get('verdict')})"))

    index_text = read("research/index.md")
    if index_text is None:
        findings.append(Finding("fail", "research/index.md tidak ditemukan"))
    else:
        for rid in sorted(seen_ids):
            if rid not in index_text:
                findings.append(Finding("fail", f"id '{rid}' tidak ada di research/index.md"))

    # Laporan celah hanya diperingatkan (warn), tidak pernah menggagalkan.
    gap_dir = os.path.join(ctx.root, "research")
    for rec in selected:
        s = _slug(rec.get("judul") or "")
        expected = os.path.join(gap_dir, f"gap-{s}.md")
        if os.path.exists(expected):
            continue
        stems = [os.path.basename(p) for p in glob.glob(os.path.join(gap_dir, "gap-*.md"))]
        if any(s and s in stem for stem in stems):
            continue
        findings.append(Finding("warn",
                                f"belum ada laporan celah untuk '{rec.get('judul')}' (research/gap-{s}.md)"))

    if not any(f.level == "fail" for f in findings):
        findings.append(Finding("ok", f"{len(data)} judul tervalidasi ({len(selected)} terpilih)"))
    return findings
