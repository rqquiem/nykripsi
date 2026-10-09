# Kerangka Teks Utuh (Full-Text) — Akuisisi dan Verifikasi Berbasis Bukti

Kerangka ini menetapkan aturan operasional untuk **memperoleh dan memverifikasi
teks utuh** sebuah karya sebelum karya itu dipakai sebagai dasar simpulan,
sitasi, atau klaim apa pun. Kerangka diturunkan dari dua sumber yang dapat
diaudit: **berkas repositori ini** (skrip, target `make`, berkas konfigurasi,
dan korpus) serta **literatur akademik internasional** yang benar-benar
terekam lewat `scholar.py` dan pencarian daring pada sesi ini. Tidak ada klaim
tanpa sumber.

Landasan empiris utama berasal dari dua pengukuran yang dapat direproduksi.
Pertama, pada artikel akses terbuka yang diperoleh dan diverifikasi lewat
tangga §3 (Lin, 2009; 15 halaman; `FULLTEXT: OK`), dilaporkan artikel memuat
rata-rata **4.148 terma**, sedangkan abstrak hanya **142 terma**; rasio
panjang ini menunjukkan bahwa sebagian besar isi tidak pernah muncul di
abstrak. Kedua, Agarwal dkk. (2023)
menghimpun estimasi bahwa **hingga 80% penulis tidak membaca teks utuh** karya
yang disitasinya dan **hanya 20% penulis membaca artikel asli**, sehingga
sekitar **20% sitasi** pada satu naskah internal ditemukan memuat galat.
Kedua temuan itu menjadi justifikasi mengapa aturan F1–F8 di bawah bersifat
mengikat.

---

## 1. Definisi dan Fungsi

**Definisi.** *Teks utuh (full text)* adalah **seluruh isi sebuah karya tulis
ilmiah** sebagaimana diterbitkan: judul, abstrak, badan tulisan
(Pendahuluan, Metode, Hasil, Pembahasan, Batasan, Simpulan), tabel, gambar,
dan daftar rujukan, dalam bentuk berkas yang benar-benar diperoleh
(PDF/HTML/EPUB). Teks utuh berbeda secara kategoris dari **abstrak**, yaitu
ringkasan mandiri satu-paragraf yang hanya memuat sebagian kecil informasi.

**Perbedaan abstrak dan teks utuh.**

| Aspek | Abstrak | Teks utuh |
|-------|---------|-----------|
| Cakupan | Ringkasan padat; seleksi dan temu kembali | Seluruh argumen, prosedur, dan data |
| Panjang | Rata-rata **142 terma** (Lin, 2009) | Rata-rata **4.148 terma** (Lin, 2009) |
| Metode | Sering hanya satu klausa ("pendekatan kualitatif") | Rancangan, instrumen, prosedur, sampel lengkap |
| Batasan | Hampir selalu tidak dimuat | Dinyatakan pada bagian Batasan/Pembahasan |
| Angka hasil | Terpilih dan dibulatkan | Tabel, uji statistik, dan nilai penuh |
| Rujukan | Tidak ada | Daftar rujukan lengkap yang dapat dilacak |

**Mengapa membaca abstrak saja tidak memadai.**

1. **Distorsi sitasi.** Agarwal dkk. (2023) menemukan bahwa mengandalkan
   abstrak menghasilkan "galat faktual", "interpretasi keliru", dan
   "ekstrapolasi simpulan yang tak berdasar"; pada satu naskah, **20% sitasi**
   memuat galat, dengan jenis terbanyak berupa informasi sitasi yang keliru.
   Sumbernya secara eksplisit menyatakan bahwa "abstrak sering tidak
   melukiskan gambaran lengkap".
2. **Abstrak menghilangkan metode, batasan, dan angka.** Abstrak yang baik
   memuat "metode" dalam satu klausa dan tidak memuat batasan; karena itu
   penilaian atas **validitas, replikabilitas, dan generalisasi** tidak dapat
   dilakukan tanpa badan tulisan.
3. **Abstrak bukan pengganti pemeriksaan kelayakan.** Hermont dkk. (2022)
   menekankan pentingnya **penyaringan teks utuh** saat menilai kriteria
   kelayakan dalam tinjauan sistematis; Polanin dkk. (2019) memposisikan
   penyaringan abstrak hanya sebagai **tahap awal** sebelum penyaringan teks
   utuh.
4. **Nilai pencarian penuh.** Lin (2009) menyimpulkan bahwa pencarian atas teks
   utuh "lebih mungkin menemukan artikel yang relevan" dibanding pencarian
   abstrak saja; informasi yang berguna kerap berada di bagian yang tidak
   terwakili di abstrak (mis. bagian diskusi atau rujukan).
5. **Rekomendasi langsung.** Dal-Ré, Castell, dan García-Puig (2015) menulis
   pada judul artikelnya: *"If the results of an article are noteworthy, read
   the entire article; do not rely on the abstract alone."*

**Fungsi kerangka.** Kerangka ini menjadikan kebiasaan di atas sebagai aturan
yang dapat diperiksa: setiap klaim tentang isi sebuah karya wajib berasal dari
teks utuh yang telah diperoleh dan diverifikasi, dan status akses setiap karya
wajib tercatat pada provenance.

---

## 2. Aturan Absolut (Wajib)

1. **F1.** Dilarang menyimpulkan **isi, temuan, metode, atau kelemahan**
   sebuah karya hanya dari abstraknya, judulnya, cuplikan hasil pencarian
   (*snippet*), atau halaman pendaratan penerbit. Setiap klaim tentang isi
   sebuah karya **wajib** berasal dari teks utuh yang benar-benar diperoleh.
2. **F2.** Setiap karya yang dipakai sebagai dasar simpulan atau sitasi
   **wajib** memiliki berkas teks utuh lokal (PDF/HTML/EPUB) yang telah
   **diverifikasi** — bukan halaman paywall dan bukan halaman abstrak.
3. **F3.** Seluruh **tangga akuisisi (§3)** wajib ditelusuri sebelum sebuah
   karya ditandai `inaccessible`; penelusuran **berhenti pada anak tangga
   pertama yang berhasil**.
4. **F4.** Integritas berkas wajib diverifikasi: bukan halaman abstrak,
   jumlah halaman **≥ 2**, badan tulisan hadir (mis. Introduction/Method/
   References atau padanannya), dan **SHA-256** tercatat.
5. **F5.** Provenance wajib: catat `access_level`, `fulltext_url`,
   `fulltext_sha256`, `fulltext_pages`, dan `fulltext_verified` untuk setiap
   karya; dilarang **mengarang** URL, hash, atau jumlah halaman.
6. **F6.** Karya berstatus `abstract-only` atau `inaccessible` **tidak boleh**
   dipakai sebagai dasar simpulan atau sitasi; bila tetap disebut, wajib
   ditandai eksplisit "hanya abstrak tersedia" dan isinya tidak boleh
   diklaim.
7. **F7.** Kutipan langsung (verbatim) hanya boleh diambil dari teks utuh yang
   telah diperoleh; nomor halaman mengikuti **berkas penuh** yang dipegang.
8. **F8.** Berkas teks utuh wajib disimpan di lokasi yang **di-*git-ignore***
   (mis. `docs/fulltext-corpus/`, mengikuti pola `docs/*-corpus/*.pdf`),
   dengan **manifest terlacak** yang memuat hash dan URL.

---

## 3. Tangga Akuisisi (Wajib Berurutan)

Tangga ditelusuri **berurutan**; penelusuran berhenti pada rung pertama yang
menghasilkan berkas teks utuh yang lolos verifikasi §4. Perintah merujuk pada
skrip repositori `tools/fulltext.py` (dan target `make fulltext`). Rung 1–3
**aman secara legal**; rung 4 bergantung pada lisensi institusi; rung 5 adalah
**upaya terakhir** dan PDF-nya tetap di-*git-ignore*.

| Rung | Sumber | Perintah | Kondisi berhenti | Kondisi lanjut |
|------|--------|----------|------------------|----------------|
| 1 | OA/Unpaywall + OpenAlex (`is_oa:true`) | `python3 tools/fulltext.py resolve --doi <DOI>` lalu `python3 tools/fulltext.py fetch --doi <DOI> [--out docs/fulltext-corpus]` | Berkas terunduh **dan** `verify` lolos (§4) | Tidak ada kandidat OA atau verifikasi gagal → rung 2 |
| 2 | CORE | kandidat CORE ikut dihasilkan `resolve` (`# backend: core`); unduh via `fetch` | Berkas terunduh dan verifikasi lolos | CORE kosong/401/429 atau verifikasi gagal → rung 3 |
| 3 | Repositori institusi/preprint (arXiv, SSRN, repositori kampus, ResearchGate bila diunggah penulis) | pencarian manual + `python3 .claude/skills/nykripsi/scripts/search.py pdf "<judul>"`; kandidat OA institusi juga muncul lewat backend `openalex-oa` (`is_oa:true`) | Berkas repositori terunduh dan verifikasi lolos | Tidak ditemukan → rung 4 |
| 4 | Akses institusi/perpustakaan atau permintaan ke penulis | akses berlisensi (proxy kampus/perpustakaan) atau surel permintaan cetak ke penulis; inter-library loan | Berkas terunduh dan verifikasi lolos | Tidak tersedia → rung 5 |
| 5 | Upaya terakhir: Anna's Archive atau Sci-Hub | `python3 tools/fulltext.py shadow --doi <DOI>` (mengeluarkan URL Sci-Hub dan Anna's Archive; skrip **tidak** melewati captcha dan **tidak** mengunduh) | Berkas diperoleh dan verifikasi lolos | Gagal → status `inaccessible` (§2 F3 selesai) |

**Catatan legal dan operasional.**

- Rung 1–3 bersandar pada sumber **akses terbuka/repositori** dan aman secara
  legal. Contoh nyata: `resolve --doi 10.1186/1471-2105-10-46` menghasilkan
  `# backend: openalex` →
  `https://bmcbioinformatics.biomedcentral.com/counter/pdf/10.1186/1471-2105-10-46`
  dan cadangan `# backend: core` → `https://core.ac.uk/download/81614486.pdf`.
- Rung 4 bergantung pada **lisensi institusi**; akses tidak boleh dibagikan
  ulang di luar izin lisensi.
- Rung 5 adalah **upaya terakhir**. Perintah `shadow` hanya mencetak URL dan
  menegaskan bahwa berkas tetap di-*git-ignore*; kegagalan akses berujung pada
  status `inaccessible`, bukan data palsu. Peringatan pada skrip berbunyi:
  *"shadow library adalah upaya TERAKHIR (rung 5) … PDF apa pun tetap
  git-ignored."* Justifikasi rung ini bersifat empiris: Sci-Hub menyediakan
  sekitar **62 juta publikasi** (Greshake, 2017) dan Himmelstein dkk. (2018)
  menunjukkan cakupan yang hampir menyeluruh, sehingga rung ini tetap dicatat
  sebagai opsi terakhir yang harus dihindari bila rung 1–4 berhasil.
- **Perintah verifikasi** yang dipakai di seluruh tangga:
  `python3 tools/fulltext.py verify <file.pdf>` dan padanan target
  `make fulltext F=<file.pdf>`.

---

## 4. Verifikasi Integritas Berkas

Tujuan verifikasi adalah memastikan bahwa berkas yang dipegang benar-benar
**teks utuh**, bukan halaman paywall, halaman abstrak, atau tangkapan layar.
Seluruh alat tersedia di sistem (`/usr/bin/pdfinfo`, `/usr/bin/pdftotext`,
`/usr/bin/sha256sum`), dan logika yang sama diimplementasikan pada
`tools/fulltext.py` (`verify_pdf`).

| Pemeriksaan | Perintah | Kriteria lolos | Kriteria gagal |
|-------------|----------|----------------|----------------|
| Jumlah halaman | `pdfinfo <file.pdf> \| grep -E '^Pages'` | **≥ 2** halaman | 1 halaman (umumnya halaman abstrak/pendaratan) |
| Isi badan | `pdftotext <file.pdf> - \| grep -ciE 'PENDAHULUAN\|INTRODUCTION\|METODE\|METHOD\|HASIL\|RESULTS\|DAFTAR PUSTAKA\|REFERENCES'` | **≥ 1** penanda isi | 0 penanda → bukan badan artikel |
| Halaman paywall | `pdftotext <file.pdf> - \| grep -ciE 'purchase\|subscribe\|access denied\|paywall'` | **0** kemunculan | kemunculan ada → **perlu pemeriksaan manual** (lihat catatan) |
| Hash berkas | `sha256sum <file.pdf>` | 64 digit heksadesimal | hash tidak dapat dihitung |

**Kriteria ringkas (lolos/gagal).** Sebuah berkas **lolos** bila: jumlah
halaman ≥ 2, setidaknya satu penanda badan tulisan ditemukan, tidak ada
penanda paywall, dan SHA-256 berhasil dihitung. Bila salah satu gagal, berkas
**tidak** boleh dipakai sebagai dasar simpulan (aturan F2/F4) dan status karya
tetap `inaccessible` sampai berkas lain diperoleh.

**Contoh nyata (dijalankan pada sesi ini).**

- Berkas nyata teks utuh —
  `make fulltext F=docs/ir-corpus/hi-bournemouth-nation-branding.pdf` →
  `FULLTEXT: OK sha256=90924c44e76d9997cb1293cbdd3dbd1d7cbc4a171c71997c75545d3d230c681f pages=7`.
- Berkas teks utuh kedua pada korpus —
  `python3 tools/fulltext.py verify docs/sinta-corpus/s2-ijccs.pdf` →
  `FULLTEXT: GAGAL halaman paywall terdeteksi` (positif palsu; lihat catatan
  di bawah).

**Catatan penting — heuristik paywall dapat keliru (positif palsu).**
Pemeriksaan `verify` pada
`docs/sinta-corpus/s2-ijccs.pdf` mengeluarkan
`FULLTEXT: GAGAL halaman paywall terdeteksi`, padahal berkas tersebut adalah
teks utuh yang sah (12 halaman; 5.672 kata; memuat penanda
`PENDAHULUAN`/`DAFTAR PUSTAKA`). Penyebabnya terukur: kata **`purchase`**
muncul 5× sebagai bagian kata **`purchasers`** pada badan artikel. Karena itu
deteksi paywall bersifat **heuristik** dan wajib dikonfirmasi manual melalui
jumlah halaman dan penanda badan sebelum sebuah karya sah ditandai
`inaccessible`.

---

## 5. Scope

**Cakupan (berlaku).**

- Artikel jurnal (nasional maupun internasional), termasuk artikel akses
  terbuka dan artikel berlisensi.
- Bab buku dan buku akademik.
- Makalah prosiding/konferensi.
- Laporan teknis, laporan lembaga, dan *working paper*.
- Kumpulan data prosais (mis. laporan naratif, transkrip) yang memiliki
  struktur teks berjalan.

**Di luar cakupan (tidak berlaku).**

- Berita pendek berita/web dengan panjang **< ±500 kata** yang tidak memiliki
  badan metodologis.
- Rekaman non-prosais: data tabular, basis data terstruktur, berkas gambar,
  atau himpunan data numerik murni.
- Cuplikan hasil mesin pencari, halaman pendaratan penerbit, dan halaman
  abstrak — semuanya **bukan** teks utuh.

**Kapan aturan berlaku.**

- Aturan berlaku ketika sebuah karya dipakai untuk **riset atau penulisan**
  (menyusun argumen, mengutip, menilai metode, atau menetapkan celah
  penelitian).
- Aturan **tidak** berlaku ketika tindakan hanya sebatas **menyimpan tautan**
  atau menandai kandidat untuk ditelaah kemudian; penyimpanan tautan belum
  merupakan klaim tentang isi karya dan tidak boleh berubah menjadi klaim
  tanpa akuisisi teks utuh.

---

## 6. Model Komponen dan Varian

**Komponen teks utuh yang wajib dipahami.** Setiap karya akademik dibaca
melalui komponen berikut; kehadirannya diverifikasi pada §4 dan dipakai pada
rubrik §9.

| Komponen | Fungsi pembacaan | Padanan label teramati di korpus |
|----------|------------------|----------------------------------|
| Pendahuluan | Latar belakang, celah, tujuan | `PENDAHULUAN`, `INTRODUCTION`, `Latar Belakang` |
| Metode | Rancangan, data, prosedur, analisis | `METODE`, `METODE PENELITIAN`, `METHOD`, `METHODS`, `Methodology` |
| Hasil | Temuan, tabel, angka, uji statistik | `HASIL`, `RESULTS`, `RESEARCH RESULTS` |
| Pembahasan | Tafsir, perbandingan, implikasi | `PEMBAHASAN`, `DISCUSSION`, `RESULTS AND DISCUSSION` |
| Batasan | Keterbatasan, ancaman validitas | `SARAN`, `Limitations and Future Works` |
| Referensi | Daftar rujukan yang dapat dilacak | `DAFTAR PUSTAKA`, `REFERENCES`, `Bibliography` |

Label di atas teramati pada korpus repositori: `docs/kamus-riset-korpus.md` §2
mencatat Pendahuluan 29/29, Metode 29/29, Hasil/Pembahasan 29/29, Simpulan
29/29, Tinjauan pustaka 19/29, dan Daftar Pustaka pada korpus Sinta;
`docs/kamus-riset-korpus-hi.md` §2 mencatat Pendahuluan 28/43, Metode 13/43,
Hasil/Pembahasan 12/43, Simpulan 29/43, dan Daftar Pustaka 31/43 pada korpus
HI/IR. Keragaman label inilah yang membuat penanda isi pada §4 harus
memakai beberapa varian sekaligus.

**Varian akses.** Medan `access_level` pada `sources/registry.json`
(didefinisikan di `.claude/skills/nykripsi/scripts/search.py`, fungsi
`_make_record`) memakai nilai awal `inaccessible`, dan `tools/fulltext.py`
menetapkan nilai `fulltext` saat verifikasi lolos. Varian akses yang dipakai
kerangka ini:

| `access_level` | Makna | Dasar |
|----------------|-------|-------|
| `open` | Akses terbuka (OA/Unpaywall/OpenAlex `is_oa:true`) | Rung 1 |
| `repository` | Tersedia di repositori institusi/preprint | Rung 3 |
| `institutional` | Diperoleh via lisensi institusi/perpustakaan | Rung 4 |
| `shadow` | Diperoleh dari shadow library | Rung 5 |
| `abstract-only` | Hanya abstrak tersedia | Tidak boleh dipakai (F6) |
| `inaccessible` | Tidak ada teks utuh setelah seluruh tangga | Tidak boleh dipakai (F6) |

---

## 7. Matriks Kepatuhan per-Tingkat

Matriks menetapkan tingkat keberlakuan setiap aturan per jenis keluaran.
`wajib` = mengikat; `disarankan` = dianjurkan, bukan syarat mutlak;
`tidak berlaku` = di luar scope (§5).

| Aturan | Sinta 1–2 | Sinta 3–6 | Scopus | Skripsi HI | Sumber berita/web |
|--------|-----------|-----------|--------|------------|-------------------|
| F1 | wajib | wajib | wajib (unverified — confirm first) | wajib | disarankan |
| F2 | wajib | wajib | wajib (unverified — confirm first) | wajib | tidak berlaku |
| F3 | wajib | wajib | wajib (unverified — confirm first) | disarankan | tidak berlaku |
| F4 | wajib | wajib | wajib (unverified — confirm first) | wajib | tidak berlaku |
| F5 | wajib | wajib | wajib (unverified — confirm first) | wajib | disarankan |
| F6 | wajib | wajib | wajib (unverified — confirm first) | wajib | tidak berlaku |
| F7 | disarankan | disarankan | wajib (unverified — confirm first) | disarankan | tidak berlaku |
| F8 | wajib | wajib | wajib (unverified — confirm first) | wajib | tidak berlaku |

**Catatan verifikasi kolom Scopus.** Kolom **Scopus** ditandai
`unverified — confirm first` karena **status indeksasi Scopus tidak dapat
diverifikasi dari korpus lokal**. Korpus repositori hanya memuat korpus Sinta
(`docs/sinta-corpus/`, Sinta 1–6) dan korpus Hubungan Internasional
(`docs/ir-corpus/`, nasional/internasional); tidak ada metadata indeksasi
Scopus di dalamnya. Karena itu status indeksasi Scopus **tidak boleh
diasumsikan** dan wajib dikonfirmasi lebih dahulu pada sumber resmi sebelum
dipakai sebagai dasar klaim.

---

## 8. Daftar Periksa Do / Don't

| ✔ Lakukan | ✘ Hindari |
|-----------|-----------|
| Peroleh dan verifikasi teks utuh sebelum menyimpulkan isi karya | Menyimpulkan isi/metode/kelemahan dari abstrak, judul, atau *snippet* |
| Simpan berkas teks utuh di `docs/fulltext-corpus/` (git-ignored) | Menyimpan PDF di lokasi terlacak atau membagikannya ulang |
| Telusuri seluruh tangga akuisisi dan berhenti pada rung pertama yang berhasil | Melompat langsung ke rung 5 atau menandai `inaccessible` terlalu cepat |
| Verifikasi jumlah halaman ≥ 2, penanda badan, dan SHA-256 | Memakai berkas tanpa memeriksa jenis halamannya |
| Catat `access_level`/`fulltext_url`/`fulltext_sha256`/`fulltext_pages`/`fulltext_verified` | Mengarang URL, hash, atau jumlah halaman |
| Tandai "hanya abstrak tersedia" bila teks utuh tak terjangkau | Mengklaim isi karya berstatus `abstract-only`/`inaccessible` |
| Ambil kutipan verbatim dari berkas teks utuh dengan nomor halaman berkas penuh | Mengutip dari abstrak atau halaman pendaratan |
| Konfirmasi manual bila heuristik paywall menandai berkas sah | Menolak berkas sah hanya karena deteksi kata kunci tunggal |
| Simpan manifest terlacak berisi hash + URL | Membiarkan provenance kosong atau tidak konsisten |

---

## 9. Rubrik Penilaian

Skor **0–2 per komponen** untuk lima komponen; skor maksimum **10** (5 × 2).

| Komponen | 0 | 1 | 2 |
|----------|---|---|---|
| **Kedalaman pembacaan** | Hanya abstrak/judul | Sebagian badan (mis. hanya Hasil) | Seluruh badan + batasan dibaca |
| **Kelengkapan teks utuh** | Berkas tidak ada | Berkas ada tetapi parsial/paywall | Berkas teks utuh lengkap dan sah |
| **Verifikasi integritas** | Tanpa pemeriksaan | Sebagian (halaman atau hash saja) | Halaman ≥ 2, penanda badan, dan SHA-256 lengkap |
| **Provenance** | Tidak dicatat | Sebagian medan dicatat | `access_level`, `fulltext_url`, `fulltext_sha256`, `fulltext_pages`, `fulltext_verified` lengkap |
| **Kepatuhan tangga** | Melompat ke rung 5 atau tidak menelusuri | Menelusuri sebagian rung | Menelusuri berurutan dan berhenti pada rung pertama yang berhasil |

**Tafsiran.** **10** = kepatuhan penuh; **7–9** = revisi ringan (lengkapi
provenance atau verifikasi); **4–6** = perlu akuisisi/verifikasi ulang;
**≤ 3** = klaim belum layak dan wajib diulang dari tangga akuisisi.

---

## 10. Sumber

**Berkas repositori (bukti utama).**

- [`tools/fulltext.py`](../tools/fulltext.py) — tangga akuisisi rung 1–3
  (`resolve`), unduh+verifikasi (`fetch`), verifikasi (`verify`), dan URL
  rung 5 (`shadow`); fungsi `verify_pdf` (halaman ≥ 2, penanda badan,
  deteksi paywall), `resolve_candidates`, `_openalex_candidates`,
  `_unpaywall_candidates`, `_core_candidates`.
- [`Makefile`](../Makefile) — target `fulltext` (`python3 tools/fulltext.py
  verify $(F)`) dan daftar target `corpus`/`corpus-hi`/`corpus-libgen`.
- [`.gitignore`](../.gitignore) — baris 17 `docs/*-corpus/*.pdf` dan baris 18
  `docs/fulltext-corpus/*.pdf` (berkas teks utuh tidak dibagikan ulang).
- [`.claude/skills/nykripsi/SKILL.md`](../.claude/skills/nykripsi/SKILL.md)
  §"Non-negotiable rules" butir 2 — "Obtain the full text before concluding".
- [`.claude/skills/nykripsi/scripts/search.py`](../.claude/skills/nykripsi/scripts/search.py)
  — `_make_record` (medan `access_level`, `fulltext_url`, `fulltext_sha256`,
  `fulltext_pages`, `fulltext_verified`), backend `openalex-oa` (`is_oa:true`),
  dan backend `core`.
- [`sources/registry.json`](registry.json) — 33 catatan dengan medan
  `access_level` (nilai awal `inaccessible`).
- [`docs/fulltext-corpus/manifest.tsv`](fulltext-corpus/manifest.tsv) — skema
  manifest `slug, doi, access_level, fulltext_url, fulltext_sha256,
  fulltext_pages`.
- [`docs/sinta-corpus/MANIFEST.md`](sinta-corpus/MANIFEST.md) dan
  [`docs/ir-corpus/manifest.tsv`](ir-corpus/manifest.tsv) — korpus Sinta
  (OK=29, FAILED=4) dan korpus HI/IR (43 PDF), sumber hitungan §6.
- [`docs/libgen-corpus/MANIFEST.md`](libgen-corpus/MANIFEST.md) — korpus
  rujukan tambahan.
- [`docs/kamus-riset-korpus.md`](kamus-riset-korpus.md) §2 — frekuensi label
  kepala bagian korpus Sinta.
- [`docs/kamus-riset-korpus-hi.md`](kamus-riset-korpus-hi.md) §2 — frekuensi
  label kepala bagian korpus HI/IR.
- [`docs/bahasa-artikel.md`](bahasa-artikel.md) — §"Ragam Bahasa Ilmiah
  Indonesia" dan §"Daftar Periksa" (larangan kata ganti orang pertama/kedua).
- [`docs/sinta-reference.md`](sinta-reference.md) — "Article anatomy"
  (badan IMRaD, rujukan lengkap).
- [`README.md`](../README.md) — "Full-text rule" (ikuti tangga akuisisi;
  catat `access_level`/`fulltext_*`).

**Literatur eksternal (rekaman nyata `scholar.py` dan verifikasi daring).**

- Agarwal, A., Arafa, M., Avidor-Reiss, T., Hamoda, T. A. A., & Shah, R.
  (2023). *Citation Errors in Scientific Research and Publications: Causes,
  Consequences, and Remedies*. The World Journal of Men's Health, 41(3),
  461–465. <https://doi.org/10.5534/wjmh.230001> ·
  <https://pmc.ncbi.nlm.nih.gov/articles/PMC10307651/>
- Dal-Ré, R., Castell, M. V., & García-Puig, J. (2015). *If the results of an
  article are noteworthy, read the entire article; do not rely on the abstract
  alone*. Revista Clínica Española (English Edition).
  <https://doi.org/10.1016/j.rceng.2015.08.004> ·
  <https://www.sciencedirect.com/science/article/pii/S2254887415000764>
- Dhakal, K. (2019). *Unpaywall*. Journal of the Medical Library Association,
  107(2). <https://doi.org/10.5195/jmla.2019.650> ·
  <https://pmc.ncbi.nlm.nih.gov/articles/PMC6466485/>
- Greshake, B. (2017). *Looking into Pandora's Box: The Content of Sci-Hub and
  its Usage*. F1000Research, 6:541.
  <https://doi.org/10.12688/f1000research.11366.1> ·
  <https://pmc.ncbi.nlm.nih.gov/articles/PMC5428489/>
- Hermont, A. P., Cruz, P. V., Occhi-Alexandre, I. G. P., Bendo, C. B.,
  Auad, S. M., Pordeus, I. A., & Martins, C. C. (2022). *The importance of
  full text screening when judging eligibility criteria in a systematic
  review*. Arquivos em Odontologia.
  <https://doi.org/10.35699/2178-1990.2022.37521>
- Himmelstein, D. S., Rodriguez Romero, A., Levernier, J. G., Munro, T. A.,
  McLaughlin, S. R., Greshake Tzovaras, B., & Greene, C. S. (2018). *Sci-Hub
  provides access to nearly all scholarly literature*. eLife, 7:e32822.
  <https://doi.org/10.7554/eLife.32822>
- Jergas, H., & Baethge, C. (2015). *Quotation accuracy in medical journal
  articles — a systematic review and meta-analysis*. PeerJ, 3:e1364.
  <https://doi.org/10.7717/peerj.1364>
- Lin, J. (2009). *Is searching full text more effective than searching
  abstracts?*. BMC Bioinformatics, 10:46.
  <https://doi.org/10.1186/1471-2105-10-46>
- Polanin, J. R., Pigott, T. D., & Espelage, D. L. (2019). *Best practice
  guidelines for abstract screening large-evidence systematic reviews and
  meta-analyses*. Research Synthesis Methods, 10(3), 330–342.
  <https://doi.org/10.1002/jrsm.1354>
- Rekdal, O. B. (2014). *Academic urban legends*. Social Studies of Science,
  44(4), 638–654. <https://doi.org/10.1177/0306312714535679>
- Steel, C. M. (1996). *Read before you cite*. The Lancet, 348(9021), 144.
  <https://doi.org/10.1016/S0140-6736(05)66108-9>
- Simkin, M. V., & Roychowdhury, V. P. (2003). *Read before you cite!*.
  Complex Systems, 14, 269–274. (Terekam pada daftar rujukan Agarwal dkk.,
  2023.)

> **Catatan integritas sumber.** URL PMC `PMC4580677` yang beredar untuk judul
> "If the results of an article are noteworthy…" **tidak** menunjuk ke rekaman
> tersebut: halaman itu memuat artikel lain (*Fixing a hole: CCN2 closes
> chronic wounds*). Karena itu sitasi Dal-Ré dkk. (2015) di atas memakai DOI
> dan URL ScienceDirect yang benar-benar terverifikasi lewat `scholar.py`,
> bukan tautan PMC yang keliru.
