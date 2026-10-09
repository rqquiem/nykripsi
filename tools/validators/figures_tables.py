"""Validator diagram, tabel, dan caption (kerangka D1-D6).

Menegakkan docs/diagram-framework.md pada berkas final
``content/artikel/*.md`` + ``content/skripsi/1[0-5]-*.md`` (level fail) dan
``content/drafts/*.md`` (level warn):
  D1 caption wajib (Tabel di atas tabel; Gambar di bawah blok diagram);
  D2 penomoran <bab>.<n> (skripsi) / <n> (artikel) berurutan dari 1;
  D3 caption ringkas (tanpa titik akhir, <= 15 kata);
  D4 blok mermaid/chart/tikz ber-#fig-<slug> unik + aset ada (warn bila belum);
  D5 cross-reference 'Tabel <n>'/'Gambar <n>' harus punya caption;
  D6 tabel berheader + >= 2 baris data.
"""

import glob
import os
import re

from .base import Context, Finding, register

FINAL_GLOBS = ("content/artikel/*.md", "content/skripsi/1[0-5]-*.md")
DRAFT_GLOBS = ("content/drafts/*.md",)
BAB_RE = re.compile(r"^(\d\d)-bab-(\d\d)-")
TABLE_CAP_RE = re.compile(r"^Tabel\s+(\d+)(?:\.(\d+))?\s+(\S.*)$")
FIG_CAP_RE = re.compile(r"^Gambar\s+(\d+)(?:\.(\d+))?\s+(\S.*)$")
DIAGRAM_OPEN_RE = re.compile(r"^```\{\.(mermaid|chart|tikz|sintesa)\b([^}]*)\}")
ASSET_TPL = "assets/figures/{slug}.png"
MAKS_KATA = 15
MIN_BARIS = 2


def _bab_dari_nama(path: str) -> int | None:
    m = BAB_RE.match(os.path.basename(path))
    return int(m.group(1)) - 9 if m else None


def _blok(lines: list[str]):
    """Hasilkan (tutup, jenis, id) tiap blok diagram fenced.

    tutup = indeks baris fence penutup; caption 'Gambar' dicari mulai tutup+1.
    """
    i = 0
    while i < len(lines):
        m = DIAGRAM_OPEN_RE.match(lines[i].strip())
        if m:
            jenis, attrs = m.group(1), m.group(2)
            mid = re.search(r"#([A-Za-z0-9_:-]+)", attrs)
            j = i + 1
            while j < len(lines) and lines[j].strip() != "```":
                j += 1
            yield j, jenis, (mid.group(1) if mid else "")
            i = j + 1
        else:
            i += 1


def _caption_berikut(lines: list[str], start: int) -> tuple[int, str] | None:
    """Cari paragraf caption 'Gambar ...' pertama setelah `start`."""
    j = start
    while j < len(lines) and lines[j].strip() == "":
        j += 1
    if j < len(lines) and FIG_CAP_RE.match(lines[j].strip()):
        return j, lines[j].strip()
    return None


def _periksa_berkas(path: str, rel: str, level: str, root: str,
                    findings: list[Finding]) -> bool:
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().splitlines()
    bab = _bab_dari_nama(path)
    final = level == "fail"
    diuji = False

    def tambah(msg: str) -> None:
        findings.append(Finding(level, f"{rel}: {msg}"))

    # --- tabel: caption 'Tabel <n>' di baris tepat sebelum pipe table ---
    tabel_caps: set[tuple[int, int | None]] = set()
    tbl_seq: list[tuple[int, int | None]] = []
    for i, ln in enumerate(lines):
        m = TABLE_CAP_RE.match(ln.strip())
        if not m:
            continue
        diuji = True
        no, sub, judul = int(m.group(1)), (int(m.group(2)) if m.group(2) else None), m.group(3)
        tabel_caps.add((no, sub))
        tbl_seq.append((no, sub))
        if judul.rstrip().endswith("."):
            tambah(f"caption tabel D3: judul diakhiri titik ({ln.strip()!r})")
        if len(judul.split()) > MAKS_KATA:
            tambah(f"caption tabel D3: {len(judul.split())} kata (> {MAKS_KATA})")
        if final:
            if bab is not None:
                if sub is None or no != bab:
                    tambah(f"caption tabel D2: harus 'Tabel {bab}.<n>' (dapat 'Tabel {no}"
                           + (f".{sub}'" if sub is not None else "'") + ")")
            elif sub is not None:
                tambah(f"caption tabel D2: artikel harus 'Tabel <n>' tanpa bab (dapat 'Tabel {no}.{sub}')")
        # header + baris data
        k = i + 1
        while k < len(lines) and lines[k].strip() == "":
            k += 1
        if k >= len(lines) or not lines[k].lstrip().startswith("|"):
            tambah(f"caption tabel D1/D6: tidak ada pipe table tepat setelah caption {ln.strip()!r}")
        else:
            baris = 0
            kk = k
            while kk < len(lines) and lines[kk].lstrip().startswith("|"):
                baris += 1
                kk += 1
            data = baris - 2  # header + separator
            if data < MIN_BARIS:
                tambah(f"tabel D6: {data} baris data (< {MIN_BARIS})")

    if tbl_seq and final:
        expected = list(range(1, len(tbl_seq) + 1))
        got = [sub for _no, sub in tbl_seq] if bab is not None else [no for no, _ in tbl_seq]
        if got != expected:
            tambah(f"tabel D2: urutan nomor {got} != {expected}")

    # --- tabel TANPA caption (D1): pipe table tanpa paragraf 'Tabel <n>' di atas ---
    i = 0
    while i < len(lines):
        if lines[i].lstrip().startswith("|"):
            j = i
            while j < len(lines) and lines[j].lstrip().startswith("|"):
                j += 1
            k = i - 1
            while k >= 0 and lines[k].strip() == "":
                k -= 1
            if not (k >= 0 and TABLE_CAP_RE.match(lines[k].strip())):
                tambah(f"tabel D1: pipe table tanpa caption 'Tabel <n> <Judul>' (baris {i + 1})")
            i = j
        else:
            i += 1

    # --- blok diagram: id + caption 'Gambar' di bawah + aset ---
    fig_caps: set[tuple[int, int | None]] = set()
    fig_seq: list[tuple[int, int | None]] = []
    ids: set[str] = set()
    for tutup, jenis, ident in _blok(lines):
        diuji = True
        if not ident:
            tambah(f"blok {jenis} D4: tanpa id #fig-<slug>")
        elif ident in ids:
            tambah(f"blok {jenis} D4: id duplikat #{ident}")
        else:
            ids.add(ident)
        cap = _caption_berikut(lines, tutup + 1)
        if not cap:
            tambah(f"blok {jenis} D1: tidak ada caption 'Gambar <n> <Judul>' di bawah blok")
        else:
            cidx, ctext = cap
            m = FIG_CAP_RE.match(ctext)
            no, sub, judul = int(m.group(1)), (int(m.group(2)) if m.group(2) else None), m.group(3)
            fig_caps.add((no, sub))
            fig_seq.append((no, sub))
            if judul.rstrip().endswith("."):
                tambah(f"caption gambar D3: judul diakhiri titik ({ctext!r})")
            if len(judul.split()) > MAKS_KATA:
                tambah(f"caption gambar D3: {len(judul.split())} kata (> {MAKS_KATA})")
            if final:
                if bab is not None:
                    if sub is None or no != bab:
                        tambah(f"caption gambar D2: harus 'Gambar {bab}.<n>' (dapat {ctext!r})")
                elif sub is not None:
                    tambah(f"caption gambar D2: artikel harus 'Gambar <n>' (dapat {ctext!r})")
            _ = cidx
        if ident:
            if not os.path.exists(os.path.join(root, ASSET_TPL.format(slug=ident))):
                findings.append(Finding(
                    "warn", f"{rel}: aset {ASSET_TPL.format(slug=ident)} belum ada (jalankan make diagrams)"))

    if fig_seq and final:
        expected = list(range(1, len(fig_seq) + 1))
        got = [sub for _no, sub in fig_seq] if bab is not None else [no for no, _ in fig_seq]
        if got != expected:
            tambah(f"gambar D2: urutan nomor {got} != {expected}")

    # --- cross-reference D5 ---
    semua = tabel_caps | fig_caps
    for i, ln in enumerate(lines):
        if TABLE_CAP_RE.match(ln.strip()) or FIG_CAP_RE.match(ln.strip()):
            continue
        for m in re.finditer(r"\b(Tabel|Gambar)\s+(\d+)(?:\.(\d+))?", ln):
            diuji = True
            no = int(m.group(2))
            sub = int(m.group(3)) if m.group(3) else None
            if (no, sub) not in semua:
                tambah(f"D5: rujukan '{m.group(0)}' tidak punya caption")
    return diuji


@register("figures_tables", "content/{artikel,skripsi}/** + content/drafts (caption & penomoran)")
def run(ctx: Context) -> list[Finding]:
    findings: list[Finding] = []
    diperiksa = 0
    for g in FINAL_GLOBS:
        for path in sorted(glob.glob(os.path.join(ctx.root, g))):
            rel = os.path.relpath(path, ctx.root)
            _periksa_berkas(path, rel, "fail", ctx.root, findings)
            diperiksa += 1
    for g in DRAFT_GLOBS:
        for path in sorted(glob.glob(os.path.join(ctx.root, g))):
            rel = os.path.relpath(path, ctx.root)
            _periksa_berkas(path, rel, "warn", ctx.root, findings)
    if not any(f.level == "fail" for f in findings):
        findings.append(Finding(
            "ok", f"diagram & tabel patuh kerangka D1-D6 pada {diperiksa} berkas final"))
    return findings
