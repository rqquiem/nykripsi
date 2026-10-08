# Riset Korpus: Struktur Artikel Jurnal Hubungan Internasional (HI/IR)

Riset ini menurunkan "kamus struktur" artikel jurnal dari PDF asli di
[`docs/ir-corpus/`](ir-corpus/) (jurnal Hubungan Internasional Indonesia dan
internasional). Setiap klaim di bawah menyebut **slug** berkas yang menjadi
bukti. Kamus mesin yang diperkaya hasil riset ini ada di
[`assets/bahasa/kamus-id.yaml`](../assets/bahasa/kamus-id.yaml); dokumen
turunan manusia ada di [`kamus-bahasa-artikel.md`](kamus-bahasa-artikel.md).

## Sumber

- Berkas: `docs/ir-corpus/<slug>.pdf` (**43 PDF** terverifikasi, lihat
  [`docs/ir-corpus/MANIFEST.md`](ir-corpus/MANIFEST.md)).
- Ekstraksi: `pdftotext -layout <pdf> -` (tanpa pandoc). Tidak ada berkas
  korpus yang diubah oleh riset ini.
- Komposisi: **22 artikel jurnal internasional** (`international`) dan
  **21 artikel jurnal Indonesia** (`national`), sesuai kolom `tier` pada
  `docs/ir-corpus/manifest.tsv`.
- Bahasa (deteksi berbasis skrip + rasio kata fungsi; lihat kolom "Bahasa"
  pada tabel §1):
  - **Inggris (30)**: `hi-atlantis-china-asea-pd`, `hi-bath-china-softpower`,
    `hi-bournemouth-nation-branding`, `hi-cjas-southeast-asia`,
    `hi-coventry-softpower-china`, `hi-david-palestinian-nation-branding`,
    `hi-gfpr-us-china-softpower`, `hi-hrmars-vaccine-softpower`,
    `hi-ieom-istanbul-vaccine`, `hi-ieom-rome-vaccine`, `hi-ijss-vtuber`,
    `hi-interaksi-g20`, `hi-irscs-bahasa`, `hi-janus-health-diplomacy`,
    `hi-jelajah-tourism`, `hi-jgs-japan-pd`, `hi-jhi-netherlands-vaccine`,
    `hi-jhi-umy-free-active-vaccine`, `hi-jhi-umy-vaccine-politics`,
    `hi-jiir-uinsa`, `hi-jiwp-korea-week`, `hi-jpr-nation-branding`,
    `hi-jsgs-korean-cuisine`, `hi-jsps-aviation`, `hi-mdpi-health-silk-road`,
    `hi-ndu-pakistan-nation-branding`, `hi-ph-china-foreign-policy`,
    `hi-reinvention-vaccine`, `hi-richtmann-japan-vaccine`,
    `hi-ssr-geopolitics-vaccine`
  - **Indonesia (8)**: `hi-dinamika-bali-democracy`,
    `hi-jhi-umy-konstruktivis`, `hi-jhi-umy-malaysia`, `hi-jhi-vanuatu`,
    `hi-padjir-asian-games`, `hi-padjir-desa-wisata`, `hi-padjir-wisatawan`,
    `hi-sentris-asian-games`
  - **Rusia (2)**: `hi-ivran-mask-diplomacy`, `hi-mgimo-health-silk-road`
  - **Vietnam (2)**: `hi-stdjssh-health-silk-road-sea`,
    `hi-stdjssh-japan-vaccine`
  - **Mandarin (1)**: `hi-brunel-softpower` (halaman awal berbahasa Mandarin)

> Catatan operasional: `hi-mdpi-health-silk-road` menyajikan 403 pada unduhan
> langsung sehingga diambil lewat Wayback Machine; `hi-jhi-umy-malaysia` dan
> `hi-jhi-umy-konstruktivis` (host `journal.umy.ac.id`) sempat membalas HTTP
> 522 (Cloudflare) dan diambil lewat Wayback Machine. Semua berkas kini PDF
> valid.

## 1. Temuan per-paper

| Slug | Bahasa | Kepala bagian tingkat-1 (verbatim) | Skema nomor | Label abstrak | Label kata kunci | Label simpulan | Gaya sitasi | Daftar pustaka |
|---|---|---|---|---|---|---|---|---|
| `hi-atlantis-china-asea-pd` | EN | `Abstract`, `1. Introduction`, `References` | `N.` + `N.M.` | `Abstract` | `Keywords:` | — | numerik `[1]` | bernomor, 5+ entri |
| `hi-bath-china-softpower` | EN | `24 Conclusions`, `48 Bibliography` | `N` (nomor baris PDF) | — (tanpa label) | `Keyword:` | `24 Conclusions` | APA | `Bibliography`, ~48 entri |
| `hi-bournemouth-nation-branding` | EN | `Abstract:`, `References:` | tanpa nomor | `Abstract:` | — | — | APA | `References:`, 19 entri |
| `hi-brunel-softpower` | ZH | — (halaman ringkas, tanpa kepala bernomor) | tanpa nomor | — (berbahasa Mandarin) | — | — | — | — |
| `hi-cjas-southeast-asia` | EN | `Abstract`, `Introduction`, `Conclusion`, `REFERENCES:` | tanpa nomor | `Abstract` | `Keywords:` | `Conclusion` | APA | `REFERENCES:`, ~55 entri |
| `hi-coventry-softpower-china` | EN | `Introduction` | tanpa nomor | — (tanpa label) | — | — | APA | — (tanpa daftar pustaka) |
| `hi-david-palestinian-nation-branding` | EN | `Introduction`, `Conclusion`, `References` | tanpa nomor | — (tanpa label) | `Keywords:` | `Conclusion` | APA | `References`, ~8 entri |
| `hi-dinamika-bali-democracy` | ID | `Abstract`, `PENDAHULUAN`, `PEMBAHASAN`, `KESIMPULAN`, `DAFTAR PUSTAKA` | tanpa nomor (kapital) | `Abstract` | `Keywords:` | `KESIMPULAN` | APA | `DAFTAR PUSTAKA`, ~51 entri |
| `hi-gfpr-us-china-softpower` | EN | `Abstract`, `Introduction`, `Literature Review`, `Conclusion`, `References` | tanpa nomor | `Abstract` | `Keywords:` | `Conclusion` | APA | `References`, ~13 entri |
| `hi-hrmars-vaccine-softpower` | EN | `Abstract`, `Introduction`, `Conclusions`, `References` | tanpa nomor | `Abstract` | `Keywords:` | `Conclusions` | APA | `References`, ~31 entri |
| `hi-ieom-istanbul-vaccine` | EN | `Abstract`, `Keyword:` (prosiding singkat) | tanpa nomor | `Abstract` | `Keyword:` | — | — | — (prosiding singkat) |
| `hi-ieom-rome-vaccine` | EN | `Abstract`, `Keywords` (prosiding singkat) | tanpa nomor | `Abstract` | `Keywords` | — | — | — (prosiding singkat) |
| `hi-ijss-vtuber` | EN | `INTRODUCTION`, `METHOD`, `CONCLUSION` | tanpa nomor (kapital) | `ABSTRACT:` | `Keywords:` | `CONCLUSION` | APA | `REFERENCES`, ~40 entri |
| `hi-interaksi-g20` | EN | `Abstrak`, `Abstract`, `Introduction`, `Conclusion`, `References` | tanpa nomor | `Abstrak` + `Abstract` | `Keywords:` | `Conclusion` | APA | `References`, ~70 entri |
| `hi-irscs-bahasa` | EN | `Abstract`, `1. Introduction`, `2. Literature Review`, `3. Methods`, `4. Results and Discussion`, `5. Conclusion`, `6. References` | `N.` + `N.M.` | `Abstract` | `Keywords:` | `5. Conclusion` | APA | `6. References`, ~19 entri |
| `hi-ivran-mask-diplomacy` | RU | `Аннотация:`, `Ключевые слова:` | tanpa nomor | `Аннотация:` | `Ключевые слова:` / `Keywords:` | — | numerik catatan akhir | catatan akhir bernomor, 11 entri |
| `hi-janus-health-diplomacy` | EN | `Abstract`, `Introduction`, `Methodology`, `References` | tanpa nomor | `Abstract` | `Keywords` | — | APA | `References`, ~76 entri |
| `hi-jelajah-tourism` | EN | `Abstract`, `INTRODUCTION`, `RESEARCH METHODS`, `CONCLUSION`, `REFERENCES` | tanpa nomor (kapital) | `Abstract` | `Keywords:` | `CONCLUSION` | APA | `REFERENCES`, ~35 entri |
| `hi-jgs-japan-pd` | EN | `ABSTRACT`, `Conclusion`, `Acknowledgement`, `References` | tanpa nomor | `ABSTRACT` | `Keywords:` | `Conclusion` | APA | `References`, ~39 entri |
| `hi-jhi-netherlands-vaccine` | EN | `Abstrak`, `Abstract`, `Introduction`, `Research methods`, `Theoretical Framework`, `Results and Discussion`, `Conclusion`, `References` | tanpa nomor | `Abstrak` + `Abstract` | `Kata Kunci:` + `Keywords:` | `Conclusion` | APA | `References`, ~50 entri |
| `hi-jhi-umy-free-active-vaccine` | EN | `Abstrak`, `Abstract`, `INTRODUCTION`, `CONCLUSION` | tanpa nomor | `Abstrak` + `Abstract` | `Kata kunci:` + `Keywords:` | `CONCLUSION` | APA | `REFERENCES`, ~27 entri |
| `hi-jhi-umy-konstruktivis` | ID | `Abstract`, `Abstrak`, `PENDAHULUAN`, `KESIMPULAN` | `N.` + `N.M.` | `Abstrak` + `Abstract` | `Kata kunci:` + `Keywords:` | `KESIMPULAN` | APA | `REFERENCES`, ~21 entri |
| `hi-jhi-umy-malaysia` | ID | `Abstract`, `Abstrak`, `PENDAHULUAN`, `PEMBAHASAN`, `KESIMPULAN`, `REFERENSI` | tanpa nomor | `Abstrak` + `Abstract` | `Kata Kunci:` + `Keywords:` | `KESIMPULAN` | APA | `REFERENSI`, ~40 entri |
| `hi-jhi-umy-vaccine-politics` | EN | `Abstrak`, `Abstract`, `INTRODUCTION`, `CONCLUSION` | tanpa nomor | `Abstrak` + `Abstract` | `Kata Kunci:` + `Keywords:` | `CONCLUSION` | APA | `REFERENCES`, ~25 entri |
| `hi-jhi-vanuatu` | ID | `Abstrak`, `Kesimpulan:`, `Referensi` | tanpa nomor | `Abstrak` | `Kata kunci:` + `Keywords:` | `Kesimpulan:` | APA | `Referensi`, ~16 entri |
| `hi-jiir-uinsa` | EN | `Abstract`, `Conclusion`, `References` | `N.` + `N.M.` | `Abstract` | `Keywords:` | `Conclusion` | APA | `References`, ~19 entri |
| `hi-jiwp-korea-week` | EN | `Abstract`, `Abstrak`, `INTRODUCTION`, `RESULTS AND DISCUSSION`, `CONCLUSION`, `REFERENCES` | tanpa nomor | `Abstract` + `Abstrak` | `Kata Kunci:` + `Keywords:` | `CONCLUSION` | APA | `REFERENCES`, ~13 entri |
| `hi-jpr-nation-branding` | EN | `Abstract`, `1.0 INTRODUCTION`, `2.0 LITERATURE REVIEW`, `3.0 METHODOLOGY`, `4.0 FINDINGS`, `5.0 CONCLUSION AND RECOMMENDATIONS`, `REFERENCES` | `N.0` + `N.M` | `Abstract` | `Keywords:` | `5.0 CONCLUSION AND RECOMMENDATIONS` | APA | `REFERENCES`, ~38 entri |
| `hi-jsgs-korean-cuisine` | EN | `Abstract:`, `Abstrak:`, `INTRODUCTION`, `METHODS`, `RESULTS AND DISCUSSIONS`, `CONCLUSIONS`, `Bibliography` | tanpa nomor (kapital) | `Abstract:` + `Abstrak:` | `Kata Kunci:` + `Keywords:` | `CONCLUSIONS` | APA | `Bibliography`, ~44 entri |
| `hi-jsps-aviation` | EN | `Abstract :`, `INTRODUCTION`, `METHOD`, `CONCLUSION`, `REFERENCES` | tanpa nomor (kapital) | `Abstract :` | `KEYWORDS :` | `CONCLUSION` | APA | `REFERENCES`, ~36 entri |
| `hi-mdpi-health-silk-road` | EN | `Abstract:`, `1. Introduction` … `7. Conclusions`, `References` | `N.` + `N.M.` | `Abstract:` | `Keywords:` | `7. Conclusions` | numerik `[1]` | `References`, ~53 entri |
| `hi-mgimo-health-silk-road` | RU | `Abstract:`, `Conclusion`, `References / Список литературы:` | tanpa nomor | `Abstract:` | `Ключевые слова:` / `Keywords:` | `Conclusion` | APA | `References`, ~5 entri |
| `hi-ndu-pakistan-nation-branding` | EN | `Abstract`, `Conclusion`, `References` | tanpa nomor | `Abstract` | `Keywords:` | `Conclusion` | numerik `[1]` | `References`, ~34 entri |
| `hi-padjir-asian-games` | ID | `PENDAHULUAN`, `METODE RISET`, `HASIL DAN PEMBAHASAN`, `KESIMPULAN`, `DAFTAR PUSTAKA` | tanpa nomor (kapital) | `ABSTRACT` + `ABSTRAK` | `Kata Kunci` + `Keywords` | `KESIMPULAN` | APA | `DAFTAR PUSTAKA`, ~19 entri |
| `hi-padjir-desa-wisata` | ID | `PENDAHULUAN`, `METODE RISET`, `KESIMPULAN`, `DAFTAR PUSTAKA` | tanpa nomor (kapital) | `ABSTRACT` + `ABSTRAK` | `Kata Kunci` + `Keywords` | `KESIMPULAN` | APA | `DAFTAR PUSTAKA`, ~37 entri |
| `hi-padjir-wisatawan` | ID | `PENDAHULUAN`, `METODE RISET`, `HASIL DAN PEMBAHASAN`, `KESIMPULAN`, `DAFTAR PUSTAKA` | tanpa nomor (kapital) | `ABSTRACT` + `ABSTRAK` | `Kata Kunci` + `Keywords` | `KESIMPULAN` | APA | `DAFTAR PUSTAKA`, ~16 entri |
| `hi-ph-china-foreign-policy` | EN | `Abstract`, `BIBLIOGRAPHY` | tanpa nomor | `Abstract` | `Keywords:` | `D. CONCLUSION` | APA | `BIBLIOGRAPHY`, ~24 entri |
| `hi-reinvention-vaccine` | EN | `References` (esai, tanpa kepala bernomor) | tanpa nomor | — (esai, tanpa label) | — | — | APA | `References`, ~23 entri |
| `hi-richtmann-japan-vaccine` | EN | `Abstract`, `1. Introduction`, `2. Literature Review`, `3. Methodology`, `5. Discussion`, `6. Conclusion`, `References` | `N.` + `N.M.` | `Abstract` | `Keywords:` | `6. Conclusion` | APA | `References`, ~45 entri |
| `hi-sentris-asian-games` | ID | `ABSTRAK`, `ABSTRACT`, `Latar Belakang`, `Metodologi Penelitian`, `Landasan Teori`, `Analisis`, `Kesimpulan`, `DAFTAR PUSTAKA` | tanpa nomor (kapital) | `ABSTRAK` + `ABSTRACT` | `Kata Kunci:` + `Keywords:` | `Kesimpulan` | APA | `DAFTAR PUSTAKA`, ~63 entri |
| `hi-ssr-geopolitics-vaccine` | EN | `Abstract`, `Introduction`, `Literature Review`, `Findings`, `Discussion`, `Conclusion` | tanpa nomor | `Abstract` | `Keywords:` | `Conclusion` | APA | `References`, ~60 entri |
| `hi-stdjssh-health-silk-road-sea` | VI | `TÓM TẮT`, `ABSTRACT` (berbahasa Vietnam) | `N.` | `TÓM TẮT` + `ABSTRACT` | `Từ khoá:` | `KẾT LUẬN` | numerik `[1]` | `TÀI LIỆU THAM KHẢO`, bernomor |
| `hi-stdjssh-japan-vaccine` | VI | `TÓM TẮT`, `ABSTRACT` (berbahasa Vietnam) | `N.` | `TÓM TẮT` + `ABSTRACT` | `Từ khoá:` | `KẾT LUẬN` | numerik `[1]` | `TÀI LIỆU THAM KHẢO`, bernomor |

### Catatan struktur penting

- **Skema penomoran tingkat-1**: **8 paper** memakai Arab `N.`
  (`hi-atlantis-china-asea-pd`, `hi-irscs-bahasa`, `hi-jhi-umy-konstruktivis`,
  `hi-jiir-uinsa`, `hi-mdpi-health-silk-road`, `hi-richtmann-japan-vaccine`,
  `hi-stdjssh-health-silk-road-sea`, `hi-stdjssh-japan-vaccine`); **1 paper**
  memakai desimal `N.0` (`hi-jpr-nation-branding` `1.0`–`5.0` + `5.1`);
  **1 paper** memakai nomor baris PDF (`hi-bath-china-softpower`); sisanya
  **tanpa nomor** (33), dengan 8 di antaranya memakai judul **KAPITAL**
  (`hi-dinamika-bali-democracy`, `hi-ijss-vtuber`, `hi-jelajah-tourism`,
  `hi-jsps-aviation`, `hi-padjir-asian-games`,
  `hi-padjir-desa-wisata`, `hi-padjir-wisatawan`, `hi-sentris-asian-games`).
- **Subbagian** umumnya `N.M.` (`hi-irscs-bahasa` `4.2`, `hi-jpr-nation-branding`
  `5.1`); `hi-mdpi-health-silk-road` turun ke `N.M.K` (`2.1.`, `2.2.`).
- **Kepala bagian yang paling sering muncul** (level-1, penanda baris
  terpisah; lihat §2 untuk hitungan): `PENDAHULUAN` / `Introduction` (28/43),
  `KESIMPULAN` / `Conclusion` (29/43), `DAFTAR PUSTAKA` / `References`
  (31/43), `METODE` / `Method(s)` / `METODOLOGI` (13/43).
- **Tinjauan pustaka berdiri sendiri** pada **7 paper**:
  `hi-gfpr-us-china-softpower`, `hi-jhi-netherlands-vaccine`
  (`Theoretical Framework`), `hi-irscs-bahasa`, `hi-jpr-nation-branding`,
  `hi-richtmann-japan-vaccine`, `hi-sentris-asian-games` (`Landasan Teori`),
  `hi-ssr-geopolitics-vaccine`.
- **Pola khas jurnal HI Indonesia**: `PENDAHULUAN` → `METODE RISET` (bukan
  `Metode Penelitian`) → `HASIL DAN PEMBAHASAN` → `KESIMPULAN` → `DAFTAR
  PUSTAKA`, judul KAPITAL tanpa nomor (`hi-padjir-asian-games`,
  `hi-padjir-desa-wisata`, `hi-padjir-wisatawan`). `hi-sentris-asian-games`
  memakai `Latar Belakang`/`Landasan Teori`/`Analisis` (bukan
  Pendahuluan/Tinjauan/Hasil).
- **Simpulan** kadang diberi label berbeda: `Kesimpulan:` (`hi-jhi-vanuatu`),
  `KESIMPULAN` (`hi-dinamika-bali-democracy`, `hi-jhi-umy-konstruktivis`,
  `hi-jhi-umy-malaysia`, `hi-padjir-asian-games`, `hi-padjir-desa-wisata`, `hi-padjir-wisatawan`), `KẾT LUẬN` (Vietnam,
  `hi-stdjssh-health-silk-road-sea`, `hi-stdjssh-japan-vaccine`), `D. CONCLUSION` (`hi-ph-china-foreign-policy`),
  `5.0 CONCLUSION AND RECOMMENDATIONS` (`hi-jpr-nation-branding`), atau tanpa
  kepala simpulan eksplisit (`hi-atlantis-china-asea-pd`,
  `hi-bournemouth-nation-branding`, `hi-coventry-softpower-china`,
  `hi-ieom-istanbul-vaccine`, `hi-ieom-rome-vaccine`, `hi-ivran-mask-diplomacy`, `hi-janus-health-diplomacy`,
  `hi-reinvention-vaccine`).
- **Ucapan terima kasih** eksplisit hanya pada `hi-jgs-japan-pd`
  (`Acknowledgement`).

## 2. Frekuensi label kepala bagian (43 paper)

Angka di bawah dihitung dari kolom "Kepala bagian tingkat-1" pada tabel §1
(penanda judul yang terpisah baris; beberapa paper prosiding/esai tidak
memuat kepala bernomor).

| Keluarga seksi | Jumlah paper | Judul yang teramati |
|---|---|---|
| Pendahuluan | 28/43 | `PENDAHULUAN`, `Pendahuluan`, `INTRODUCTION`, `Introduction`, `1. Introduction`, `1.0 INTRODUCTION`, `Latar Belakang` |
| Metode | 13/43 | `METODE`, `METODE RISET`, `Metodologi Penelitian`, `METODOLOGI`, `Method`, `METHOD`, `Methods`, `Methodology`, `RESEARCH METHODS`, `Research methods`, `3.0 METHODOLOGY` |
| Hasil/Pembahasan | 12/43 | `HASIL DAN PEMBAHASAN`, `PEMBAHASAN`, `ANALISIS`, `Results and Discussion`, `RESULTS AND DISCUSSIONS`, `DISCUSSION`, `Discussion`, `Findings`, `4.0 FINDINGS` |
| Simpulan | 29/43 | `KESIMPULAN`, `Kesimpulan`, `Kesimpulan:`, `CONCLUSION`, `Conclusion`, `Conclusions`, `CONCLUSIONS`, `7. Conclusions`, `5.0 CONCLUSION AND RECOMMENDATIONS`, `KẾT LUẬN`, `D. CONCLUSION` |
| Tinjauan pustaka/teori | 7/43 | `LITERATURE REVIEW`, `Literature Review`, `Theoretical Framework`, `Landasan Teori`, `2.0 LITERATURE REVIEW` |
| Ucapan terima kasih | 1/43 | `Acknowledgement` (`hi-jgs-japan-pd`) |
| Daftar Pustaka | 31/43 | `DAFTAR PUSTAKA`, `Referensi`, `REFERENSI`, `References`, `REFERENCES:`, `Bibliography`, `BIBLIOGRAPHY`, `TÀI LIỆU THAM KHẢO`, `Список литературы` |

> Sebagian paper (mis. `hi-jgs-japan-pd`, `hi-jiir-uinsa`,
> `hi-ndu-pakistan-nation-branding`, `hi-ph-china-foreign-policy`,
> `hi-ieom-istanbul-vaccine`, `hi-ieom-rome-vaccine`) menggabungkan kepala
> bagian ke dalam alur naratif tanpa baris judul terpisah, sehingga tidak
> terhitung pada tabel di atas meski strukturnya lengkap.

## 3. Gaya abstrak dan kata kunci

- **Label abstrak** (43 paper): `Abstract` (paling banyak), `ABSTRACT`,
  `Abstrak`, `ABSTRAK`, `Abstract:`/`Abstract :`, `Abstract.`, `ABSTRACT:`,
  `Аннотация:` (Rusia), `TÓM TẮT` (Vietnam). **14 paper** memuat abstrak
  **dua bahasa** (Indonesia/Inggris atau Vietnam/Inggris):
  `hi-interaksi-g20`, `hi-jhi-netherlands-vaccine`,
  `hi-jhi-umy-free-active-vaccine`, `hi-jhi-umy-konstruktivis`,
  `hi-jhi-umy-malaysia`, `hi-jhi-umy-vaccine-politics`, `hi-jiwp-korea-week`,
  `hi-jsgs-korean-cuisine`, `hi-padjir-asian-games`, `hi-padjir-desa-wisata`,
  `hi-padjir-wisatawan`, `hi-sentris-asian-games`,
  `hi-stdjssh-health-silk-road-sea`, `hi-stdjssh-japan-vaccine`.
- **Label kata kunci**: `Keywords:` (paling banyak), `Keyword:`,
  `KEYWORDS :`, `Kata Kunci:`, `Kata kunci:`, `Kata Kunci` (tanpa titik dua),
  `Ключевые слова:`, `Từ khoá:`. Pemisah kata kunci umumnya **koma**;
  titik koma dipakai sebagian paper Indonesia (`hi-jiwp-korea-week`,
  `hi-sentris-asian-games`).
- **Panjang abstrak** (perkiraan kata, 35 paper berabstrak terdeteksi): rentang
  **91–484 kata**; **25/35 (71%)** berada di **100–250 kata**, sedangkan 9
  melampaui 250 kata. Terpendek `hi-sentris-asian-games` (~91), terpanjang
  `hi-bournemouth-nation-branding` (~484) dan `hi-interaksi-g20` (~438).
- **Struktur abstrak**: umumnya satu paragraf naratif
  (latar belakang → tujuan → metode → hasil → simpulan). Abstrak terstruktur
  berlabel hanya `hi-jpr-nation-branding` (`Methodology:` / `Findings:`).
- **Tanpa sitasi** di dalam abstrak (semua paper).

## 4. Gaya sitasi dan daftar pustaka

| Gaya | Jumlah paper | Paper |
|---|---:|---|
| **APA name-year** `(Author, year)` + daftar pustaka alfabetis | 34 | `hi-bath-china-softpower`, `hi-bournemouth-nation-branding`, `hi-cjas-southeast-asia`, `hi-coventry-softpower-china`, `hi-david-palestinian-nation-branding`, `hi-dinamika-bali-democracy`, `hi-gfpr-us-china-softpower`, `hi-hrmars-vaccine-softpower`, `hi-ijss-vtuber`, `hi-interaksi-g20`, `hi-irscs-bahasa`, `hi-janus-health-diplomacy`, `hi-jelajah-tourism`, `hi-jgs-japan-pd`, `hi-jhi-netherlands-vaccine`, `hi-jhi-umy-free-active-vaccine`, `hi-jhi-umy-konstruktivis`, `hi-jhi-umy-malaysia`, `hi-jhi-umy-vaccine-politics`, `hi-jhi-vanuatu`, `hi-jiir-uinsa`, `hi-jiwp-korea-week`, `hi-jpr-nation-branding`, `hi-jsgs-korean-cuisine`, `hi-jsps-aviation`, `hi-mgimo-health-silk-road`, `hi-padjir-asian-games`, `hi-padjir-desa-wisata`, `hi-padjir-wisatawan`, `hi-ph-china-foreign-policy`, `hi-reinvention-vaccine`, `hi-richtmann-japan-vaccine`, `hi-sentris-asian-games`, `hi-ssr-geopolitics-vaccine` |
| **Numerik kurung** `[1]`, `[7]–[9]` + daftar pustaka bernomor | 6 | `hi-atlantis-china-asea-pd`, `hi-mdpi-health-silk-road`, `hi-ndu-pakistan-nation-branding`, `hi-stdjssh-health-silk-road-sea`, `hi-stdjssh-japan-vaccine`, `hi-ivran-mask-diplomacy` (catatan akhir) |
| — (tanpa sitasi/daftar pustaka) | 3 | `hi-brunel-softpower`, `hi-ieom-istanbul-vaccine`, `hi-ieom-rome-vaccine` |

- **Rentang jumlah entri daftar pustaka**: ~5 (`hi-mgimo-health-silk-road`)
  hingga ~76 (`hi-janus-health-diplomacy`); mayoritas **15–60 entri**.
- Nama seksi daftar pustaka bervariasi: `DAFTAR PUSTAKA` (Indonesia),
  `REFERENSI`/`Referensi` (`hi-jhi-umy-malaysia`, `hi-jhi-vanuatu`),
  `References`/`REFERENCES`, `Bibliography`/`BIBLIOGRAPHY`
  (`hi-bath-china-softpower`, `hi-jsgs-korean-cuisine`,
  `hi-ph-china-foreign-policy`), `TÀI LIỆU THAM KHẢO` (Vietnam).

> **Penting untuk build repo**: build artikel/skripsi repo ini memakai
> **APA name-year** (`assets/csl/apa.csl`, `--citeproc`). Gaya numerik
> adalah varian korpus, **bukan** gaya build. Karena itu kamus mencatat
> keduanya tetapi tidak mengubah gaya default.

## 5. Frekuensi konektor (8 paper berbahasa Indonesia)

| Konektor | Jumlah | Konektor | Jumlah |
|---|---:|---|---:|
| karena | 130 | berdasarkan | 28 |
| yaitu | 86 | sejalan dengan | 18 |
| hal ini | 67 | dengan demikian | 17 |
| selain itu | 52 | meskipun | 16 |
| sehingga | 48 | oleh karena itu | 6 |
| agar | 39 | sementara itu | 6 |
| namun | 36 | adapun | 4 |
| sedangkan | 33 | dapat dilihat pada | 3 |

Konektor yang **sudah** ada di kamus dan terkonfirmasi di korpus HI: `yaitu`,
`sehingga`, `karena`, `berdasarkan`, `selain itu`, `dengan demikian`, `namun`,
`sedangkan`, `agar`, `adapun`, `oleh karena itu`, `meskipun`, `hal ini`,
`dapat dilihat pada`, `sementara itu`, `sejalan dengan`. **Tidak ada konektor
baru** yang perlu ditambahkan dari korpus HI (semua sudah terdaftar).

## 6. Frekuensi kolokasi verba (8 paper berbahasa Indonesia, lemma)

| Verba | Jumlah | Verba | Jumlah |
|---|---:|---|---:|
| meningkatkan | 90 | menjelaskan | 14 |
| menunjukkan | 54 | memengaruhi | 14 |
| membangun | 50 | berperan | 13 |
| menggunakan | 39 | bertujuan | 12 |
| melibatkan | 22 | memperkuat | 10 |

Kolokasi/verba teramati yang layak dicatat (dengan sumber): `diplomasi publik`
(431×, 14 paper), `kepentingan nasional` (62×, 7 paper), `kerja sama` (35×,
8 paper), `kebijakan luar negeri` (19×, 10 paper), `membangun citra` (4×,
`hi-jhi-umy-konstruktivis`, `hi-sentris-asian-games`,
`hi-jsgs-korean-cuisine`, `hi-dinamika-bali-democracy`), `persepsi publik`
(4×, `hi-jhi-umy-malaysia`, `hi-jhi-vanuatu`), `diplomasi vaksin` (9×,
`hi-jhi-umy-free-active-vaccine`, `hi-jhi-netherlands-vaccine`),
`menunjukkan bahwa` (22×), `menggunakan metode` (6×), `berperan penting` (1×),
`bertujuan untuk` (8×), `menganalisis` (9×).

## 7. "Argument moves" yang teramati (konvensi HI/IR)

### Pendahuluan
`konteks/objek` → `masalah` → `kajian terdahulu` → `celah/tujuan`.
Contoh `hi-jhi-umy-free-active-vaccine`: konteks kebijakan luar negeri bebas
aktif → masalah pandemi → `INTRODUCTION` → tujuan menganalisis diplomasi
vaksin Indonesia. Contoh `hi-padjir-wisatawan`: konteks pariwisata →
`PENDAHULUAN` → tujuan menjelaskan peran diplomasi publik. Penanda tujuan:
`Artikel ini bertujuan menjelaskan …` (`hi-padjir-desa-wisata`), `Penelitian
ini bertujuan untuk …` (`hi-jhi-umy-free-active-vaccine`, `hi-jhi-umy-vaccine-politics`), `This article examines …`
(`hi-reinvention-vaccine`), `This paper examines the strategies …`
(`hi-ieom-rome-vaccine`).

### Metode
`jenis/pendekatan` → `sumber data` → `teknik analisis`. Hampir semua paper HI
memakai **kualitatif deskriptif** atau **studi pustaka**: `METODE RISET`
(`hi-padjir-asian-games`, `hi-padjir-desa-wisata`, `hi-padjir-wisatawan`), `Research methods` (`hi-jhi-netherlands-vaccine`), `uses
descriptive qualitative methods` (`hi-ieom-rome-vaccine`), `desktop research
methodology` (`hi-jpr-nation-branding`), `qualitative method in term of
interpretivism` (`hi-padjir-desa-wisata`). Pembuka teramati: `Metode yang
digunakan dalam penelitian ini adalah …`, `This article uses qualitative
method …`.

### Hasil dan pembahasan
`rujuk kasus/data` → `analisis` → `interpretasi`. Contoh
`hi-padjir-asian-games`: `HASIL DAN PEMBAHASAN` → analisis tiga lapis
diplomasi publik → `Hasil penelitian ini menunjukkan bahwa …`. Contoh
`hi-jhi-netherlands-vaccine`: `Results and Discussion` → analisis diplomasi
vaksin Belanda. Penanda interpretasi: `Hasil penelitian ini menunjukkan
bahwa …` (`hi-padjir-wisatawan`), `Hasil yang ditemukan menunjukkan bahwa …`
(`hi-padjir-desa-wisata`), `The results … show that …`.

### Simpulan
`Berdasarkan hasil … dapat disimpulkan bahwa` → `implikasi` →
keterbatasan/saran. Contoh `hi-jhi-umy-malaysia`: `KESIMPULAN` →
`Berdasarkan hasil penelitian …`. Contoh `hi-richtmann-japan-vaccine`:
`6. Conclusion` → ringkasan temuan diplomasi vaksin Jepang. Contoh
`hi-padjir-asian-games`: `KESIMPULAN` → simpulan strategi diplomasi publik.

## 8. Konvensi yang ditetapkan untuk skripsi HI (dari sintesis di atas)

1. **Penomoran seksi**: `<n>.` untuk tingkat-1 dan `<n>.<m>.` untuk
   tingkat-2 (mengikuti pola dominan korpus; lihat `hi-irscs-bahasa`,
   `hi-mdpi-health-silk-road`).
2. **Abstrak dua bahasa**: `Abstrak` (Indonesia) **dan** `Abstract`
   (Inggris), **100–250 kata**, tanpa sitasi, diakhiri `Kata kunci:` dan
   `Keywords:` (lihat 14 paper dwibahasa pada §3).
3. **Sitasi**: **APA name-year** (`assets/csl/apa.csl`) — gaya build repo;
   korpus memuat keduanya (APA 34, numerik 6).
4. **Judul bab**: KAPITAL dengan label angka Romawi (`I.`), mengikuti
   konvensi bab skripsi repo dan label KAPITAL yang lazim di korpus HI.
5. **Daftar pustaka**: `DAFTAR PUSTAKA` alfabetis bergaya APA.

## 9. Ringkasan untuk kamus

- `formula` ditambah id baru bertema HI (attestasi pola kalimat korpus HI):
  `gambaran_umum`, `hasil_penelitian`, `strategi_diplomasi`,
  `instrumen_mekanisme`, `pembahasan`, `implikasi`, `perbandingan`.
- `varian_kepala.hasil` diperluas dengan varian **teramati**: `Analisis`
  (`hi-sentris-asian-games`), `Findings`/`FINDINGS`
  (`hi-ssr-geopolitics-vaccine`, `hi-jpr-nation-branding`),
  `RESULTS AND DISCUSSIONS` (`hi-jsgs-korean-cuisine`), serta `Hasil
  Penelitian` (teramati di korpus Sinta, mis. `s3-mib`, `s2-jsinbis`).
- `varian_kepala.simpulan` diperluas dengan `CONCLUSION AND RECOMMENDATIONS`
  (`hi-jpr-nation-branding`). Varian `KESIMPULAN DAN SARAN`,
  `KESIMPULAN DAN REKOMENDASI`, dan `PENUTUP` sudah terdaftar. Enam id
  `kepala_bagian` utama **tidak** diubah.
- `konektor` dan `leksikon_verba` korpus HI **tidak menambah** entri baru
  (semua konektor/verba yang dominan sudah terdaftar); kolokasi HI dicatat di
  dokumen ini.
- `kosakata_baku` dan `frasa_ai_generik` **tidak** diperluas dari korpus HI
  (tidak ada bukti kuat; menghindari tabrakan dengan `tools/check-bahasa.sh`).
- Rujukan silang ditambahkan ke kamus: `korpus_hi: docs/ir-corpus/` dan
  `catatan_riset_hi: docs/kamus-riset-korpus-hi.md`, dirender pada tabel
  **Sumber Data** di `docs/kamus-bahasa-artikel.md`.

## 10. Leksikon dan kolokasi HI terattestasi

Hitungan di bawah berasal dari ekstraksi `pdftotext -layout` atas **43 berkas**
korpus HI (`docs/ir-corpus/*.pdf`), pencocokan tak peka huruf besar-kecil
seluruh berkas. Kolom "Bukti" menyebut slug dengan kemunculan terbanyak
(dihitung atas seluruh korpus).

### 10.1 Istilah/leksikon inti (lintas bahasa korpus)

| Istilah | Kemunculan | Bukti (slug, kemunculan) |
|---|---:|---|
| `soft power` | 933 | `hi-bath-china-softpower` (251), `hi-coventry-softpower-china` (96), `hi-irscs-bahasa` (92) |
| `public diplomacy` | 728 | `hi-ijss-vtuber` (97), `hi-jpr-nation-branding` (81), `hi-irscs-bahasa` (78) |
| `COVID-19` | 616 | `hi-jhi-umy-free-active-vaccine` (122), `hi-stdjssh-health-silk-road-sea` (96), `hi-jhi-netherlands-vaccine` (74) |
| `ASEAN` | 578 | `hi-jsps-aviation` (144), `hi-hrmars-vaccine-softpower` (97), `hi-cjas-southeast-asia` (82) |
| `Southeast Asia` | 454 | `hi-ssr-geopolitics-vaccine` (113), `hi-richtmann-japan-vaccine` (89), `hi-cjas-southeast-asia` (84) |
| `diplomasi publik` | 431 | `hi-jhi-umy-konstruktivis` (88), `hi-sentris-asian-games` (74), `hi-jhi-vanuatu` (60) |
| `vaccine diplomacy` | 294 | `hi-jhi-netherlands-vaccine` (93), `hi-ssr-geopolitics-vaccine` (72), `hi-richtmann-japan-vaccine` (36) |
| `foreign policy` | 285 | `hi-ph-china-foreign-policy` (59), `hi-bath-china-softpower` (36), `hi-jhi-umy-vaccine-politics` (28) |
| `nation branding` | 235 | `hi-david-palestinian-nation-branding` (78), `hi-jpr-nation-branding` (48), `hi-ndu-pakistan-nation-branding` (43) |
| `regional` | 247 | `hi-cjas-southeast-asia` (53), `hi-jsps-aviation` (26), `hi-mdpi-health-silk-road` (18) |
| `international relations` | 202 | `hi-janus-health-diplomacy` (22), `hi-bath-china-softpower` (20), `hi-padjir-desa-wisata` (12) |
| `hegemoni` | 140 | `hi-bath-china-softpower` (133), `hi-cjas-southeast-asia` (4) |
| `bilateral` | 130 | `hi-jhi-netherlands-vaccine` (24), `hi-cjas-southeast-asia` (18), `hi-ssr-geopolitics-vaccine` (15) |
| `hubungan internasional` | 113 | `hi-jhi-netherlands-vaccine` (20), `hi-jhi-vanuatu` (18), `hi-jhi-umy-konstruktivis` (14) |
| `multilateral` | 97 | `hi-cjas-southeast-asia` (19), `hi-jhi-umy-free-active-vaccine` (13), `hi-jhi-netherlands-vaccine` (10) |
| `health diplomacy` | 96 | `hi-janus-health-diplomacy` (67), `hi-mdpi-health-silk-road` (7), `hi-richtmann-japan-vaccine` (5) |
| `kawasan` | 88 | `hi-dinamika-bali-democracy` (25), `hi-sentris-asian-games` (23), `hi-padjir-wisatawan` (20) |
| `national interest` | 67 | `hi-sentris-asian-games` (11), `hi-jhi-umy-free-active-vaccine` (6), `hi-jhi-netherlands-vaccine` (6) |
| `kepentingan nasional` | 62 | `hi-sentris-asian-games` (40), `hi-jhi-umy-konstruktivis` (14) |
| `global governance` | 64 | `hi-bath-china-softpower` (55), `hi-janus-health-diplomacy` (3) |
| `identitas` | 57 | `hi-jhi-umy-malaysia` (27), `hi-jhi-umy-konstruktivis` (17) |
| `pembangunan` | 56 | `hi-padjir-desa-wisata` (19), `hi-jhi-vanuatu` (12) |
| `norma` | 43 | `hi-bath-china-softpower` (10), `hi-jhi-netherlands-vaccine` (8) |
| `kerja sama` | 35 | `hi-jhi-umy-malaysia` (14), `hi-jhi-vanuatu` (9) |
| `aktor non-negara` | 17 | `hi-jhi-vanuatu` (10), `hi-padjir-desa-wisata` (5) |
| `kebijakan luar negeri` | 19 | `hi-sentris-asian-games` (4), `hi-jhi-umy-malaysia` (4), `hi-padjir-desa-wisata` (3) |
| `politik luar negeri` | 15 | `hi-jhi-umy-malaysia` (4), `hi-jhi-umy-free-active-vaccine` (3) |
| `diplomasi budaya` | 14 | `hi-sentris-asian-games` (5), `hi-jhi-umy-konstruktivis` (2) |
| `kemerdekaan` | 14 | `hi-jhi-vanuatu` (5), `hi-jhi-umy-konstruktivis` (5) |
| `diplomasi vaksin` | 9 | `hi-jhi-umy-free-active-vaccine` (5), `hi-jhi-netherlands-vaccine` (4) |
| `kedaulatan` | 7 | `hi-jhi-umy-malaysia` (3), `hi-jhi-vanuatu` (2) |
| `organisasi internasional` | 6 | `hi-dinamika-bali-democracy` (3), `hi-padjir-wisatawan` (2) |
| `citra Indonesia` | 6 | `hi-jhi-umy-konstruktivis` (3), `hi-sentris-asian-games` (2) |
| `persepsi publik` | 4 | `hi-jhi-vanuatu` (3), `hi-jhi-umy-malaysia` (1) |
| `citra negara` | 3 | `hi-jhi-umy-konstruktivis` (2), `hi-sentris-asian-games` (1) |

> Terjemahan Indonesia terattestasi: `kekuatan lunak` (2, `hi-jsgs-korean-cuisine`,
> `hi-jiwp-korea-week`), `branding negara` (5, `hi-padjir-desa-wisata`).
> `soft power` jauh lebih lazim dipakai verbatim (933) daripada padanan
> Indonesianya — bukti kuat bahwa istilah asing dibiarkan miring/verbatim.

### 10.2 Kolokasi verba (8 artikel berbahasa Indonesia)

| Verba | Kemunculan | Bukti (slug, kemunculan) |
|---|---:|---|
| `meningkatkan` | 90 | `hi-padjir-wisatawan` (39), `hi-padjir-desa-wisata` (16) |
| `melakukan` | 67 | `hi-padjir-wisatawan` (17), `hi-sentris-asian-games` (11) |
| `memberikan` | 57 | `hi-jhi-umy-konstruktivis` (13), `hi-jhi-umy-malaysia` (12) |
| `menunjukkan` | 54 | `hi-jhi-umy-malaysia` (15), `hi-padjir-desa-wisata` (15) |
| `membangun` | 50 | `hi-sentris-asian-games` (13), `hi-jhi-umy-konstruktivis` (8) |
| `menggunakan` | 39 | `hi-padjir-asian-games` (13), `hi-sentris-asian-games` (12) |
| `menciptakan` | 32 | `hi-sentris-asian-games` (8), `hi-padjir-desa-wisata` (6) |
| `mendorong` | 31 | `hi-jhi-umy-malaysia` (8), `hi-dinamika-bali-democracy` (7) |
| `membentuk` | 25 | `hi-jhi-umy-malaysia` (6), `hi-padjir-wisatawan` (5) |
| `melibatkan` | 22 | `hi-jhi-vanuatu` (5), `hi-padjir-desa-wisata` (5) |
| `menjelaskan` | 14 | `hi-jhi-umy-malaysia` (3), `hi-jhi-vanuatu` (3) |
| `memengaruhi` | 14 | `hi-jhi-umy-malaysia` (7), `hi-jhi-vanuatu` (6) |
| `berperan` | 13 | `hi-padjir-desa-wisata` (5), `hi-jhi-vanuatu` (3) |
| `bertujuan` | 12 | `hi-dinamika-bali-democracy` (3), `hi-padjir-wisatawan` (3) |
| `memperkuat` | 10 | `hi-dinamika-bali-democracy` (4), `hi-sentris-asian-games` (4) |

### 10.3 Kolokasi frasa (verba + objek)

| Kolokasi | Kemunculan | Bukti (slug) |
|---|---:|---|
| `diplomasi publik Indonesia` | 120 | `hi-sentris-asian-games` (32), `hi-jhi-vanuatu` (31) |
| `mempromosikan` | 55 | `hi-sentris-asian-games` (23), `hi-padjir-desa-wisata` (12) |
| `menunjukkan bahwa` | 22 | `hi-jhi-umy-malaysia` (9), `hi-padjir-desa-wisata` (4) |
| `bertujuan untuk` | 8 | `hi-jhi-umy-malaysia` (2), `hi-dinamika-bali-democracy` (2) |
| `meningkatkan citra` | 7 | `hi-sentris-asian-games` (2), `hi-padjir-asian-games` (2) |
| `citra positif` | 7 | `hi-padjir-wisatawan` (2), `hi-dinamika-bali-democracy` (2) |
| `kepentingan nasional Indonesia` | 6 | `hi-sentris-asian-games` (5), `hi-ijss-vtuber` (1) |
| `memainkan peran` | 5 | `hi-jhi-umy-malaysia` (2), `hi-jsgs-korean-cuisine` (1) |
| `kebijakan luar negeri Indonesia` | 5 | `hi-sentris-asian-games` (2), `hi-jhi-umy-malaysia` (2) |
| `membangun citra` | 4 | `hi-sentris-asian-games`, `hi-jsgs-korean-cuisine`, `hi-jhi-umy-konstruktivis`, `hi-dinamika-bali-democracy` |
| `berperan penting` | 1 | `hi-padjir-asian-games` |

> Pola argumentatif dominan: `membangun/meningkatkan citra positif` untuk
> diplomasi publik; `memperkuat kerja sama` **tidak** terattestasi verbatim
> (0×) meski terasa lazim — penulis memakai `kerja sama` (35×) secara lepas.

## 11. Pemarkah wacana dan pembuka kalimat

Dihitung atas **8 artikel berbahasa Indonesia** (tabel §1), pencocokan tak
peka huruf besar-kecil.

### 11.1 Konektor/pemarkah wacana

| Pemarkah | Kemunculan | Bukti (slug, kemunculan) |
|---|---:|---|
| `guna` (kata utuh) | 6 | tersebar; mayoritas `menggunakan` |
| `karena` | 138 | `hi-jhi-umy-malaysia` (30), `hi-padjir-desa-wisata` (27) |
| `yaitu` | 86 | `hi-padjir-wisatawan` (18), `hi-sentris-asian-games` (17) |
| `kedua` | 84 | `hi-jhi-umy-malaysia` (22), `hi-padjir-asian-games` (19) |
| `hal ini` | 68 | `hi-sentris-asian-games` (18), `hi-jhi-umy-malaysia` (14) |
| `selain itu` | 52 | `hi-sentris-asian-games` (17), `hi-padjir-desa-wisata` (14) |
| `kemudian` | 50 | `hi-jhi-umy-malaysia` (14), `hi-padjir-desa-wisata` (12) |
| `sehingga` | 48 | `hi-padjir-desa-wisata` (16), `hi-padjir-wisatawan` (16) |
| `pertama` | 45 | `hi-padjir-asian-games` (16), `hi-dinamika-bali-democracy` (12) |
| `agar` | 42 | `hi-padjir-wisatawan` (14), `hi-padjir-desa-wisata` (9) |
| `namun` | 36 | `hi-padjir-wisatawan` (8), `hi-jhi-umy-malaysia` (7) |
| `yakni` | 36 | `hi-padjir-asian-games` (22), `hi-padjir-wisatawan` (6) |
| `sedangkan` | 33 | `hi-padjir-desa-wisata` (17), `hi-jhi-umy-malaysia` (4) |
| `ketiga` | 31 | `hi-padjir-asian-games` (10), `hi-jhi-vanuatu` (9) |
| `berdasarkan` | 28 | `hi-padjir-desa-wisata` (11), `hi-sentris-asian-games` (8) |
| `sejalan dengan` | 18 | `hi-padjir-desa-wisata` (5), `hi-jhi-umy-konstruktivis` (4) |
| `dengan demikian` | 17 | `hi-jhi-umy-malaysia` (8), `hi-jhi-umy-konstruktivis` (4) |
| `selanjutnya` | 17 | `hi-dinamika-bali-democracy` (7), `hi-jhi-vanuatu` (3) |
| `meskipun` | 16 | `hi-jhi-umy-konstruktivis` (4), `hi-jhi-vanuatu` (4) |
| `walaupun` | 16 | `hi-padjir-desa-wisata` (9), `hi-sentris-asian-games` (4) |
| `akan tetapi` | 11 | `hi-padjir-asian-games` (7), `hi-padjir-desa-wisata` (2) |
| `sementara itu` | 6 | `hi-jhi-umy-malaysia` (5), `hi-jhi-umy-konstruktivis` (1) |
| `oleh karena itu` | 6 | `hi-sentris-asian-games` (3), `hi-padjir-asian-games` (2) |
| `di sisi lain` | 5 | `hi-padjir-desa-wisata` (3) |
| `adapun` | 4 | `hi-jhi-umy-malaysia`, `hi-jhi-vanuatu`, `hi-padjir-wisatawan`, `hi-sentris-asian-games` (masing-masing 1) |
| `dapat dilihat pada` | 3 | `hi-sentris-asian-games` (2), `hi-jhi-vanuatu` (1) |
| `oleh sebab itu` | 2 | `hi-padjir-wisatawan` (2) |
| `misalnya` | 18 | `hi-jhi-umy-malaysia` (13), `hi-padjir-desa-wisata` (3) |

### 11.2 Pembuka kalimat (opener, awal kalimat)

| Pembuka | Kemunculan | Catatan |
|---|---:|---|
| `Hal …` | 75 | terutama `Hal ini …` (68×) |
| `Dalam …` | 55 | pembuka konteks |
| `Selain …` | 45 | `Selain itu …` (52×) |
| `Pada …` | 35 | rujukan waktu/tempat |
| `Dengan …` | 30 | `Dengan demikian …` |
| `Sementara …` | 17 | kontras |
| `Maka …` | 14 | konsekuensi |
| `Sedangkan …` | 13 | kontras |
| `Namun …` | 10 | kontras |
| `Berdasarkan …` | 9 | rujukan hasil |
| `Penelitian …` | 7 | rujukan penelitian sendiri |
| `Hasil …` | 6 | rujukan hasil |

> Pembuka paling produktif adalah `Hal ini …` (68×) dan `Selain itu …` (52×) —
> keduanya **terattestasi** dan bukan frasa AI generik.

## 12. Hedging dan booster

Hitungan atas seluruh 43 berkas; kolom bukti menyebut slug teratas.

### 12.1 Hedging (pelemah klaim)

| Hedging | Kemunculan | Bukti (slug, kemunculan) |
|---|---:|---|
| `cukup` | 29 | `hi-jhi-umy-malaysia` (7), `hi-padjir-asian-games` (6) |
| `cenderung` | 23 | `hi-jhi-umy-malaysia` (21) |
| `dapat dikatakan` | 10 | `hi-jhi-vanuatu` (3), `hi-sentris-asian-games` (2) |
| `seringkali` | 11 | `hi-jhi-umy-malaysia` (7) |
| `relatif` | 7 | `hi-padjir-desa-wisata` (3), `hi-jhi-umy-konstruktivis` (3) |
| `memungkinkan` | 7 | `hi-padjir-desa-wisata` (3) |
| `hampir` | 6 | `hi-padjir-desa-wisata` (3) |
| `mungkin` | 6 | `hi-sentris-asian-games` (2) |
| `berpotensi` | 5 | `hi-sentris-asian-games` (2), `hi-padjir-wisatawan` (2) |
| `diasumsikan` | 4 | `hi-jhi-umy-konstruktivis` (3) |
| `kemungkinan` | 3 | `hi-padjir-desa-wisata` (3) |
| `umumnya` | 3 | `hi-padjir-wisatawan` (2) |
| `kecenderungan` | 2 | `hi-jhi-vanuatu` (2) |
| `tampak` | 2 | `hi-padjir-wisatawan` (1), `hi-jhi-vanuatu` (1) |
| `tampaknya` | 1 | `hi-jhi-vanuatu` (1) |

### 12.2 Booster (penegas klaim)

| Booster | Kemunculan | Bukti (slug, kemunculan) |
|---|---:|---|
| `sangat` | 57 | `hi-jhi-umy-malaysia` (20), `hi-padjir-asian-games` (11) |
| `harus` | 36 | `hi-sentris-asian-games` (10), `hi-padjir-desa-wisata` (6) |
| `penting` | 66 | `hi-jhi-umy-konstruktivis` (16), `hi-sentris-asian-games` (14) |
| `tentu` | 15 | `hi-sentris-asian-games` (3), `hi-padjir-desa-wisata` (3) |
| `perlu` | 15 | `hi-padjir-desa-wisata` (6) |
| `nyata` | 10 | `hi-jhi-umy-malaysia` (6), `hi-dinamika-bali-democracy` (3) |
| `signifikan` | 9 | `hi-sentris-asian-games` (2), `hi-padjir-wisatawan` (2) |
| `pasti` | 6 | `hi-padjir-desa-wisata` (4) |
| `jelas` | 4 | `hi-sentris-asian-games`, `hi-padjir-asian-games`, `hi-jhi-vanuatu`, `hi-jhi-umy-malaysia` (masing-masing 1) |
| `krusial` | 1 | `hi-dinamika-bali-democracy` (1) |

> `sangat penting` (8×) jauh lebih jarang daripada `penting` lepas (66×);
> `sangat krusial`, `mutlak`, `wajib`, `tidak diragukan` praktis absen.
> Gaya HI lebih memilih **hedging** (`cenderung`, `dapat dikatakan`,
> `berpotensi`) daripada booster absolut.

## 13. Tipografi dan gaya penulisan korpus

| Ciri | Hitungan | Contoh / bukti |
|---|---:|---|
| Tanda persen `%` (tanpa spasi) | 414 (semua 43 berkas) | `70%`, `12,92%` (`hi-sentris-asian-games`); `20%` (`hi-padjir-asian-games`) |
| Kata `persen` | 2 | hanya `hi-padjir-desa-wisata` — jadi `%` jauh dominan |
| Desimal **koma** (ID) | 23 (8 artikel ID) | `12,92%` (`hi-sentris-asian-games`) |
| Desimal **titik** (ID) | 155 (8 artikel ID) | jumlah halaman/tabel/nomor |
| Em dash `—` | 93 (semua berkas) | `international decision making — framing the …` (`hi-bath-china-softpower`) |
| En dash `–` | 481 | rentang halaman/sitasi |
| Tanda kutip melengkung `“…”` | 773 | `hi-bath-china-softpower` (251), `hi-sentris-asian-games` (90) |
| Tanda kutip lurus `"…"` | 89 | minoritas, umumnya di badan berbahasa Inggris |
| `Tiongkok` | 20 | `hi-jiir-uinsa` (15), `hi-padjir-desa-wisata` (2) |
| `Cina` | 22 | `hi-sentris-asian-games` (15), `hi-jiir-uinsa` (5) |
| `China` (Inggris) | 2694 | `hi-bath-china-softpower` (637) |
| `et al.` | 85 | `hi-janus-health-diplomacy` (20), `hi-irscs-bahasa` (16) |
| Penanda daftar pustaka `diakses` | 112 | `hi-sentris-asian-games` (39), `hi-jiir-uinsa` (30) |
| Penanda daftar pustaka `Retrieved` | 219 | `hi-jhi-umy-free-active-vaccine` (71) |

Catatan gaya terattestasi:

- **Persen**: korpus memakai simbol `%` menempel angka (`70%`, `12,92%`),
  bukan kata `persen` (hanya 2× di seluruh korpus). Penulisan desimal
  Indonesia memakai **koma** (`12,92%`, `hi-sentris-asian-games`).
- **Istilah asing**: `soft power` (933), `public diplomacy` (728),
  `nation branding` (235) dibiarkan verbatim, bukan diterjemahkan —
  padanan `kekuatan lunak` hanya 2×.
- **Nama negara**: korpus **campur** antara `Tiongkok` (20×) dan `Cina` (22×);
  tidak ada satu bentuk baku. `China` mendominasi karena korpus Inggris.
- **Tanda kutip**: kutipan langsung memakai tanda melengkung `“…”` (773×),
  bukan tanda lurus.
- **Halaman/sitasi**: penanda `diakses`/`Retrieved` lazim di daftar pustaka
  bergaya APA (112/219×).

## 14. Frasa AI-generik yang absen dari korpus HI

Diuji atas seluruh 43 berkas (`pdftotext -layout`, pencocokan tak peka huruf
besar-kecil). Frasa bertanda **0** adalah frasa yang **tidak** dipakai penulis
jurnal HI — bukti bahwa frasa itu memang bukan gaya korpus dan layak dihindari
dalam draf skripsi.

| Frasa diuji | Kemunculan | Catatan |
|---|---:|---|
| `dalam era digital saat ini` | 0 | absen |
| `seiring dengan perkembangan zaman` | 0 | absen |
| `tidak dapat dipungkiri` | 2 | `hi-padjir-desa-wisata` (2) |
| `perlu dicatat bahwa` | 0 | absen |
| `penting untuk dicatat bahwa` | 0 | absen |
| `pada akhirnya` | 6 | `hi-sentris-asian-games` (3), `hi-padjir-desa-wisata` (1) |
| `secara keseluruhan` | 4 | `hi-padjir-desa-wisata` (3), `hi-padjir-asian-games` (1) |
| `dalam konteks ini` | 2 | `hi-padjir-desa-wisata` (1), `hi-jsgs-korean-cuisine` (1) |
| `dengan kata lain` | 3 | `hi-padjir-desa-wisata` (2), `hi-jhi-vanuatu` (1) |
| `pada dasarnya` | 7 | `hi-padjir-desa-wisata` (6), `hi-padjir-wisatawan` (1) |
| `memainkan peran penting` | 3 | `hi-jsgs-korean-cuisine` (1), `hi-jhi-vanuatu` (1), `hi-jhi-umy-malaysia` (1) |
| `memiliki peran penting` | 0 | absen |
| `dalam rangka untuk` | 0 | absen |
| `sangat krusial` | 0 | absen |
| `kompleks dan beragam` | 0 | absen |
| `sebagai kesimpulan` | 0 | absen |

Kesimpulan §14: **10 dari 16** frasa uji berjumlah 0 di seluruh korpus HI.
Enam frasa sisanya muncul sporadis (2–7×, terpusat pada 1–2 artikel), sehingga
tidak dapat disebut "gaya korpus". Karena itu daftar `frasa_ai_generik` di
kamus **tidak** bertabrakan dengan gaya HI nyata; justru frasa-frasa ini
memperkuat bukti bahwa penulisan jurnal HI menghindarinya.
