# Research Gap Store

Direktori ini menyimpan judul penelitian, hasil pemeriksaan ketersediaan
(availability), dan laporan celah penelitian (research gap) untuk Nykripsi v2.

- `judul.json` — registry (array JSON) berisi catatan judul. Ini sumber kebenaran.
- `index.md` — indeks Markdown yang **dibuat ulang** oleh `research_gap.py render`.
  Jangan sunting berkas ini; sunting `judul.json`.
- `gap-<slug>.md` — laporan celah penelitian per judul yang terpilih.

Alat utamanya adalah `.claude/skills/nykripsi/scripts/research_gap.py` (stdlib
saja). Rincian metode ada di `docs/research-gap.md`.

## Skema Catatan

Setiap catatan di `judul.json` selalu memuat kunci berikut:

| Kunci | Tipe | Keterangan |
| --- | --- | --- |
| `id` | str | `judul-<checked>-<slug(judul)>`; bentrokan diberi akhiran `-1`, `-2`, … |
| `judul` | str | Judul apa adanya seperti dimasukkan. |
| `judul_norm` | str | Judul ternormalisasi (`norm_title`): ASCII-fold, huruf kecil, hanya `[a-z0-9]`, spasi tunggal. |
| `status` | str | `selected` \| `candidate` \| `rejected`. |
| `verdict` | str | `available` \| `duplicate` \| `too-similar`. |
| `threshold` | float | Ambang kemiripan (bawaan `0.8`). |
| `origin` | str | `auto` \| `browser` \| `manual`. |
| `checked` | str | Tanggal `YYYY-MM-DD` saat diperiksa. |
| `query` | str | String judul yang dipakai untuk pencarian. |
| `matches` | list | Daftar objek match (lihat di bawah). |
| `notes` | str | Catatan bebas. |

Setiap objek `matches` selalu memuat:

| Kunci | Tipe | Keterangan |
| --- | --- | --- |
| `title` | str | Judul karya yang ditemukan. |
| `url` | str | URL non-kosong (untuk registry: `registry:<id>`). |
| `doi` | str \| null | DOI bila ada. |
| `year` | int \| null | Tahun bila ada. |
| `backend` | str | `crossref` \| `openalex` \| `scholar` \| `registry` \| nama lain (mis. `google-scholar`). |
| `similarity` | float | Skor Jaccard token judul (`1.0` bila identik). |
| `kind` | str | `exact` bila `norm_title` sama persis, selain itu `similar`. |

## Aturan Ketersediaan dan Verdict

Judul dinilai dari kumpulan match yang terkumpul:

- `duplicate` — ada match dengan `kind == "exact"` (judul ternormalisasi sama
  persis). Judul tidak boleh dipakai.
- `too-similar` — tidak ada match persis, tetapi kemiripan maksimum
  `>= threshold`. Judul tidak boleh dipakai.
- `available` — selain kedua hal di atas. Judul boleh dipakai.

Aturan blokir: catatan berstatus `selected` **wajib** berverdict `available`.
Validator `research` akan gagal bila ada judul terpilih yang tidak tersedia,
atau bila ada lebih dari satu judul terpilih.

Alur status: judul `available` otomatis menjadi `selected` dan menurunkan
catatan `selected` sebelumnya menjadi `candidate`. Judul `duplicate` /
`too-similar` menjadi `rejected`. Bila lintasan browser kemudian menemukan
match baru yang memblokir sebuah judul `selected`, statusnya diubah menjadi
`rejected`.

## Subperintah `research_gap.py`

- `check JUDUL [--limit N] [--threshold F] [--registry PATH] [--json] [--no-save] [--email ADDR]`
  — kumpulkan match dari `crossref`, `openalex`, `scholar`, dan `registry`,
  hitung verdict, lalu tulis catatan. Keluar `0` bila tersedia, `1` bila
  diblokir.
- `browser-record JUDUL --title T --url U [--doi D] [--year Y] [--backend B] [--registry PATH] [--threshold F] [--json]`
  — catat satu match hasil lintasan browser ke catatan yang sudah ada.
- `gap JUDUL [--registry PATH] [--out PATH] [--prior "TITLE|URL|WEAKNESS|ANGLE"]`
  — tulis kerangka laporan celah penelitian.
- `render [--registry PATH] [--index PATH]`
  — tulis ulang `research/index.md` dari registry.

## Cross-Check Browser (Wajib)

Pemeriksaan otomatis tidak cukup: beberapa basis data dan mesin pencari tidak
dapat diakses dari skrip. Setelah `check`, lakukan lintasan browser manual
(Google Scholar, Google, repositori institusi, dsb.) atas judul tersebut, lalu
catat setiap temuan yang relevan dengan `browser-record`. Ini menandai catatan
sebagai `origin="browser"` dan menghitung ulang verdict.

## Metode Research Gap

Laporan celah (`gap`) memakai dua alat berpikir:

1. **Dimensi kelemahan** — periksa penelitian terdahulu pada sumbu: cakupan
   (kasus/konteks terbatas), metode (desain, sampel, pengukuran), teori
   (kerangka usang atau tidak sesuai konteks), data (sumber, rentang waktu),
   dan generalisasi (klaim melebihi bukti).
2. **Matriks sudut pandang** — silangkan setiap kelemahan dengan alternatif
   sudut: aktor lain, level analisis berbeda (mikro/meso/makro), periode lain,
   kerangka teori alternatif, metode berbeda, dan konteks komparatif.

Hasil silang ini dirumuskan menjadi celah penelitian dan kebaruan yang
diusulkan pada laporan `research/gap-<slug>.md`.

## Aturan Provenance

**Jangan pernah mengarang match.** Setiap match berasal dari pengambilan data
langsung (Crossref, OpenAlex, scholar) atau dari lintasan browser agen yang
dicatat dengan `browser-record`. Bila tidak ada bukti, biarkan `matches` kosong
dan judul dinilai `available`.
