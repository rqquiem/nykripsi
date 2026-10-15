# Statistik korpus BAB I / Pendahuluan — Sinta, IR, dan LibGen

**Tujuan dan metode.** Dokumen ini mengukur secara empiris struktur bagian **Pendahuluan/Introduction** pada tiga korpus PDF lokal — `docs/sinta-corpus/` (artikel Sinta 1–6, bidang komputasi/sistem informasi Indonesia), `docs/ir-corpus/` (artikel Hubungan Internasional nasional & internasional), dan `docs/libgen-corpus/` (buku & artikel HI) — sebagai bukti angka untuk kerangka BAB I di `docs/bab1-framework.md`. Alat: **Poppler `pdftotext`** (`/usr/bin/pdftotext`) mengekstrak setiap PDF ke teks polos di `/tmp`. Seluruh berkas diekstrak **dua kali**: pertama dengan `pdftotext` bawaan, lalu diekstrak ulang dengan `pdftotext -raw` karena mode `-raw` mempertahankan urutan kolom dan pemisah paragraf pada berkas dua-kolom (temuan kunci: mode bawaan mencacah teks dua-kolom baris demi baris sehingga jumlah paragraf/kata salah). Judul bagian Pendahuluan dicari dengan pola judul (`PENDAHULUAN`, `Pendahuluan`, `Introduction`, `1. INTRODUCTION`, `MỞ ĐẦU`, `ĐẶT VẤN ĐỀ`, `Background`, `Latar Belakang`); akhir bagian ditandai judul seksi berikutnya (`METODE`, `METHOD`, `LITERATURE REVIEW`, `KERANGKA KONSEPTUAL`, `PEMBAHASAN`, `REFERENCES`, dst.). Berkas yang membuka langsung dengan badan tanpa label seksi (mis. artikel/editorial/op-ed) dan berkas dua-kolom yang labelnya sulit dipisahkan ditentukan batasnya secara manual dan dicatat sebagai “tanpa judul”. Jumlah kata = token whitespace prosa Pendahuluan (esai berbahasa Tionghoa dihitung jumlah karakter Han); jumlah paragraf = blok teks dipisah baris kosong (blok < 15 kata diabaikan); penanda gerak dideteksi lewat pencocokan pola leksikal (kata kunci per gerak ada di blok `## Reproduce`); sitasi dihitung best-effort dari pola `(Penulis, tahun)`, `[n]`, dan `Penulis tahun`. Semua angka ringkas di §2 **dihitung langsung** dari tabel §1 (median = nilai tengah; untuk N genap, rata-rata dua nilai tengah).

## 1. Tabel per-paper

Kolom gerak: `Y` = penanda hadir, `–` = tidak terdeteksi. Gerak: **Ko** = konteks/objek, **Ma** = masalah, **Ka** = kajian terdahulu, **Ce** = celah, **Tu** = tujuan. Kolom terakhir = subbagian bab-1 yang teramati (berkas bergaya bab/buku) atau `—`.

| # | slug | korpus | bahasa | judul Pendahuluan (verbatim) | paragraf | kata | Ko | Ma | Ka | Ce | Tu | sitasi | subbagian bab-1 |
|---|------|:------:|:------:|------------------------------|:--------:|-----:|:--:|:--:|:--:|:--:|:--:|------:|-----------------|
| 1 | `s1-register` | sinta | EN | 1. Introduction | 7 | 944 | – | Y | Y | Y | – | 48 | — |
| 2 | `s1-telkomnika` | sinta | EN | INTRODUCTION | 4 | 668 | Y | – | – | Y | – | 11 | — |
| 3 | `s2-ijccs` | sinta | EN | 1. INTRODUCTION | 4 | 293 | – | – | – | Y | Y | 2 | — |
| 4 | `s2-ilkom` | sinta | EN | Introduction | 4 | 558 | Y | – | Y | Y | Y | 10 | — |
| 5 | `s2-jiki` | sinta | EN | 1. Introduction | 4 | 398 | Y | Y | – | – | Y | 14 | — |
| 6 | `s2-jisebi` | sinta | EN | I. INTRODUCTION | 8 | 1024 | Y | Y | – | Y | Y | 22 | — |
| 7 | `s2-jptk` | sinta | EN | INTRODUCTION | 5 | 442 | – | Y | Y | Y | Y | 9 | — |
| 8 | `s2-jsinbis` | sinta | ID | 1. Pendahuluan | 4 | 330 | – | Y | – | – | Y | 9 | — |
| 9 | `s2-jti` | sinta | EN | INTRODUCTION | 6 | 699 | – | Y | Y | Y | Y | 16 | — |
| 10 | `s2-jtie` | sinta | EN | INTRODUCTION | 3 | 860 | Y | Y | Y | Y | – | 9 | — |
| 11 | `s2-resti` | sinta | EN | 1. Introduction | 5 | 489 | Y | Y | Y | Y | – | 12 | — |
| 12 | `s2-sji` | sinta | EN | INTRODUCTION | 4 | 411 | Y | Y | Y | – | – | 14 | — |
| 13 | `s3-coreit` | sinta | EN | INTRODUCTION | 5 | 720 | Y | Y | Y | Y | Y | 11 | — |
| 14 | `s3-jsce` | sinta | EN | 1. Introduction | 2 | 475 | Y | – | – | Y | Y | 9 | — |
| 15 | `s3-jsi-ui` | sinta | EN | Introduction | 8 | 704 | Y | Y | Y | Y | – | 7 | — |
| 16 | `s3-juti` | sinta | EN | 1. Introduction | 4 | 437 | Y | Y | – | – | – | 7 | — |
| 17 | `s3-mib` | sinta | ID | 1. PENDAHULUAN | 5 | 539 | Y | Y | Y | – | Y | 10 | — |
| 18 | `s3-sinkron` | sinta | EN | INTRODUCTION | 8 | 1171 | Y | Y | Y | – | – | 19 | — |
| 19 | `s3-sisfokom` | sinta | EN | INTRODUCTION | 5 | 559 | Y | Y | – | – | – | 14 | — |
| 20 | `s3-sistemasi` | sinta | ID | 1. Pendahuluan | 5 | 553 | Y | Y | Y | Y | Y | 13 | — |
| 21 | `s4-jsi` | sinta | ID | 1. PENDAHULUAN | 1 | 176 | – | Y | Y | – | Y | 8 | — |
| 22 | `s4-scan` | sinta | ID | PENDAHULUAN | 4 | 275 | Y | Y | – | – | Y | 10 | — |
| 23 | `s4-sitekin` | sinta | EN | Introduction | 10 | 1073 | Y | Y | Y | Y | Y | 14 | — |
| 24 | `s4-transformatika` | sinta | ID | PENDAHULUAN | 16 | 1208 | Y | Y | Y | Y | Y | 28 | — |
| 25 | `s5-jatisi` | sinta | ID | 1. PENDAHULUAN | 4 | 530 | – | Y | Y | – | Y | 17 | — |
| 26 | `s5-misi` | sinta | ID | 1. PENDAHULUAN | 3 | 447 | Y | Y | – | – | Y | 13 | — |
| 27 | `s5-nuansa` | sinta | EN | 1. INTRODUCTION | 7 | 503 | Y | – | – | Y | Y | 8 | — |
| 28 | `s6-jupiter` | sinta | ID | 1. PENDAHULUAN | 3 | 376 | – | Y | Y | – | Y | 6 | — |
| 29 | `s6-jutik` | sinta | ID | 1. PENDAHULUAN | 4 | 553 | – | Y | – | – | – | 10 | — |
| 30 | `hi-atlantis-china-asea-pd` | ir | EN | 1. Introduction | 1 | 90 | Y | – | – | – | – | 0 | — |
| 31 | `hi-bath-china-softpower` | ir | EN | (none — body begins after front matter/abstract) | 7 | 1141 | Y | Y | Y | – | Y | 7 | — |
| 32 | `hi-bournemouth-nation-branding` | ir | EN | Why did Russia invade Ukraine? | 3 | 487 | Y | Y | Y | – | – | 2 | — |
| 33 | `hi-brunel-softpower` | ir | ZH | (none — Chinese-language essay opens directly with body) | 3 | 2159 | Y | Y | Y | Y | Y | 0 | — |
| 34 | `hi-cjas-southeast-asia` | ir | EN | Introduction | 12 | 1185 | Y | Y | – | – | Y | 10 | — |
| 35 | `hi-coventry-softpower-china` | ir | EN | Introduction | 3 | 736 | Y | Y | – | Y | – | 2 | — |
| 36 | `hi-david-palestinian-nation-branding` | ir | EN | Chapter 1: A Theoretical Framework | 22 | 3322 | Y | Y | Y | – | – | 15 | Chapter 1 “A Theoretical Framework”: Nation Branding; Significance of National Branding (National Image) |
| 37 | `hi-dinamika-bali-democracy` | ir | ID | PENDAHULUAN | 6 | 778 | Y | Y | – | – | Y | 7 | — |
| 38 | `hi-gfpr-us-china-softpower` | ir | EN | Introduction | 3 | 721 | Y | Y | – | – | Y | 4 | — |
| 39 | `hi-hrmars-vaccine-softpower` | ir | EN | Introduction | 6 | 1758 | Y | Y | – | – | Y | 18 | — |
| 40 | `hi-ijss-vtuber` | ir | EN | INTRODUCTION | 11 | 2080 | Y | Y | – | – | Y | 44 | — |
| 41 | `hi-interaksi-g20` | ir | EN | Introduction | 12 | 2125 | Y | Y | Y | Y | Y | 33 | — |
| 42 | `hi-irscs-bahasa` | ir | EN | Introduction | 5 | 848 | Y | Y | Y | Y | Y | 4 | — |
| 43 | `hi-ivran-mask-diplomacy` | ir | RU | (none — body begins after abstract/annotation) | 12 | 2057 | Y | – | – | – | – | 0 | — |
| 44 | `hi-janus-health-diplomacy` | ir | EN | Introduction | 4 | 1000 | Y | Y | – | – | Y | 16 | — |
| 45 | `hi-jelajah-tourism` | ir | EN | INTRODUCTION | 7 | 1024 | Y | – | – | Y | Y | 19 | — |
| 46 | `hi-jgs-japan-pd` | ir | EN | (none — body begins after dual abstract) | 6 | 847 | Y | Y | – | – | Y | 6 | — |
| 47 | `hi-jhi-netherlands-vaccine` | ir | ID | Introduction | 8 | 1097 | Y | Y | Y | – | Y | 16 | — |
| 48 | `hi-jhi-umy-free-active-vaccine` | ir | EN | INTRODUCTION | 1 | 326 | Y | Y | – | – | Y | 7 | — |
| 49 | `hi-jhi-umy-konstruktivis` | ir | ID | PENDAHULUAN | 8 | 489 | Y | Y | – | Y | Y | 9 | — |
| 50 | `hi-jhi-umy-malaysia` | ir | ID | PENDAHULUAN | 11 | 964 | Y | Y | Y | Y | Y | 9 | — |
| 51 | `hi-jhi-umy-vaccine-politics` | ir | EN | INTRODUCTION | 12 | 893 | Y | Y | – | – | Y | 9 | — |
| 52 | `hi-jhi-vanuatu` | ir | ID | (none — body begins after dual abstract) | 4 | 276 | Y | Y | – | – | Y | 4 | — |
| 53 | `hi-jiir-uinsa` | ir | EN | Background | 4 | 711 | Y | – | Y | Y | – | 2 | — |
| 54 | `hi-jiwp-korea-week` | ir | EN | INTRODUCTION | 6 | 1196 | Y | Y | Y | Y | Y | 16 | — |
| 55 | `hi-jpr-nation-branding` | ir | EN | 1.0 INTRODUCTION | 11 | 1767 | Y | Y | Y | Y | Y | 35 | — |
| 56 | `hi-jsgs-korean-cuisine` | ir | EN | INTRODUCTION | 11 | 2216 | Y | Y | – | – | Y | 12 | — |
| 57 | `hi-jsps-aviation` | ir | EN | INTRODUCTION | 3 | 577 | Y | Y | Y | Y | – | 9 | — |
| 58 | `hi-mdpi-health-silk-road` | ir | EN | 1. Introduction | 3 | 537 | Y | Y | Y | – | Y | 4 | — |
| 59 | `hi-mgimo-health-silk-road` | ir | EN | (none — body begins after abstract) | 7 | 748 | Y | Y | – | Y | – | 7 | — |
| 60 | `hi-ndu-pakistan-nation-branding` | ir | EN | (none — body begins after abstract) | 2 | 337 | Y | Y | Y | – | – | 1 | — |
| 61 | `hi-padjir-asian-games` | ir | ID | PENDAHULUAN | 9 | 1003 | Y | Y | – | – | Y | 21 | — |
| 62 | `hi-padjir-desa-wisata` | ir | ID | PENDAHULUAN | 8 | 629 | Y | Y | – | – | – | 11 | — |
| 63 | `hi-padjir-wisatawan` | ir | ID | PENDAHULUAN | 8 | 930 | Y | Y | – | – | Y | 13 | — |
| 64 | `hi-ph-china-foreign-policy` | ir | EN | A. INTRODUCTION | 1 | 458 | Y | Y | – | – | – | 0 | — |
| 65 | `hi-reinvention-vaccine` | ir | EN | (unlabeled — opens directly with body) | 10 | 1506 | Y | Y | – | Y | Y | 24 | — |
| 66 | `hi-richtmann-japan-vaccine` | ir | EN | Introduction | 1 | 153 | Y | Y | – | – | – | 3 | — |
| 67 | `hi-sentris-asian-games` | ir | ID | Latar Belakang | 4 | 916 | Y | Y | – | – | – | 35 | — |
| 68 | `hi-ssr-geopolitics-vaccine` | ir | EN | Introduction | 3 | 815 | Y | Y | – | Y | Y | 3 | — |
| 69 | `hi-stdjssh-health-silk-road-sea` | ir | VI | ĐẶT VẤN ĐỀ | 4 | 1089 | – | – | – | – | – | 0 | — |
| 70 | `hi-stdjssh-japan-vaccine` | ir | VI | MỞ ĐẦU | 3 | 483 | – | – | – | – | – | 0 | — |
| 71 | `lg-art-nation-branding-in-a-transitional-democracy-the-role-of-cor` | libgen | EN | INTRODUCTION | 3 | 655 | Y | Y | – | – | – | 9 | — |
| 72 | `lg-art-peace-through-vaccine-diplomacy` | libgen | EN | (none — editorial opens directly with body) | 6 | 575 | Y | Y | – | – | – | 2 | — |
| 73 | `lg-art-public-diplomacy-and-soft-power` | libgen | EN | (none — article opens directly with body) | 53 | 6602 | Y | Y | – | Y | – | 53 | — |
| 74 | `lg-art-taking-the-new-public-diplomacy-online-russia-and-china` | libgen | EN | INTRODUCTION | 3 | 344 | Y | Y | – | – | – | 3 | — |
| 75 | `lg-art-the-english-school-international-relations-and-progress` | libgen | EN | The English School and the Concept of a Research Enterprise | 14 | 1910 | Y | Y | Y | Y | Y | 7 | — |
| 76 | `lg-art-vaccine-diplomacy` | libgen | EN | (none — op-ed opens directly with body) | 10 | 837 | Y | Y | – | – | – | 5 | — |
| 77 | `lg-book-classical-liberalism-and-international-relations-theory-hum` | libgen | EN | CHAPTER 1 — Introduction | 25 | 6238 | Y | Y | Y | Y | Y | 0 | CHAPTER 1 “Introduction”: Classical Liberalism and IR Theory; Four Classical Liberals; Theoretical Framework: The English School; Realist or International System Tradition; Kantian or World Society Tradition |
| 78 | `lg-book-constructivism-in-international-relations-the-politics-of-r` | libgen | EN | 1 Introduction | 132 | 13737 | Y | Y | Y | Y | Y | 68 | 1 Introduction: Constructivism in International Relations; Three constructivisms; German military involvement abroad; Plan of the book |
| 79 | `lg-book-making-sense-making-worlds-constructivism-in-social-theory` | libgen | EN | 1 Constructivism: a user's manual | 60 | 7850 | Y | Y | Y | – | – | 1 | 1 “Constructivism: a user’s manual”: Overview; Rules make agents, agents make rules |
| 80 | `lg-book-power-interdependence-4` | libgen | EN | 1 Interdependence in World Politics | 34 | 8118 | Y | Y | – | Y | Y | 4 | CHAPTER 1 “Interdependence in World Politics”: The New Rhetoric of Interdependence; Interdependence as an Analytic Concept; Power and Interdependence; International Regime Change |
| 81 | `lg-book-realism-and-international-relations` | libgen | EN | 1 The realist tradition | 79 | 7135 | Y | Y | – | Y | – | 62 | 1 “The realist tradition”: A definition; Six realist paradigms |
| 82 | `lg-book-realist-constructivism-rethinking-international-relations-t` | libgen | EN | 1 Introduction | 18 | 4454 | Y | Y | Y | – | Y | 24 | 1 Introduction (single section, no named subsections) |
| 83 | `lg-book-social-theory-of-international-politics` | libgen | EN | 1 Four sociologies of international politics | 97 | 16181 | Y | Y | Y | Y | Y | 0 | 1 “Four sociologies of international politics”: The states systemic project; State-centrism; Systems theory; Neorealism and its critics; A map of structural theorizing; Four sociologies; Locating international theories; Three interpretations; Epistemology and the via media; Plan of the book |
| 84 | `lg-book-the-anarchical-society-a-study-of-order-in-world-politics` | libgen | EN | The Concept of Order in World Politics | 30 | 7281 | Y | Y | – | – | – | 0 | “The Concept of Order in World Politics”: The Nature of Order in World Politics; Does Order Exist in World Politics?; The Balance of Power and International Order; International Law and International Order; Diplomacy and International Order; War and International Order; The Great Powers and International Order; Alternative Paths to World Order |
| 85 | `lg-book-the-restructuring-of-international-relations-theory` | libgen | EN | Introduction | 32 | 7105 | Y | Y | Y | Y | – | 0 | Introduction: project; Defining positivism; Reflexivity and International Relations theory; Human consciousness and International Relations theory; Conclusion |

_Rows written: **85** = 29 Sinta + 41 IR + 15 LibGen. Setiap paper dihitung sekali._
## 2. Statistik ringkas (terhitung dari tabel §1)

### 2.1 Jumlah kata Pendahuluan

| Grup | N | min | median | maks |
|------|--:|----:|-------:|----:|
| Sinta | 29 | 176 | 539 | 1208 |
| IR (`ir-corpus`) | 41 | 90 | 893 | 3322 |
| LibGen | 15 | 344 | 6602 | 16181 |
| Semua | 85 | 90 | 778 | 16181 |

Aritmetika median: Sinta N=29 (ganjil) → nilai ke-15 = 539; IR N=41 (ganjil) → nilai ke-21 = 893; LibGen N=15 (ganjil) → nilai ke-8 = 6602. Nilai ekstrem: Sinta min 176 (`s4-jsi`), maks 1208 (`s4-transformatika`); IR min 90 (`hi-atlantis-china-asea-pd`, satu paragraf sebelum seksi-2), maks 3322 (`hi-david-palestinian-nation-branding`, bab-1 gaya skripsi); LibGen min 344 (`lg-art-taking-the-new-public-diplomacy-online-russia-and-china`), maks 16181 (`lg-book-social-theory-of-international-politics`).

### 2.2 Penanda gerak (deteksi kata kunci)

| Grup | konteks/objek | masalah | kajian terdahulu | celah | tujuan |
|------|:-------------:|:-------:|:----------------:|:-----:|:------:|
| Sinta (N=29) | 20/29 (69.0%) | 24/29 (82.8%) | 17/29 (58.6%) | 16/29 (55.2%) | 19/29 (65.5%) |
| IR (N=41) | 39/41 (95.1%) | 35/41 (85.4%) | 14/41 (34.1%) | 14/41 (34.1%) | 26/41 (63.4%) |
| LibGen (N=15) | 15/15 (100.0%) | 15/15 (100.0%) | 7/15 (46.7%) | 8/15 (53.3%) | 6/15 (40.0%) |
| Semua (N=85) | 74/85 (87.1%) | 74/85 (87.1%) | 38/85 (44.7%) | 38/85 (44.7%) | 51/85 (60.0%) |

**Penanda tujuan** hadir pada 19/29 (65.5%) artikel Sinta dan 26/41 (63.4%) artikel IR. **Penanda celah** hadir pada 16/29 (55.2%) artikel Sinta dan 14/41 (34.1%) artikel IR.

### 2.3 Distribusi jumlah paragraf

| Grup | 1 | 2 | 3 | 4 | 5–6 | 7–10 | >10 |
|------|--:|--:|--:|--:|:---:|:----:|:---:|
| Sinta (N=29) | 1 | 1 | 3 | 10 | 7 | 6 | 1 |
| IR (N=41) | 4 | 1 | 8 | 5 | 5 | 9 | 9 |
| LibGen (N=15) | 0 | 0 | 2 | 0 | 1 | 1 | 11 |
| Semua (N=85) | 5 | 2 | 13 | 15 | 13 | 16 | 21 |

Modus jumlah paragraf Pendahuluan Sinta = 4 paragraf (10 artikel); modus IR = 7–10 paragraf (9 artikel). Hampir semua berkas bergaya buku (LibGen) berada pada >10 paragraf (11 dari 15).

### 2.4 Sitasi dalam Pendahuluan

| Grup | min | median | maks |
|------|----:|-------:|----:|
| Sinta | 2 | 11 | 48 |
| IR | 0 | 7 | 44 |
| LibGen | 0 | 4 | 68 |

Angka ini best-effort (pola name-year/numerik); dokumen bergaya buku memakai catatan akhir bernomor sehingga hitungannya lebih rendah dari sitasi sebenarnya.

### 2.5 Set subbagian bab-1 yang paling sering muncul (berkas bergaya bab)

Sepuluh berkas bergaya bab/buku teramati (9 LibGen book + `hi-david-palestinian-nation-branding`). Tidak ada dua berkas yang berbagi set subbagian persis sama; **pola urutan** yang paling sering muncul adalah:

- **Set 4 subbagian** (paling sering pada bab-1 buku HI): *konteks/pengantar teori → definisi konsep → kerangka teoretis → sistematika/rencana bab*. Teramati pada `lg-book-classical-liberalism-and-international-relations-theory-hum` (Classical Liberalism and IR Theory; Four Classical Liberals; Theoretical Framework: The English School; Realist or International System Tradition; Kantian or World Society Tradition) dan `lg-book-power-interdependence-4` (The New Rhetoric of Interdependence; Interdependence as an Analytic Concept; Power and Interdependence; International Regime Change).
- **Set 3–10 subbagian** pada buku lain: `lg-book-constructivism-...` (4), `lg-book-the-restructuring-...` (5), `lg-book-the-anarchical-society-...` (8), `lg-book-social-theory-...` (10).
- Berkas bergaya skripsi (`hi-david-palestinian-nation-branding`) memakai judul bab eksplisit `Chapter 1: A Theoretical Framework` dengan 2 subbagian (Nation Branding; Significance of National Branding).

Pola umum: bab-1 buku HI **selalu** memuat (a) pernyataan konteks/ruang lingkup dan (b) peta/sistematika bab (`Plan of the book` / `Chapter outline`), sedangkan artikel jurnal tidak.

### 2.6 Bahasa bagian Pendahuluan

| Bahasa | Sinta | IR | LibGen | Semua |
|--------|------:|---:|-------:|------:|
| Inggris (EN) | 19 | 28 | 15 | 62 |
| Indonesia (ID) | 10 | 9 | 0 | 19 |
| Vietnam (VI) | 0 | 2 | 0 | 2 |
| Rusia (RU) | 0 | 1 | 0 | 1 |
| Tionghoa (ZH) | 0 | 1 | 0 | 1 |
## 3. Berkas UNREADABLE

**Tidak ada berkas yang sepenuhnya UNREADABLE** — `pdftotext` menghasilkan teks non-kosong untuk **semua 87 PDF** (29 Sinta + 43 IR + 15 LibGen). Namun **2 berkas IR tidak dapat dibaca bagian Pendahuluannya** dan dicatat di sini (bukan diarang):

| Berkas | Korpus | Alasan |
|--------|--------|--------|
| `hi-ieom-istanbul-vaccine.pdf` | ir | PDF 1 halaman; ekstraksi berhenti setelah blok `Keyword`/`Abstract` (tidak ada badan artikel — versi yang tersimpan hanya lembar abstrak). Tidak ada bagian Pendahuluan untuk diukur. |
| `hi-ieom-rome-vaccine.pdf` | ir | PDF 1 halaman; sama seperti di atas — hanya judul, abstrak, keyword, dan biografi; badan artikel tidak ada di berkas. |

Catatan: `hi-brunel-softpower.pdf` (esai berbahasa Tionghoa) **berhasil dibaca** dan dimasukkan ke tabel (penghitungan kata memakai jumlah karakter Han, 2.159); ia bukan UNREADABLE. Empat PDF yang `docs/sinta-corpus/MANIFEST.md` tandai FAILED (`s2-jtiik`, `s4-zonasi`, `s4-jusifor`, `s5-intek`) tidak ada di disk sehingga tidak diproses; 29 PDF Sinta yang ada semuanya terbaca.

## Reproduce

Dijalankan dari akar repo:

```sh
# 1. Ekstraksi teks setiap PDF (poppler pdftotext), lalu ulang dengan -raw.
mkdir -p /tmp/bab1_txt /tmp/bab1_raw
for f in docs/sinta-corpus/*.pdf docs/ir-corpus/*.pdf docs/libgen-corpus/*.pdf; do
  b=$(basename "$f" .pdf)
  pdftotext -q "$f" "/tmp/bab1_txt/$b.txt"
  pdftotext -raw -q "$f" "/tmp/bab1_raw/$b.txt"
done

# 2. Cek non-kosong (tidak ada UNREADABLE penuh).
for t in /tmp/bab1_raw/*.txt; do
  printf "%s %s\n" "$(basename "$t")" "$(tr -d '[:space:]' < "$t" | wc -c)"
done | sort

# 3. Lokasi judul Pendahuluan dan seksi berikutnya.
grep -n -E '^[[:space:]]*((I|1)\.?[[:space:]]+)?(PENDAHULUAN|Pendahuluan|INTRODUCTION|Introduction|MỞ ĐẦU|ĐẶT VẤN ĐỀ|Background|Latar Belakang)' /tmp/bab1_raw/*.txt
grep -n -E '^[[:space:]]*(METODE|METHOD|METHODS|LITERATURE REVIEW|KERANGKA KONSEPTUAL|PEMBAHASAN|REFERENCES|Daftar Pustaka)' /tmp/bab1_raw/*.txt
```

Batas baris `(start, end)` tiap berkas ditulis eksplisit dalam skrip scratch `/tmp` (tidak ditambahkan ke repo). Skrip itu (a) membuang baris nomor halaman/URL/DOI/footer jurnal, (b) menyatukan baris menjadi paragraf — blok dipisah baris kosong, blok < 15 kata diabaikan, (c) menghitung token kata, (d) mendeteksi penanda gerak dengan pola leksikal berikut (disederhanakan; pola lengkap ada di skrip):

```
konteks : (konteks|context|fenomena|latar belakang|background|global|internasional|international|pandemic|pandemi|di era|in the era|world politics|era)
masalah : (masalah|problem|persoalan|issue|isu|permasalahan|challenge|tantangan|krisis|crisis|bagaimana|mengapa|why|question|pertanyaan|how)
kajian  : (penelitian terdahulu|kajian terdahulu|studi terdahulu|previous studies|prior work|literature review|tinjauan pustaka|scholars?|has been studied|et al\.)
celah   : (gap|celah|kesenjangan|belum (banyak|diteliti|dikaji|dibahas)|still (unclear|unknown|limited)|few studies|little (research|attention)|lack(s|ing)? of|has not been|research gap|masih minim|jarang)
tujuan  : (bertujuan|aims? to|this (article|paper|study|research) (aims?|seeks?|examines?|analy[sz]es?)|tujuan penelitian|penelitian ini|studi ini|the (purpose|aim|objective) of|tulisan ini|will (discuss|examine|analy[sz]e)|menganalisis|menjelaskan)
```

Sitasi dihitung dengan tiga pola: `(Penulis, tahun)`, `[n]`/`[n-m]`, dan `Penulis tahun`.

Batas Pendahuluan diverifikasi manual terhadap judul seksi tetangga (mis. berakhir di `2. METHODS`, `PEMBAHASAN`, `LITERATURE REVIEW`, `REFERENCES`). Untuk berkas tanpa label, awal/akhir badan ditentukan dari judul pertama yang dapat dipisahkan (mis. `Why did Russia invade Ukraine?`, `Chapter 1: A Theoretical Framework`, `During 60 years of bilateral relations`) atau akhir berkas untuk op-ed/editorial pendek. Untuk buku, bab-1 diambil dari judul bab (`CHAPTER 1`, `1 Introduction`, `The Concept of Order in World Politics`) hingga judul bab-2 (`CHAPTER 2`, `2 Definitions`, `Does Order Exist in World Politics?`). Jumlah berkas dicek silang dengan `docs/sinta-corpus/MANIFEST.md`, `docs/ir-corpus/MANIFEST.md`, dan `docs/libgen-corpus/manifest.tsv`.
