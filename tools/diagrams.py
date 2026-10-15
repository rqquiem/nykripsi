#!/usr/bin/env python3
"""Render sumber diagram Markdown menjadi aset gambar (kerangka D1-D6).

Blok berkode berkelas ``mermaid``/``chart``/``tikz`` dirender ke
``assets/figures/<id>.png`` (``id`` = ``#fig-...`` pada atribut blok).
Mermaid butuh Node + unduhan sekali (daring); chart (matplotlib) dan tikz
(xelatex + pdftoppm) berjalan luring. Kegagalan satu blok tidak menghentikan
blok lain.
"""

import argparse
import glob
import os
import re
import shutil
import subprocess
import sys
import tempfile

import yaml

GLOBS = (
    "content/artikel/*.md",
    "content/artikel-en/*.md",
    "content/skripsi/1[0-5]-*.md",
    "content/drafts/*.md",
)
DIAGRAM_OPEN_RE = re.compile(r"^```\{\.(mermaid|chart|tikz|sintesa|bagan)\b([^}]*)\}")
ASSET_DIR = "assets/figures"
MERMAID_TIMEOUT = 120


def _wrap(teks: str, lebar: int) -> list[str]:
    """Bungkus `teks` menjadi baris <= `lebar` karakter (kata utuh)."""
    kata, baris, cur = str(teks).split(), [], ""
    for w in kata:
        if cur and len(cur) + 1 + len(w) > lebar:
            baris.append(cur); cur = w
        else:
            cur = f"{cur} {w}".strip()
    if cur:
        baris.append(cur)
    return baris or [""]

def _kotak(ax, x, y, w, h, teks, warna, lebar_kar=18, fs=8):
    """Kotak ber-`w`/`h` dengan teks terbungkus di tengah; kembalikan (x_tengah, y_tengah)."""
    from matplotlib.patches import FancyBboxPatch
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.008",
                 linewidth=0.8, edgecolor="#444444", facecolor=warna))
    baris = _wrap(teks, lebar_kar)
    ax.text(x + w / 2, y + h / 2, "\n".join(baris), ha="center", va="center", fontsize=fs)
    return x + w / 2, y + h / 2

def _panah(ax, x0, y0, x1, y1):
    """Garis sambung berujung panah dari (x0,y0) ke (x1,y1)."""
    from matplotlib.patches import FancyArrowPatch
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>",
                 mutation_scale=8, color="#555555", linewidth=0.8))


def _blok(root: str):
    for g in GLOBS:
        for path in sorted(glob.glob(os.path.join(root, g))):
            lines = open(path, encoding="utf-8").read().splitlines()
            i = 0
            while i < len(lines):
                m = DIAGRAM_OPEN_RE.match(lines[i].strip())
                if not m:
                    i += 1
                    continue
                jenis, attrs = m.group(1), m.group(2)
                mid = re.search(r"#([A-Za-z0-9_:-]+)", attrs)
                body: list[str] = []
                j = i + 1
                while j < len(lines) and lines[j].strip() != "```":
                    body.append(lines[j])
                    j += 1
                yield (os.path.relpath(path, root), i + 1, jenis,
                       (mid.group(1) if mid else ""), "\n".join(body))
                i = j + 1


def _render_chart(body: str, png: str) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    spec = yaml.safe_load(body) or {}
    if spec.get("type") not in ("bar", "line", "pie"):
        raise ValueError("chart 'type' harus bar|line|pie")
    x, y = spec.get("x"), spec.get("y")
    if x is None or y is None:
        raise ValueError("chart butuh 'x' dan 'y'")
    fig = plt.figure(figsize=(4, 3))
    if spec["type"] == "bar":
        plt.bar(x, y)
    elif spec["type"] == "line":
        plt.plot(x, y, marker="o")
    else:
        plt.pie(y, labels=x, autopct="%1.1f%%")
    if spec.get("title"):
        plt.title(spec["title"])
    if spec.get("xlabel"):
        plt.xlabel(spec["xlabel"])
    if spec.get("ylabel"):
        plt.ylabel(spec["ylabel"])
    fig.savefig(png, dpi=150, bbox_inches="tight")
    plt.close(fig)


def _render_tikz(body: str, png: str, tmp: str) -> None:
    tex = os.path.join(tmp, "tik.tex")
    doc = ("\\documentclass[tikz,border=2pt]{standalone}\n"
           "\\usepackage{tikz}\n\\begin{document}\n" + body + "\n\\end{document}\n")
    with open(tex, "w", encoding="utf-8") as fh:
        fh.write(doc)
    subprocess.run(["xelatex", "-interaction=nonstopmode", "-halt-on-error",
                    "tik.tex"], cwd=tmp, check=True, capture_output=True)
    stem = os.path.join(tmp, "tik")
    subprocess.run(["pdftoppm", "-png", "-r", "300", stem + ".pdf", stem],
                   check=True, capture_output=True)
    shutil.move(stem + "-1.png", png)


def _render_mermaid(body: str, png: str, tmp: str) -> None:
    mmd = os.path.join(tmp, "diag.mmd")
    with open(mmd, "w", encoding="utf-8") as fh:
        fh.write(body + "\n")
    if shutil.which("npx") is None:
        raise RuntimeError("npx tidak ada")
    subprocess.run(
        ["npx", "-y", "@mermaid-js/mermaid-cli", "-i", mmd, "-o", png,
         "-b", "white", "-w", "1600"],
        check=True, capture_output=True, timeout=MERMAID_TIMEOUT,
    )


def _render_sintesa(body: str, png: str) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    spec = yaml.safe_load(body) or {}
    if not isinstance(spec, dict):
        raise ValueError("sintesa: badan harus mapping YAML")

    lensa = spec.get("lensa")
    if not isinstance(lensa, dict) or not str(lensa.get("nama", "")).strip():
        raise ValueError("sintesa: butuh 'lensa.nama' tak kosong")
    if not isinstance(lensa.get("gabungan"), list) or len(lensa["gabungan"]) < 2:
        raise ValueError("sintesa: butuh 'lensa.gabungan' >= 2")

    utama = spec.get("teori_utama")
    if not isinstance(utama, dict) or not str(utama.get("nama", "")).strip() \
            or not str(utama.get("peran", "")).strip():
        raise ValueError("sintesa: butuh 'teori_utama' dengan 'nama' + 'peran'")

    def daftar_peran(kunci: str) -> list[dict]:
        val = spec.get(kunci)
        if not isinstance(val, list) or not val:
            raise ValueError(f"sintesa: butuh '{kunci}' list >= 1")
        for it in val:
            if not isinstance(it, dict) or not str(it.get("nama", "")).strip() \
                    or not str(it.get("peran", "")).strip():
                raise ValueError(f"sintesa: '{kunci}' tiap entri butuh 'nama' + 'peran'")
        return val

    pendukung = daftar_peran("teori_pendukung")
    cabang = daftar_peran("cabang_bukti")

    lingkup = spec.get("lingkup")
    if not isinstance(lingkup, list) or not lingkup \
            or any(not str(s).strip() for s in lingkup):
        raise ValueError("sintesa: butuh 'lingkup' list >= 1 string tak kosong")

    judul = spec.get("judul") or lensa["nama"]

    def label(it: dict) -> str:
        return f"{it['nama']}\n({it['peran']})"

    # L0 judul, L1 teori_utama, L2 teori_pendukung, L3 cabang_bukti, L4 lingkup
    L1 = [label(utama)]
    L2 = [label(t) for t in pendukung]
    L3 = [label(c) for c in cabang]
    L4 = [str(s) for s in lingkup]

    n_max = max(len(L2), len(L3), len(L4))
    w = 0.9 / n_max
    lebar_kar = max(12, int(w * 90))
    gap = 0.06
    jumlah_lapisan = 5

    def tinggi(items: list[str]) -> float:
        return 0.055 * max(len(_wrap(t, lebar_kar)) for t in items)

    tinggi_lapisan = [0.06, tinggi(L1), tinggi(L2), tinggi(L3), tinggi(L4)]
    warna = [None, "#eaf2fb", "#e8f5e9", "#fff3e0", "#f3e5f5"]
    isi = [None, L1, L2, L3, L4]

    fig = plt.figure(figsize=(8.5, 1.2 + 1.05 * jumlah_lapisan))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    tengah: dict[tuple[int, int], tuple[float, float]] = {}
    y_top = 1.0
    for li in range(jumlah_lapisan):
        h = tinggi_lapisan[li]
        y0 = y_top - h
        items = isi[li]
        if li == 0:
            ax.text(0.5, y_top - h / 2, judul, ha="center", va="center",
                    fontsize=11, fontweight="bold")
        else:
            n = len(items)
            for i, teks in enumerate(items):
                x = (1.0 - n * w) / 2 + i * w
                tengah[(li, i)] = _kotak(ax, x, y0, w, h, teks, warna[li],
                                         lebar_kar=lebar_kar)
        y_top = y0 - gap

    def terdekat(n_src: int, n_dst: int, j: int) -> int:
        if n_src <= 1:
            return 0
        return round(j * (n_dst - 1) / (n_src - 1))

    for j in range(len(L2)):
        _panah(ax, *tengah[(1, 0)], *tengah[(2, j)])
    for j in range(len(L2)):
        _panah(ax, *tengah[(2, j)], *tengah[(3, terdekat(len(L2), len(L3), j))])
    for j in range(len(L3)):
        _panah(ax, *tengah[(3, j)], *tengah[(4, terdekat(len(L3), len(L4), j))])

    fig.savefig(png, dpi=150, bbox_inches="tight")
    plt.close(fig)

def _render_bagan(body: str, png: str) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import FancyBboxPatch

    spec = yaml.safe_load(body) or {}
    simpul = spec.get("simpul") or []
    sisi = spec.get("sisi") or []
    if not isinstance(simpul, list) or len(simpul) < 2:
        raise ValueError("bagan butuh 'simpul' >= 2")
    ids: list[str] = []
    teks: dict[str, str] = {}
    induk: dict[str, str] = {}
    for s in simpul:
        if not isinstance(s, dict) or not str(s.get("id", "")).strip() \
                or not str(s.get("teks", "")).strip():
            raise ValueError("bagan tiap simpul butuh 'id' + 'teks'")
        sid = str(s["id"]).strip()
        if sid in teks:
            raise ValueError(f"bagan id duplikat: {sid}")
        ids.append(sid)
        teks[sid] = str(s["teks"]).strip()
        induk[sid] = str(s.get("induk", "")).strip()
    for sid, par in induk.items():
        if par and par not in teks:
            raise ValueError(f"bagan induk '{par}' tidak ada (simpul '{sid}')")
    for e in sisi:
        if not isinstance(e, dict) or str(e.get("dari", "")).strip() not in teks \
                or str(e.get("ke", "")).strip() not in teks:
            raise ValueError("bagan tiap sisi butuh 'dari' + 'ke' yang ada")

    anak: dict[str, list[str]] = {sid: [] for sid in ids}
    akar: list[str] = []
    for sid in ids:
        if induk[sid]:
            anak[induk[sid]].append(sid)
        else:
            akar.append(sid)

    # kedalaman BFS dari akar
    depth: dict[str, int] = {}
    queue = list(akar)
    for sid in akar:
        depth[sid] = 0
    while queue:
        cur = queue.pop(0)
        for ch in anak[cur]:
            depth[ch] = depth[cur] + 1
            queue.append(ch)

    # posisi-x: daun diberi kolom berurutan (DFS), simpul dalam = rata-rata anak
    xpos: dict[str, float] = {}
    counter = [0]

    def tetapkan(sid: str) -> float:
        if not anak[sid]:
            xpos[sid] = float(counter[0])
            counter[0] += 1
        else:
            xs = [tetapkan(c) for c in anak[sid]]
            xpos[sid] = sum(xs) / len(xs)
        return xpos[sid]

    for sid in akar:
        tetapkan(sid)
    maks_d = max(depth.values()) if depth else 0
    lebar = max(1, counter[0])

    # lebar kotak dihitung dari jumlah kotak pada tingkat terdalam (kolom terpadat)
    kolom_per_tingkat: dict[int, int] = {}
    for sid in ids:
        d = depth.get(sid, maks_d + 1)
        kolom_per_tingkat[d] = kolom_per_tingkat.get(d, 0) + 1
    n_terdalam = max(kolom_per_tingkat.values()) if kolom_per_tingkat else 1
    bw = min(0.9, 0.9 * lebar / max(1, n_terdalam))
    lebar_kar = max(8, int((bw / lebar) * 90))

    def bbox_h(sid: str) -> float:
        nbaris = len(_wrap(teks[sid], lebar_kar))
        return min(0.78, 0.2 * nbaris + 0.22)

    # figsize tumbuh bersama kedalaman (baris) dan jumlah daun (kolom)
    fig = plt.figure(figsize=(max(8.0, 1.1 * lebar), 0.9 + 0.9 * (maks_d + 1)))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(-0.5, lebar - 0.5)
    ax.set_ylim(-0.5, maks_d + 0.9)
    ax.axis("off")
    ax.text((lebar - 1) / 2, maks_d + 0.85, spec.get("judul") or "Bagan",
            ha="center", va="top", fontsize=11, fontweight="bold")

    for sid in ids:
        if sid not in depth:      # tak terjangkau dari akar: taruh di baris dasar
            depth[sid] = maks_d + 1
            xpos[sid] = float(counter[0])
            counter[0] += 1
        x, y = xpos[sid], maks_d - depth[sid]
        bh = bbox_h(sid)
        ax.add_patch(FancyBboxPatch(
            (x - bw / 2, y - bh / 2), bw, bh,
            boxstyle="round,pad=0.02", linewidth=0.8,
            edgecolor="#444444", facecolor="#eaf2fb"))
        ax.text(x, y, "\n".join(_wrap(teks[sid], lebar_kar)),
                ha="center", va="center", fontsize=7)
        par = induk[sid]
        if par and par in depth:
            xp, yp = xpos[par], maks_d - depth[par]
            yb = yp - bbox_h(par) / 2   # dasar kotak induk
            yt = y + bh / 2             # puncak kotak anak
            ym = (yb + yt) / 2
            ax.plot([xp, xp], [yb, ym], color="#555555", linewidth=0.8)
            ax.plot([xp, x], [ym, ym], color="#555555", linewidth=0.8)
            ax.plot([x, x], [ym, yt], color="#555555", linewidth=0.8)

    for e in sisi:
        xd, yd = xpos[str(e["dari"]).strip()], maks_d - depth[str(e["dari"]).strip()]
        xk, yk = xpos[str(e["ke"]).strip()], maks_d - depth[str(e["ke"]).strip()]
        ax.plot([xd, xk], [yd, yk], color="#b71c1c", linewidth=0.7, linestyle="--")

    fig.savefig(png, dpi=150, bbox_inches="tight")
    plt.close(fig)

def cmd_list(root: str) -> int:
    for rel, ln, jenis, ident, _ in _blok(root):
        print(f"{rel}:{ln} {jenis} #{ident or '(tanpa id)'}")
    return 0


def cmd_render(root: str) -> int:
    dibuat = dilewati = 0
    os.makedirs(os.path.join(root, ASSET_DIR), exist_ok=True)
    for rel, ln, jenis, ident, body in _blok(root):
        if not ident:
            print(f"GAGAL: blok tanpa id di {rel}:{ln}")
            dilewati += 1
            continue
        png = os.path.join(root, ASSET_DIR, ident + ".png")
        tmp = tempfile.mkdtemp(prefix="diagrams-")
        try:
            if jenis == "chart":
                _render_chart(body, png)
            elif jenis == "tikz":
                _render_tikz(body, png, tmp)
            elif jenis == "sintesa":
                _render_sintesa(body, png)
            elif jenis == "bagan":
                _render_bagan(body, png)
            else:
                _render_mermaid(body, png, tmp)
            dibuat += 1
            print(f"OK: {png}")
        except Exception as exc:  # noqa: BLE001
            print(f"GAGAL: {jenis} {ident} ({exc})")
            dilewati += 1
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
    print(f"RENDER: {dibuat} aset dibuat, {dilewati} dilewati.")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Render sumber diagram -> assets/figures/.")
    ap.add_argument("cmd", nargs="?", default="render", choices=("render", "list"))
    ap.add_argument("--root", default=".")
    args = ap.parse_args(argv)
    return cmd_list(args.root) if args.cmd == "list" else cmd_render(args.root)


if __name__ == "__main__":
    sys.exit(main())
