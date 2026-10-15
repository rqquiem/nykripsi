"""Validator bagan simpul-sisi / pohon (kerangka BG1-BG5).

Menegakkan docs/bagan-diagram-framework.md pada blok berkode berkelas ``bagan``
di ``content/artikel/*.md`` + ``content/skripsi/1[0-5]-*.md`` (level fail) dan
``content/drafts/*.md`` (level warn):
  BG1 blok bagan ber-YAML sah (mapping dengan kunci 'simpul');
  BG2 'simpul' >= 2, tiap simpul punya 'id' + 'teks' tak kosong, id unik;
  BG3 tiap 'induk' menunjuk id yang ada, graf asiklik, >= 1 akar;
  BG4 'sisi' (bila ada) tiap entri punya 'dari' + 'ke' yang menunjuk id ada;
  BG5 bagan terhubung: tiap simpul terjangkau dari sebuah akar.
"""

import glob
import os
import re

import yaml

from .base import Context, Finding, register

FINAL_GLOBS = ("content/artikel/*.md", "content/skripsi/1[0-5]-*.md")
DRAFT_GLOBS = ("content/drafts/*.md",)
BAGAN_OPEN_RE = re.compile(r"^```\{\.bagan\b([^}]*)\}")


def _blok_bagan(lines: list[str]):
    """Hasilkan (baris_buka, baris_tutup, body) tiap blok bagan."""
    i = 0
    while i < len(lines):
        if BAGAN_OPEN_RE.match(lines[i].strip()):
            j = i + 1
            while j < len(lines) and lines[j].strip() != "```":
                j += 1
            yield i, j, "\n".join(lines[i + 1:j])
            i = j + 1
        else:
            i += 1


def _periksa(path: str, rel: str, level: str, findings: list[Finding]) -> bool:
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().splitlines()
    blocks = list(_blok_bagan(lines))
    if not blocks:
        return False
    diuji = True

    def tambah(msg: str) -> None:
        findings.append(Finding(level, f"{rel}: {msg}"))

    for buka, _tutup, body in blocks:
        try:
            spec = yaml.safe_load(body)
        except yaml.YAMLError as exc:
            tambah(f"bagan BG1: YAML tidak sah (baris {buka + 1}): {exc}")
            continue
        if not isinstance(spec, dict) or "simpul" not in spec:
            tambah(f"bagan BG1: badan bukan mapping atau tanpa 'simpul' (baris {buka + 1})")
            continue

        simpul = spec.get("simpul")
        if not isinstance(simpul, list) or len(simpul) < 2:
            tambah("bagan BG2: 'simpul' harus list >= 2")
            continue

        ids: list[str] = []
        induk: dict[str, str] = {}
        rusak = False
        for s in simpul:
            if not isinstance(s, dict) or not str(s.get("id", "")).strip() \
                    or not str(s.get("teks", "")).strip():
                tambah("bagan BG2: setiap simpul butuh 'id' dan 'teks'")
                rusak = True
                continue
            sid = str(s["id"]).strip()
            if sid in induk:
                tambah(f"bagan BG2: id duplikat '{sid}'")
                rusak = True
                continue
            ids.append(sid)
            induk[sid] = str(s.get("induk", "")).strip()
        if rusak:
            continue

        ok_induk = True
        for sid, par in induk.items():
            if par and par not in induk:
                tambah(f"bagan BG3: induk '{par}' tidak ada (simpul '{sid}')")
                ok_induk = False
        akar = [sid for sid, par in induk.items() if not par]
        if not akar:
            tambah("bagan BG3: tidak ada akar (semua simpul punya 'induk')")
            ok_induk = False

        # deteksi siklus pada graf induk (DFS warna)
        warna: dict[str, int] = {sid: 0 for sid in induk}
        siklus = False

        def dfs(sid: str) -> None:
            nonlocal siklus
            warna[sid] = 1
            par = induk[sid]
            if par and par in induk:
                if warna[par] == 1:
                    siklus = True
                elif warna[par] == 0:
                    dfs(par)
            warna[sid] = 2

        for sid in induk:
            if warna[sid] == 0:
                dfs(sid)
        if siklus:
            tambah("bagan BG3: graf 'induk' memuat siklus")
            ok_induk = False
        if not ok_induk:
            continue

        sisi = spec.get("sisi") or []
        if not isinstance(sisi, list):
            tambah("bagan BG4: 'sisi' harus list")
            sisi = []
        for e in sisi:
            if not isinstance(e, dict) or str(e.get("dari", "")).strip() not in induk \
                    or str(e.get("ke", "")).strip() not in induk:
                tambah("bagan BG4: setiap sisi butuh 'dari' + 'ke' yang menunjuk id ada")

        # keterhubungan: BFS dari akar lewat induk-anak dan sisi
        anak: dict[str, list[str]] = {sid: [] for sid in induk}
        for sid, par in induk.items():
            if par:
                anak[par].append(sid)
        tetangga = {sid: set(anak[sid]) for sid in induk}
        for sid in induk:
            if induk[sid]:
                tetangga[sid].add(induk[sid])
        for e in sisi:
            if isinstance(e, dict):
                a, b = str(e.get("dari", "")).strip(), str(e.get("ke", "")).strip()
                if a in induk and b in induk:
                    tetangga[a].add(b)
                    tetangga[b].add(a)
        terlihat = set(akar)
        queue = list(akar)
        while queue:
            cur = queue.pop(0)
            for nb in tetangga[cur]:
                if nb not in terlihat:
                    terlihat.add(nb)
                    queue.append(nb)
        for sid in induk:
            if sid not in terlihat:
                tambah(f"bagan BG5: simpul '{sid}' tidak terhubung ke akar")
    return diuji


@register("bagan_diagram", "content/{artikel,skripsi}/** + content/drafts (bagan simpul-sisi)")
def run(ctx: Context) -> list[Finding]:
    findings: list[Finding] = []
    diperiksa = 0
    for g in FINAL_GLOBS:
        for path in sorted(glob.glob(os.path.join(ctx.root, g))):
            rel = os.path.relpath(path, ctx.root)
            _periksa(path, rel, "fail", findings)
            diperiksa += 1
    for g in DRAFT_GLOBS:
        for path in sorted(glob.glob(os.path.join(ctx.root, g))):
            rel = os.path.relpath(path, ctx.root)
            _periksa(path, rel, "warn", findings)
            diperiksa += 1
    if not any(f.level == "fail" for f in findings):
        findings.append(Finding(
            "ok", f"bagan simpul-sisi patuh kerangka BG1-BG5 pada {diperiksa} berkas final"))
    return findings
