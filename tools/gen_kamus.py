#!/usr/bin/env python3
"""Generator kamus bahasa artikel.

Membaca kamus `assets/bahasa/kamus-id.yaml` lalu menyelaraskan:
  - kepala bagian + formula artikel  (content/artikel/artikel-sinta.md)
  - formula pemandu bab skripsi      (content/skripsi/1[0-5]-*.md)
  - dokumen turunan                  (docs/kamus-bahasa-artikel.md)

Tag terkelola (grammar): sebuah baris Markdown diakhiri komentar HTML
`<!-- kamus:(h|f) id=([a-z0-9_]+) -->`. `h` = kepala bagian, `f` = baris
formula. Generator memiliki teks SEBELUM tag.
"""

import argparse
import glob
import os
import re
import sys

try:
    import yaml
except ImportError:  # pragma: no cover
    print("GAGAL: jalankan 'make setup' (PyYAML belum terpasang)")
    sys.exit(2)

KAMUS = "assets/bahasa/kamus-id.yaml"
ARTIKEL = "content/artikel/artikel-sinta.md"
DOC = "docs/kamus-bahasa-artikel.md"
BAB_GLOB = "content/skripsi/1[0-5]-*.md"

# Sebuah baris terkelola: teks apa pun, lalu tag kamus di akhir baris.
RE_TAG = re.compile(r"^(?P<pre>.*?)<!-- kamus:(?P<kind>[hf]) id=(?P<id>[a-z0-9_]+) -->\s*$")


class GagalBagian(Exception):
    """Kepala bagian tidak ditemukan di artikel."""

    def __init__(self, sid):
        super().__init__(sid)
        self.sid = sid


class Writer:
    """Penulis berkas dengan mode uji (dry) dan tulis atomik."""

    def __init__(self, dry):
        self.dry = dry
        self.changed = []
        self._seen = set()

    def __call__(self, path, content):
        try:
            with open(path, encoding="utf-8") as fh:
                old = fh.read()
        except OSError:
            old = None
        if old == content:
            return False
        if path not in self._seen:
            self._seen.add(path)
            self.changed.append(path)
        if not self.dry:
            tmp = path + ".tmp"
            with open(tmp, "w", encoding="utf-8", newline="") as fh:
                fh.write(content)
            os.replace(tmp, path)
        return True


def load():
    """Muat kamus YAML."""
    with open(KAMUS, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def _normalize(text, tag, line=None):
    """Bangun ulang baris terkelola: teks kamus + komentar yang sudah ada + tag.

    Generator memiliki teks SEBELUM komentar HTML pertama. Komentar lain
    (mis. `<!-- TODO: … -->`) dipertahankan, lalu tag kamus ditambahkan.
    """
    tail = ""
    if line is not None:
        stripped = re.sub(r"\s*<!-- kamus:[hf] id=[a-z0-9_]+ -->", "", line)
        pos = stripped.find("<!--")
        if pos != -1:
            tail = stripped[pos:].strip()
    parts = [text]
    if tail:
        parts.append(tail)
    parts.append(tag)
    return " ".join(parts)


def _find_heading(lines, sid, judul, varian):
    """Kembalikan indeks baris kepala bagian, atau None."""
    pat = re.compile(r"^# .*<!-- kamus:h id=%s -->\s*$" % re.escape(sid))
    for i, ln in enumerate(lines):
        if pat.match(ln):
            return i
    targets = {"# " + judul}
    for v in varian or []:
        targets.add("# " + v)
    for i, ln in enumerate(lines):
        if ln.rstrip() in targets:
            return i
    return None


def emit_artikel(d, write):
    """Selaraskan kepala bagian + formula pemandu di artikel."""
    lines = _read(ARTIKEL).split("\n")
    kepala = d.get("kepala_bagian", [])
    formula = d.get("formula", {})
    varian = d.get("varian_kepala", {}) or {}

    located = []
    for s in kepala:
        i = _find_heading(lines, s["id"], s["judul"], varian.get(s["id"]))
        if i is None:
            raise GagalBagian(s["id"])
        located.append((i, s))

    # Normalisasi kepala bagian (jumlah baris tetap).
    for i, s in located:
        lines[i] = _normalize("# %s" % s["judul"], "<!-- kamus:h id=%s -->" % s["id"], lines[i])

    # Formula pemandu: proses dari bawah ke atas agar indeks tetap valid.
    for i, s in reversed(located):
        fid = s.get("formula_id")
        if not fid or fid not in formula:
            continue
        new_line = "%s <!-- kamus:f id=%s -->" % (formula[fid], fid)
        j = i + 1
        while j < len(lines) and not lines[j].startswith("# "):
            j += 1
        found = None
        for k in range(i + 1, j):
            m = RE_TAG.match(lines[k])
            if m and m.group("kind") == "f" and m.group("id") == fid:
                found = k
                break
        if found is None:
            # Belum bertag: adopsi baris yang teksnya sama dengan formula.
            for k in range(i + 1, j):
                if RE_TAG.match(lines[k]):
                    continue
                if lines[k].split("<!--")[0].strip() == formula[fid]:
                    found = k
                    break
        if found is not None:
            lines[found] = _normalize(formula[fid], "<!-- kamus:f id=%s -->" % fid, lines[found])
        else:
            lines.insert(i + 1, new_line)

    write(ARTIKEL, "\n".join(lines))


def emit_bab(d, write):
    """Selaraskan baris formula bertag di bab skripsi."""
    formula = d.get("formula", {})
    for path in sorted(glob.glob(BAB_GLOB)):
        lines = _read(path).split("\n")
        for k, ln in enumerate(lines):
            m = RE_TAG.match(ln)
            if not m or m.group("kind") != "f":
                continue
            fid = m.group("id")
            if fid in formula:
                lines[k] = _normalize(formula[fid], "<!-- kamus:f id=%s -->" % fid, ln)
        write(path, "\n".join(lines))


def _table(headers, rows):
    out = ["| " + " | ".join(headers) + " |"]
    out.append("|" + "|".join(["---"] * len(headers)) + "|")
    for row in rows:
        out.append("| " + " | ".join(str(c) for c in row) + " |")
    return out


def render_doc(d):
    """Render docs/kamus-bahasa-artikel.md dari kamus."""
    kepala = d.get("kepala_bagian", [])
    formula = d.get("formula", {})
    rangkai = d.get("rangkai_argumen", {}) or {}
    varian = d.get("varian_kepala", {}) or {}
    L = []
    L.append("<!-- DIBANGUN OTOMATIS oleh tools/gen_kamus.py; jangan sunting manual. -->")
    L.append("")
    L.append("# Kamus Bahasa Artikel")
    L.append("")
    L.append(
        "Kamus ini diturunkan dari korpus jurnal Sinta 1-6 di `%s` "
        "(lihat `docs/sinta-corpus/MANIFEST.md`) dan korpus Hubungan Internasional di `%s` "
        "(lihat `docs/ir-corpus/MANIFEST.md`)."
        % (
            d.get("korpus", "docs/sinta-corpus/"),
            d.get("korpus_hi", "docs/ir-corpus/"),
        )
    )
    L.append("")

    # --- Sumber Data ---
    L.append("## Sumber Data")
    L.append("")
    sumber_rows = [
        ["`versi`", d.get("versi")],
        ["`korpus`", "`%s`" % d.get("korpus")],
        ["`catatan`", d.get("catatan")],
    ]
    if d.get("catatan_riset"):
        sumber_rows.append(["`catatan_riset`", "`%s`" % d["catatan_riset"]])
    if d.get("korpus_hi"):
        sumber_rows.append(["`korpus_hi`", "`%s`" % d["korpus_hi"]])
    if d.get("catatan_riset_hi"):
        sumber_rows.append(["`catatan_riset_hi`", "`%s`" % d["catatan_riset_hi"]])
    L.extend(_table(["Kunci", "Nilai"], sumber_rows))
    L.append("")

    # --- Kepala Bagian dan Urutan ---
    L.append("## Kepala Bagian dan Urutan")
    L.append("")
    rows = []
    for n, s in enumerate(kepala, 1):
        rows.append(
            [
                n,
                "`%s`" % s["id"],
                s["judul"],
                ("`%s`" % s["formula_id"]) if s.get("formula_id") else "—",
                ", ".join(varian.get(s["id"], []) or []) or "—",
            ]
        )
    L.extend(_table(["#", "id", "judul", "formula_id", "varian"], rows))
    L.append("")
    tambahan = d.get("kepala_tambahan", []) or []
    if tambahan:
        L.append("Kepala bagian non-kanonik yang teramati di korpus (tidak mengubah enam id utama):")
        L.append("")
        L.extend(
            _table(
                ["judul", "sumber"],
                [[x.get("judul", ""), x.get("sumber", "")] for x in tambahan],
            )
        )
        L.append("")

    # --- Formula Kalimat ---
    L.append("## Formula Kalimat")
    L.append("")
    L.extend(
        _table(
            ["id", "formula"],
            [["`%s`" % k, v] for k, v in formula.items()],
        )
    )
    L.append("")

    # --- Rangkai Argumen ---
    L.append("## Rangkai Argumen")
    L.append("")
    for s in kepala:
        L.append("### %s" % s["judul"])
        L.append("")
        bullets = rangkai.get(s["id"])
        if bullets:
            for b in bullets:
                L.append("- %s" % b)
        else:
            L.append("_Tidak ada rangkai argumen khusus._")
        L.append("")
    if rangkai.get("abstrak"):
        L.append("### Abstrak")
        L.append("")
        for b in rangkai["abstrak"]:
            L.append("- %s" % b)
        L.append("")

    # --- Leksikon Verba ---
    L.append("## Leksikon Verba")
    L.append("")
    for v in d.get("leksikon_verba", []):
        L.append("- %s" % v)
    L.append("")

    # --- Konektor ---
    L.append("## Konektor")
    L.append("")
    for v in d.get("konektor", []):
        L.append("- %s" % v)
    L.append("")

    # --- Leksikon Nomina (HI/IR) ---
    nomina = d.get("leksikon_nomina", []) or []
    if nomina:
        L.append("## Leksikon Nomina (HI/IR)")
        L.append("")
        L.extend(
            _table(
                ["Nomina/istilah", "Jumlah", "Sumber (slug)"],
                [
                    [x.get("nomina", ""), x.get("jumlah", ""), x.get("sumber", "")]
                    for x in nomina
                ],
            )
        )
        L.append("")

    # --- Kolokasi Verba+Objek ---
    kolokasi = d.get("kolokasi_verba", []) or []
    if kolokasi:
        L.append("## Kolokasi Verba+Objek")
        L.append("")
        L.extend(
            _table(
                ["Kolokasi", "Jumlah", "Sumber (slug)"],
                [
                    [x.get("kolokasi", ""), x.get("jumlah", ""), x.get("sumber", "")]
                    for x in kolokasi
                ],
            )
        )
        L.append("")

    # --- Pembuka Kalimat ---
    pembuka = d.get("pembuka_kalimat", []) or []
    if pembuka:
        L.append("## Pembuka Kalimat")
        L.append("")
        L.extend(
            _table(
                ["Pembuka", "Jumlah", "Sumber (slug)"],
                [
                    [x.get("pembuka", ""), x.get("jumlah", ""), x.get("sumber", "")]
                    for x in pembuka
                ],
            )
        )
        L.append("")

    # --- Hedging dan Booster ---
    hedging = d.get("hedging_booster", []) or []
    if hedging:
        L.append("## Hedging dan Booster")
        L.append("")
        L.extend(
            _table(
                ["Leksikon", "Jenis", "Jumlah", "Sumber (slug)"],
                [
                    [
                        x.get("leksikon", ""),
                        x.get("jenis", ""),
                        x.get("jumlah", ""),
                        x.get("sumber", ""),
                    ]
                    for x in hedging
                ],
            )
        )
        L.append("")

    # --- Tipografi dan Gaya ---
    tipografi = d.get("tipografi", []) or []
    if tipografi:
        L.append("## Tipografi dan Gaya")
        L.append("")
        L.extend(
            _table(
                ["Konvensi", "Catatan"],
                [
                    [x.get("konvensi", ""), x.get("catatan", "")]
                    for x in tipografi
                ],
            )
        )
        L.append("")

    # --- Kosakata Baku ---
    L.append("## Kosakata Baku")
    L.append("")
    L.extend(
        _table(
            ["Tidak baku", "Baku"],
            [[x["salah"], x["benar"]] for x in d.get("kosakata_baku", [])],
        )
    )
    L.append("")

    # --- Frasa yang Dihindari ---
    L.append("## Frasa yang Dihindari")
    L.append("")
    L.extend(
        _table(
            ["Frasa", "Ganti"],
            [[x["frasa"], x["ganti"]] for x in d.get("frasa_ai_generik", [])],
        )
    )
    L.append("")

    # --- Abstrak dan Kata Kunci ---
    ab = d.get("abstrak", {}) or {}
    L.append("## Abstrak dan Kata Kunci")
    L.append("")
    L.append("- Label: `%s`" % ab.get("label", "Abstrak"))
    if ab.get("label_varian"):
        L.append("- Varian label teramati: %s" % ", ".join("`%s`" % x for x in ab["label_varian"]))
    L.append("- Komponen (urutan): %s" % " → ".join(ab.get("komponen", [])))
    pk = ab.get("panjang_kata", [])
    L.append("- Panjang: %s kata" % ("–".join(str(x) for x in pk) if pk else "—"))
    pkt = ab.get("panjang_kata_teramati", [])
    if pkt:
        L.append("- Panjang teramati di korpus: %s kata" % "–".join(str(x) for x in pkt))
    L.append("- Diakhiri dengan: `%s`" % ab.get("kata_kunci", "Kata Kunci:"))
    if ab.get("kata_kunci_varian"):
        L.append("- Varian label kata kunci: %s" % ", ".join("`%s`" % x for x in ab["kata_kunci_varian"]))
    if ab.get("pemisah_kata_kunci"):
        L.append("- Pemisah kata kunci: %s" % " atau ".join("`%s`" % x for x in ab["pemisah_kata_kunci"]))
    if ab.get("struktur_varian"):
        L.append("- Struktur teramati: %s" % "; ".join(ab["struktur_varian"]))
    if ab.get("dwibahasa"):
        L.append("- Dwibahasa: %s" % ab["dwibahasa"])
    if ab.get("pembuka_teramati"):
        L.append("- Pembuka teramati: %s" % "; ".join(ab["pembuka_teramati"]))
    L.append("- Larangan: %s" % ", ".join(ab.get("larangan", [])))
    L.append("")

    # --- Kutipan ---
    ku = d.get("kutipan", {}) or {}
    L.append("## Kutipan")
    L.append("")
    L.append(
        "- Gaya default build repo: **APA name-year** (`%s`) — contoh: %s."
        % (ku.get("gaya_default", "apa_nama_tahun"), ", ".join("`%s`" % c for c in ku.get("contoh_apa", [])))
    )
    L.append(
        "- Varian teramati pada korpus: **numerik kurung** (`%s`) dengan **DAFTAR PUSTAKA bernomor** — contoh: %s."
        % (ku.get("gaya_korpus", "numerik_kurung"), ", ".join("`%s`" % c for c in ku.get("contoh_numerik", [])))
    )
    if ku.get("paper_numerik"):
        L.append("- Paper bergaya numerik (%d): %s" % (len(ku["paper_numerik"]), ", ".join("`%s`" % x for x in ku["paper_numerik"])))
    if ku.get("paper_apa"):
        L.append("- Paper bergaya APA: %s" % ", ".join("`%s`" % x for x in ku["paper_apa"]))
    dp = d.get("daftar_pustaka", {}) or {}
    L.append(
        "- Daftar pustaka: default **%s**; varian korpus **%s** (didokumentasikan, bukan gaya build repo)."
        % (dp.get("gaya_default", "APA"), dp.get("gaya_korpus", "numerik"))
    )
    L.append("")

    # --- Daftar Periksa ---
    L.append("## Daftar Periksa")
    L.append("")
    L.append("- [ ] Kepala bagian lengkap dan berurutan sesuai `kepala_bagian`.")
    L.append("- [ ] Formula kalimat inti dipakai pada tiap bagian.")
    L.append("- [ ] Tidak ada kosakata tidak baku (lihat tabel Kosakata Baku).")
    L.append("- [ ] Tidak ada frasa AI generik (lihat tabel Frasa yang Dihindari).")
    L.append("- [ ] Abstrak satu paragraf, tanpa sitasi, 100–250 kata, diakhiri `Kata Kunci:`.")
    L.append("- [ ] Gaya kutipan konsisten (APA name-year untuk build repo).")
    L.append("")
    L.append(
        "> Catatan: untuk menyempitkan pola positif palsu, sesuaikan pola di "
        "`tools/check-bahasa.sh` (mis. batasi ke kata utuh dengan `-w` dan kecualikan "
        "konteks kutipan). Placeholder ini disediakan agar penyesuaian pola terdokumentasi."
    )
    L.append("")
    return "\n".join(L)


def emit_doc(d, write):
    write(DOC, render_doc(d))


def _esc_pola(s):
    """Escape untuk grep -E; ruang dibiarkan literal agar tidak memicu
    peringatan 'stray \\ before white space' pada GNU grep."""
    return re.escape(s).replace("\\ ", " ")


def cmd_pattern(d, key):
    if key == "kosakata_baku":
        items = [x["salah"] for x in d.get("kosakata_baku", [])]
    elif key == "frasa_ai_generik":
        items = [x["frasa"] for x in d.get("frasa_ai_generik", [])]
    else:
        sys.stderr.write("GAGAL: pola tidak dikenal: %s\n" % key)
        return 2
    print("|".join(_esc_pola(i) for i in items))
    return 0


def cmd_check(d):
    w = Writer(dry=True)
    unresolved = None
    try:
        emit_artikel(d, w)
    except GagalBagian as e:
        unresolved = e
    emit_bab(d, w)
    emit_doc(d, w)

    failed = False
    if unresolved is not None:
        print("GAGAL: bagian '%s' tidak ditemukan di %s" % (unresolved.sid, ARTIKEL))
        failed = True
    for p in w.changed:
        print("GAGAL: %s tidak selaras dengan kamus" % p)
        failed = True
    if failed:
        return 1
    print("KAMUS: SELARAS.")
    return 0


def cmd_emit(d, only_doc=False):
    w = Writer(dry=False)
    try:
        if only_doc:
            emit_doc(d, w)
        else:
            emit_artikel(d, w)
            emit_bab(d, w)
            emit_doc(d, w)
    except GagalBagian as e:
        print("GAGAL: bagian '%s' tidak ditemukan di %s" % (e.sid, ARTIKEL))
        return 1
    print("KAMUS: %d berkas diperbarui." % len(w.changed))
    return 0


def main(argv):
    ap = argparse.ArgumentParser(prog="gen_kamus.py", description="Generator kamus bahasa artikel.")
    ap.add_argument("--check", action="store_true", help="uji keselarasan tanpa menulis")
    ap.add_argument("--emit", action="store_true", help="tulis berkas terkelola (default)")
    ap.add_argument("--doc", action="store_true", help="hanya bangun docs/kamus-bahasa-artikel.md")
    ap.add_argument("--pattern", metavar="KEY", help="cetak pola regex untuk KEY")
    args = ap.parse_args(argv)

    try:
        d = load()
    except (OSError, yaml.YAMLError):
        print("GAGAL: jalankan 'make setup' (PyYAML belum terpasang)")
        return 2

    if args.pattern is not None:
        return cmd_pattern(d, args.pattern)
    if args.check:
        return cmd_check(d)
    return cmd_emit(d, only_doc=(args.doc and not args.emit))


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
