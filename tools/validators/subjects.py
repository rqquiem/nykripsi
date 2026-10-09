"""Validator subjek: ``subjects/registry.json`` + ``subjects/index.md``."""

import json

from .base import Context, Finding, read, register

REQUIRED = ("id", "name", "aliases", "accessed", "channels", "queries",
            "saturation", "status")
CHANNELS = ("press", "news", "article", "official", "web")
STATUSES = {"incomplete", "complete"}


@register("subjects", "subjects/registry.json + subjects/index.md")
def run(ctx: Context) -> list[Finding]:
    findings: list[Finding] = []

    text = read("subjects/registry.json")
    if text is None:
        return [Finding("warn", "subjects/registry.json belum ada")]

    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return [Finding("fail", "subjects/registry.json bukan JSON valid")]

    if not isinstance(data, list):
        return [Finding("fail", "subjects/registry.json bukan array JSON")]

    # Hitung sumber bertanda subjek dari sources/registry.json (bila ada).
    subject_counts: dict[str, int] | None = None
    sources_text = read("sources/registry.json")
    if sources_text is not None:
        try:
            sources_data = json.loads(sources_text)
        except json.JSONDecodeError:
            sources_data = None
        if isinstance(sources_data, list):
            subject_counts = {}
            for src in sources_data:
                if isinstance(src, dict):
                    subj = src.get("subject")
                    if isinstance(subj, str):
                        subject_counts[subj] = subject_counts.get(subj, 0) + 1

    seen_ids: set[str] = set()
    n_complete = 0
    n_incomplete = 0

    for index, rec in enumerate(data):
        if not isinstance(rec, dict):
            findings.append(Finding("fail", f"catatan #{index} bukan objek JSON"))
            continue

        rid = rec.get("id")
        label = str(rid) if rid else f"#{index}"

        for key in REQUIRED:
            if key not in rec:
                findings.append(Finding("fail", f"subjek '{label}' tidak punya kunci '{key}'"))

        name = rec.get("name")
        if not isinstance(name, str) or not name.strip():
            findings.append(Finding("fail", f"subjek '{label}' punya name kosong / bukan string"))

        status = rec.get("status")
        if status not in STATUSES:
            findings.append(Finding("fail",
                                    f"subjek '{label}' punya status tidak dikenal '{status}'"))
        elif status == "complete":
            n_complete += 1
        else:
            n_incomplete += 1

        channels = rec.get("channels")
        channels_ok = True
        if not isinstance(channels, dict):
            findings.append(Finding("fail", f"subjek '{label}' channels bukan objek JSON"))
            channels_ok = False
        else:
            for ch in CHANNELS:
                if ch not in channels:
                    findings.append(Finding("fail", f"subjek '{label}' channels tidak punya '{ch}'"))
                    channels_ok = False
                    continue
                chrec = channels.get(ch)
                if not isinstance(chrec, dict):
                    findings.append(Finding("fail",
                                            f"subjek '{label}' kanal '{ch}' bukan objek JSON"))
                    channels_ok = False
                    continue
                req = chrec.get("required")
                if not isinstance(req, bool):
                    findings.append(Finding("fail",
                                            f"subjek '{label}' kanal '{ch}' required bukan bool"))
                    channels_ok = False
                cnt = chrec.get("count")
                if not isinstance(cnt, int) or isinstance(cnt, bool) or cnt < 0:
                    findings.append(Finding("fail",
                                            f"subjek '{label}' kanal '{ch}' count bukan int >= 0"))
                    channels_ok = False

        saturation = rec.get("saturation")
        saturation_ok = True
        if not isinstance(saturation, dict):
            findings.append(Finding("fail", f"subjek '{label}' saturation bukan objek JSON"))
            saturation_ok = False
        else:
            k = saturation.get("k")
            if not isinstance(k, int) or isinstance(k, bool) or k < 1:
                findings.append(Finding("fail",
                                        f"subjek '{label}' saturation.k bukan int >= 1"))
                saturation_ok = False
            barren = saturation.get("barren_rounds")
            if not isinstance(barren, int) or isinstance(barren, bool) or barren < 0:
                findings.append(Finding("fail",
                                        f"subjek '{label}' saturation.barren_rounds bukan int >= 0"))
                saturation_ok = False
            if not isinstance(saturation.get("saturated"), bool):
                findings.append(Finding("fail",
                                        f"subjek '{label}' saturation.saturated bukan bool"))
                saturation_ok = False

        # Aturan kelengkapan untuk subjek berstatus complete.
        if status == "complete" and channels_ok:
            for ch in CHANNELS:
                chrec = channels.get(ch)
                if isinstance(chrec, dict) and chrec.get("required") is True:
                    cnt = chrec.get("count")
                    if not (isinstance(cnt, int) and not isinstance(cnt, bool) and cnt >= 1):
                        findings.append(Finding(
                            "fail",
                            f"subjek '{name}' complete tetapi kanal '{ch}' kosong"))
            if saturation_ok and saturation.get("saturated") is not True:
                findings.append(Finding(
                    "fail",
                    f"subjek '{name}' complete tetapi belum saturasi"))

        # Konsistensi silang dengan sources/registry.json.
        if channels_ok and subject_counts is not None and isinstance(name, str):
            total = sum(ch.get("count", 0) for ch in channels.values()
                        if isinstance(ch, dict) and isinstance(ch.get("count"), int))
            tagged = subject_counts.get(name, 0)
            if total != tagged:
                findings.append(Finding(
                    "fail",
                    f"subjek '{name}' hitungan kanal ({total}) != "
                    f"sumber bertanda subjek ({tagged})"))

        if rid is not None:
            if rid in seen_ids:
                findings.append(Finding("fail", f"id duplikat '{rid}'"))
            seen_ids.add(rid)

    index_text = read("subjects/index.md")
    if index_text is None:
        findings.append(Finding("fail", "subjects/index.md tidak ditemukan"))
    else:
        for rid in sorted(seen_ids):
            if rid not in index_text:
                findings.append(Finding("fail", f"id '{rid}' tidak ada di subjects/index.md"))

    if not any(f.level == "fail" for f in findings):
        findings.append(Finding(
            "ok",
            f"{len(data)} subjek tervalidasi ({n_complete} complete, {n_incomplete} incomplete)"))
    return findings
