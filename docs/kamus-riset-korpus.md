# Riset Korpus: Struktur Artikel Jurnal Indonesia

Riset ini menurunkan "kamus struktur" artikel jurnal dari PDF asli di
[`docs/sinta-corpus/`](sinta-corpus/) (Sinta 1–6, bidang komputasi/sistem
informasi). Setiap klaim di bawah menyebut **slug** berkas yang menjadi bukti.
Kamus mesin yang diperkaya hasil riset ini ada di
[`assets/bahasa/kamus-id.yaml`](../assets/bahasa/kamus-id.yaml); dokumen
turunan manusia ada di [`kamus-bahasa-artikel.md`](kamus-bahasa-artikel.md).

## Sumber

- Berkas: `docs/sinta-corpus/<slug>.pdf` (**29 PDF** terverifikasi, lihat
  [`docs/sinta-corpus/MANIFEST.md`](sinta-corpus/MANIFEST.md)).
- Ekstraksi: `pdftotext -layout <pdf> -` (tanpa pandoc). Tidak ada berkas
  korpus yang diubah oleh riset ini.
- Bahasa: **10 paper berbahasa Indonesia** dan **19 paper berbahasa Inggris**
  (deteksi berbasis rasio kata fungsi; lihat kolom "Bahasa" pada tabel §1).
  - Indonesia (10): `s2-jsinbis`, `s3-mib`, `s3-sistemasi`, `s4-jsi`,
    `s4-scan`, `s4-transformatika`, `s5-jatisi`, `s5-misi`, `s6-jupiter`,
    `s6-jutik`
  - Inggris (19): `s1-register`, `s1-telkomnika`, `s2-ijccs`, `s2-ilkom`,
    `s2-jiki`, `s2-jisebi`, `s2-jptk`, `s2-jti`, `s2-jtie`, `s2-resti`,
    `s2-sji`, `s3-coreit`, `s3-jsce`, `s3-jsi-ui`, `s3-juti`, `s3-sinkron`,
    `s3-sisfokom`, `s4-sitekin`, `s5-nuansa`

> Catatan operasional: saat riset gelombang pertama berjalan,
> `s3-sistemasi.pdf` sempat berisi halaman arahan OJS (HTML) karena penulis
> lain sedang menyegarkan korpus; ekstraksi diulang setelah berkas menjadi
> PDF valid (18 halaman). Korpus kini berjumlah 29 PDF.

## 1. Temuan per-paper

| Slug | Bahasa | Kepala bagian tingkat-1 (verbatim) | Skema nomor | Label abstrak | Label kata kunci | Label simpulan | Sitasi dalam teks | Daftar pustaka |
|---|---|---|---|---|---|---|---|---|
| `s1-register` | EN | `1. Introduction`, `2. Materials and Methods`, `3. Experimental Results and Evaluation`, `4. Conclusion` | `N.` + `N.M.` | `ABSTRACT` | `Keywords:` | `4. Conclusion` | numerik `[1]`, rentang `[14]–[17]` | bernomor, 56 entri |
| `s1-telkomnika` | EN | `1. INTRODUCTION`, `2. METHOD`, `3. RESULTS AND DISCUSSION`, `4. CONCLUSION`, `REFERENCES` | `N.` + `N.M.` | `ABSTRACT` | `Keywords:` | `4. CONCLUSION` | numerik `[1]`, rentang `[1]-[3]` | bernomor, 26 entri |
| `s2-ijccs` | EN | `1. INTRODUCTION`, `2. METHODS`, `3. RESULTS AND DISCUSSION`, `4. CONCLUSIONS`, `REFERENCES` | `N.` + `N.M.` | `Abstrak` **dan** `Abstract` | `Kata kunci—` / `Keywords—` | `4. CONCLUSIONS` | numerik `[1]` | bernomor, 28 entri |
| `s2-ilkom` | EN | `Introduction`, `Method`, `Results and Discussion`, `Conclusion` | tanpa nomor | `Abstract` | `Keywords:` (pemisah `;`) | `Conclusion` | numerik `[1]` | bernomor, 30 entri |
| `s2-jiki` | EN | `1. Introduction`, `2. Related Works`, `3. Metodhology`, `4. Results and Analysis`, `5. Discussion and Conclusion` | `N.` + `N.M.` | `Abstract` | `Keywords:` | `5. Discussion and Conclusion` | numerik `[2], [3]`, rentang `[2-4]` | bernomor, 22 entri |
| `s2-jisebi` | EN | `I. INTRODUCTION`, `II. LITERATURE REVIEW`, `III. METHODS`, `IV. RESULTS`, `V. DISCUSSION`, `VI. CONCLUSIONS`, `REFERENCES` | **romawi** | `Abstract` (terstruktur) | `Keywords:` | `VI. CONCLUSIONS` | numerik `[1]`, rentang `[7] -[12]` | bernomor, 78 entri |
| `s2-jptk` | EN | `INTRODUCTION`, `METHOD`, `RESULTS AND DISCUSSION`, `CONCLUSION`, `ACKNOWLEDGMENT`, `REFERENCES` | tanpa nomor (kapital) | `ABSTRACT` | `Keywords:` | `CONCLUSION` | **APA** `(Tarjiah et al., 2023)` | APA, 18 entri |
| `s2-jsinbis` | ID | `1. Pendahuluan`, `2. Kerangka Teori`, `3. Metodologi`, `4. Hasil dan Pembahasan`, `5. Kesimpulan` | `N.` + `N.M.` | `Abstract` **dan** `Abstrak` | `Keyword :` / `Kata Kunci :` (pemisah `;`) | `Kesimpulan` | **APA** `(Wong et al., 2011)` | APA |
| `s2-jti` | EN | `1. INTRODUCTION`, `2. METHODS`, `3. RESULTS AND DISCUSSION`, `4. CONCLUSION` | `N.` + `N.M.` | `ABSTRACT` | `Keywords :` (pemisah `;`) | `CONCLUSION` | numerik `[1]`, rentang `[1]–[2]` | bernomor, 20 entri |
| `s2-jtie` | EN | `I. INTRODUCTION`, `II. LITERATURE REVIEW`, `III. RESEARCH METHOD`, `IV. RESULT AND DISCUSSION`, `V. CONCLUSION AND RECOMMENDATION` | **romawi** | `Abstract` | `Keywords:` (pemisah `;`) | `V. CONCLUSION AND RECOMMENDATION` | **APA** `(Gkintoni et al., 2025)` | APA, 29 entri |
| `s2-resti` | EN | `1. Introduction`, `2. Methods`, `3. Results and Discussions`, `4. Conclusions` | `N.` + `N.M.` | `Abstract` | `Keywords:` (pemisah `;`) | `4. Conclusions` | numerik `[1]`, rentang `[4-7]` | bernomor, 35 entri |
| `s2-sji` | EN | `INTRODUCTION`, `METHODS`, `RESULTS AND DISCUSSIONS`, `CONCLUSION`, `REFERENCES` | tanpa nomor (kapital) | `Abstract.` (terstruktur) | `Keywords:` | `CONCLUSION` | numerik `[1]` | bernomor, 36 entri |
| `s3-coreit` | EN | `INTRODUCTION`, `METHODS`, `RESULT AND DISCUSSION`, `CONCLUSION`, `REFERENCES` | tanpa nomor (kapital) | `Abstract` | `Keywords:` | `CONCLUSION` | numerik `[1]` | bernomor, 19 entri |
| `s3-jsce` | EN | `1. Introduction`, `2. Method`, `3. Results And Discussion`, `4. Conclusions` | `N.` + `N.M.` | `Abstract` | `Keywords:` (pemisah `;`) | `4. Conclusions` | **APA** `(Hu et al., 2023)` | APA, 17 entri |
| `s3-jsi-ui` | EN | `Introduction`, `Literature Review`, `Methodology`, `Results`, `Discussion`, `Conclusion`, `Limitations and Future Works`, `References` | tanpa nomor | `Abstract` | `Keywords:` | `Conclusion` | **APA** `(Kumar et al., 2023)` | APA, 37 entri |
| `s3-juti` | EN | `1. Introduction`, `2. Related work`, `3. Methodology`, `4. Result and discussion`, `5. Conclusion` | `N.` + `N.M.` | `ABSTRACT` | `Keywords:` | `5. Conclusion` | numerik `[1]` | bernomor, 26 entri |
| `s3-mib` | ID | `1. PENDAHULUAN`, `2. METODOLOGI PENELITIAN`, `3. HASIL DAN PEMBAHASAN`, `4. KESIMPULAN` | `N.` + `N.M.` | `Abstrak−` **dan** `Abstract−` | `Kata Kunci:` (pemisah `;`) | `4. KESIMPULAN` | numerik `[1]` | bernomor, 25 entri |
| `s3-sinkron` | EN | `INTRODUCTION`, `LITERATURE REVIEW`, `METHOD`, `RESULT`, `CONCLUSION`, `REFERENCES` | tanpa nomor (kapital) | `Abstract:` | `Keywords:` | `CONCLUSION` | **APA** `(Sung et al., 2026)` | APA, 25 entri |
| `s3-sisfokom` | EN | `I. INTRODUCTION`, `II. METHODOLOGY`, `III. DISCUSSION AND RESULT`, `IV. CONCLUSION`, `REFERENCES` | **romawi** | `Abstract` | — (tanpa label) | `IV. CONCLUSION` | numerik `[1]` | bernomor, 19 entri |
| `s3-sistemasi` | ID | `1. Pendahuluan`, `2. Tinjauan Literatur`, `3. Metode Penelitian`, `4. Hasil dan Pembahasan`, `5. Kesimpulan` | `N.` + `N.M.` | `Abstrak` **dan** `Abstract` | `Kata kunci:` / `Keywords:` | `5. Kesimpulan` | numerik `[1]`, rentang `[13]–[15]` | bernomor, 24 entri |
| `s4-jsi` | ID | `1. PENDAHULUAN`, `2. TINJAUAN PUSTAKA`, `3. METODE PENELITIAN`, `4. PEMBAHASAN`, `5. KESIMPULAN`, `DAFTAR PUSTAKA` | `N.` + `N.M.` | `Abstrak` **dan** `Abstract` | `Kata kunci:` / `Keywords:` | `5. KESIMPULAN` | numerik `[1]` | bernomor, 23 entri |
| `s4-scan` | ID | `PENDAHULUAN`, `METODE PENELITIAN`, `HASIL DAN PEMBAHASAN`, `DAFTAR PUSTAKA` | tanpa nomor (kapital) | `ABSTRAK` **dan** `ABSTRACT` | `Kata Kunci:` / `Keywords:` | `HASIL DAN PEMBAHASAN` | numerik `[1]` | bernomor, 22 entri |
| `s4-sitekin` | EN | `Introduction`, `Research Methods`, `Results and Discussion`, `Conclusion`, `References` | tanpa nomor | `ABSTRACT` | `Keywords:` | `Conclusion` | numerik `[1]` | bernomor, 16 entri |
| `s4-transformatika` | ID | `PENDAHULUAN`, `METODE PENELITIAN`, `HASIL`, `PEMBAHASAN`, `KESIMPULAN DAN REKOMENDASI`, `REFERENSI` | tanpa nomor (kapital) | `ABSTRACT` | `Keywords:` | `KESIMPULAN DAN REKOMENDASI` | numerik `[1]` | bernomor, 42 entri |
| `s5-jatisi` | ID | `1. PENDAHULUAN`, `2. METODE`, `3. HASIL DAN PEMBAHASAN`, `4. KESIMPULAN`, `5. SARAN`, `DAFTAR PUSTAKA` | `N.` + `N.M.` | `Abstrak` **dan** `Abstract` | `Kata kunci—` / `Keywords—` | `4. KESIMPULAN` (saran jadi `5. SARAN`) | numerik `[1]` | bernomor, 34 entri |
| `s5-misi` | ID | `1. PENDAHULUAN`, `2. TINJAUAN PUSTAKA`, `3. METODOLOGI PENELITIAN`, `4. HASIL DAN PEMBAHASAN`, `5. KESIMPULAN DAN SARAN`, `DAFTAR PUSTAKA:` | `N.` + `N.M.` | `Abstrak` **dan** `Abstract` | `Kata kunci :` / `Keywords :` | `5. KESIMPULAN DAN SARAN` | numerik `[1]` | bernomor, 17 entri |
| `s5-nuansa` | EN | `1. INTRODUCTION`, `2. RESEARCH METHODS`, `3. RESEARCH RESULTS`, `4. DISCUSSION`, `5. CONCLUSION`, `6. SUGGESTIONS`, `REFERENCES` | `N.` + `N.M.` | `Abstract` | — (tanpa label) | `5. CONCLUSION` (saran jadi `6. SUGGESTIONS`) | numerik `[1]` | bernomor, 18 entri |
| `s6-jupiter` | ID | `1. PENDAHULUAN`, `2. LANDASAN TEORI`, `3. METODOLOGI PENELITIAN`, `4. HASIL DAN PEMBAHASAN`, `4.6. PENUTUP`, `DAFTAR PUSTAKA` | `N.` + `N.M.K` | `ABSTRAK` **dan** `ABSTRACT` | `Kata Kunci –` / `Keywords –` | `4.6. PENUTUP` | numerik `[1]` | bernomor, 14 entri |
| `s6-jutik` | ID | `1. PENDAHULUAN`, `2. METODE`, `3. HASIL DAN PEMBAHASAN`, `4. KESIMPULAN DAN SARAN`, `5. DAFTAR PUSTAKA` | `N.` (tanpa subbagian) | `ABSTRAK` **dan** `ABSTRACT` | `Kata kunci:` / `Keywords:` | `4. KESIMPULAN DAN SARAN` | numerik `[1]` | bernomor, 12 entri |

### Catatan struktur penting

- **Skema penomoran tingkat-1**: **17 paper** memakai Arab `N.`
  (`s1-register`, `s1-telkomnika`, `s2-ijccs`, `s2-jiki`, `s2-jsinbis`,
  `s2-jti`, `s2-resti`, `s3-jsce`, `s3-juti`, `s3-mib`, `s3-sistemasi`,
  `s4-jsi`, `s5-jatisi`, `s5-misi`, `s5-nuansa`, `s6-jupiter`, `s6-jutik`);
  **3 paper** memakai **angka Romawi** (`s2-jisebi` `I.`–`VI.`, `s2-jtie`
  `I.`–`V.`, `s3-sisfokom` `I.`–`IV.`); **9 paper** memakai judul
  **tanpa nomor** (`s2-ilkom`, `s2-jptk`, `s2-sji`, `s3-coreit`,
  `s3-jsi-ui`, `s3-sinkron`, `s4-scan`, `s4-sitekin`, `s4-transformatika`).
- **Subbagian** umumnya `N.M.` (mis. `2.1`, `3.4`); `s6-jupiter` turun ke
  `N.M.K` (`4.4.1`, `4.5.2`); `s6-jutik` dan `s4-transformatika` memakai
  penomoran daftar di dalam badan (bukan subbab berjudul).
- **Daftar Pustaka** umumnya bagian tak bernomor, kecuali `s6-jutik`
  (`5. DAFTAR PUSTAKA`).
- **Simpulan** kadang berjudul `PENUTUP` (`s6-jupiter` `4.6. PENUTUP`),
  `KESIMPULAN DAN REKOMENDASI` (`s4-transformatika`),
  `CONCLUSION AND RECOMMENDATION` (`s2-jtie`), atau dipisah dari saran:
  `s5-jatisi` (`4. KESIMPULAN` + `5. SARAN`) dan `s5-nuansa`
  (`5. CONCLUSION` + `6. SUGGESTIONS`).
- **Seksi tinjauan pustaka** berdiri sendiri pada **19 paper** dengan judul
  beragam: `TINJAUAN PUSTAKA` (`s4-jsi`, `s5-misi`), `LANDASAN TEORI`
  (`s6-jupiter`), `TINJAUAN LITERATUR` (`s3-sistemasi`), `Kerangka Teori`
  (`s2-jsinbis`), `LITERATURE REVIEW` (`s2-jisebi`, `s2-jtie`, `s3-sinkron`),
  `Related Works` (`s2-jiki`), `Related work` (`s3-juti`), `Literature
  Review` (`s3-jsi-ui`).
- **Ucapan terima kasih** eksplisit pada 7 paper: `s1-register`,
  `s1-telkomnika`, `s2-ilkom`, `s2-jptk` (`ACKNOWLEDGMENT`), `s2-jsinbis`,
  `s3-juti`, `s3-sisfokom`.
- `s3-jsi-ui` menambah seksi **`Limitations and Future Works`** sebelum
  `References`; `s2-jtie` menaruh `5. Limitations and Future Research
  Directions` sebagai subbagian hasil.

## 2. Frekuensi label kepala bagian (29 paper)

| Keluarga seksi | Jumlah paper | Judul yang teramati |
|---|---|---|
| Pendahuluan | 29/29 | `PENDAHULUAN`, `Pendahuluan`, `INTRODUCTION`, `Introduction` |
| Metode | 29/29 | `METODE`, `METODE PENELITIAN`, `Metode Penelitian`, `METODOLOGI PENELITIAN`, `Metodologi`, `METHOD`, `METHODS`, `Method`, `Methods`, `METHODOLOGY`, `Methodology`, `Materials and Methods`, `RESEARCH METHOD(S)`, `Research Methods`, `Metodhology` (salah ketik di `s2-jiki`) |
| Hasil/Pembahasan | 29/29 | `HASIL`, `HASIL DAN PEMBAHASAN`, `Hasil dan Pembahasan`, `PEMBAHASAN`, `Pembahasan`, `RESULTS`, `RESULTS AND DISCUSSION`, `Results and Discussion`, `RESULTS AND DISCUSSIONS`, `Result and discussion`, `Result`, `RESEARCH RESULTS`, `Experimental Results and Evaluation`, `DISCUSSION`, `Discussion`, `DISCUSSION AND RESULT` |
| Simpulan | 29/29 | `KESIMPULAN`, `KESIMPULAN DAN SARAN`, `KESIMPULAN DAN REKOMENDASI`, `Kesimpulan`, `PENUTUP`, `CONCLUSION`, `CONCLUSIONS`, `Conclusion`, `Conclusions`, `CONCLUSION AND RECOMMENDATION` |
| Tinjauan pustaka | 19/29 | `TINJAUAN PUSTAKA`, `LANDASAN TEORI`, `TINJAUAN LITERATUR`, `Kerangka Teori`, `LITERATURE REVIEW`, `Related Works`, `Related work`, `Literature Review` |
| Saran terpisah | 6/29 | `SARAN` (`s5-jatisi`, `s5-misi`), `SUGGESTIONS` (`s5-nuansa`), `Rekomendasi` (`s4-transformatika`), `Limitations and Future Works` (`s3-jsi-ui`) |
| Ucapan terima kasih | 7/29 | `ACKNOWLEDGMENT`, `UCAPAN TERIMA KASIH` |
| Daftar Pustaka bernomor | 1/29 | `5. DAFTAR PUSTAKA` (`s6-jutik`) |

## 3. Frekuensi konektor (29 paper, jumlah kemunculan kata utuh)

| Konektor | Jumlah | Konektor | Jumlah |
|---|---:|---|---:|
| yaitu | 160 | selain itu | 19 |
| sehingga | 86 | dapat dilihat pada | 19 |
| karena | 77 | meskipun | 14 |
| berdasarkan | 76 | terlihat pada | 11 |
| kemudian | 67 | misalnya | 9 |
| selanjutnya | 50 | sejalan dengan | 8 |
| sedangkan | 39 | oleh karena itu | 8 |
| agar | 35 | dengan demikian | 8 |
| hal ini | 33 | yakni | 7 |
| hasil penelitian | 27 | disajikan pada | 7 |
| kedua | 23 | guna | 6 |
| adapun | 23 | lebih lanjut | 5 |
| pertama | 22 | meskipun demikian | 4 |
| namun | 21 | dapat disimpulkan | 4 |
| | | sementara itu | 2 |
| | | sebagai contoh | 2 |
| | | namun demikian | 2 |
| | | walaupun / oleh sebab itu / di sisi lain / akan tetapi | 1 each |

Konektor yang **sudah** ada di kamus dan terkonfirmasi: `sehingga`,
`berdasarkan`, `karena`, `hal ini`, `agar`, `adapun`, `sedangkan`, `namun`,
`selain itu`, `guna`, `dengan demikian`, `oleh karena itu`, `lebih lanjut`,
`sejalan dengan`, `yaitu`, `kemudian`, `selanjutnya`, `pertama`, `kedua`,
`meskipun`, `meskipun demikian`, `namun demikian`, `misalnya`,
`sebagai contoh`, `akan tetapi`, `walaupun`, `oleh sebab itu`, `di sisi lain`,
`dapat dilihat pada`, `terlihat pada`, `disajikan pada`. Tambahan baru dari
gelombang kedua: **`sementara itu`** (2×).

## 4. Frekuensi kolokasi verba (29 paper, lemma)

| Verba | Jumlah | Verba | Jumlah |
|---|---:|---|---:|
| menggunakan | 272 | menganalisis | 13 |
| menunjukkan | 83 | mengidentifikasi | 11 |
| menghasilkan | 73 | membandingkan | 11 |
| memiliki | 71 | memprediksi | 9 |
| melakukan | 65 | mengembangkan | 8 |
| menghitung | 41 | melatih | 8 |
| memberikan | 39 | menguji | 6 |
| meningkatkan | 36 | membangun | 6 |
| mengukur | 32 | menyusun | 5 |
| menentukan | 26 | disimpulkan | 5 |
| memperoleh | 23 | merancang | 4 |
| membuat | 22 | mengimplementasikan | 4 |
| bertujuan | 22 | mengakibatkan | 4 |
| menyebabkan | 17 | menyajikan | 2 |
| menerapkan | 17 | mengumpulkan | 2 |
| mengevaluasi | 15 | mengusulkan | 1 |
| mengklasifikasikan | 14 | mengadopsi | 1 |

Kolokasi (verba + objek) yang paling sering:

| Kolokasi | Jumlah | Sumber |
|---|---:|---|
| `menggunakan metode support vector` | 16 | `s2-jti`, `s4-sitekin`, `s4-transformatika`, `s6-jutik` |
| `menggunakan algoritma random forest` | 15 | `s4-jsi`, `s5-jatisi`, `s5-misi` |
| `menggunakan persamaan` | 10 | `s2-ijccs`, `s3-sistemasi`, `s6-jupiter` |
| `menghasilkan akurasi` | 7 | `s4-jsi`, `s4-transformatika`, `s5-misi` |
| `memperoleh akurasi sebesar` | 4 | `s4-scan`, `s4-transformatika`, `s5-misi` |
| `menggunakan metode ahp` | 4 | `s6-jupiter` |
| `menggunakan mediapipe hands` | 4 | `s4-scan` |
| `menggunakan metode` | 20 | 6 paper |
| `menggunakan data` | 5 | `s4-jsi`, `s5-misi` |
| `melakukan analisis` | 5 | `s5-jatisi`, `s6-jupiter` |
| `membuat matriks` | 5 | `s6-jupiter` |
| `melatih model` | 4 | `s5-misi`, `s4-scan` |
| `meningkatkan akurasi` | 4 | `s4-jsi`, `s5-misi` |
| `mengukur kinerja` | 4 | `s5-misi`, `s6-jupiter` |
| `menghitung nilai` | 3 | `s6-jupiter` |
| `menghitung rasio konsistensi` | 3 | `s6-jupiter` |
| `menggunakan tensorflow` | 3 | `s4-scan` |
| `melakukan konfigurasi` | 4 | `s6-jutik` |
| `memiliki pengaruh` | 3 | `s5-jatisi` |
| `menentukan kriteria` | 3 | `s6-jupiter` |

## 5. Pembuka kalimat (opener) teramati

Dihitung dari 10 paper berbahasa Indonesia (`s2-jsinbis`, `s3-mib`,
`s3-sistemasi`, `s4-jsi`, `s4-scan`, `s4-transformatika`, `s5-jatisi`,
`s5-misi`, `s6-jupiter`, `s6-jutik`):

| Pembuka | Jumlah | Catatan |
|---|---:|---|
| `Gambar …` / `Pada gambar …` | 40 + 11 | rujukan gambar, terutama `s6-jutik` (13×) |
| `Tabel …` | 33 | rujukan tabel, terutama `s6-jupiter` (7×) |
| `Hal ini …` | 22 | `Hal ini menunjukkan bahwa` 3×, `Hal ini berarti bahwa` 1×, `Hal ini menyebabkan` 1× |
| `Hasil …` | 20 | `Hasil pengujian menunjukkan` (s4-scan, s4-transformatika) |
| `Selain itu …` | 17 | penambahan |
| `Pada penelitian …` | 15 | rujukan ke penelitian sendiri |
| `Penelitian ini …` | 14 | pembuka tujuan/metode |
| `Namun …` | 9 | penanda kontras/keterbatasan |
| `Setelah itu …` | 8 | langkah prosedural |
| `Dengan demikian …` | 8 | penutup argumen |
| `Dari hasil …` | 6 | rujukan hasil |
| `Hasil penelitian …` | 6 | |

Pada 19 paper berbahasa Inggris, pembuka terbanyak: `The …` (96), `Table …`
(78), `However …` (63), `Figure …` (38), `Therefore …` (34), `This study …`
(33), `The results …` (27), `Based on …` (22), `These findings …` (21),
`In addition …` / `Furthermore …` (23 each), `According to …` (15),
`Consequently …` (14), `Moreover …` (13).

Pola rujukan gambar/tabel (Indonesia): `dapat dilihat pada` 19×
(`s5-jatisi` 9×, `s6-jutik` 3×, `s4-scan`), `terlihat pada` 11×
(`s6-jupiter` 9×), `disajikan pada` 7× (`s3-sistemasi` 4×, `s2-jiki`),
`pada Tabel` 25×, `pada Gambar` 36× (versi lama; kini termasuk gelombang
kedua).

## 6. "Argument moves" yang teramati

### Pendahuluan
`objek/konteks` → `masalah` → `kajian terdahulu` → `celah/tujuan`.
Contoh `s4-jsi`: konteks sampah plastik global → masalah Kota Tanjungpinang
(100–150 ton/hari) → `Penelitian sebelumnya menunjukkan bahwa Faster R-CNN …`
→ `Penelitian ini bertujuan untuk mengukur akurasi …`. Contoh `s4-scan`:
`Tujuan penelitian ini adalah membangun pipeline pengenalan alfabet BISINDO
…`. Penanda celah: `masih terkendala oleh keterbatasan fasilitas dan
teknologi` (`s4-jsi`), `Atas dasar tersebut, penelitian ini berfokus untuk …`
(`s5-jatisi`), `Research Gap` sebagai subbagian eksplisit (`s2-jiki` 2.3,
`s3-juti` 2.5).

### Metode
`jenis/pendekatan` → `tahapan` → `pengumpulan data` → `pengujian`.
Contoh `s5-jatisi`: `Penelitian ini menggunakan metode Cross-Industry Standard
Process for Data Mining (CRISP-DM)` → tahapan `2.1 Business Understanding` …
`2.6 Deployment`. Contoh `s2-jsinbis`: `Metode yang digunakan pada penelitian
ini adalah manajemen rantai pasok yang ramah lingkungan`. Contoh `s4-jsi`:
`Penelitian ini bertujuan untuk mengukur akurasi metode Faster R-CNN …` →
dataset 800 citra dari enam lokasi.

### Hasil
`rujuk Gambar/Tabel` → `angka` → `interpretasi`.
Contoh `s4-transformatika`: `Hasil penelitian menunjukkan bahwa rasio 90:10
memberikan performa terbaik, dengan Polynomial memperoleh akurasi tertinggi
…` → `Berdasarkan hasil pengujian, kernel polynomial menghasilkan akurasi
tertinggi sebesar 91,66%` → `Hal ini menunjukkan bahwa penggunaan jumlah data
latih yang lebih besar …`. Contoh `s4-scan`: `Hasil pengujian menunjukkan
akurasi pengenalan sebesar 97,77% dengan macro precision 97,54% …`.

### Simpulan
`Berdasarkan hasil … dapat disimpulkan bahwa` → `Dengan demikian` →
keterbatasan `Namun` → saran.
Contoh `s6-jupiter`: `Berdasarkan hasil penelitian dan pengujian yang telah
dilakukan maka dapat disimpulkan bahwa …`. Contoh `s4-transformatika`:
`Berdasarkan hasil pengujian, didapatkan bahwa metode Support Vector Machine
(SVM) mampu …` dan `Oleh karena itu, penelitian selanjutnya disarankan untuk
menerapkan metode …`. Keterbatasan: `Namun demikian, kecepatan 64 kbps
tergolong sangat rendah …` (`s6-jutik`). Saran: `Penelitian selanjutnya
disarankan untuk memperluas variasi jenis sampah …` (`s4-jsi`).

## 7. Konvensi abstrak yang teramati

- **Label** (29 paper): `Abstract` 19×, `ABSTRACT` 10×, `Abstrak` 7×,
  `ABSTRAK` 3×. `s3-mib` memakai **`Abstrak−`** / **`Abstract−`** dengan
  tanda **minus** (U+2212), bukan hyphen.
- **Dwi bahasa**: **10 paper** memuat abstrak Indonesia **dan** Inggris
  (`s2-ijccs`, `s2-jsinbis`, `s3-mib`, `s3-sistemasi`, `s4-jsi`, `s4-scan`,
  `s5-jatisi`, `s5-misi`, `s6-jupiter`, `s6-jutik`).
- **Label kata kunci**: `Keywords:` (21), `Kata kunci:` (3), `Keywords :` (2),
  `Kata Kunci:` (2), `Kata Kunci :` (1), `Kata kunci :` (1), `Keyword :` (1),
  `Kata Kunci –` (1), `Keywords –` (1). `s5-nuansa` dan `s3-sisfokom` tidak
  memakai label kata kunci terpisah.
- **Pemisah kata kunci**: **7 paper** memakai **titik koma** (`;`) —
  `s2-ilkom`, `s2-jsinbis`, `s2-jti`, `s2-jtie`, `s2-resti`, `s3-jsce`,
  `s3-mib`; sisanya koma.
- **Struktur**: umumnya satu paragraf naratif. **Dua paper** memakai abstrak
  **terstruktur**:
  - `s2-jisebi`: `Background:`, `Objective:`, `Methods:`, `Results:`,
    `Conclusion:`.
  - `s2-sji`: `Purpose:`, `Methods:`, `Results:`, `Novelty:` (label
    `Abstract.`).
- **Panjang** (perkiraan kasar, kata): `s4-scan` ~138, `s5-jatisi` ~175,
  `s4-jsi` ~188, `s2-ijccs` ~192, `s6-jutik` ~212, `s2-jsinbis` ~217,
  `s3-mib` ~239, `s3-sistemasi` ~240, `s5-misi` ~302, `s6-jupiter` ~367.
  Rentang teramati ~138–367 kata (beberapa melampaui pedoman 250 kata).
- **Pembuka abstrak** teramati: `Penelitian ini mengkaji …` (`s2-ijccs`),
  `Penelitian ini menganalisis …` (`s5-jatisi`), `Studi ini bertujuan untuk …`
  (`s5-misi`), `Penelitian ini bertujuan untuk …` (`s4-jsi`,
  `s4-transformatika`), `Data berasal dari …` (`s3-sistemasi`),
  `This study presents …` (`s5-nuansa`), `This paper evaluates …`
  (`s2-jiki`).

## 8. Gaya sitasi: APA vs numerik

| Gaya | Jumlah paper | Paper |
|---|---:|---|
| Numerik kurung `[1]`, `[7]–[9]` + Daftar Pustaka bernomor | 23 | `s1-register`, `s1-telkomnika`, `s2-ijccs`, `s2-ilkom`, `s2-jiki`, `s2-jisebi`, `s2-jti`, `s2-resti`, `s2-sji`, `s3-coreit`, `s3-juti`, `s3-mib`, `s3-sisfokom`, `s3-sistemasi`, `s4-jsi`, `s4-scan`, `s4-sitekin`, `s4-transformatika`, `s5-jatisi`, `s5-misi`, `s5-nuansa`, `s6-jupiter`, `s6-jutik` |
| APA name-year `(Author, year)` + Daftar Pustaka alfabetis | 6 | `s2-jptk`, `s2-jsinbis`, `s2-jtie`, `s3-jsce`, `s3-jsi-ui`, `s3-sinkron` |

Varian rentang numerik yang teramati:

- `[14]–[17]`, `[18]–[21]`, `[24]–[26]`, `[31]–[33]` (`s1-register`)
- `[1]-[3]`, `[6]-[8]`, `[17]-[19]`, `[20]-[22]` (tanda hubung, `s1-telkomnika`)
- `[7] -[12]`, `[26]-[30]` (`s2-jisebi`)
- `[1]–[2]`, `[3]–[5]`, `[6]–[8]`, `[9]–[11]`, `[18]–[20]`, `[12]–[14]` (`s2-jti`)
- `[13]–[15]` (`s3-sistemasi`)
- **rentang inline tanpa kurung ganda**: `[2-4]` (`s2-jiki`), `[4-7]`,
  `[8-11]`, `[12-14]`, `[16-19]`, `[20-23]`, `[25-28]`, `[29-34]` (`s2-resti`)
- rujukan ganda `[2], [3]` (`s2-jiki`)

Contoh APA: `(Sung et al., 2026)`, `(Ridwansyah et al., 2026)` (`s3-sinkron`);
`(Tarjiah et al., 2023)`, `(Arung et al., 2023)` (`s2-jptk`);
`(Kumar et al., 2023)`, `(Ramezanian & Neimi, 2024)` (`s3-jsi-ui`);
`(CIGRE, 2024)`, `(Hu et al., 2023)` (`s3-jsce`); daftar pustaka alfabetis
bergaya APA.

> **Penting untuk build repo**: build artikel/skripsi repo ini memakai
> **APA name-year** (`assets/csl/apa.csl`, `--citeproc`). Gaya numerik adalah
> varian korpus, **bukan** gaya build. Karena itu kamus mencatat keduanya
> tetapi tidak mengubah gaya default.

## 9. Diksi: kosakata tidak baku yang teramati di korpus

Kata tidak baku yang benar-benar muncul di PDF korpus (jumlah kemunculan,
gelombang kedua menambah bukti):

| Tidak baku | Baku | Kemunculan | Sumber |
|---|---|---:|---|
| `analisa` | analisis | 12 | `s2-jsinbis`, `s4-transformatika`, `s5-misi`, `s6-jupiter`, `s6-jutik` |
| `dimana` | di mana | 19 | `s2-jsinbis`, `s3-mib`, `s5-misi`, `s6-jutik` |
| `mempengaruhi` | memengaruhi | 9 | `s2-jsinbis`, `s4-jsi`, `s4-transformatika`, `s5-jatisi` |
| `dikarenakan` | karena / disebabkan oleh | 7 | `s2-jsinbis`, `s4-jsi`, `s4-transformatika`, `s6-jupiter`, `s6-jutik` |
| `kwalitas` | kualitas | 1 | `s2-jsinbis` |
| `efektifitas` | efektivitas | 1 | `s2-jsinbis` |
| `prosentase` | persentase | 1 | `s2-jsinbis` |
| `simpel` | sederhana | 1 | `s4-scan` |

> `standard` (40 kemunculan) **sengaja tidak** dijadikan pasangan tidak-baku
> di kamus karena hampir semua kemunculannya adalah bagian nama baku Inggris
> `Cross-Industry Standard Process for Data Mining (CRISP-DM)` dan nama baku
> lain, sehingga melarangnya akan menimbulkan positif palsu. Lihat laporan
> akhir.

## 10. Frasa pengisi bergaya AI generik

Pengujian 25 frasa klise (mis. `pada era digital saat ini`, `seiring dengan
perkembangan zaman`, `tak dapat dipungkiri bahwa`, `mari kita`, `adalah
merupakan`) pada seluruh 29 PDF menghasilkan **0 kemunculan**, kecuali
`dewasa ini` (1×, `s5-jatisi`) dan `merupakan hal yang sangat penting` (1×,
`s6-jupiter`). Artinya daftar `frasa_ai_generik` di kamus **tidak**
bertabrakan dengan gaya korpus nyata — frasa-frasa itu memang hampir tidak
dipakai penulis jurnal. Karena itu daftar tersebut tidak diperluas.

## 11. Ringkasan untuk kamus

- `varian_kepala` diperluas dengan varian **teramati** (mis.
  `PENDAHULUAN`, `METODOLOGI PENELITIAN`, `PEMBAHASAN`, `PENUTUP`,
  `DAFTAR PUSTAKA`, `REFERENCES`, `RESEARCH METHODS`, `Materials and Methods`,
  `Methodology`, `RESEARCH METHOD`, `Research Methods`, `Result and
  discussion`, `Results And Discussion`, `DISCUSSION AND RESULT`,
  `KESIMPULAN DAN REKOMENDASI`, `CONCLUSION AND RECOMMENDATION`).
- Kepala bagian non-kanonik (`TINJAUAN PUSTAKA`, `LANDASAN TEORI`,
  `TINJAUAN LITERATUR`, `Kerangka Teori`, `LITERATURE REVIEW`, `Related
  Works`, `Related work`, `SARAN`, `SUGGESTIONS`, `ACKNOWLEDGMENT`,
  `Limitations and Future Works`) dicatat di kunci `kepala_tambahan`
  (tidak mengubah enam id `kepala_bagian`).
- `formula` ditambah id baru yang terattestasi (mis.
  `metode_digunakan_pada`, `hasil_analisis_menunjukkan`,
  `penelitian_ini_mengembangkan`).
- `rangkai_argumen` diperluas per seksi + kunci `abstrak` + `pustaka`.
- `leksikon_verba` dan `konektor` ditambah kolokasi/konektor teramati.
- `abstrak` mencatat varian label, varian label kata kunci, varian struktur
  (termasuk `Purpose/Methods/Results/Novelty`), pemisah titik koma, dan
  rentang panjang teramati.
- `kutipan` mencatat paper bergaya numerik vs APA, termasuk rentang inline
  `[2-4]`.

## 12. Leksikon dan kolokasi SI terattestasi

Hitungan dari ekstraksi `pdftotext -layout` atas **29 berkas** korpus Sinta
(`docs/sinta-corpus/*.pdf`), pencocokan tak peka huruf besar-kecil. Kolom
"Bukti" menyebut slug dengan kemunculan terbanyak.

### 12.1 Istilah/leksikon inti

| Istilah | Kemunculan | Bukti (slug, kemunculan) |
|---|---:|---|
| `model` | 1034 | `s2-ijccs` (91), `s3-sinkron` (75), `s2-jisebi` (62) |
| `dataset` | 396 | `s2-jiki` (110), `s2-ilkom` (46), `s2-ijccs` (31) |
| `classification` | 267 | `s1-register` (65), `s2-jti` (50), `s3-sinkron` (38) |
| `algorithm` | 257 | `s1-telkomnika` (59), `s2-ilkom` (58), `s5-nuansa` (45) |
| `pengujian` | 243 | `s4-jsi` (194), `s6-jutik` (17) |
| `accuracy` | 235 | `s3-coreit` (30), `s3-sinkron` (28), `s2-jti` (26) |
| `user` | 210 | `s5-nuansa` (67), `s3-juti` (49), `s2-sji` (23) |
| `evaluation` | 195 | `s2-resti` (28), `s2-jtie` (28), `s3-juti` (23) |
| `akurasi` | 187 | `s3-mib` (69), `s4-transformatika` (49), `s4-jsi` (26) |
| `recall` | 183 | `s3-sistemasi` (37), `s3-sinkron` (34), `s4-transformatika` (22) |
| `random forest` | 181 | `s5-jatisi` (42), `s2-ijccs` (41), `s3-sistemasi` (32) |
| `klasifikasi` | 174 | `s4-transformatika` (59), `s3-mib` (52), `s4-jsi` (25) |
| `training` | 153 | `s3-coreit` (28), `s2-ijccs` (18), `s1-register` (16) |
| `development` | 143 | `s1-telkomnika` (31), `s2-sji` (22), `s2-jtie` (20) |
| `machine learning` | 135 | `s2-ijccs` (24), `s4-sitekin` (23), `s5-jatisi` (17) |
| `prediction` | 118 | `s2-ijccs` (32), `s2-jiki` (31), `s3-sinkron` (14) |
| `f1-score` | 106 | `s2-jiki` (30), `s3-jsce` (19), `s4-transformatika` (16) |
| `testing` | 103 | `s3-juti` (29), `s3-jsce` (11), `s5-nuansa` (9) |
| `implementation` | 95 | `s5-nuansa` (18), `s2-sji` (15), `s3-juti` (13) |
| `prediksi` | 94 | `s3-sistemasi` (24), `s5-misi` (17), `s5-jatisi` (14) |
| `precision` | 93 | `s2-resti` (16), `s3-sistemasi` (12), `s3-sinkron` (12) |
| `algoritma` | 87 | `s5-jatisi` (20), `s5-misi` (17), `s3-mib` (17) |
| `pengguna` | 86 | `s6-jutik` (28), `s4-scan` (17), `s4-transformatika` (15) |
| `evaluasi` | 86 | `s4-transformatika` (21), `s3-sistemasi` (17), `s4-jsi` (10) |
| `sistem informasi` | 81 | `s3-sistemasi` (18), `s3-jsi-ui` (17), `s2-jsinbis` (13) |
| `information system` | 81 | `s2-jisebi` (31), `s3-jsi-ui` (18), `s1-telkomnika` (11) |
| `support vector machine` | 78 | `s3-mib` (33), `s4-transformatika` (25), `s4-sitekin` (9) |
| `preprocessing` | 62 | `s2-jiki` (9), `s4-transformatika` (8), `s4-sitekin` (7) |
| `chatbot` | 59 | `s5-misi` (32), `s2-resti` (26) |
| `implementasi` | 58 | `s5-misi` (21), `s6-jutik` (8), `s6-jupiter` (7) |
| `neural network` | 49 | `s3-coreit` (15), `s4-jsi` (9), `s1-register` (9) |
| `deep learning` | 41 | `s2-jti` (10), `s1-register` (9), `s3-coreit` (5) |
| `naive bayes` | 38 | `s3-mib` (23), `s4-sitekin` (6), `s2-jiki` (6) |
| `decision tree` | 35 | `s2-ijccs` (15), `s1-telkomnika` (6), `s4-sitekin` (5) |
| `confusion matrix` | 34 | `s3-mib` (9), `s5-misi` (5), `s4-transformatika` (5) |
| `k-nearest neighbor` | 32 | `s3-mib` (31) |
| `pengembangan` | 32 | `s5-misi` (8), `s3-sistemasi` (8), `s4-scan` (5) |
| `data uji` | 19 | `s4-transformatika` (9), `s4-scan` (6) |
| `crisp-dm` | 18 | `s5-misi` (9), `s5-jatisi` (9) |
| `data latih` | 16 | `s4-transformatika` (11), `s5-misi` (4) |
| `antarmuka` | 16 | `s5-jatisi` (7), `s6-jupiter` (6) |
| `big data` | 13 | `s2-jisebi` (8), `s2-resti` (2) |
| `pembelajaran mesin` | 9 | `s5-misi` (4), `s2-ijccs` (3) |
| `jaringan saraf` | 4 | `s4-jsi` (2), `s4-scan` (1) |
| `basis data` | 6 | `s6-jupiter` (3) |

> Padanan Indonesia (`klasifikasi` 174, `akurasi` 187, `algoritma` 87,
> `prediksi` 94) hidup berdampingan dengan istilah Inggris
> (`classification` 267, `accuracy` 235, `algorithm` 257, `prediction` 118).
> Artikel Indonesia memakai padanan; artikel Inggris memakai istilah asli.

### 12.2 Kolokasi verba (10 artikel berbahasa Indonesia)

| Verba | Kemunculan | Bukti (slug, kemunculan) |
|---|---:|---|
| `menggunakan` | 272 (semua berkas) | `s3-mib` (69), `s4-transformatika` (49) |
| `menunjukkan` | 83 | `s4-transformatika`, `s4-jsi` |
| `menghasilkan` | 73 | `s3-mib`, `s4-transformatika` |
| `melakukan` | 65 | `s4-transformatika`, `s5-jatisi` |
| `menghitung` | 41 | `s6-jupiter` (4), `s4-transformatika` (4) |
| `memberikan` | 39 | — |
| `meningkatkan` | 36 | — |
| `mengukur` | 32 | `s2-jsinbis` (5) |
| `menentukan` | 26 | `s6-jupiter` (3) |
| `memperoleh` | 23 | `s3-mib` (4) |
| `membuat` | 22 | — |
| `bertujuan` | 22 | — |
| `menyebabkan` | 17 | — |
| `menerapkan` | 17 | — |
| `mengevaluasi` | 15 | `s5-misi` (2) |
| `mengklasifikasikan` | 14 | — |
| `menganalisis` | 13 | `s4-transformatika` (5) |
| `mengidentifikasi` | 11 | — |
| `membandingkan` | 11 | — |
| `memprediksi` | 9 | — |
| `mengembangkan` | 8 | — |
| `melatih` | 8 | `s5-misi` (4) |
| `menguji` | 6 | — |
| `membangun` | 6 | `s4-scan` (1), `s5-jatisi` (1) |
| `menyusun` | 5 | — |

### 12.3 Kolokasi frasa (verba + objek)

| Kolokasi | Kemunculan | Bukti (slug, kemunculan) |
|---|---:|---|
| `menggunakan metode` | 50 | `s4-transformatika` (18), `s3-mib` (10), `s5-misi` (5) |
| `menunjukkan bahwa` | 35 | `s4-transformatika` (12), `s4-jsi` (11), `s6-jutik` (6) |
| `menggunakan algoritma` | 28 | `s5-jatisi` (15), `s4-jsi` (3) |
| `menghasilkan akurasi` | 24 | `s3-mib` (10), `s4-transformatika` (9), `s4-jsi` (4) |
| `mengukur kinerja` | 11 | `s2-jsinbis` (5), `s6-jupiter` (2) |
| `melakukan analisis` | 10 | `s4-transformatika` (5), `s6-jupiter` (2) |
| `menghitung nilai` | 10 | `s6-jupiter` (4), `s4-transformatika` (4) |
| `menggunakan data` | 7 | `s5-misi` (3), `s4-jsi` (2) |
| `melatih model` | 6 | `s5-misi` (4), `s4-scan` (1) |
| `memperoleh akurasi` | 5 | `s3-mib` (4), `s4-transformatika` (1) |
| `meningkatkan akurasi` | 4 | `s4-jsi` (3), `s3-mib` (1) |
| `mengevaluasi kinerja` | 4 | `s5-misi` (2), `s5-jatisi` (1) |
| `menentukan kriteria` | 3 | `s6-jupiter` (3) |
| `menghasilkan nilai` | 3 | `s4-transformatika` (2), `s4-scan` (1) |
| `merancang sistem` | 2 | `s5-misi` (1), `s4-scan` (1) |

> Pola dominan: `menggunakan metode/algoritma <X>` → `melatih model` →
> `menghasilkan/memperoleh akurasi` → `menunjukkan bahwa …`. Kolokasi
> spesifik metode: `menggunakan metode support vector` (16, `s2-jti`,
> `s4-sitekin`, `s4-transformatika`, `s6-jutik`), `menggunakan algoritma
> random forest` (15, `s4-jsi`, `s5-jatisi`, `s5-misi`), `menggunakan
> mediapipe hands` (4, `s4-scan`), `menggunakan metode ahp` (4, `s6-jupiter`).

## 13. Pemarkah wacana dan pembuka kalimat

Dihitung atas **10 artikel berbahasa Indonesia** (tabel §1), pencocokan tak
peka huruf besar-kecil.

### 13.1 Konektor/pemarkah wacana

| Pemarkah | Kemunculan | Bukti (slug, kemunculan) |
|---|---:|---|
| `yaitu` | 160 | `s6-jupiter` (36), `s4-transformatika` (28), `s5-jatisi` (24) |
| `sehingga` | 86 | `s3-sistemasi` (23), `s4-scan` (12), `s4-transformatika` (11) |
| `karena` | 84 | `s2-jsinbis` (18), `s3-sistemasi` (18) |
| `berdasarkan` | 75 | `s3-mib` (20), `s4-transformatika` (17) |
| `kemudian` | 67 | `s6-jutik` (29), `s2-jsinbis` (13) |
| `selanjutnya` | 50 | `s6-jupiter` (12), `s2-jsinbis` (10) |
| `sedangkan` | 39 | `s2-jsinbis` (12), `s3-sistemasi` (11) |
| `agar` | 35 | `s6-jutik` (10), `s4-transformatika` (6) |
| `hal ini` | 33 | `s5-jatisi` (14), `s2-jsinbis` (5) |
| `hasil penelitian` | 27 | `s4-scan` (8), `s4-transformatika` (5) |
| `kedua` | 26 | `s3-sistemasi` (10), `s2-jsinbis` (4) |
| `pertama` | 24 | `s2-jsinbis` (6), `s3-sistemasi` (4) |
| `adapun` | 23 | `s5-jatisi` (15), `s2-jsinbis` (4) |
| `namun` | 21 | `s6-jutik` (5), `s3-sistemasi` (4), `s4-jsi` (4) |
| `selain itu` | 19 | `s4-transformatika` (10), `s2-jsinbis` (3) |
| `dapat dilihat pada` | 19 | `s5-jatisi` (9), `s6-jutik` (4) |
| `meskipun` | 13 | `s5-jatisi` (5), `s4-transformatika` (3) |
| `sebagai berikut` | 12 | `s2-jsinbis` (5), `s4-transformatika` (4) |
| `terlihat pada` | 11 | `s6-jupiter` (9) |
| `ketiga` | 10 | `s3-sistemasi` (5), `s3-mib` (2) |
| `misalnya` | 9 | `s3-sistemasi` (3), `s5-jatisi` (3) |
| `sejalan dengan` | 8 | `s3-sistemasi` (5) |
| `dengan demikian` | 8 | `s4-transformatika` (3), `s5-jatisi` (2) |
| `oleh karena itu` | 8 | `s3-mib` (2), `s4-transformatika` (2) |
| `yakni` | 7 | `s3-sistemasi` (3), `s4-transformatika` (2) |
| `disajikan pada` | 7 | `s3-sistemasi` (4), `s3-mib` (2) |
| `guna` (kata utuh) | 6 | tersebar; mayoritas `menggunakan` |
| `lebih lanjut` | 5 | `s5-jatisi` (2) |
| `meskipun demikian` | 4 | `s4-transformatika` (2), `s5-jatisi` (2) |
| `dapat disimpulkan` | 4 | `s2-jsinbis`, `s4-transformatika`, `s6-jupiter`, `s6-jutik` (masing-masing 1) |
| `sementara itu` | 2 | `s4-transformatika` (2) |
| `sebagai contoh` | 2 | `s3-mib` (1), `s5-misi` (1) |
| `namun demikian` | 2 | `s4-jsi` (1), `s6-jutik` (1) |
| `di sisi lain` / `akan tetapi` / `oleh sebab itu` / `walaupun` | 1 each | `s5-jatisi` / `s3-sistemasi` / `s5-misi` / `s3-sistemasi` |

### 13.2 Pembuka kalimat (opener, awal kalimat)

| Pembuka | Kemunculan | Catatan |
|---|---:|---|
| `Pada …` | 67 | rujukan tabel/gambar/waktu |
| `Hasil …` | 65 | rujukan hasil |
| `Gambar …` | 40 | rujukan gambar |
| `Tabel …` | 33 | rujukan tabel |
| `Data …` | 25 | deskripsi data |
| `Penelitian …` | 23 | rujukan penelitian sendiri |
| `Hal …` | 22 | terutama `Hal ini …` (33×) |
| `Dengan …` | 21 | `Dengan demikian …` |
| `Adapun …` | 21 | pembuka enumerasi |
| `Dalam …` | 20 | pembuka konteks |
| `Selain …` | 20 | `Selain itu …` |
| `Setelah …` | 19 | langkah prosedural |
| `Model …` | 19 | deskripsi model |
| `Analisis …` | 19 | `s3-mib` |
| `Berdasarkan …` | 12 | rujukan hasil |
| `Namun …` | 13 | kontras/keterbatasan |
| `Dari …` | 9 | `Dari hasil …` |
| `Selanjutnya …` | 8 | urutan |

> Pembuka khas artikel SI Indonesia adalah **rujukan gambar/tabel**
> (`Pada …`, `Gambar …`, `Tabel …`) dan **rujukan hasil** (`Hasil …`),
> bukan frasa retoris.

## 14. Hedging dan booster

Hitungan atas seluruh 29 berkas; kolom bukti menyebut slug teratas.

### 14.1 Hedging (pelemah klaim)

| Hedging | Kemunculan | Bukti (slug, kemunculan) |
|---|---:|---|
| `cukup` | 27 | `s5-jatisi` (7), `s4-transformatika` (4) |
| `relatif` | 22 | `s6-jupiter` (5), `s4-scan` (5), `s3-sistemasi` (5) |
| `berhasil` | 17 | `s5-misi` (7), `s6-jutik` (5) |
| `cenderung` | 16 | `s4-transformatika` (6), `s5-jatisi` (4) |
| `sering` | 14 | `s6-jutik` (4), `s3-sistemasi` (4) |
| `memungkinkan` | 11 | `s4-jsi` (3), `s4-transformatika` (2) |
| `umumnya` | 10 | `s3-sistemasi` (6) |
| `berpotensi` | 8 | `s4-jsi` (4), `s3-sistemasi` (2) |
| `kemungkinan` | 7 | `s4-scan` (2) |
| `hampir` | 7 | `s3-sistemasi` (5) |
| `tampak` | 5 | `s3-sistemasi` (3), `s4-jsi` (2) |
| `dapat dikatakan` | 5 | `s2-jsinbis` (5) |
| `kecenderungan` | 4 | `s4-transformatika` (3) |
| `dapat disimpulkan` | 4 | `s2-jsinbis`, `s4-transformatika`, `s6-jupiter`, `s6-jutik` |
| `mungkin` | 2 | `s6-jupiter` (1), `s4-jsi` (1) |

### 14.2 Booster (penegas klaim)

| Booster | Kemunculan | Bukti (slug, kemunculan) |
|---|---:|---|
| `sangat` | 35 | `s3-sistemasi` (9), `s6-jutik` (5), `s5-misi` (5) |
| `penting` | 28 | `s6-jupiter` (10), `s3-sistemasi` (4) |
| `perlu` | 23 | `s3-sistemasi` (10), `s6-jutik` (3) |
| `signifikan` | 19 | `s5-jatisi` (9), `s4-jsi` (3) |
| `harus` | 14 | `s2-jsinbis` (9), `s6-jupiter` (2) |
| `nyata` | 9 | `s3-sistemasi` (5), `s4-jsi` (3) |
| `sangat penting` | 3 | `s6-jutik` (1), `s6-jupiter` (1), `s2-ijccs` (1) |
| `jelas` | 2 | `s5-misi` (1), `s4-jsi` (1) |
| `mutlak` | 1 | `s3-sistemasi` (1) |
| `tentu` (kata utuh) | 0 | absen (semua kemunculan `tentunya`/`tentukan`) |
| `pasti` | 0 | absen (kata utuh) |
| `wajib` | 0 | absen |
| `krusial` | 0 | absen |

> Seperti korpus HI, gaya SI lebih memilih **hedging** (`cenderung`, `relatif`,
> `umumnya`, `berpotensi`) daripada booster absolut; `sangat krusial`,
> `krusial`, `wajib` praktis absen.

## 15. Tipografi dan gaya penulisan korpus

| Ciri | Hitungan | Contoh / bukti |
|---|---:|---|
| Tanda persen `%` | 991 (semua 29 berkas) | `73,57%`, `68,57%` (`s3-mib`); `21,85%` (`s5-jatisi`) |
| Kata `persen` | 1 | hanya `s3-sistemasi` — jadi `%` sangat dominan |
| Desimal **koma** (ID) | 476 (10 artikel ID) | `73,57%` (`s3-mib`) |
| Desimal **titik** (ID) | 1262 (10 artikel ID) | nomor/versi/angka tabel |
| Em dash `—` | 43 (semua berkas) | `intervention—limiting their practicality` (`s1-register`) |
| En dash `–` | 636 | rentang halaman/sitasi |
| Tanda kutip melengkung `“…”` | 194 | `s2-jisebi` (48), `s2-ilkom` (16) |
| Tanda kutip lurus `"…"` | 85 | `s2-jisebi` (18), `s4-sitekin` (14) |
| `et al.` | 265 | `s3-jsi-ui` (41), `s2-jtie` (39), `s3-sinkron` (37) |
| Penanda daftar pustaka `doi` | 716 | `s3-sinkron` (65), `s1-register` (63) |
| Penanda daftar pustaka `Retrieved` | 10 | `s2-resti` (9) |
| Penanda daftar pustaka `diakses` | 5 | `s5-misi` (2), `s4-scan` (2) |
| `Tiongkok` / `Cina` | 0 / 0 | absen (bidang komputasi, bukan HI) |

Catatan gaya terattestasi:

- **Persen & desimal**: artikel Indonesia memakai simbol `%` menempel angka
  dengan **koma** desimal (`73,57%`, `s3-mib`); kata `persen` hanya 1× di
  seluruh korpus. Artikel Inggris memakai titik (`95.5%`).
- **Tanda kutip**: kutipan langsung memakai tanda melengkung `“…”` (194×);
  tanda lurus (85×) umumnya muncul di potongan kode/URL, bukan prosa.
- **Istilah teknis Inggris** dibiarkan verbatim (`dataset` 396, `model` 1034,
  `machine learning` 135), termasuk singkatan (`KNN` 12, `IoT` 7).
- **Daftar pustaka**: `doi` (716×) jauh mendominasi penanda akses; `diakses`
  (5×) jarang — berbeda dari korpus HI yang banyak memakai `diakses` (112×).
- **Tidak ada** toponimi `Tiongkok`/`Cina` di korpus SI (bidang komputasi).

## 16. Frasa AI-generik yang absen dari korpus SI

Diuji atas seluruh 29 berkas (`pdftotext -layout`, pencocokan tak peka huruf
besar-kecil). Frasa bertanda **0** tidak dipakai penulis jurnal Sinta — bukti
bahwa frasa itu bukan gaya korpus.

| Frasa diuji | Kemunculan | Catatan |
|---|---:|---|
| `dalam era digital saat ini` | 0 | absen |
| `seiring dengan perkembangan zaman` | 0 | absen |
| `tidak dapat dipungkiri` | 0 | absen |
| `perlu dicatat bahwa` | 0 | absen |
| `penting untuk dicatat bahwa` | 0 | absen |
| `pada akhirnya` | 0 | absen |
| `secara keseluruhan` | 4 | `s5-jatisi` (4) |
| `dalam konteks ini` | 0 | absen |
| `dengan kata lain` | 0 | absen |
| `pada dasarnya` | 2 | `s6-jutik` (1), `s3-mib` (1) |
| `memainkan peran penting` | 1 | `s5-jatisi` (1) |
| `memiliki peran penting` | 0 | absen |
| `dalam rangka untuk` | 0 | absen |
| `sangat krusial` | 0 | absen |
| `kompleks dan beragam` | 0 | absen |
| `sebagai kesimpulan` | 0 | absen |

Kesimpulan §16: **13 dari 16** frasa uji berjumlah 0 di seluruh korpus SI.
Tiga frasa sisanya muncul sangat sporadis (1–4×, terpusat pada satu artikel),
sehingga tidak dapat disebut "gaya korpus". Karena itu daftar
`frasa_ai_generik` di kamus **tidak** bertabrakan dengan gaya SI nyata.
