# Kerangka Artikel Jurnal HI/IR — Varian Dwibahasa `artikel-hi` (IA1–IA10)

Kerangka ini menurunkan **aturan absolut**, **frame drafting**, **pita dan
ambang**, serta **rubrik** untuk **varian artikel jurnal HI/IR dwibahasa
(Indonesia utama)** yang diberi nama **`artikel-hi`** beserta padanan
Inggrisnya **`artikel-hi-en`**. Kerangka ini **melengkapi** — **tidak
menggantikan** — [`docs/article-framework.md`](article-framework.md) (kerangka
artikel Sinta/Scopus/HI-IR, AR1–AR9),
[`docs/conversion-skripsi-to-article.md`](conversion-skripsi-to-article.md)
(kepala bagian kanonik + tiga rumus inti),
[`docs/abstrak-framework.md`](abstrak-framework.md) (anatomi abstrak 150–250
kata + 3–6 kata kunci),
[`docs/bab1-framework.md`](bab1-framework.md) (gerak Pendahuluan CARS/Swales),
[`docs/fulltext-framework.md`](fulltext-framework.md) (F1–F8, teks utuh),
[`docs/subject-framework.md`](subject-framework.md) (S1–S8, kanal sapuan
sumber), [`docs/sintesa-diagram-framework.md`](sintesa-diagram-framework.md)
(TS1–TS6, diagram sintesa lensa),
[`docs/layout-framework.md`](layout-framework.md) (LT6, tata letak Sinta
terpusat), [`docs/citation-framework.md`](citation-framework.md) (CT1–CT6,
sitasi APA `[@key]`), dan [`docs/bahasa-artikel.md`](bahasa-artikel.md) (ragam
bahasa ilmiah Indonesia). Setiap klaim di sini bersumber pada **berkas
repositori** (dengan bagiannya) atau **literatur** yang beralamat URL; **tidak
ada klaim tanpa sumber**.

> **Status.** Kesepuluh aturan absolut (IA1–IA10) berlaku pada **dua berkas
> baru**: `content/artikel/artikel-hi.md` (ID, fail-tier) dan
> `content/artikel-en/artikel-hi-en.md` (EN, fail-tier). Keduanya belum
> terisi naskah penuh; harness (meta, skeleton, target `make`, validator)
> ditegakkan lebih dahulu agar pengisian naskah mengikuti kerangka.

---

## 1. Definisi dan Fungsi

**Definisi.** Artikel HI/IR adalah **laporan mandiri (self-contained)**
berstruktur IMRaD yang membaca fenomena hubungan internasional melalui
**lensa teori**, bukan sekadar deskripsi peristiwa. Varian **`artikel-hi`**
adalah varian **dwibahasa (Indonesia utama)** yang menghadirkan **dua berkas,
dua keluaran** — berkas Indonesia `content/artikel/artikel-hi.md` dan berkas
Inggris `content/artikel-en/artikel-hi-en.md` — yang masing-masing memuat
abstrak dwibahasa (`docs/abstrak-framework.md` §4;
`docs/article-framework.md` §2 Tabel 2.2).

**Fungsi.** Artikel HI/IR menjalankan tiga fungsi yang saling terkait:

1. **Seleksi (screening).** Memungkinkan penyunting dan pembaca memutuskan
   apakah naskah layak ditelaah dan dibaca penuh; substansi artikel adalah
   indikator terberat akreditasi (bobot **39**) di ARJUNA
   ([`docs/sinta-reference.md`](sinta-reference.md) §"ARJUNA 8 indicators +
   weights").
2. **Diseminasi (dissemination).** Menyebarkan temuan melalui jurnal terindeks
   sehingga dapat dikutip; anatomi lengkap (judul, abstrak, kata kunci, IMRaD,
   referensi) menaikkan keterindeksan
   ([`docs/sinta-reference.md`](sinta-reference.md) §"Article anatomy").
3. **Kepatuhan (compliance).** Memenuhi syarat pelaporan dan tata kelola
   jurnal — abstrak dwibahasa, referensi lengkap & tersitasi, serta bagian
   akhir sesuai kebijakan jurnal
   ([`docs/sinta-reference.md`](sinta-reference.md) §"Pre-submit checklist").

---

## 2. Lanskap Venue & Anatomi

Artikel HI/IR berdiri pada lanskap venue yang sama dengan artikel jurnal lain
(`docs/article-framework.md` §2 Tabel 2.1), tetapi varian **`artikel-hi`**
menambahkan syarat **kembar berkas** (ID + EN). Tabel 2.1 memetakan venue yang
relevan; Tabel 2.2 merangkum komponen anatomi yang berlaku umum; Tabel 2.3
menambahkan komponen khas varian dwibahasa.

### Tabel 2.1 — Venue

| Venue | Struktur wajib | Panjang | Sumber |
|---|---|---|---|
| HI/IR | `Pendahuluan` → `Metode Penelitian` → `Hasil dan Pembahasan` → `Simpulan dan Saran` → `Daftar Pustaka` | 5.000–7.000 kata (contoh Global UI) | `docs/ir-corpus/MANIFEST.md`; `docs/argument-framework.md` §2 |
| Sinta 3–6 | IMRaD; sering berbahasa Indonesia; kepala bagian kanonik enam | 3.000–8.000 kata / 10–20 halaman | `docs/sinta-reference.md`; `docs/conversion-skripsi-to-article.md` |
| Scopus | IMRaD + gerak CARS; **bagian akhir per-jurnal** — `unverified — confirm first` | per *author guidelines* — `unverified — confirm first` | `docs/bab1-framework.md` §10 |

### Tabel 2.2 — Komponen anatomi

| Komponen | Isi | Sumber |
|---|---|---|
| Title | ringkas, 6–16 kata | `docs/judul-framework.md` (JD1–JD6) |
| Abstract | 150–250 kata, ID + EN | `docs/abstrak-framework.md` §4 |
| Keywords | 3–6 | `docs/abstrak-framework.md` §5 |
| `periode` (meta) | periode sasaran dokumen, bawaan `2020–2025`; jendela kebaruan ≤ 5 tahun diukur terhadapnya | `templates/artikel-hi-meta.yaml`; `assets/bahasa/kamus-id.yaml` §`recency.periode_default`; §3 IA9 |
| IMRaD | Pendahuluan → Metode → Hasil dan Pembahasan → Simpulan | `docs/article-framework.md` §3 |
| References | lengkap, konsisten, dan **tersitasi dalam teks** | `docs/citation-framework.md` (CT1–CT6) |

### Tabel 2.3 — Komponen khas varian `artikel-hi`

| Komponen | Isi | Sumber |
|---|---|---|
| Dua berkas | `content/artikel/artikel-hi.md` (ID) + `content/artikel-en/artikel-hi-en.md` (EN) | `Makefile` (`artikel-hi`, `artikel-hi-en`) |
| Abstrak berlapis | ID: `lang=id` lalu `lang=en`; EN: `lang=en` lalu `lang=id` | `docs/abstrak-framework.md` §4 |
| Lensa terpadu | diagram sintesa (`.sintesa`) IPE + konsumen | `docs/sintesa-diagram-framework.md` (TS1–TS6) |

Anatomi menentukan **komponen apa** yang harus ada; aturan IA1–IA10 di §3
menentukan **tingkat kepatuhan** dan **penegaknya**.

---

## 3. Aturan Absolut (IA1–IA10)

Sepuluh aturan berikut bersifat **absolut**. Setiap butir menyebut definisi,
penegak (bila ada mesinnya), dan sumbernya.

1. **IA1 — Bentuk HI/IR.** Lima kepala kanonik berurutan: `Pendahuluan` →
   `Metode Penelitian` → `Hasil dan Pembahasan` → `Simpulan dan Saran` →
   `Daftar Pustaka` (**tanpa** `Ucapan Terima Kasih`). Urutan ini mengikat
   build repositori. Penegak: `tools/validators/article_framework.py`
   (tuple `HEADING_IDS_5`). Sumber:
   `docs/conversion-skripsi-to-article.md` §"Struktur dan Kamus";
   `assets/bahasa/kamus-id.yaml` §`kepala_bagian`.
2. **IA2 — Dwibahasa (Indonesia utama).** Dua berkas, dua keluaran:
   `content/artikel/artikel-hi.md` (ID) dan
   `content/artikel-en/artikel-hi-en.md` (EN); target `make artikel-hi` dan
   `make artikel-hi-en`. Berkas ID memuat abstrak dwibahasa (`lang=id` lalu
   `lang=en`); berkas EN memuat abstrak `lang=en` lalu `lang=id`. Penegak:
   `tools/validators/article_framework.py`. Sumber:
   `docs/abstrak-framework.md`; `Makefile`.
3. **IA3 — Data sekunder.** Seluruh bukti berasal dari sumber sekunder (laman
   web, artikel, berita, siaran pers) yang dikumpulkan lewat `search.py` /
   `scrape.py` dan dipromosikan ke `assets/refs.bib`; tidak ada data primer.
   Sumber: `docs/source-classification.md`;
   `docs/subject-framework.md` §3; `.claude/skills/nykripsi/scripts/search.py`;
   `tools/scrape.py`.
4. **IA4 — Provenans.** Setiap sumber dicatat `subject`/`channel` pada
   `sources/registry.json`; setiap klaim disitasi `[@key]`; dilarang mengarang
   URL, hash, atau data. Penegak: `tools/validators/citation_framework.py`
   (CT1–CT6); `tools/validators/papers.py`. Sumber:
   `docs/subject-framework.md` (S1); `docs/citation-framework.md`.
5. **IA5 — Teks utuh.** Sumber sekunder tunduk pada
   [`docs/fulltext-framework.md`](fulltext-framework.md) (F1–F8) sebelum
   dipakai mengklaim isi. Sumber: `docs/fulltext-framework.md` §3–§6.
6. **IA6 — Lensa terpadu.** Lensa IPE (kebijakan perdagangan/impor) +
   konsumen (ekuitas merek/negara asal), disajikan sebagai diagram sintesa
   (blok `.sintesa`). Penegak: `tools/validators/sintesa_diagram.py`
   (TS1–TS6). Sumber: `docs/sintesa-diagram-framework.md`.
7. **IA7 — Ragam bahasa.** ID baku EYD Edisi V, impersonal; EN register
   akademik; tanpa frasa AI generik. Penegak: `tools/check-bahasa.sh`. Sumber:
   `docs/bahasa-artikel.md`.
8. **IA8 — Tata letak & sitasi.** Tata letak Sinta terpusat (LT6) dan sitasi
   APA `[@key]` dengan blok `::: {#refs} :::`. Penegak:
   `tools/validators/layout_typography.py` (LT6);
   `tools/validators/citation_framework.py` (CT3). Sumber:
   `docs/layout-framework.md` §2–§3; `tools/pandoc_filters/sinta_layout.lua`;
   `templates/artikel-preamble.tex`; `Makefile`.
9. **IA9 — Kebaruan bukti.** Setiap sumber bukti (Berita/Siaran pers/Artikel/
   Web) **wajib** ≤ 5 tahun dan **di dalam** `periode` dokumen (bawaan
   `2020–2025`); kanal ditandai pada `note` bib. Penegak:
   `tools/validators/evidence_recency.py`. Sumber:
   `templates/artikel-hi-meta.yaml`; `assets/bahasa/kamus-id.yaml`
   §`recency.periode_default`; `docs/bab1-framework.md` A8.
10. **IA10 — Tautan daftar pustaka.** Hanya berita/siaran pers/web menampilkan
   URL; karya akademik menampilkan DOI (`assets/csl/apa.csl` `source-DOI-URL`),
   tidak pernah URL. Penegak: `tools/validators/citation_framework.py` (CT7).
   Sumber: `docs/citation-framework.md` (CT7); `assets/csl/apa.csl`.

**Perintah verifikasi.** Pemeriksaan kepatuhan mesin dijalankan dengan:

```
python3 tools/validate.py article_framework judul figures_tables sintesa_diagram citation_framework papers
```

Build kedua keluaran dijalankan dengan:

```
make artikel-hi
make artikel-hi-en
```

---

## 4. Frame (Alur Drafting)

Menulis artikel `artikel-hi` mengikuti enam langkah berurutan:

1. **Tetapkan venue.** Pilih jurnal sasaran dan unduh templatnya lebih dahulu;
   struktur dan panjang mengikuti *Author Guidelines* (§2, §6).
2. **Kumpulkan sumber sekunder.** Sapu kanal `press` → `news` → `article` →
   `official` → `web` hingga saturasi (`docs/subject-framework.md` §3–§4);
   promosikan entri ke `assets/refs.bib`.
3. **Tulis abstrak terakhir.** Abstrak ditulis **paling akhir** setelah badan
   selesai (`docs/conversion-skripsi-to-article.md` §"Rewrite rules").
4. **Susun IMRaD lima kepala.** Bangun badan mengikuti IA1 (§3).
5. **Pasang lensa terpadu.** Sajikan diagram sintesa IPE + konsumen (§3 IA6).
6. **Jalankan verifikasi.** Periksa kepatuhan mesin (§3) dan linter register
   (`tools/check-bahasa.sh`).

---

## 5. Model Komponen

| Lapis | Isi | Sumber |
|---|---|---|
| **Sumber (naskah)** | artikel draf repositori | `content/artikel/artikel-hi.md`; `content/artikel-en/artikel-hi-en.md` |
| **Metadata** | meta 17 kunci (varian HI) | `templates/artikel-hi-meta.yaml`; `templates/artikel-hi-en-meta.yaml` |
| **Registry (kamus mesin)** | urutan kepala bagian + formula | `assets/bahasa/kamus-id.yaml` §`kepala_bagian` |
| **Penegak** | validator kerangka, sitasi, diagram, judul | `tools/validators/article_framework.py`; `tools/validators/citation_framework.py`; `tools/validators/sintesa_diagram.py`; `tools/validators/judul.py` |
| **Build pipeline** | target build artikel | `Makefile` (`artikel-hi`, `artikel-hi-en`) |

Registry mengikat komponen ke **id kanonik** (`pendahuluan`, `metode`, `hasil`,
`simpulan`, `pustaka`); penegak memastikan himpunan dan urutannya sesuai (§3
IA1), sitasi ↔ entri pustaka seimbang (§3 IA4), dan diagram sintesa sah (§3
IA6).

---

## 6. Pita dan Ambang

| Komponen | Pita / ambang | Sumber |
|---|---|---|
| Judul | 6–16 kata, satu bahasa | `docs/judul-framework.md` (JD4, JD6) |
| Abstrak | 150–250 kata × 2 per berkas | `docs/abstrak-framework.md` §4 |
| Kata kunci | 3–6 | `docs/abstrak-framework.md` §5 |
| Kepala bagian | 5 kanonik (tanpa `Ucapan Terima Kasih`) | §3 IA1 |
| Referensi | lengkap & tersitasi | `docs/citation-framework.md` |
| Sumber mutakhir | ≥ 30% sumber ≤ 5 tahun, diukur terhadap `periode` (penegak `tools/validators/evidence_recency.py`; §3 IA9) | `docs/bab1-framework.md` A8 |
| `periode` (meta) | periode sasaran dokumen, bawaan `2020–2025`; jendela ≤ 5 tahun diukur terhadapnya | `templates/artikel-hi-meta.yaml`; `assets/bahasa/kamus-id.yaml` §`recency.periode_default` |

Ambang di atas **dikalibrasi pada berkas varian** yang baru dibuat
(`content/artikel/artikel-hi.md`, `content/artikel-en/artikel-hi-en.md`) serta
dipadankan dengan kerangka yang dirujuk tiap baris. Bila kelak muncul berkas
sah yang melampaui ambang, konstanta di
`tools/validators/article_framework.py` **dan** tabel di dokumen ini harus
diubah **bersamaan** agar tetap selaras.

---

## 7. Matriks Kepatuhan per-Tingkat

Legenda sel: **wajib** = harus ada; **disarankan** = praktik baik, bukan syarat
keras; **varian** = berlaku **per jurnal** dan ditandai `unverified — confirm
first`; **tidak berlaku** = aturan tidak relevan untuk tingkat itu.

| Aturan | HI/IR (ID) | HI/IR (EN) | Sinta 3–6 | Scopus |
|---|---|---|---|---|
| **IA1** lima kepala kanonik, urut | wajib | wajib | disarankan | disarankan |
| **IA2** dwibahasa (dua berkas, dua keluaran) | wajib | wajib | disarankan | disarankan |
| **IA3** data sekunder (tanpa data primer) | wajib | wajib | wajib | wajib |
| **IA4** provenans (`subject`/`channel`, `[@key]`) | wajib | wajib | wajib | wajib |
| **IA5** teks utuh (F1–F8) | wajib | wajib | wajib | wajib |
| **IA6** lensa terpadu (`.sintesa`) | wajib | disarankan | disarankan | disarankan |
| **IA7** ragam bahasa (EYD V / akademik EN) | wajib | wajib | wajib | disarankan |
| **IA8** tata letak LT6 & sitasi APA | wajib | disarankan | wajib | disarankan |

**Catatan.** Kolom **Scopus** hanya menyatakan bar struktural yang lazim
diminta jurnal terindeks; setiap syarat spesifik jurnal ditandai `unverified —
confirm first` dan harus dikonfirmasi dari *Author Guidelines* jurnal sasaran.

---

## 8. Daftar Periksa Do / Don't

| ✔ Lakukan | ✘ Hindari |
|---|---|
| Pakai lima kepala kanonik (`Pendahuluan` … `Daftar Pustaka`) | Menambah `Ucapan Terima Kasih` pada varian HI |
| Sediakan dua berkas (ID + EN) dan dua target build | Hanya menyediakan satu bahasa |
| Kumpulkan bukti dari sumber sekunder lewat `search.py`/`scrape.py` | Menyisipkan data primer tanpa pencatatan |
| Catat `subject`/`channel` dan sitasi `[@key]` | Mengarang URL, hash, atau data |
| Verifikasi teks utuh (F1–F8) sebelum mengklaim isi | Mengklaim isi dari abstrak saja |
| Sajikan lensa terpadu sebagai diagram `.sintesa` | Menyajikan lensa tanpa diagram sintesa |
| Pakai ragam impersonal & diksi baku EYD Edisi V | Kata ganti orang / frasa AI generik |

---

## 9. Rubrik Penilaian (0–2 per IA1–IA8)

Skor **0–2** per aturan; **8 aturan × 2 = maksimum 16**.

| Aturan | 0 | 1 | 2 |
|---|---|---|---|
| **IA1** lima kepala kanonik | Kepala tidak sesuai / urutan salah | Sebagian kepala ada, urutan tidak lengkap | Lima kepala kanonik hadir dan berurutan |
| **IA2** dwibahasa | Tidak ada / hanya satu bahasa | Dua berkas ada, abstrak tidak berlapis | Dua berkas + abstrak berlapis lengkap |
| **IA3** data sekunder | Ada data primer tanpa pencatatan | Sumber campuran | Seluruh bukti dari sumber sekunder |
| **IA4** provenans | Tanpa `subject`/`channel` atau tanpa `[@key]` | Sebagian sumber tercatat | Semua sumber tercatat + tersitasi |
| **IA5** teks utuh | Klaim dari abstrak | Sebagian diverifikasi | Seluruh klaim tervalidasi F1–F8 |
| **IA6** lensa terpadu | Tidak ada lensa | Lensa ada tanpa diagram | Lensa terpadu + diagram `.sintesa` |
| **IA7** ragam bahasa | Ada kata ganti / frasa AI | Satu pelanggaran ringan | Nol pelanggaran |
| **IA8** tata letak & sitasi | Tanpa LT6 / tanpa `::: {#refs} :::` | Salah satu belum lengkap | LT6 + sitasi APA lengkap |

**Tafsiran skor total (0–16):**

- **15–16** — siap kirim (seluruh aturan absolut terpenuhi).
- **11–14** — revisi ringan (perkuat lensa, provenans, atau pita).
- **6–10** — perlu menulis ulang bagian yang lemah sebelum diajukan.
- **≤ 5** — kerangka artikel belum layak; kembalikan ke tahap drafting (§4).

---

## 10. Sumber

### 10.1 Berkas repositori (bukti utama)

- `docs/article-framework.md` — kerangka artikel Sinta/Scopus/HI-IR (AR1–AR9).
- `docs/abstrak-framework.md` — anatomi abstrak 150–250 kata + 3–6 kata kunci.
- `docs/conversion-skripsi-to-article.md` — kepala kanonik + *rewrite rules*.
- `docs/fulltext-framework.md` — aturan teks utuh (F1–F8).
- `docs/subject-framework.md` — kanal sapuan sumber (S1–S8).
- `docs/sintesa-diagram-framework.md` — diagram sintesa lensa (TS1–TS6).
- `docs/layout-framework.md` — tata letak Sinta terpusat (LT6).
- `docs/citation-framework.md` — sitasi APA `[@key]` (CT1–CT6).
- `docs/bahasa-artikel.md` — ragam bahasa ilmiah Indonesia.
- `docs/judul-framework.md` — mutu judul (JD1–JD6).
- `assets/bahasa/kamus-id.yaml` — §`kepala_bagian`, §`artikel`, §`judul`.
- `assets/refs.bib` — daftar pustaka terpusat.
- `sources/registry.json` — registry `subject`/`channel`.
- `tools/validators/article_framework.py` — penegak IA1–IA2.
- `tools/validators/citation_framework.py` — penegak IA4, IA8.
- `tools/validators/sintesa_diagram.py` — penegak IA6.
- `tools/validators/judul.py` — penegak mutu judul (JD1–JD6).
- `tools/validators/papers.py` — penegak sitasi ↔ entri pustaka.
- `content/artikel/artikel-hi.md` — naskah varian ID (fail-tier).
- `content/artikel-en/artikel-hi-en.md` — naskah varian EN (fail-tier).
- `templates/artikel-hi-meta.yaml`, `templates/artikel-hi-en-meta.yaml` —
  metadata varian.
- `Makefile` — target `artikel-hi`, `artikel-hi-en`.

### 10.2 Perintah seed penemuan sumber

Penemuan sumber sekunder (IA3–IA4) dijalankan dengan perintah persis berikut
(dari `docs/subject-framework.md` §3):

```
python3 .claude/skills/nykripsi/scripts/search.py news "Alpinestars" --class secondary
python3 .claude/skills/nykripsi/scripts/search.py article "Alpinestars" --class secondary
python3 tools/scrape.py sweep "Alpinestars" --channel press
python3 tools/scrape.py sweep "Alpinestars" --channel news
python3 tools/scrape.py sweep "Alpinestars" --channel article
python3 tools/scrape.py sweep "Alpinestars" --channel official
python3 tools/scrape.py sweep "Alpinestars" --channel web
make scrape S="Alpinestars"
```

Setiap sumber yang terkumpul dipromosikan ke `assets/refs.bib` lewat
`make promote` dan diverifikasi teks utuhnya lewat `make fulltext F=<berkas>`
(`docs/fulltext-framework.md` §3).

### 10.3 Verifikasi

```
python3 tools/validate.py article_framework judul figures_tables sintesa_diagram citation_framework papers
make artikel-hi
make artikel-hi-en
```
