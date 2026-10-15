# Pedoman Skripsi — STMIK Triguna Dharma (Hubungan Internasional)

Checklist encoding the STMIK Triguna Dharma (TGD) *Hubungan Internasional*
skripsi pedoman. Tata letak PDF kini mengikuti konvensi jurnal Hubungan
Internasional: margin **2,5 cm** di keempat sisi, spasi **1,5**, dan penomoran
bab memakai angka Romawi dengan titik (`I.`, `II.`, …) **tanpa kata "BAB"**.

## Paper & page layout

- [ ] Paper: **A4 70 g**.
- [ ] Margins (all pages): top **2,5 cm** / right **2,5 cm** / bottom **2,5 cm** / left **2,5 cm**.
- [ ] First-line indent: **0,5 cm**.
- [ ] Body text: **1,5 spasi**.

## Typography

- [ ] **Judul Bab**: Times New Roman **14 pt bold**, ALL-CAPS, centered.
- [ ] **Sub-judul**: Times New Roman **12 pt bold**.

## Front matter & pagination

- [ ] **DAFTAR SINGKATAN** (setelah DAFTAR ISI) di `content/skripsi/07-daftar-singkatan.md`; setiap singkatan dijabarkan `SINGKATAN (Kepanjangan)` pada penyebutan pertama. Rincian: `docs/layout-framework.md`.
- [ ] Front-matter items followed by **Abstrak** in Times New Roman **12 pt**, with **roman** page numbers at **bottom-center**.
- [ ] Chapter (BAB) pages use **arabic** page numbers: chapter opening page at **bottom-center**, other pages at **top-right**.

## Figures, tables, equations & code

- [ ] Figures numbered `Gambar <bab>.<n>` with the caption **BELOW** the figure.
- [ ] Tables numbered `Tabel <bab>.<n>` with the caption **ABOVE** the table.
- [ ] Equations numbered `(<bab>.<n>)`, right-numbered, in **Cambria Math 12**.
- [ ] Code listings in **Courier New 10**, **1 spasi**.

## References & length

- [ ] ≥ **20 references**, all within the **last 5 years**.
- [ ] Periode sasaran dideklarasikan pada `assets/bahasa/kamus-id.yaml` §`recency.periode_default`; sumber bukti di luar periode gagal `tools/validators/evidence_recency.py`.
- [ ] Sitasi memakai markup `[@key]` (APA author-date); catatan kaki hanya penjelas (tanpa sitasi); daftar pustaka dirender lewat blok `::: {#refs} :::`. Rincian: `docs/citation-framework.md`.
- [ ] ≥ **30%** of sources are **international journal/proceedings**.
- [ ] **BAB I–VI** total ≥ **50 pages**.

## BAB structure with required sub-sections

- **BAB I Pendahuluan**
  - Latar Belakang
  - Rumusan Masalah
  - Batasan Masalah
  - Tujuan
  - Manfaat
  Aturan BAB I (A1–A8/B1–B3) ditegakkan mesin: `docs/bab1-framework.md`.
- **BAB II Tinjauan Pustaka**
  - Objek Penelitian
  - Bidang Ilmu
  - Kajian Teori (Diplomasi Publik; Soft Power dan Nation Branding; Analisis Kebijakan Luar Negeri (FPA))
  - Penelitian Relevan
  - Kerangka Pemikiran
  - Metode Penelitian
  - Alat Pengembangan
- **BAB III Metodologi Penelitian**
  - Metode Penelitian (Teknik Pengumpulan Data, Studi Pustaka)
  - Penerapan Kerangka Analisis FPA
- **BAB IV Hasil Penelitian**
  - Gambaran Umum Objek Penelitian
  - Hasil Penelitian (Strategi Diplomasi Vaksin Tiongkok; Instrumen dan Mekanisme Diplomasi Publik)
- **BAB V Pembahasan**
  - Pembahasan (Implikasi terhadap Persepsi Publik Indonesia; Perbandingan dengan Penelitian Terdahulu)
- **BAB VI Kesimpulan dan Saran**
  - Kesimpulan
  - Saran

## Ragam Bahasa

The skripsi body must use the Indonesian academic register (same rules as the
article — see [docs/bahasa-artikel.md](bahasa-artikel.md)):

- **No first/second person pronouns** (`saya`, `aku`, `kami`, `kita`, `anda`,
  `kamu`, `kalian`) in body chapters; prefer passive (`dilakukan`, `digunakan`,
  `dikumpulkan`, `dianalisis`) and allow `penulis`/`peneliti` as impersonal
  self-reference.
- **Baku diction** (EYD Edisi V): `analisa→analisis`, `praktek→praktik`,
  `merubah→mengubah`, `aktifitas→aktivitas`, `hipotesa→hipotesis`,
  `sistim→sistem`, `standard→standar`, `jadual→jadwal`, `obyek→objek`,
  `metoda→metode`.
- **Exemption:** `content/skripsi/03-surat-pernyataan.md` is exempt — it is a
  personal legal declaration (`karya saya sendiri`) and legitimately uses first
  person.

Struktur, rangkai argumen, dan leksikon mengikuti `docs/kamus-bahasa-artikel.md`; `make check` menegakkannya.

`make check` runs the register linter over the body chapters and the article.

## Convention: ALL-CAPS BAB headings in Markdown

Write BAB headings in the Markdown source in **ALL CAPS**, e.g.:

```markdown
# PENDAHULUAN
```

## DAFTAR RUMUS

DAFTAR RUMUS entries require a **manual** `\addcontentsline{rum}{rumus}{...}` line
after each listed equation.

## Citation conflict (IEEE vs APA 7)

The pedoman mandates **IEEE**, but this repo defaults to **APA 7**. To switch to IEEE,
set `CSL := assets/csl/ieee.csl` in the Makefile.
