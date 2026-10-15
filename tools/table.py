#!/usr/bin/env python3
"""Renderer tabel dari blok ```{.table}``` (YAML) ke LaTeX / DOCX (openxml).

Pemakaian:
  python3 tools/table.py --format {latex,docx} [--caption "Tabel 1 Judul"]   # YAML via stdin
  python3 tools/table.py --check                                            # pindai content/

Skema YAML (isi blok ```{.table}```):
  judul: "Ringkasan"                 # opsional
  kolom:                             # wajib, >= 1
    - {judul: "Sumber", lebar: 0.45, rata: kiri}
  baris:                             # wajib, >= 1
    - ["Lahan", "$A_1$"]
    - ["Air", {rumus: "=SUM(B1:B1)"}]
  border: {luar: {...}, dalam: {...}, warna: "#1F4E79", gaya: solid}
  isi: {kepala: "#FFF2CC", zebra: ["#FFFFFF", "#F2F2F2"]}
  gabung: [{baris: 2, kolom: 1, tinggi: 2, lebar: 1}]

Sel: string, angka, pemetaan {rumus: "=..."}, atau string berawalan "=".
Rumus: =FUNC(args) dengan FUNC dalam {SUM, AVERAGE, AVG, MIN, MAX, COUNT, ROUND};
arg berupa angka, rujukan sel X<n> (huruf kolom 1-basis -> indeks 0; n = indeks
baris DATA 1-basis), atau rentang X1:Y2. ROUND(value, digits) menerima 2 argumen.
"""

import argparse
import glob
import os
import re
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
TABLE_OPEN_RE = re.compile(r"^```\{\.table\b([^}]*)\}")
MATH_RE = re.compile(r"\$[^$]*\$")
REF_RE = re.compile(r"^([A-Za-z]+)(\d+)$")
RANGE_RE = re.compile(r"^([A-Za-z]+)(\d+):([A-Za-z]+)(\d+)$")
FUNC_RE = re.compile(r"^([A-Za-z]+)\s*\((.*)\)$", re.DOTALL)

RATA_MAP = {
    "kiri": "l", "left": "l", "l": "l",
    "kanan": "r", "right": "r", "r": "r",
    "tengah": "c", "center": "c", "centre": "c", "c": "c",
}
GAYA_MAP = {"solid": "single", "dashed": "dashed", "dotted": "dotted"}
LATEX_SPECIALS = {
    "&": r"\&", "%": r"\%", "_": r"\_", "#": r"\#",
    "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}",
}


class TableError(ValueError):
    """Kesalahan skema atau evaluasi rumus."""


# --- utilitas umum ---------------------------------------------------------

def _col_index(letters: str) -> int:
    idx = 0
    for ch in letters.upper():
        idx = idx * 26 + (ord(ch) - ord("A") + 1)
    return idx - 1


def _fmt_num(v) -> str:
    if isinstance(v, float) and v.is_integer():
        return str(int(v))
    return str(v)


def _is_number(v) -> bool:
    return isinstance(v, (int, float)) and not isinstance(v, bool)


def esc_text(s: str) -> str:
    return "".join(LATEX_SPECIALS.get(ch, ch) for ch in s)


def esc_latex_cell(s: str) -> str:
    out, i = [], 0
    for m in MATH_RE.finditer(s):
        out.append(esc_text(s[i:m.start()]))
        out.append(m.group(0))
        i = m.end()
    out.append(esc_text(s[i:]))
    return "".join(out)


def esc_xml(s: str) -> str:
    return (s.replace("&", "&amp;").replace("<", "&lt;")
             .replace(">", "&gt;").replace('"', "&quot;"))


def _hex_no_hash(s: str) -> str:
    return (s or "").lstrip("#")


# --- evaluasi rumus --------------------------------------------------------

def _cell_numeric(baris, r, c, memo, stack):
    """Nilai numerik sel (r,c) 0-basis; ValueError bila bukan numerik."""
    key = (r, c)
    if key in memo:
        return memo[key]
    if key in stack:
        raise TableError(f"siklus rumus pada sel {chr(ord('A') + c)}{r + 1}")
    try:
        val = baris[r][c]
    except IndexError:
        raise TableError(f"rujukan sel di luar jangkauan: {chr(ord('A') + c)}{r + 1}")
    if isinstance(val, dict):
        val = val.get("rumus", "")
    if isinstance(val, str) and val.startswith("="):
        stack.add(key)
        num = _eval_formula(val[1:], baris, memo, stack)
        stack.discard(key)
        memo[key] = num
        return num
    if _is_number(val):
        memo[key] = val
        return val
    raise TableError(f"sel {chr(ord('A') + c)}{r + 1} bukan numerik")


def _eval_formula(expr: str, baris, memo, stack):
    m = FUNC_RE.match(expr.strip())
    if not m:
        raise TableError(f"rumus tidak dikenali: ={expr}")
    func = m.group(1).upper()
    if func == "AVG":
        func = "AVERAGE"
    if func not in ("SUM", "AVERAGE", "MIN", "MAX", "COUNT", "ROUND"):
        raise TableError(f"fungsi tidak didukung: {func}")
    args = [a.strip() for a in m.group(2).split(",")] if m.group(2).strip() else []

    values: list = []
    for a in args:
        rng = RANGE_RE.match(a)
        if rng:
            c0, r0 = _col_index(rng.group(1)), int(rng.group(2)) - 1
            c1, r1 = _col_index(rng.group(3)), int(rng.group(4)) - 1
            for rr in range(min(r0, r1), max(r0, r1) + 1):
                for cc in range(min(c0, c1), max(c0, c1) + 1):
                    values.append(_cell_numeric(baris, rr, cc, memo, stack))
            continue
        ref = REF_RE.match(a)
        if ref:
            cc, rr = _col_index(ref.group(1)), int(ref.group(2)) - 1
            values.append(_cell_numeric(baris, rr, cc, memo, stack))
            continue
        try:
            values.append(float(a) if ("." in a or "e" in a.lower()) else int(a))
        except ValueError:
            raise TableError(f"argumen tidak dikenali: {a}")

    if func == "SUM":
        return sum(values)
    if func == "AVERAGE":
        if not values:
            raise TableError("AVERAGE tanpa argumen numerik")
        return sum(values) / len(values)
    if func == "MIN":
        return min(values)
    if func == "MAX":
        return max(values)
    if func == "COUNT":
        return len([v for v in values if _is_number(v)])
    # ROUND
    if len(values) != 2:
        raise TableError("ROUND butuh 2 argumen")
    return round(values[0], int(values[1]))


def _resolve_grid(spec: dict) -> list:
    """Kembalikan matriks baris dengan sel rumus sudah dievaluasi."""
    baris = spec.get("baris") or []
    memo: dict = {}
    out = []
    for r, row in enumerate(baris):
        new_row = []
        for c, val in enumerate(row):
            raw = val.get("rumus", "") if isinstance(val, dict) else val
            if isinstance(raw, str) and raw.startswith("="):
                new_row.append(_cell_numeric(baris, r, c, memo, set()))
            else:
                new_row.append(val)
        out.append(new_row)
    return out


# --- normalisasi skema -----------------------------------------------------

def _border(spec: dict) -> dict:
    b = spec.get("border") or {}
    luar = b.get("luar") or {}
    dalam = b.get("dalam") or {}
    return {
        "atas": luar.get("atas", 1),
        "bawah": luar.get("bawah", 1),
        "kiri": luar.get("kiri", 1),
        "kanan": luar.get("kanan", 1),
        "baris": dalam.get("baris", 1),
        "kolom": dalam.get("kolom", 1),
        "warna": b.get("warna", "#000000"),
        "gaya": b.get("gaya", "solid"),
    }


def _isi(spec: dict) -> dict:
    return spec.get("isi") or {}


def _gabung(spec: dict) -> list:
    out = []
    for g in spec.get("gabung") or []:
        if not isinstance(g, dict):
            continue
        out.append({
            "r": int(g.get("baris", 1)) - 1,
            "c": int(g.get("kolom", 1)) - 1,
            "tinggi": int(g.get("tinggi", 1)),
            "lebar": int(g.get("lebar", 1)),
        })
    return out


def _cell_latex(val) -> str:
    if _is_number(val):
        return _fmt_num(val)
    return esc_latex_cell(str(val))


def _cell_plain(val) -> str:
    if _is_number(val):
        return _fmt_num(val)
    return str(val)


# --- emitter LaTeX ---------------------------------------------------------

def emit_latex(spec: dict, caption: str) -> str:
    kolom = spec.get("kolom") or []
    if not kolom:
        raise TableError("'kolom' wajib (>= 1)")
    baris = _resolve_grid(spec)
    if not baris:
        raise TableError("'baris' wajib (>= 1)")
    ncols = len(kolom)
    b = _border(spec)
    isi = _isi(spec)
    warna_hex = _hex_no_hash(b["warna"]) or "000000"
    gaya = b["gaya"]
    kepala = isi.get("kepala")
    zebra = isi.get("zebra") or []

    # spesifikasi kolom
    parts = []
    if b["kiri"]:
        parts.append("|")
    for idx, col in enumerate(kolom):
        rata = RATA_MAP.get(str(col.get("rata", "kiri")).lower(), "l")
        lebar = col.get("lebar")
        if lebar:
            parts.append("p{" + _fmt_num(lebar) + "\\linewidth}")
        else:
            parts.append("p{" + _fmt_num(0.98 / ncols) + "\\linewidth}")
        if idx < ncols - 1 and b["kolom"]:
            parts.append("|")
    if b["kanan"]:
        parts.append("|")
    colspec = "".join(parts)

    def line_cmd() -> str:
        if b["baris"] == 0:
            return "\\cline{1-%d}" % ncols
        if gaya in ("dashed", "dotted"):
            return "\\hdashline"
        return "\\hline"

    # merges
    merges = _gabung(spec)
    covered: set = set()
    anchors: dict = {}
    for g in merges:
        anchors[(g["r"], g["c"])] = g
        for rr in range(g["r"], g["r"] + g["tinggi"]):
            for cc in range(g["c"], g["c"] + g["lebar"]):
                if (rr, cc) != (g["r"], g["c"]):
                    covered.add((rr, cc))

    def col_spec_span(c0: int, span: int) -> str:
        rata = RATA_MAP.get(str(kolom[c0].get("rata", "kiri")).lower(), "l")
        lebar = kolom[c0].get("lebar")
        base = ("p{" + _fmt_num(lebar) + "\\linewidth}") if lebar \
            else ("p{" + _fmt_num(0.98 / ncols) + "\\linewidth}")
        left = "|" if (c0 == 0 and b["kiri"]) else ("|" if b["kolom"] else "")
        right = "|" if (c0 + span >= ncols and b["kanan"]) else ("|" if b["kolom"] else "")
        return left + base + right

    def build_row(cells, row_index, header=False) -> str:
        pieces = []
        c = 0
        while c < ncols:
            if (row_index, c) in covered:
                c += 1
                continue
            g = anchors.get((row_index, c))
            val = cells[c] if c < len(cells) else ""
            content = _cell_latex(val)
            if g and g["tinggi"] > 1:
                content = "\\multirow{%d}{*}{%s}" % (g["tinggi"], content)
            if g and g["lebar"] > 1:
                content = "\\multicolumn{%d}{%s}{%s}" % (
                    g["lebar"], col_spec_span(c, g["lebar"]), content)
            pieces.append(content)
            c += g["lebar"] if g else 1
        fill = None
        if header and kepala:
            fill = _hex_no_hash(kepala)
        elif zebra:
            fill = _hex_no_hash(zebra[row_index % len(zebra)])
        if fill:
            pieces[0] = "\\rowcolor[HTML]{" + fill + "} " + pieces[0]
        return " & ".join(pieces) + " \\\\ " + line_cmd()

    rows_tex = []
    header_cells = [col.get("judul", "") for col in kolom]
    rows_tex.append(build_row(header_cells, 0, header=True))
    for r, row in enumerate(baris):
        rows_tex.append(build_row(row, r))

    judul = caption or spec.get("judul", "")
    return (
        "\\begin{table}[htbp]\\centering\n"
        "\\caption{" + esc_latex_cell(str(judul)) + "}\n"
        "{\\arrayrulecolor[HTML]{" + warna_hex + "}"
        "\\setlength{\\arrayrulewidth}{" + _fmt_num(b["atas"]) + "pt}"
        "\\begin{tabular}{" + colspec + "}\n"
        + "\n".join(rows_tex) + "\n"
        "\\end{tabular}}\n"
        "\\end{table}"
    )


# --- emitter DOCX (openxml) ------------------------------------------------

def _docx_borders(b: dict) -> str:
    val = GAYA_MAP.get(b["gaya"], "single")
    hexc = _hex_no_hash(b["warna"]) or "000000"

    def one(tag: str, pt) -> str:
        try:
            pt = float(pt)
        except (TypeError, ValueError):
            pt = 0
        if pt <= 0:
            return f'<w:{tag} w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
        return (f'<w:{tag} w:val="{val}" w:sz="{int(round(pt * 8))}" '
                f'w:space="0" w:color="{hexc}"/>')

    return ("<w:tblBorders>"
            + one("top", b["atas"]) + one("left", b["kiri"])
            + one("bottom", b["bawah"]) + one("right", b["kanan"])
            + one("insideH", b["baris"]) + one("insideV", b["kolom"])
            + "</w:tblBorders>")


def _cell_xml(val, math: list, shd: str | None = None,
              span: int = 0, vmerge: str | None = None) -> str:
    tcpr = []
    if shd:
        tcpr.append(f'<w:shd w:val="clear" w:color="auto" w:fill="{_hex_no_hash(shd)}"/>')
    if span and span > 1:
        tcpr.append(f'<w:gridSpan w:val="{span}"/>')
    if vmerge == "restart":
        tcpr.append('<w:vMerge w:val="restart"/>')
    elif vmerge == "continue":
        tcpr.append('<w:vMerge/>')

    if vmerge == "continue":
        para = "<w:p/>"
    else:
        text = _cell_plain(val)
        runs = []
        idx = 0
        last = 0
        for m in MATH_RE.finditer(text):
            if m.start() > last:
                runs.append("<w:r><w:t xml:space=\"preserve\">"
                            + esc_xml(text[last:m.start()]) + "</w:t></w:r>")
            k = len(math)
            math.append(m.group(0))
            runs.append(f"<w:r>@@MATH{k}@@</w:r>")
            last = m.end()
            idx += 1
        if last < len(text):
            runs.append("<w:r><w:t xml:space=\"preserve\">"
                        + esc_xml(text[last:]) + "</w:t></w:r>")
        if not runs:
            runs.append("<w:r><w:t></w:t></w:r>")
        para = "<w:p>" + "".join(runs) + "</w:p>"

    tcpr_xml = ("<w:tcPr>" + "".join(tcpr) + "</w:tcPr>") if tcpr else ""
    return "<w:tc>" + tcpr_xml + para + "</w:tc>"


def _math_bridge(xml: str, math: list) -> str:
    if not math:
        return xml
    tmpdir = tempfile.mkdtemp(prefix="tblmath-")
    md = os.path.join(tmpdir, "m.md")
    docx_out = os.path.join(tmpdir, "m.docx")
    with open(md, "w", encoding="utf-8") as fh:
        fh.write("\n\n".join(math) + "\n")
    try:
        subprocess.run(["pandoc", "-f", "markdown", "-t", "docx", "-o", docx_out, md],
                       check=True, capture_output=True)
        import zipfile
        with zipfile.ZipFile(docx_out) as z:
            doc = z.read("word/document.xml").decode("utf-8", "ignore")
        oms = re.findall(r"<m:oMath>.*?</m:oMath>", doc, re.DOTALL)
    except Exception:  # noqa: BLE001
        oms = []
    if len(oms) < len(math):
        sys.stderr.write("table: math fallback (pandoc gagal)\n")
        for k, m in enumerate(math):
            xml = xml.replace(f"@@MATH{k}@@", esc_xml(m.replace("$", "")))
        return xml
    for k, om in enumerate(oms):
        xml = xml.replace(f"@@MATH{k}@@", om)
    return xml


def emit_docx(spec: dict, caption: str) -> str:
    kolom = spec.get("kolom") or []
    if not kolom:
        raise TableError("'kolom' wajib (>= 1)")
    baris = _resolve_grid(spec)
    if not baris:
        raise TableError("'baris' wajib (>= 1)")
    ncols = len(kolom)
    b = _border(spec)
    isi = _isi(spec)
    kepala = isi.get("kepala")
    zebra = isi.get("zebra") or []
    merges = _gabung(spec)
    covered: set = set()
    anchors: dict = {}
    for g in merges:
        anchors[(g["r"], g["c"])] = g
        for rr in range(g["r"], g["r"] + g["tinggi"]):
            for cc in range(g["c"], g["c"] + g["lebar"]):
                if (rr, cc) != (g["r"], g["c"]):
                    covered.add((rr, cc))

    math: list = []
    out = []
    judul = caption or spec.get("judul", "")
    if judul:
        out.append("<w:p><w:pPr><w:jc w:val=\"center\"/></w:pPr>"
                   "<w:r><w:rPr><w:b/></w:rPr><w:t xml:space=\"preserve\">"
                   + esc_xml(str(judul)) + "</w:t></w:r></w:p>")
    out.append("<w:tbl><w:tblPr><w:tblW w:w=\"0\" w:type=\"auto\"/>"
               + _docx_borders(b) + "</w:tblPr>")
    out.append("<w:tblGrid>" + "<w:gridCol/>" * ncols + "</w:tblGrid>")

    def build_row(cells, row_index, header=False):
        tr = []
        shd = kepala if (header and kepala) else (
            zebra[row_index % len(zebra)] if zebra else None)
        c = 0
        while c < ncols:
            if (row_index, c) in covered:
                tr.append(_cell_xml("", math, vmerge="continue"))
                c += 1
                continue
            g = anchors.get((row_index, c))
            val = cells[c] if c < len(cells) else ""
            span = g["lebar"] if g else 0
            vm = "restart" if (g and g["tinggi"] > 1) else None
            tr.append(_cell_xml(val, math, shd=shd, span=span, vmerge=vm))
            if g and g["tinggi"] > 1:
                for rr in range(row_index + 1, row_index + g["tinggi"]):
                    covered.add((rr, c))
            c += g["lebar"] if g else 1
        return "<w:tr>" + "".join(tr) + "</w:tr>"

    out.append(build_row([col.get("judul", "") for col in kolom], 0, header=True))
    for r, row in enumerate(baris):
        out.append(build_row(row, r))
    out.append("</w:tbl>")
    xml = "".join(out)
    return _math_bridge(xml, math)


# --- pemindaian --check ----------------------------------------------------

def _table_blocks(lines: list):
    i = 0
    while i < len(lines):
        m = TABLE_OPEN_RE.match(lines[i].strip())
        if m:
            attrs = m.group(1)
            mid = re.search(r"#([A-Za-z0-9_:-]+)", attrs)
            body = []
            j = i + 1
            while j < len(lines) and lines[j].strip() != "```":
                body.append(lines[j])
                j += 1
            yield i, j, (mid.group(1) if mid else ""), "\n".join(body)
            i = j + 1
        else:
            i += 1


def _validate_spec(spec) -> str | None:
    if not isinstance(spec, dict):
        return "YAML bukan pemetaan"
    kolom = spec.get("kolom")
    if not isinstance(kolom, list) or len(kolom) < 1:
        return "'kolom' wajib (daftar, >= 1)"
    baris = spec.get("baris")
    if not isinstance(baris, list) or len(baris) < 1:
        return "'baris' wajib (daftar, >= 1)"
    return None


def cmd_check(root: str) -> int:
    gagal = 0
    for g in GLOBS:
        for path in sorted(glob.glob(os.path.join(root, g))):
            rel = os.path.relpath(path, root)
            with open(path, encoding="utf-8") as fh:
                lines = fh.read().splitlines()
            for oi, _ci, ident, body in _table_blocks(lines):
                tag = "#" + ident if ident else "#(tanpa id)"
                try:
                    spec = yaml.safe_load(body) or {}
                except yaml.YAMLError as exc:
                    print(f"GAGAL: {rel}:{oi + 1} ({exc})")
                    gagal += 1
                    continue
                reason = _validate_spec(spec)
                if reason:
                    print(f"GAGAL: {rel}:{oi + 1} ({reason})")
                    gagal += 1
                else:
                    print(f"OK: {rel}:{oi + 1} {tag}")
    return 1 if gagal else 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Render blok {.table} -> LaTeX/DOCX.")
    ap.add_argument("--format", choices=["latex", "docx"])
    ap.add_argument("--caption", default="")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--root", default=".")
    args = ap.parse_args(argv)

    if args.check:
        return cmd_check(args.root)
    if not args.format:
        ap.error("--format wajib kecuali --check")

    raw = sys.stdin.read()
    try:
        spec = yaml.safe_load(raw) or {}
    except yaml.YAMLError as exc:
        sys.stderr.write(f"table: YAML tidak valid ({exc})\n")
        return 2
    try:
        if args.format == "latex":
            sys.stdout.write(emit_latex(spec, args.caption))
        else:
            sys.stdout.write(emit_docx(spec, args.caption))
    except TableError as exc:
        sys.stderr.write(f"table: {exc}\n")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
