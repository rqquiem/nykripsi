#!/usr/bin/env python3
"""scaffold.py — generate the 14-file skripsi skeleton for the Nykripsi v2 workspace.

Stdlib only. Mirrors the structure, heading text, and ``kamus:f id=…`` comment
markers of the existing ``content/skripsi/*.md`` files (STMIK Triguna Dharma
Hubungan Internasional pedoman). See ``.claude/skills/nykripsi/references/skripsi-structure.md``.

Usage:
    scaffold.py [--out DIR] [--title T] [--author A] [--nim N] [--prodi P]
                [--year YYYY] [--force] [--with-bib] [--list]
"""

import argparse
import os
import sys
import textwrap
from pathlib import Path

DEFAULT_OUT = "content/skripsi"

# Ordered list of the 14 skeleton files (zero-padded numeric prefixes).
FILE_ORDER = [
    "00-halaman-judul.md",
    "01-lembar-persetujuan.md",
    "02-lembar-pengesahan.md",
    "03-surat-pernyataan.md",
    "04-kata-pengantar.md",
    "05-abstrak.md",
    "06-daftar-isi.md",
    "10-bab-01-pendahuluan.md",
    "11-bab-02-tinjauan-pustaka.md",
    "12-bab-03-metodologi-penelitian.md",
    "13-bab-04-perancangan-sistem.md",
    "14-bab-05-hasil-dan-pembahasan.md",
    "15-bab-06-kesimpulan-dan-saran.md",
    "90-daftar-pustaka.md",
]

# Minimal refs.bib written only with --with-bib and only when absent.
REFS_BIB_STUB = """\
% assets/refs.bib — BibTeX bibliography for the skripsi and article builds.
% Add at least 20 references (pedoman: all within the last 5 years, >= 30%
% international journals/proceedings). Example entry:
%
% @article{contoh2025sistem,
%   author  = {Nama, Penulis and Kedua, Penulis},
%   title   = {Judul Artikel Contoh},
%   journal = {Nama Jurnal},
%   year    = {2025},
%   volume  = {1},
%   number  = {1},
%   pages   = {1--10},
%   doi     = {10.0000/contoh.v1i1.1}
% }
"""


def dedent(text):
    return textwrap.dedent(text).strip("\n") + "\n"


# --------------------------------------------------------------------------- #
# Front matter (00–06, 90): sensible templates with <!-- TODO --> placeholders.
# --------------------------------------------------------------------------- #

def _halaman_judul(a):
    return dedent(f"""\
        ```{{=latex}}
        \\frontmatter
        \\pagestyle{{plain}}
        \\begin{{singlespace}}
        ```

        ```{{=latex}}
        \\begin{{center}}
        {{\\large\\bfseries {a['title'].upper()}\\par}}
        \\vspace{{1.5cm}}
        \\includegraphics[width=3cm]{{assets/figures/contoh.png}}\\par
        \\vspace{{1.5cm}}
        {{\\large\\bfseries SKRIPSI\\par}}
        \\vspace{{0.75cm}}
        {{\\normalsize Diajukan sebagai Salah Satu Syarat untuk Menyelesaikan\\\\
        Pendidikan Strata Satu (S1) pada Program Studi {a['prodi']}\\par}}
        \\vspace{{1.5cm}}
        {{\\normalsize
        \\begin{{tabular}}{{l@{{\\hspace{{0.5em}}}}l@{{\\hspace{{0.5em}}}}l}}
        Nama          & : & {a['author']} \\\\
        NIM           & : & {a['nim']} \\\\
        Program Studi & : & {a['prodi']} \\\\
        Jurusan       & : & [Jurusan] \\\\
        \\end{{tabular}}\\par}}
        \\vspace{{1.5cm}}
        {{\\large\\bfseries SEKOLAH TINGGI MANAJEMEN INFORMATIKA DAN KOMPUTER (STMIK) TRIGUNA DHARMA\\par}}
        \\vspace{{0.5cm}}
        {{\\normalsize [KOTA] \\\\{{}} [{a['year']}]\\par}}
        \\vspace{{2cm}}
        {{\\normalsize
        \\begin{{tabular}}{{p{{0.42\\textwidth}}@{{\\hspace{{0.08\\textwidth}}}}p{{0.42\\textwidth}}}}
        Medan, .................... {a['year']} & \\\\[0.25em]
        Dosen Pembimbing I, & Dosen Pembimbing II, \\\\[3cm]
        (................................) & (................................) \\\\
        \\end{{tabular}}\\par}}
        \\end{{center}}
        ```

        ```{{=latex}}
        \\end{{singlespace}}
        ```

        <!-- TODO: lengkapi halaman judul (jurusan, kota, nama pembimbing) -->
        """)


def _lembar_persetujuan(a):
    return dedent(f"""\
        ```{{=latex}}
        \\chapter*{{LEMBAR PERSETUJUAN}}
        \\addcontentsline{{toc}}{{chapter}}{{LEMBAR PERSETUJUAN}}
        ```

        ```{{=latex}}
        \\begin{{singlespace}}
        \\noindent Skripsi ini diajukan oleh:

        \\vspace{{0.5cm}}
        \\noindent
        \\begin{{tabular}}{{l@{{\\hspace{{0.5em}}}}l@{{\\hspace{{0.5em}}}}l}}
        Nama          & : & {a['author']} \\\\
        NIM           & : & {a['nim']} \\\\
        Program Studi & : & {a['prodi']} \\\\
        Judul Skripsi & : & {a['title']} \\\\
        \\end{{tabular}}

        \\vspace{{1cm}}
        \\noindent Telah diperiksa dan disetujui untuk diajukan dalam Sidang Skripsi pada
        Program Studi {a['prodi']} STMIK Triguna Dharma.

        \\vspace{{1.5cm}}
        \\noindent
        \\begin{{tabular}}{{p{{0.45\\textwidth}}p{{0.45\\textwidth}}}}
        Dosen Pembimbing I, & Dosen Pembimbing II, \\\\[3cm]
        (................................) & (................................) \\\\
        \\end{{tabular}}

        \\vspace{{1.5cm}}
        \\noindent Mengetahui,\\\\
        Ketua Program Studi {a['prodi']}

        \\vspace{{2cm}}
        \\noindent (................................)
        \\end{{singlespace}}
        ```

        <!-- TODO: sesuaikan nama pembimbing dan ketua program studi -->
        """)


def _lembar_pengesahan(a):
    return dedent(f"""\
        ```{{=latex}}
        \\chapter*{{LEMBAR PENGESAHAN}}
        \\addcontentsline{{toc}}{{chapter}}{{LEMBAR PENGESAHAN}}
        ```

        ```{{=latex}}
        \\begin{{singlespace}}
        \\noindent Skripsi ini telah dipertahankan di depan Sidang Skripsi Program Studi
        {a['prodi']} STMIK Triguna Dharma dan dinyatakan LULUS.

        \\vspace{{0.5cm}}
        \\noindent
        \\begin{{tabular}}{{l@{{\\hspace{{0.5em}}}}l@{{\\hspace{{0.5em}}}}l}}
        Nama          & : & {a['author']} \\\\
        NIM           & : & {a['nim']} \\\\
        Program Studi & : & {a['prodi']} \\\\
        Judul Skripsi & : & {a['title']} \\\\
        \\end{{tabular}}

        \\vspace{{1.5cm}}
        \\noindent
        \\begin{{tabular}}{{p{{0.45\\textwidth}}p{{0.45\\textwidth}}}}
        Ketua Penguji, & Penguji I, \\\\[3cm]
        (................................) & (................................) \\\\[1.5cm]
        Penguji II, & Dosen Pembimbing, \\\\[3cm]
        (................................) & (................................) \\\\
        \\end{{tabular}}

        \\vspace{{1.5cm}}
        \\noindent Disahkan oleh,\\\\
        Ketua STMIK Triguna Dharma

        \\vspace{{2cm}}
        \\noindent (................................)
        \\end{{singlespace}}
        ```

        <!-- TODO: sesuaikan nama penguji dan ketua STMIK -->
        """)


def _surat_pernyataan(a):
    # Personal legal declaration: exempt from the no-pronoun register rule.
    return dedent(f"""\
        ```{{=latex}}
        \\chapter*{{SURAT PERNYATAAN}}
        \\addcontentsline{{toc}}{{chapter}}{{SURAT PERNYATAAN}}
        ```

        ```{{=latex}}
        \\begin{{singlespace}}
        \\noindent Yang bertanda tangan di bawah ini:

        \\vspace{{0.5cm}}
        \\noindent
        \\begin{{tabular}}{{l@{{\\hspace{{0.5em}}}}l@{{\\hspace{{0.5em}}}}l}}
        Nama          & : & {a['author']} \\\\
        NIM           & : & {a['nim']} \\\\
        Program Studi & : & {a['prodi']} \\\\
        \\end{{tabular}}

        \\vspace{{1cm}}
        \\noindent dengan ini menyatakan bahwa skripsi yang berjudul {a['title']} adalah
        benar hasil karya saya sendiri dan belum pernah diajukan untuk memperoleh gelar
        kesarjanaan di suatu perguruan tinggi mana pun. Semua sumber yang saya gunakan
        dalam penulisan skripsi ini telah saya cantumkan sesuai dengan ketentuan yang
        berlaku. Apabila di kemudian hari terbukti terdapat unsur plagiat, maka saya
        bersedia menerima sanksi sesuai dengan peraturan yang berlaku.

        \\vspace{{1.5cm}}
        \\noindent Medan, .................... {a['year']}\\\\
        Yang menyatakan,

        \\vspace{{3cm}}
        \\noindent (................................)\\\\
        NIM: {a['nim']}
        \\end{{singlespace}}
        ```

        <!-- TODO: tanda tangani surat pernyataan asli (kata ganti orang pertama dikecualikan) -->
        """)


def _kata_pengantar(a):
    return dedent("""\
        ```{=latex}
        \\chapter*{KATA PENGANTAR}
        \\addcontentsline{toc}{chapter}{KATA PENGANTAR}
        ```

        Puji syukur penulis panjatkan kepada Tuhan Yang Maha Esa atas segala rahmat dan
        karunia-Nya sehingga penulis dapat menyelesaikan penyusunan skripsi ini dengan
        baik. Skripsi ini disusun sebagai salah satu syarat untuk menyelesaikan
        pendidikan Strata Satu (S1) pada Program Studi Hubungan Internasional STMIK
        Triguna Dharma.

        Penulis menyadari bahwa penyusunan skripsi ini tidak akan terlaksana dengan baik
        tanpa bantuan, bimbingan, serta dukungan dari berbagai pihak. Oleh karena itu,
        pada kesempatan ini penulis menyampaikan terima kasih kepada seluruh pihak yang
        telah membantu penyelesaian skripsi ini.

        Penulis menyadari bahwa skripsi ini masih jauh dari sempurna. Oleh karena itu,
        kritik dan saran yang membangun sangat penulis harapkan demi perbaikan di masa
        yang akan datang. Akhirnya, penulis berharap skripsi ini dapat memberikan
        manfaat bagi pembaca dan pihak-pihak yang membutuhkan.

        <!-- TODO: sesuaikan ucapan terima kasih dan daftar pihak yang membantu -->
        """)


def _abstrak(a):
    return dedent("""\
        ```{=latex}
        \\chapter*{ABSTRAK}
        \\addcontentsline{toc}{chapter}{ABSTRAK}
        \\begin{singlespace}
        ```

        Penelitian ini mengkaji … <!-- TODO: isi abstrak (satu paragraf naratif: latar belakang → tujuan → metode → hasil → simpulan; tanpa sitasi) -->

        Kata kunci: kata kunci satu, kata kunci dua, kata kunci tiga <!-- TODO: pilih 3–5 kata kunci spesifik -->

        This study examines … <!-- TODO: fill the English abstract (background → objective → method → findings → conclusion; no citations) -->

        Keywords: keyword one, keyword two, keyword three <!-- TODO: pick 3–5 specific English keywords -->

        ```{=latex}
        \\end{singlespace}
        ```
        """)


def _daftar_isi(a):
    return dedent("""\
        ```{=latex}
        \\singlespacing
        \\renewcommand{\\contentsname}{DAFTAR ISI}
        \\tableofcontents
        \\clearpage
        \\renewcommand{\\listfigurename}{DAFTAR GAMBAR}
        \\listoffigures
        \\clearpage
        \\renewcommand{\\listtablename}{DAFTAR TABEL}
        \\listoftables
        \\clearpage
        \\listofrumus
        \\doublespacing
        ```

        <!-- TODO: daftar isi, gambar, tabel, dan rumus dibangkitkan otomatis oleh LaTeX -->
        """)


def _daftar_pustaka(a):
    return dedent("""\
        ```{=latex}
        \\clearpage
        \\singlespacing
        \\chapter*{DAFTAR PUSTAKA}
        \\addcontentsline{toc}{chapter}{DAFTAR PUSTAKA}
        ```

        ::: {#refs}
        :::

        ```{=latex}
        \\doublespacing
        ```

        <!-- TODO: lengkapi >= 20 rujukan (5 tahun terakhir, >= 30% internasional) di assets/refs.bib -->
        """)


# --------------------------------------------------------------------------- #
# BAB I–VI body chapters: heading, sub-sections, TODO + kamus:f id markers.
# --------------------------------------------------------------------------- #

def _bab_01(a):
    return dedent("""\
        ```{=latex}
        \\mainmatter
        \\pagestyle{fancy}
        ```

        # PENDAHULUAN

        ## Latar Belakang

        Penelitian ini dilatarbelakangi oleh … <!-- TODO: isi latar belakang (kondisi ideal vs kondisi nyata, fakta/angka, celah penelitian) --> <!-- kamus:f id=latar_belakang -->

        ## Rumusan Masalah

        Berdasarkan latar belakang tersebut, rumusan masalah dalam penelitian ini adalah … <!-- TODO: isi rumusan masalah --> <!-- kamus:f id=rumusan_masalah -->

        ## Batasan Masalah

        Batasan masalah dalam penelitian ini adalah … <!-- TODO: isi batasan masalah --> <!-- kamus:f id=batasan_masalah -->

        ## Tujuan

        Penelitian ini bertujuan untuk … <!-- TODO: isi tujuan --> <!-- kamus:f id=tujuan -->

        ## Manfaat

        Hasil penelitian ini diharapkan dapat memberikan manfaat … <!-- TODO: isi manfaat teoretis dan praktis --> <!-- kamus:f id=manfaat -->
        """)


def _bab_02(a):
    return dedent("""\
        # TINJAUAN PUSTAKA

        ## Objek Penelitian

        Objek penelitian ini adalah … <!-- TODO: isi objek penelitian --> <!-- kamus:f id=objek_penelitian -->

        ## Bidang Ilmu

        Bidang ilmu yang dikaji dalam penelitian ini adalah … <!-- TODO: isi bidang ilmu --> <!-- kamus:f id=bidang_ilmu -->

        ## Kajian Teori

        <!-- TODO: sajikan kerangka teori yang digunakan beserta definisinya. -->

        ### Diplomasi Publik

        <!-- TODO: uraikan konsep diplomasi publik. -->

        ### Soft Power dan Nation Branding

        <!-- TODO: uraikan konsep soft power dan nation branding. -->

        ### Analisis Kebijakan Luar Negeri (FPA)

        <!-- TODO: uraikan kerangka analisis kebijakan luar negeri. -->

        ## Penelitian Relevan

        <!-- TODO: ringkas penelitian terdahulu dan tunjukkan celah penelitian. -->

        ## Kerangka Pemikiran

        <!-- TODO: jelaskan rantai analisis dan sertakan Tabel 2.1 Kerangka Pemikiran. -->

        ## Metode Penelitian

        Metode yang digunakan dalam penelitian ini adalah … <!-- TODO: isi metode penelitian --> <!-- kamus:f id=metode_bab2 -->

        ## Alat Pengembangan

        Alat pengembangan yang digunakan dalam penelitian ini adalah … <!-- TODO: isi alat pengembangan --> <!-- kamus:f id=alat_pengembangan -->
        """)


def _bab_03(a):
    return dedent("""\
        # METODOLOGI PENELITIAN

        ## Metode Penelitian

        Penelitian ini menggunakan pendekatan … <!-- TODO: isi metode penelitian (jenis/pendekatan, studi kasus, unit analisis) --> <!-- kamus:f id=metode -->

        ### Teknik Pengumpulan Data

        Data dikumpulkan melalui … <!-- TODO: isi teknik pengumpulan data (dokumen resmi, pernyataan pemerintah, pemberitaan, publikasi akademik) --> <!-- kamus:f id=teknik_pengumpulan_data -->

        ### Studi Pustaka

        Studi pustaka dilakukan dengan … <!-- TODO: isi studi pustaka --> <!-- kamus:f id=studi_pustaka -->

        ## Penerapan Kerangka Analisis FPA

        Algoritma yang diterapkan dalam penelitian ini adalah … <!-- TODO: isi penerapan kerangka analisis FPA (tahapan: aktor, proses, keputusan, keluaran) dan sertakan Tabel 3.1 Kerangka Analisis FPA --> <!-- kamus:f id=penerapan_algoritma -->
        """)


def _bab_04(a):
    return dedent("""\
        # HASIL PENELITIAN

        ## Gambaran Umum Objek Penelitian

        Gambaran umum objek penelitian ini adalah … <!-- TODO: isi gambaran umum objek penelitian --> <!-- kamus:f id=gambaran_umum -->

        ## Hasil Penelitian

        Hasil penelitian ini menunjukkan bahwa … <!-- TODO: isi hasil penelitian secara ringkas --> <!-- kamus:f id=hasil_penelitian -->

        ### Strategi Diplomasi Vaksin Tiongkok

        Strategi diplomasi vaksin Tiongkok terhadap Indonesia … <!-- TODO: isi strategi diplomasi vaksin Tiongkok terhadap Indonesia --> <!-- kamus:f id=strategi_diplomasi -->

        ### Instrumen dan Mekanisme Diplomasi Publik

        Instrumen dan mekanisme diplomasi publik yang digunakan … <!-- TODO: isi instrumen dan mekanisme diplomasi publik --> <!-- kamus:f id=instrumen_mekanisme -->
        """)


def _bab_05(a):
    return dedent("""\
        # PEMBAHASAN

        ## Pembahasan

        Pembahasan dalam penelitian ini … <!-- TODO: isi pembahasan (kaitkan temuan dengan kerangka teori) --> <!-- kamus:f id=pembahasan -->

        ### Implikasi terhadap Persepsi Publik Indonesia

        Implikasi diplomasi vaksin terhadap persepsi publik Indonesia … <!-- TODO: isi implikasi terhadap persepsi publik Indonesia --> <!-- kamus:f id=implikasi -->

        ### Perbandingan dengan Penelitian Terdahulu

        Perbandingan hasil penelitian ini dengan penelitian terdahulu … <!-- TODO: isi perbandingan dengan penelitian terdahulu --> <!-- kamus:f id=perbandingan -->
        """)


def _bab_06(a):
    return dedent("""\
        # KESIMPULAN DAN SARAN

        ## Kesimpulan

        Berdasarkan hasil penelitian dan pembahasan, dapat disimpulkan bahwa … <!-- TODO: isi kesimpulan (jawab rumusan masalah) --> <!-- kamus:f id=simpulan -->

        ## Saran

        Saran untuk penelitian selanjutnya adalah … <!-- TODO: isi saran penelitian selanjutnya --> <!-- kamus:f id=saran -->
        """)


BUILDERS = {
    "00-halaman-judul.md": _halaman_judul,
    "01-lembar-persetujuan.md": _lembar_persetujuan,
    "02-lembar-pengesahan.md": _lembar_pengesahan,
    "03-surat-pernyataan.md": _surat_pernyataan,
    "04-kata-pengantar.md": _kata_pengantar,
    "05-abstrak.md": _abstrak,
    "06-daftar-isi.md": _daftar_isi,
    "10-bab-01-pendahuluan.md": _bab_01,
    "11-bab-02-tinjauan-pustaka.md": _bab_02,
    "12-bab-03-metodologi-penelitian.md": _bab_03,
    "13-bab-04-perancangan-sistem.md": _bab_04,
    "14-bab-05-hasil-dan-pembahasan.md": _bab_05,
    "15-bab-06-kesimpulan-dan-saran.md": _bab_06,
    "90-daftar-pustaka.md": _daftar_pustaka,
}


def build_parser():
    p = argparse.ArgumentParser(
        prog="scaffold.py",
        description="Generate the 14-file skripsi skeleton (STMIK Triguna Dharma).",
    )
    p.add_argument("--out", default=DEFAULT_OUT,
                   help=f"output directory (default: {DEFAULT_OUT})")
    p.add_argument("--title", default="Judul Skripsi", help="skripsi title")
    p.add_argument("--author", default="Nama Mahasiswa", help="author name")
    p.add_argument("--nim", default="0000000000", help="student id (NIM)")
    p.add_argument("--prodi", default="Hubungan Internasional", help="study program")
    p.add_argument("--year", default=None, help="year (default: current year)")
    p.add_argument("--force", action="store_true",
                   help="overwrite existing files")
    p.add_argument("--with-bib", dest="with_bib", action="store_true",
                   help="create a minimal assets/refs.bib if absent")
    p.add_argument("--list", action="store_true",
                   help="print the planned file list and exit")
    return p


def plan(out_dir):
    return [os.path.join(out_dir, name) for name in FILE_ORDER]


def main(argv=None):
    args = build_parser().parse_args(argv)

    year = args.year if args.year is not None else str(_current_year())
    ctx = {
        "title": args.title,
        "author": args.author,
        "nim": args.nim,
        "prodi": args.prodi,
        "year": year,
    }

    if args.list:
        print(f"DAFTAR FILE (out={args.out}):")
        for path in plan(args.out):
            print(f"  {path}")
        return 0

    created = 0
    skipped = 0

    out_dir = args.out
    os.makedirs(out_dir, exist_ok=True)

    for name in FILE_ORDER:
        path = os.path.join(out_dir, name)
        existed = os.path.exists(path)
        if existed and not args.force:
            print(f"LEWATI (sudah ada): {path}")
            skipped += 1
            continue
        content = BUILDERS[name](ctx)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(content)
        print(f"TULIS (timpa): {path}" if existed else f"BUAT: {path}")
        created += 1

    if args.with_bib:
        _maybe_write_bib(args.out)

    print(f"SKAFOLD: {created} dibuat, {skipped} dilewati")
    return 0


def _current_year():
    import datetime
    return datetime.date.today().year


def _maybe_write_bib(out_dir):
    """Write a minimal assets/refs.bib only if no refs.bib exists anywhere."""
    candidates = [
        os.path.join(out_dir, os.pardir, "assets", "refs.bib"),
        os.path.join(out_dir, os.pardir, os.pardir, "assets", "refs.bib"),
        os.path.join("assets", "refs.bib"),
    ]
    candidates = [os.path.normpath(c) for c in candidates]
    if any(os.path.exists(c) for c in candidates):
        return
    target = candidates[0]
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8") as fh:
        fh.write(REFS_BIB_STUB)
    print(f"BUAT: {target}")


if __name__ == "__main__":
    sys.exit(main())
