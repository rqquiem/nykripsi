# Kerangka Penulisan Abstrak Artikel Jurnal — Berbasis Bukti

Kerangka ini menurunkan aturan penulisan **abstrak artikel jurnal** dari dua
korpus lokal di repositori ini dan dari literatur penulisan akademik
internasional. Setiap aturan disertai bukti: **hitungan terukur** dari korpus
atau **sitasi** (berkas repositori + bagian, atau rekaman nyata dari
`scholar.py` beserta URL). Tidak ada klaim tanpa sumber.

Ringkasan hitungan mentah yang dikutip di bawah dihasilkan dengan
`pdftotext -f 1 -l 4 <pdf> -` atas **29 PDF** di
[`docs/sinta-corpus/`](sinta-corpus/) (Sinta 1–6) dan **43 PDF** di
[`docs/ir-corpus/`](ir-corpus/) (21 jurnal Indonesia + 22 jurnal
internasional). Hitungan lengkap tersedia di
[`docs/kamus-riset-korpus.md`](kamus-riset-korpus.md) §7 dan
[`docs/kamus-riset-korpus-hi.md`](kamus-riset-korpus-hi.md).

---

## 1. Definisi dan Fungsi Abstrak

**Definisi.** Abstrak adalah **ringkasan mandiri (self-contained) dan padat**
atas seluruh artikel yang dapat dibaca terpisah dari badan tulisan.

**Fungsi.** Abstrak menjalankan tiga fungsi yang saling terkait:

1. **Seleksi (screening)** — membantu pembaca memutuskan apakah artikel layak
   dibaca penuh.
2. **Temu kembali (discovery)** — menjadi unit yang diindeks mesin pencari dan
   basis data; abstrak yang baik menaikkan visibilitas dan sitasi
   (Pottier, Lagisz, & Burke, 2024,
   <https://pmc.ncbi.nlm.nih.gov/articles/PMC11288685/>; Tullu, 2019,
   <https://pmc.ncbi.nlm.nih.gov/articles/PMC6398294/>).
3. **Kepatuhan pelaporan** — pada artikel uji klinis, abstrak yang lengkap
   mencegah pelaporan yang tidak akurat (CONSORT for abstracts; Altman &
   Schulz, 2008, <https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.0050020>;
   Hopewell et al., 2008,
   <https://www.thelancet.com/article/S0140-6736(07)61835-2/abstract>).

**Bukti korpus.** Setiap artikel terindeks dalam kedua korpus memuat abstrak di
halaman pertama; 29/29 PDF Sinta dan 43/43 PDF HI/IR menempatkan abstrak
sebelum bagian tubuh pertama (`PENDAHULUAN`/`INTRODUCTION`).

---

## 2. Model Komponen

**Urutan kanonis (5 komponen):**

> `latar belakang/masalah → tujuan → metode → hasil → simpulan/implikasi`

**Bukti.**

- Aturan komponen ini eksplisit di [`docs/bahasa-artikel.md`](bahasa-artikel.md)
  §"Abstrak dan Kata Kunci": *"Component order: latar belakang → tujuan →
  metode → hasil → simpulan."*
- Kamus mesin [`assets/bahasa/kamus-id.yaml`](../assets/bahasa/kamus-id.yaml)
  §`abstrak` menetapkan `komponen: [latar belakang, tujuan, metode, hasil, simpulan]`.
- Teramati verbatim pada korpus: pembuka latar belakang
  (`Penelitian ini mengkaji …`, `s2-ijccs`; `Data berasal dari …`,
  `s3-sistemasi`), tujuan (`Penelitian ini bertujuan untuk …`, `s4-jsi`,
  `s4-transformatika`), metode (`Penelitian ini menggunakan pendekatan …`),
  hasil (`Hasil penelitian menunjukkan bahwa …`), dan simpulan
  (`… dapat disimpulkan bahwa …`) — lihat
  [`docs/kamus-riset-korpus.md`](kamus-riset-korpus.md) §7 ("Pembuka abstrak
  teramati").
- Literatur gerak retoris (*move analysis*) mengonfirmasi lima gerak yang sama
  sebagai pola lintas disiplin (Darabad, 2016,
  <https://www.academia.edu/download/83165390/pdf4.pdf>; Tankó, 2017,
  <https://www.sciencedirect.com/science/article/pii/S1475158517300243>).

**Tabel pemetaan komponen → fungsi → formula korpus:**

| # | Komponen | Pertanyaan yang dijawab | Formula terattestasi |
|---|----------|------------------------|----------------------|
| 1 | Latar belakang/masalah | Mengapa ini penting? | `<Fakta/konteks> … karena …` |
| 2 | Tujuan | Apa yang hendak dicapai? | `Penelitian ini bertujuan untuk …` |
| 3 | Metode | Bagaimana dikerjakan? | `Penelitian ini menggunakan pendekatan …` |
| 4 | Hasil | Apa yang ditemukan? | `Hasil penelitian menunjukkan bahwa …` |
| 5 | Simpulan/implikasi | Apa maknanya? | `Berdasarkan hasil … dapat disimpulkan bahwa …` |

---

## 3. Abstrak Terstruktur vs Naratif

**Abstrak naratif (unstructured)** = satu paragraf kontinu; komponen hadir
**tanpa judul** dan hanya dikenali dari urutan kalimat.

**Abstrak terstruktur (structured)** = komponen diberi **judul eksplisit**
(`Background:`/`Objective:`/`Methods:`/`Results:`/`Conclusion:`).

**Bukti korpus.** Dari 29 PDF Sinta, **2 paper (±7%)** memakai abstrak
terstruktur, sedangkan **27 paper (±93%)** memakai naratif satu paragraf
([`docs/kamus-riset-korpus.md`](kamus-riset-korpus.md) §7):

- `s2-jisebi` → `Background:`, `Objective:`, `Methods:`, `Results:`,
  `Conclusion:`.
- `s2-sji` (label `Abstract.`) → `Purpose:`, `Methods:`, `Results:`,
  `Novelty:`.

**Bukti literatur.** Abstrak terstruktur diperkenalkan untuk meningkatkan
kelengkapan dan keterbacaan; Guimarães (2006) merangkum perkembangannya
(*Structured abstracts: narrative review*,
<https://www.scielo.br/j/acb/a/PfRSnY4XKkh94fyJJczRLgL/?lang=en>), dan
Shannon (2000) memberi panduan penulisannya
(*Writing a structured abstract*). CONSORT for abstracts juga memakai bentuk
berjudul (Altman & Schulz, 2008, tautan di atas).

**Implikasi.** Untuk artikel Sinta bidang sosial/manajemen dan mayoritas
jurnal Indonesia, gunakan **naratif satu paragraf**; pakai bentuk terstruktur
hanya bila *author guidelines* jurnal sasaran memintanya.

---

## 4. Pita Panjang (Length Bands)

**Norma yang diterima.** Panduan repositori menetapkan **100–250 kata** untuk
abstrak Indonesia ([`docs/bahasa-artikel.md`](bahasa-artikel.md) §"Abstrak dan
Kata Kunci") dan **150–250 kata** untuk abstrak dwibahasa
([`docs/sinta-reference.md`](sinta-reference.md) "Article anatomy"). Norma
internasional umumnya **150–300 kata** untuk abstrak Inggris.

**Panjang terukur (penelitian ini, `pdftotext -f 1 -l 4`):**

| Korpus | Bahasa | n | Min | Maks | Median | Rata-rata |
|--------|--------|---|-----|------|--------|-----------|
| Sinta (29 PDF) | ID | 10 | 137 | 301 | 195 | 200 |
| Sinta (29 PDF) | EN | 27 | 151 | 291 | 202 | 213 |
| HI/IR (43 PDF) | ID | 13 | 91 | 244 | 169 | 169 |
| HI/IR (43 PDF) | EN | 34 | 101 | 356 | 194 | 200 |

Dua nilai ekstrem (EN `s1-register` 2291 kata, EN `hi-bournemouth` 2182 kata)
dikeluarkan karena merupakan artefak penggabungan teks dua kolom, bukan abstrak
sungguhan; rentang mentah penuh tercatat di §11. Estimasi independen di
[`docs/kamus-riset-korpus.md`](kamus-riset-korpus.md) §7 menyebut rentang
teramati **~138–367 kata** (beberapa melampaui pedoman 250 kata).

**Rekonsiliasi dengan [`docs/abstrak-corpus-stats.md`](abstrak-corpus-stats.md).**
Berkas statistik pendamping mengukur korpus yang sama secara **per-paper**
(setiap paper dihitung **sekali** pada blok pertamanya), sehingga memperoleh
Sinta **n=29** (9 ID + 20 EN), internasional **n=38**, dan gabungan **n=67**
dengan **median 200 kata** (Sinta 206; internasional 192; min 91, maks 356).
Tabel di atas menghitung **per-blok** (paper dwibahasa muncul di baris ID *dan*
EN), karena itu Sinta terpecah menjadi 10 ID + 27 EN dan total blok lebih
banyak. Perbedaan ini murni **perbedaan unit hitung**, bukan data yang
bertentangan: kedua metode sepakat bahwa panjang abstrak berpusat pada
**~150–250 kata** (median 192–206), dan keduanya mendukung pita sasaran
**150–250 kata per abstrak**.

**Pita yang direkomendasikan (aturan):**

- **ID:** 150–250 kata (norma 100–250; median teramati 195).
- **EN:** 150–250 kata untuk terjemahan setia; 150–300 bila jurnal
  internasional sasaran mengizinkan lebih panjang (median teramati 194–202).
- **Sasaran kerja:** **150–250 kata per abstrak** — konsisten dengan kedua
  norma dan kedua median korpus.

---

## 5. Kata Kunci (Keywords)

**Label.** `Kata Kunci:` untuk Indonesia dan `Keywords:` untuk Inggris.
Varian teramati: `Kata kunci:`, `Kata Kunci :`, `Keyword :`, `Keywords :`,
`Kata Kunci –`, `Keywords –`, `Kata kunci—`, `Keywords—`
([`docs/kamus-riset-korpus.md`](kamus-riset-korpus.md) §7; kamus
[`assets/bahasa/kamus-id.yaml`](../assets/bahasa/kamus-id.yaml) §`abstrak`).
`s5-nuansa` dan `s3-sisfokom` tidak memakai label terpisah.

**Jumlah.** **3–6 kata kunci** ([`docs/sinta-reference.md`](sinta-reference.md)
"Article anatomy"). Terukur: korpus Sinta n=28, median **5**, rentang 1–7,
dengan **24/28** berkisar 3–6; korpus HI/IR n=31, median **5**, rentang 1–8,
dengan **27/31** berkisar 3–6. Aturan: **pakai 4–5**, jangan kurang dari 3.

**Pemisah.** Koma lebih lazim daripada titik koma. Terukur pada 72 berkas
kedua korpus: **koma 42×** vs **titik koma 15×** (7 paper Sinta memakai titik
koma, `s2-ilkom`, `s2-jsinbis`, `s2-jti`, `s2-jtie`, `s2-resti`, `s3-jsce`,
`s3-mib` — kamus §7). Untuk naskah ini, gunakan **koma**.

**Urutan.** Susun dari yang **paling umum → paling spesifik**: topik/konsep
inti, metode/kerangka, objek/konteks, lalu nama diri. Contoh korpus: `Random
Forest, Hyperparameter Tuning, Housing Price Prediction, XGBoost, Decision
Tree` (`s2-ijccs`).

**Bukti tambahan.** Pemilihan kata kunci memengaruhi visibilitas dan
keterindeksan artikel (Pottier et al., 2024, tautan di atas; Fujita, Agustín-
Lacruz, & Terra, 2018,
<https://www.academia.edu/download/57881731/ESENov18_origart-TEXTO_PUBLICADO.pdf>).

---

## 6. Bahasa, Kala, dan Diatesis

### 6.1 Abstrak Indonesia (ID)

- **Impersonal & pasif.** Gunakan bentuk pasif untuk metode dan temuan
  (`dikumpulkan`, `dianalisis`, `digunakan`, `dilakukan`); hindari kata ganti
  orang pertama/kedua (`saya`, `aku`, `kami`, `kita`, `anda`, `kamu`,
  `kalian`) — [`docs/bahasa-artikel.md`](bahasa-artikel.md) §"Ragam Bahasa
  Ilmiah Indonesia". Linter [`tools/check-bahasa.sh`](../tools/check-bahasa.sh)
  menegakkan ini.
- **Kala.** Gunakan **kala kini** untuk latar belakang dan tujuan, **kala
  lampau** untuk metode/hasil (`Data dikumpulkan … lalu dianalisis …`).
- **Hedging.** Pertahankan `cenderung`, `berpotensi`, `dapat dikatakan`,
  `umumnya` alih-alih booster absolut (`pasti`, `wajib`, `mutlak`) —
  [`docs/bahasa-artikel.md`](bahasa-artikel.md) §"Register Anti-AI".
- **Konektor terattestasi.** `Hal ini`, `Selain itu`, `Dengan demikian`,
  `Berdasarkan hasil`, `menunjukkan bahwa`
  ([`docs/bahasa-artikel.md`](bahasa-artikel.md) §"Do / Don't"; hitungan:
  `menunjukkan bahwa` 22× HI / 35× SI).
- **Diksi baku (EYD Edisi V).** Hindari `analisa`, `praktek`, `merubah`,
  `aktifitas`, `standard`, `dimana`, `dikarenakan`, `mempengaruhi`, dsb. —
  tabel padanan di [`docs/bahasa-artikel.md`](bahasa-artikel.md).

### 6.2 Abstrak Inggris (EN)

- **Kala.** **Kala lampau (past tense)** untuk metode dan hasil (`Data were
  collected …`, `The findings indicated …`); **kala kini (present tense)**
  untuk latar belakang, tujuan, dan simpulan umum (`This study aims …`, `The
  European market is …`). Pola ini teramati pada abstrak EN korpus, mis.
  `s2-jsinbis` (`This research was based on …`), `s5-jatisi` (`This research
  examines …`), dan `s2-ijccs` (`The accurate prediction … is essential`).
- **Diatesis.** Baik aktif maupun pasif lazim; pilih pasif bila pelaku tidak
  penting (`Data were collected`), aktif bila pelaku adalah kajian
  (`This study aims …`). Tinjauan lintas disiplin menemukan variasi kala dan
  diatesis yang dapat dipetakan per gerak (Tseng, 2011,
  <https://pdfs.semanticscholar.org/637c/867727eb949c845cf56fde1268c00d09f5f8.pdf>).
- **Register.** Imperpersonal; hindari kata ganti orang pertama
  (`I`, `we`).

### 6.3 Larangan yang Berlaku untuk Kedua Bahasa

- **Tanpa sitasi.** **0 dari 29** abstrak Sinta yang dipindai memuat pola
  sitasi kurung/numerik; aturan eksplisit "no citations" di
  [`docs/bahasa-artikel.md`](bahasa-artikel.md) §"Abstrak dan Kata Kunci".
- **Tanpa singkatan yang tidak dijabarkan**, tanpa catatan kaki, tanpa tabel
  atau gambar, tanpa rujukan ke nomor bagian
  ([`docs/bahasa-artikel.md`](bahasa-artikel.md); Tullu, 2019, tautan di atas;
  Bahadoran, Mirmiran, & Kashfi, 2020,
  <https://pmc.ncbi.nlm.nih.gov/articles/PMC7144240/>).
- **Tanpa frasa pengisi AI generik** (`pada era digital saat ini`,
  `seiring dengan perkembangan zaman`, `dalam rangka untuk`, `sangat krusial`,
  `sebagai kesimpulan`, …) — daftar lengkap di
  [`assets/bahasa/kamus-id.yaml`](../assets/bahasa/kamus-id.yaml)
  §`frasa_ai_generik`.

---

## 7. Dwibahasa (Bilingual)

**Aturan.** Sertakan **kedua** abstrak, Indonesia **dan** Inggris; versi
Inggris adalah **terjemahan setia** versi Indonesia (isi, urutan komponen,
angka, dan istilah kunci identik). Ini norma hampir universal di jurnal
Indonesia ([`docs/bahasa-artikel.md`](bahasa-artikel.md) §"Abstrak dan Kata
Kunci"; [`docs/sinta-reference.md`](sinta-reference.md) "Pre-submit
checklist").

**Bukti korpus.** Pada korpus Sinta, **10/29 paper** memuat abstrak ID **dan**
EN (`s2-ijccs`, `s2-jsinbis`, `s3-mib`, `s3-sistemasi`, `s4-jsi`, `s4-scan`,
`s5-jatisi`, `s5-misi`, `s6-jupiter`, `s6-jutik`) —
[`docs/kamus-riset-korpus.md`](kamus-riset-korpus.md) §7. Di kedua korpus
digabung, **22/72 berkas** memuat label `Abstrak`/`ABSTRAK` **dan**
`Abstract`/`ABSTRACT` (penelitian ini).

**Urutan.** Letakkan **ID dahulu, lalu EN** (mayoritas korpus Sinta), atau
ikut *author guidelines* bila menetapkan sebaliknya.

---

## 8. Varian Struktural yang Teramati

| Aspek | Varian teramati | Bukti |
|-------|-----------------|-------|
| Label ID | `Abstrak`, `ABSTRAK`, `Abstrak−` | kamus §7 |
| Label EN | `Abstract`, `ABSTRACT`, `Abstract−`, `Abstract.` | kamus §7 |
| Frekuensi label (29 paper) | `Abstract` 19×, `ABSTRACT` 10×, `Abstrak` 7×, `ABSTRAK` 3× | kamus §7 |
| Penempatan | Sebelum `PENDAHULUAN`/`INTRODUCTION`, setelah judul-penulis-afiliasi | 29/29 PDF Sinta |
| Paragraf | **Satu paragraf** (mayoritas) vs **dua paragraf** (ID lalu EN terpisah) | `s2-jsinbis`, `s3-mib`, `s5-misi` |
| Bentuk | Naratif (27/29) vs terstruktur (2/29) | kamus §7 |
| Pemisah kata kunci | Koma 42× vs titik koma 15× | penelitian ini |
| Tanda pisah label | `—` (em dash), `−` (minus U+2212), `:`, `.` | kamus §7 |

**Implikasi.** Bila jurnal sasaran tidak menetapkan templat, pilih varian
mayoritas: label `Abstrak` + `Abstract`, satu paragraf kontinu per bahasa,
pemisah koma, kata kunci 4–5.

---

## 9. Daftar Periksa Do / Don't

| ✔ Lakukan | ✘ Hindari |
|-----------|-----------|
| Lima komponen berurutan: latar belakang → tujuan → metode → hasil → simpulan | Melompati komponen atau mengubah urutannya |
| Satu paragraf kontinu (naratif) | Beberapa paragraf bercampur judul tanpa diminta jurnal |
| Panjang 150–250 kata | < 100 kata atau > 300 kata |
| Kata kunci 3–6 (idealnya 4–5), dipisah koma | 1–2 kata kunci atau > 6 |
| Abstrak ID **dan** EN yang setara maknanya | Hanya satu bahasa |
| Pasif & impersonal (`dikumpulkan`, `dianalisis`) | Kata ganti orang (`saya`, `kami`, `kita`, `we`) |
| Kala lampau untuk metode/hasil (EN) | Semua kala kini, atau semua lampau |
| Hedging (`cenderung`, `berpotensi`) | Booster absolut (`pasti`, `mutlak`) |
| Konektor terattestasi (`Hal ini`, `Dengan demikian`) | Frasa AI generik (`pada era digital saat ini`) |
| Diksi baku EYD (`standar`, `analisis`, `praktik`) | Bentuk tidak baku (`standard`, `analisa`, `praktek`) |
| Tanpa sitasi, singkatan tak terjabarkan, catatan kaki | Sitasi `(X, 2020)` atau `[1]` di abstrak |

---

## 10. Rubrik Penilaian Abstrak (0–2 per komponen)

Skor maksimum **12** (5 komponen × 2 + 2 butir kepatuhan).

| Aspek | 0 | 1 | 2 |
|-------|---|---|---|
| **Latar belakang/masalah** | Tidak ada | Ada tetapi tidak mengaitkan urgensi | Menyatakan celah/urgensi secara ringkas |
| **Tujuan** | Tidak ada | Tersirat, tidak eksplisit | Eksplisit (`Penelitian ini bertujuan untuk …`) |
| **Metode** | Tidak ada | Hanya menyebut "kualitatif" tanpa rancangan/sumber data | Pendekatan + rancangan + sumber data/analisis |
| **Hasil** | Tidak ada | Umum, tanpa temuan spesifik | Temuan spesifik yang menjawab tujuan |
| **Simpulan/implikasi** | Tidak ada | Mengulang hasil tanpa makna | Menyatakan implikasi/kontribusi |
| **Panjang & kata kunci** | Di luar 100–300 kata atau < 3 kata kunci | Sedikit di luar pita | 150–250 kata & 3–6 kata kunci |
| **Kepatuhan (bahasa)** | Ada kata ganti / diksi tak baku / frasa AI / sitasi | Satu pelanggaran ringan | Nol pelanggaran |

**Tafsiran:** 11–12 = siap kirim; 8–10 = revisi ringan; ≤ 7 = tulis ulang.

---

## 11. Ringkasan Angka Korpus (penelitian ini)

- **Berkas dipindai:** 29 PDF `docs/sinta-corpus/` + 43 PDF `docs/ir-corpus/`.
- **Abstrak ID terukur:** Sinta n=10 (137–301, median 195); HI/IR n=13
  (91–244, median 169).
- **Abstrak EN terukur:** Sinta n=27 (151–291, median 202); HI/IR n=34
  (101–356, median 194). Nilai ekstrem (2291, 2182) = artefak tata letak.
- **Kata kunci:** median **5** di kedua korpus; 3–6 pada 24/28 (Sinta) dan
  27/31 (HI/IR).
- **Pemisah kata kunci:** koma 42× vs titik koma 15× (72 berkas).
- **Abstrak terstruktur:** 2/29 (Sinta).
- **Abstrak dengan sitasi:** 0/29 (Sinta).
- **Dwibahasa:** 10/29 (Sinta, kamus §7); 22/72 (kedua korpus, penelitian ini).
- **Keterbacaan PDF.** Tidak ada PDF artikel yang gagal dibaca: seluruh 29
  berkas `docs/sinta-corpus/` dan 43 berkas `docs/ir-corpus/` menghasilkan
  teks via `pdftotext`. Empat baris Sinta berstatus **FAILED** pada manifest
  (`s2-jtiik`, `s4-zonasi`, `s4-jusifor`, `s5-intek`) **tidak ada di disk**,
  sehingga tidak disertakan dalam hitungan. Lima buku di
  `docs/libgen-corpus/` hanya memiliki *front matter* yang tipis (sampul/daftar
  isi) tetapi teksnya lengkap mulai halaman isi; buku tidak memuat abstrak,
  jadi tidak disampling untuk hitungan abstrak. Dua nilai ekstrem tata letak
  dua kolom (2291 dan 2182 kata) dilaporkan sebagai artefak dan dikeluarkan.

**Rekonsiliasi dengan [`docs/abstrak-corpus-stats.md`](abstrak-corpus-stats.md)
(per-paper, bukan per-blok).** Berkas statistik pendamping mengukur 72 PDF yang
sama dan mencatat setiap paper **sekali** (blok pertama), sehingga:

| Ukuran (per-paper) | Sinta | Internasional | Gabungan |
|---|---|---|---|
| n paper | 29 | 38 | 67 |
| Kata: min–median–maks | 137–206–292 | 91–192–356 | 91–200–356 |
| ID / EN (blok pertama) | 9 / 20 | 6 / 32 | 15 / 52 |
| Terstruktur | 2 (6,9%) | 1 (2,6%) | 3 (4,5%) |
| Median kata kunci | 5 | 5 | 5 |
| Dwibahasa (dua blok) | 10 | 13 | 23 |

Kedua pengukuran **sepakat pada substansi** dan **tidak ada klaim keras yang
bertentangan**: abstrak didominasi bentuk **tak terstruktur (~93–95%)**;
median kata kunci **5** (modal 5) dengan rentang umum **3–6**; **tidak ada
sitasi** di abstrak; **dwibahasa lazim**; dan **pita sasaran 150–250 kata**
konsisten dengan median 192–206. Perbedaan angka (mis. Sinta "n=10 ID + 27 EN"
di §4 vs "9 ID + 20 EN" di berkas statistik) berasal dari **unit hitung** —
§4 menghitung blok abstrak, berkas statistik menghitung paper — bukan dari
data yang saling menyalahkan. Satu-satunya koreksi silang: **abstrak
terstruktur** juga muncul **1×** di korpus internasional (`hi-jpr-nation-
branding`), sehingga totalnya **3/67 (4,5%)**, bukan hanya 2/29 di Sinta.

---

## Sumber

**Berkas repositori (bukti utama):**

- [`docs/sinta-corpus/MANIFEST.md`](sinta-corpus/MANIFEST.md) — 29 PDF Sinta 1–6
  (OK=29, FAILED=4).
- [`docs/ir-corpus/manifest.tsv`](ir-corpus/manifest.tsv) — 43 PDF HI/IR
  (21 nasional, 22 internasional).
- [`docs/libgen-corpus/MANIFEST.md`](libgen-corpus/MANIFEST.md) — 15 PDF
  tambahan (10 buku + 5 artikel).
- [`docs/bahasa-artikel.md`](bahasa-artikel.md) — §"Abstrak dan Kata Kunci",
  §"Ragam Bahasa Ilmiah Indonesia", §"Register Anti-AI".
- [`docs/sinta-reference.md`](sinta-reference.md) — "Article anatomy",
  "Technical spec table".
- [`docs/kamus-riset-korpus.md`](kamus-riset-korpus.md) — §7 "Konvensi abstrak
  yang teramati".
- [`docs/kamus-riset-korpus-hi.md`](kamus-riset-korpus-hi.md) — register HI/IR.
- [`docs/abstrak-corpus-stats.md`](abstrak-corpus-stats.md) — statistik
  per-paper abstrak (word-count, presence komponen, jumlah kata kunci) dari
  29 PDF Sinta + 43 PDF internasional; dikutip di §4 dan §11.
- [`assets/bahasa/kamus-id.yaml`](../assets/bahasa/kamus-id.yaml) — §`abstrak`,
  §`kosakata_baku`, §`frasa_ai_generik`.
- [`tools/check-bahasa.sh`](../tools/check-bahasa.sh) — linter register.

**Literatur eksternal (rekaman nyata `scholar.py`):**

- Altman, D. G., & Schulz, K. F. (2008). *CONSORT for reporting randomized
  controlled trials in journal and conference abstracts: explanation and
  elaboration*. PLoS Medicine.
  <https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.0050020>
- Bahadoran, Z., Mirmiran, P., & Kashfi, K. (2020). *The principles of
  biomedical scientific writing: abstract and keywords*. International Journal
  of Endocrinology and Metabolism.
  <https://pmc.ncbi.nlm.nih.gov/articles/PMC7144240/>
- Darabad, A. M. (2016). *Move analysis of research article abstracts: A
  cross-disciplinary study*. International Journal of Linguistics.
  <https://www.academia.edu/download/83165390/pdf4.pdf>
- Fujita, M. S. L., Agustín-Lacruz, M. C., & Terra, A. L. (2018). *Journals'
  guidelines about title, abstract and keywords: an overview of Information
  Science and Communication Science areas*.
  <https://www.academia.edu/download/57881731/ESENov18_origart-TEXTO_PUBLICADO.pdf>
- Guimarães, C. A. (2006). *Structured abstracts: narrative review*. Acta
  Cirúrgica Brasileira.
  <https://www.scielo.br/j/acb/a/PfRSnY4XKkh94fyJJczRLgL/?lang=en>
- Hopewell, S., Clarke, M., Moher, D., Wager, E., & Middleton, P. (2008).
  *CONSORT for reporting randomised trials in journal and conference
  abstracts*. The Lancet.
  <https://www.thelancet.com/article/S0140-6736(07)61835-2/abstract>
- Pottier, P., Lagisz, M., & Burke, S. (2024). *Title, abstract and keywords:
  a practical guide to maximize the visibility and impact of academic papers*.
  Proceedings of the Royal Society B.
  <https://pmc.ncbi.nlm.nih.gov/articles/PMC11288685/>
- Shannon, S. (2000). *Writing a structured abstract*. Canadian Association of
  Radiologists Journal.
- Tankó, G. (2017). *Literary research article abstracts: An analysis of
  rhetorical moves and their linguistic realizations*. Journal of English for
  Academic Purposes.
  <https://www.sciencedirect.com/science/article/pii/S1475158517300243>
- Tseng, F. (2011). *Analyses of move structure and verb tense of research
  article abstracts in applied linguistics journals*. International Journal of
  English Linguistics.
  <https://pdfs.semanticscholar.org/637c/867727eb949c845cf56fde1268c00d09f5f8.pdf>
- Tullu, M. S. (2019). *Writing the title and abstract for a research paper:
  Being concise, precise, and meticulous is the key*. Saudi Journal of
  Anaesthesia. <https://pmc.ncbi.nlm.nih.gov/articles/PMC6398294/>
