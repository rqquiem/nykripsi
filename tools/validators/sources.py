"""Validator sumber: ``sources/registry.json`` + ``sources/index.md``."""

import json
import re

from .base import Context, Finding, read, register

ALLOWED = {"news", "article", "book", "interview", "dataset", "publicdata", "company", "pdf",
           "web", "forum", "video"}
REQUIRED = ("id", "type", "title", "url", "backend", "accessed", "source_class")
CLASSES = {"primary", "secondary"}
ORIGINS = {"auto", "manual"}
ACCESS_LEVELS = {"fulltext", "abstract-only", "inaccessible"}
FULLTEXT_FIELDS = ("fulltext_url", "fulltext_sha256", "fulltext_pages", "fulltext_verified")


@register("sources", "sources/registry.json + sources/index.md")
def run(ctx: Context) -> list[Finding]:
    findings: list[Finding] = []

    text = read("sources/registry.json")
    if text is None:
        return [Finding("warn", "sources/registry.json belum ada")]

    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return [Finding("fail", "registry.json bukan JSON valid")]

    if not isinstance(data, list):
        return [Finding("fail", "registry.json bukan array JSON")]

    seen_ids: set[str] = set()
    seen_urls: set[str] = set()

    for index, rec in enumerate(data):
        if not isinstance(rec, dict):
            findings.append(Finding("fail", f"catatan #{index} bukan objek JSON"))
            continue

        rid = rec.get("id")
        label = str(rid) if rid else f"#{index}"

        for key in REQUIRED:
            if key not in rec:
                findings.append(Finding("fail", f"sumber '{label}' tidak punya kunci '{key}'"))

        rtype = rec.get("type")
        if rtype not in ALLOWED:
            findings.append(Finding("fail", f"sumber '{label}' punya tipe tidak dikenal '{rtype}'"))

        sclass = rec.get("source_class")
        if sclass not in CLASSES:
            findings.append(Finding("fail",
                                    f"sumber '{label}' punya source_class tidak dikenal '{sclass}'"))
        origin = rec.get("class_origin")
        if origin is not None and origin not in ORIGINS:
            findings.append(Finding("fail",
                                    f"sumber '{label}' punya class_origin tidak dikenal '{origin}'"))

        level = rec.get("access_level")
        if "access_level" not in rec:
            findings.append(Finding("fail", f"sumber '{label}' tidak punya kunci 'access_level'"))
        elif level not in ACCESS_LEVELS:
            findings.append(Finding("fail",
                                    f"sumber '{label}' punya access_level tidak dikenal '{level}'"))
        elif level == "fulltext":
            for key in FULLTEXT_FIELDS:
                if key not in rec:
                    findings.append(Finding("fail",
                                            f"sumber '{label}' fulltext tidak punya kunci '{key}'"))
            ft_url = rec.get("fulltext_url")
            if not isinstance(ft_url, str) or not ft_url.strip():
                findings.append(Finding("fail",
                                        f"sumber '{label}' fulltext_url kosong / bukan string"))
            sha = rec.get("fulltext_sha256")
            if not isinstance(sha, str) or not re.fullmatch(r"[0-9a-fA-F]{64}", sha):
                findings.append(Finding("fail",
                                        f"sumber '{label}' fulltext_sha256 bukan hex 64 karakter"))
            pages = rec.get("fulltext_pages")
            if not isinstance(pages, int) or isinstance(pages, bool) or pages < 2:
                findings.append(Finding("fail",
                                        f"sumber '{label}' fulltext_pages bukan int >= 2"))
            if rec.get("fulltext_verified") is not True:
                findings.append(Finding("fail",
                                        f"sumber '{label}' fulltext_verified bukan True"))
        # abstract-only / inaccessible: tidak ada syarat tambahan (aturan F6
        # melarang keduanya dipakai sebagai dasar kesimpulan).

        url = rec.get("url")
        if not isinstance(url, str) or not url.strip():
            findings.append(Finding("fail", f"sumber '{label}' punya url kosong"))

        if rid is not None:
            if rid in seen_ids:
                findings.append(Finding("fail", f"id duplikat '{rid}'"))
            seen_ids.add(rid)
        if isinstance(url, str) and url.strip():
            low = url.strip().lower()
            if low in seen_urls:
                findings.append(Finding("fail", f"url duplikat '{url}'"))
            seen_urls.add(low)

    index_text = read("sources/index.md")
    if index_text is None:
        findings.append(Finding("fail", "sources/index.md tidak ditemukan"))
    else:
        for rid in sorted(seen_ids):
            if rid not in index_text:
                findings.append(Finding("fail", f"id '{rid}' tidak ada di sources/index.md"))

    if not any(f.level == "fail" for f in findings):
        p = sum(1 for r in data if isinstance(r, dict) and r.get("source_class") == "primary")
        s = sum(1 for r in data if isinstance(r, dict) and r.get("source_class") == "secondary")
        f = sum(1 for r in data if isinstance(r, dict) and r.get("access_level") == "fulltext")
        a = sum(1 for r in data if isinstance(r, dict) and r.get("access_level") == "abstract-only")
        i = sum(1 for r in data if isinstance(r, dict) and r.get("access_level") == "inaccessible")
        findings.append(Finding(
            "ok",
            f"{len(data)} sumber tervalidasi ({p} primer, {s} sekunder; "
            f"{f} fulltext, {a} abstract-only, {i} inaccessible)"))
    return findings
