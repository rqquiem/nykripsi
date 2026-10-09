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
    "content/skripsi/1[0-5]-*.md",
    "content/drafts/*.md",
)
DIAGRAM_OPEN_RE = re.compile(r"^```\{\.(mermaid|chart|tikz|sintesa)\b([^}]*)\}")
ASSET_DIR = "assets/figures"
MERMAID_TIMEOUT = 120


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
    from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

    spec = yaml.safe_load(body) or {}
    teori = spec.get("teori") or []
    lensa = spec.get("lensa") or {}
    lintas = spec.get("lintas_tahap") or []
    tahap = spec.get("tahap") or []
    if not isinstance(teori, list) or len(teori) < 2:
        raise ValueError("sintesa butuh 'teori' >= 2")
    if not isinstance(lensa, dict) or not lensa.get("nama") \
            or len(lensa.get("gabungan") or []) < 2:
        raise ValueError("sintesa butuh 'lensa.nama' + 'lensa.gabungan' >= 2")
    if not isinstance(tahap, list) or len(tahap) < 2:
        raise ValueError("sintesa butuh 'tahap' >= 2")

    fig = plt.figure(figsize=(8, 5))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    def kotak(x, y, w, h, teks, warna):
        ax.add_patch(FancyBboxPatch(
            (x, y), w, h, boxstyle="round,pad=0.008",
            linewidth=0.8, edgecolor="#444444", facecolor=warna))
        ax.text(x + w / 2, y + h / 2, teks, ha="center", va="center", fontsize=8)

    ax.text(0.5, 0.97, spec.get("judul") or lensa["nama"], ha="center",
            va="top", fontsize=11, fontweight="bold")

    n = len(teori)
    for i, t in enumerate(teori):
        w = 0.9 / n
        kotak(0.05 + i * w, 0.72, w * 0.92, 0.16,
              f"{t.get('nama', '')}\n({t.get('peran', '')})", "#eaf2fb")

    kotak(0.05, 0.40, 0.52, 0.20,
          lensa["nama"] + "\n= " + " + ".join(lensa.get("gabungan") or []),
          "#e8f5e9")
    nl = len(lintas)
    for i, l in enumerate(lintas):
        h = 0.20 / nl
        kotak(0.62, 0.60 - (i + 1) * h, 0.33, h * 0.9,
              f"{l.get('nama', '')}\n({l.get('peran', '')})", "#fff3e0")

    m = len(tahap)
    for i, s in enumerate(tahap):
        w = 0.9 / m
        x = 0.05 + i * w
        kotak(x, 0.08, w * 0.85, 0.16, str(s), "#f3e5f5")
        if i:
            ax.add_patch(FancyArrowPatch(
                (x - w * 0.13, 0.16), (x - 0.005, 0.16),
                arrowstyle="-|>", mutation_scale=8, color="#555555"))

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
