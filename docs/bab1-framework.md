# Kerangka BAB I / Pendahuluan Hubungan Internasional — Aturan Absolut, Frame, dan Scope (Sinta 1–6, Scopus, Skripsi)

Kerangka ini menurunkan **aturan absolut**, **frame** (model gerak argumen +
administrasi bab), dan **scope** untuk **BAB I / Pendahuluan** dalam artikel
jurnal Hubungan Internasional (HI), makalah akademik, dan skripsi HI. Kerangka
diselaraskan dengan tingkatan **Sinta 1–6**, jurnal **Scopus**, dan struktur
skripsi HI.

Setiap aturan disertai bukti: **hitungan korpus** (dari
[`docs/bab1-corpus-stats.md`](bab1-corpus-stats.md) — statistik Langkah 1 atas
**85 paper** = 29 Sinta + 41 IR + 15 LibGen, dan dari kamus korpus yang sudah
ada di repositori), **sitasi berkas repositori + bagian**, dan/atau **rekaman
nyata `scholar.py` beserta URL/DOI**. **Tidak ada klaim tanpa sumber.** Klaim
spesifik tentang status indeksasi Scopus sebuah jurnal **tidak** dinyatakan;
bila muncul, ditandai `unverified — confirm first`.

> **Status.** Kesepuluh bagian ada dan lengkap. **§6 "Pita Panjang per
> Bagian"** kini memuat **angka terukur** dari
> [`docs/bab1-corpus-stats.md`](bab1-corpus-stats.md) §2.1–§2.4 (panjang kata,
> penanda gerak, distribusi paragraf, sitasi Pendahuluan). **§7** kini
> menyumberkan struktur CARS/IMRaD (IMRaD; ARJST) sementara angka pita
> per-jurnal tetap ditandai `unverified — confirm first`.

---

## 1. Definisi dan Fungsi BAB I / Pendahuluan

**Definisi.** BAB I / Pendahuluan adalah **unit pembuka** yang menempatkan
penelitian pada ruang masalahnya: ia memindahkan pembaca dari **konteks umum
(objek/domain)** ke **masalah spesifik**, menunjukkan **apa yang sudah dan
belum dikerjakan** penelitian terdahulu, lalu **menyatakan celah dan tujuan**
penelitian. Pada skripsi HI, unit ini dipecah menjadi lima subbagian
administratif; pada artikel HI, unit ini berupa **satu bagian kontinu** tanpa
subbagian.

**Fungsi.** Pendahuluan menjalankan empat fungsi yang saling terkait:

1. **Membangun ruang riset (establishing a territory).** Menyatakan pentingnya
   objek dan domain — pada HI umumnya dimulai dari **konteks kebijakan luar
   negeri / hubungan bilateral**, lalu masalah pandemi/geopolitik
   ([`docs/kamus-riset-korpus-hi.md`](kamus-riset-korpus-hi.md) §7
   "Pendahuluan"; [`docs/kamus-bahasa-artikel.md`](kamus-bahasa-artikel.md)
   §"Rangkai Argumen → Pendahuluan").
2. **Menetapkan celah (establishing a niche).** Membandingkan apa yang sudah
   dikerjakan dengan apa yang belum; model CARS (Swales) menyebut gerak ini
   sebagai inti "menetapkan ceruk" — lihat §3 dan §10 (Swales, 2014;
   Choe & Hwang, 2014; Arsyad & Zainil, 2023).
3. **Menyatakan tujuan (occupying the niche).** Mengunci arah penelitian
   dengan rumusan tujuan kanonik `Penelitian ini bertujuan untuk …`
   ([`docs/kamus-riset-korpus-hi.md`](kamus-riset-korpus-hi.md) §7; rekaman
   teramati pada korpus: `hi-jhi-umy-free-active-vaccine`,
   `hi-jhi-umy-vaccine-politics`).
4. **Mengarahkan administrasi bab.** Pada skripsi, fungsi ini terwujud sebagai
   lima subbagian tetap yang memetakan pertanyaan → tujuan → manfaat
   ([`docs/skripsi-pedoman.md`](skripsi-pedoman.md) §"BAB structure with
   required sub-sections").

**Mengapa penting.** Untuk **artikel HI**, Pendahuluan adalah bagian pertama
yang dibaca setelah abstrak dan memutuskan apakah artikel diteruskan ke
penelaahan; ia juga yang mengaitkan kajian pada **percakapan disiplin HI**
(aktor, kepentingan nasional, kebijakan luar negeri). Untuk **skripsi HI**,
BAB I adalah kontrak penelitian: rumusan masalah dan tujuan yang ditetapkan di
sini mengikat seluruh bab berikutnya
([`docs/skripsi-pedoman.md`](skripsi-pedoman.md)). Bukti bobot substantif:
instrumen akreditasi Sinta menempatkan **Substansi Artikel** sebagai indikator
terberat (39 dari total bobot) — pendahuluan yang kuat adalah bagian dari
substansi tersebut ([`docs/sinta-reference.md`](sinta-reference.md) §"ARJUNA 8
indicators + weights").

---

## 2. Aturan Absolut (Wajib)

Daftar bernomor aturan non-negosiabel. Setiap butir menyebut **sumber**
repositori dan/atau literatur eksternal. Aturan **A** berlaku untuk **skripsi
HI**; **B** untuk **artikel HI**; **C** berlaku untuk **keduanya**.

### A. Skripsi HI

- **A1 (skripsi HI) — Lima subbagian dengan urutan tetap.**
  `Latar Belakang` → `Rumusan Masalah` → `Batasan Masalah` → `Tujuan` →
  `Manfaat`. Sumber: [`docs/skripsi-pedoman.md`](skripsi-pedoman.md) §"BAB
  structure with required sub-sections" (BAB I Pendahuluan). Draf rujukan
  `content/skripsi/10-bab-01-pendahuluan.md` memuat kelima `##` dalam urutan
  tersebut.
- **A2 — Setiap subbagian dibuka baris formula verbatim ber-tag `kamus:f`.**
  Tag `<!-- kamus:f id=latar_belakang -->`, `id=rumusan_masalah`,
  `id=batasan_masalah`, `id=tujuan`, `id=manfaat` (total **5**). Baris formula
  **tidak diubah tangan** — dikelola mesin
  `tools/gen_kamus.py --check` yang menyelaraskan `content/skripsi/1[0-5]-*.md`.
  Sumber: draf `content/skripsi/10-bab-01-pendahuluan.md` (5 tag `kamus:f`) +
  penegak `tools/gen_kamus.py`.
- **A3 — `Latar Belakang` memuat lima gerak berurutan.** konteks/objek →
  masalah → kajian terdahulu → celah penelitian → tujuan; pita panjang
  **~700–1200 kata**; **≥ 15** sitasi. Pita ini konsisten dengan korpus:
  median panjang Pendahuluan IR terukur **893 kata** dan maksimum Sinta
  **1208 kata** ([`docs/bab1-corpus-stats.md`](bab1-corpus-stats.md) §2.1).
  Sumber: gerak Pendahuluan HI di
  [`docs/kamus-riset-korpus-hi.md`](kamus-riset-korpus-hi.md) §7 (konvensi HI:
  konteks kebijakan luar negeri → masalah pandemi/geopolitik → celah → tujuan);
  jumlah referensi mengikuti [`docs/skripsi-pedoman.md`](skripsi-pedoman.md)
  §"References & length" (≥ 20 total, sehingga ≥ 15 di Latar Belakang adalah
  pembagian konservatif); median sitasi Pendahuluan Sinta **11** (maks 48)
  mendukung ambang ≥ 15 ([`docs/bab1-corpus-stats.md`](bab1-corpus-stats.md)
  §2.4).
- **A4 — `Rumusan Masalah` = pertanyaan bernomor (lazimnya 3).** Tiap
  pertanyaan memetakan **1:1** ke satu butir `Tujuan`. Sumber:
  [`docs/skripsi-pedoman.md`](skripsi-pedoman.md) (lima subbagian BAB I);
  draf `content/skripsi/10-bab-01-pendahuluan.md` memuat tiga pertanyaan
  bernomor yang memetakan satu-satu ke tiga butir Tujuan.
- **A5 — `Batasan Masalah` menyatakan lima batas.** rentang waktu, objek,
  kerangka analisis, sumber data, dan hal yang dikecualikan. Sumber:
  [`docs/skripsi-pedoman.md`](skripsi-pedoman.md) (subbagian Batasan Masalah);
  draf `content/skripsi/10-bab-01-pendahuluan.md` menyebut kelima batas
  eksplisit (rentang 2020–2022, objek diplomasi publik, kerangka FPA/soft
  power/nation branding, sumber data dokumen publik, pengecualian efektivitas
  klinis & kinerja keuangan).
- **A6 — `Tujuan` = butir bernomor yang memetakan 1:1 ke `Rumusan Masalah`.**
  Sumber: [`docs/skripsi-pedoman.md`](skripsi-pedoman.md); draf
  `content/skripsi/10-bab-01-pendahuluan.md` (tiga butir tujuan ↔ tiga
  pertanyaan).
- **A7 — `Manfaat` memuat dua bagian: teoretis dan praktis**, masing-masing
  ≥ 1 paragraf. Sumber: [`docs/skripsi-pedoman.md`](skripsi-pedoman.md)
  (subbagian Manfaat); draf `content/skripsi/10-bab-01-pendahuluan.md` membuka
  dua paragraf dengan "Secara teoretis, …" dan "Secara praktis, …".
- **A8 — Sitasi APA name-year; ≥ 20 referensi, ≥ 30% sumber internasional,
  semua terbitan ≤ 5 tahun.** Sumber: [`docs/skripsi-pedoman.md`](skripsi-pedoman.md)
  §"References & length". Gaya APA name-year adalah gaya build repositori
  (`assets/csl/apa.csl`) dan gaya dominan korpus HI/IR (**34/43** paper;
  [`docs/kamus-riset-korpus-hi.md`](kamus-riset-korpus-hi.md) §4).
  Penegak: `tools/validators/evidence_recency.py`. Jendela ≤ 5 tahun diukur
  terhadap `periode` yang dideklarasikan dokumen (bawaan `2020–2025`), sehingga
  sumber bukti di luar periode itu ditolak.

### B. Artikel HI

- **B1 (artikel HI) — Pendahuluan artikel = empat beat kontinu** (tanpa
  subbagian): konteks → penelitian terdahulu → celah → tujuan. Sumber:
  [`docs/conversion-skripsi-to-article.md`](conversion-skripsi-to-article.md)
  §"Rewrite rules" ("Introduction in 4 beats: context → prior work → gap →
  objective"); konsisten dengan model CARS/Swales (§3, §10).
- **B2 — Pendahuluan artikel diakhiri kalimat tujuan kanonik
  `Penelitian ini bertujuan untuk …`.** Sumber:
  [`docs/conversion-skripsi-to-article.md`](conversion-skripsi-to-article.md)
  §"Three core formulas"; [`assets/bahasa/kamus-id.yaml`](../assets/bahasa/kamus-id.yaml)
  §`formula` → `tujuan: "Penelitian ini bertujuan untuk …"`. Varian
  terattestasi di korpus HI/IR: `Artikel ini bertujuan menjelaskan …`
  (`hi-padjir-desa-wisata`), `This article examines …`
  (`hi-reinvention-vaccine`) — [`docs/kamus-riset-korpus-hi.md`](kamus-riset-korpus-hi.md)
  §7.
- **B3 — Pita panjang Pendahuluan artikel ~700–900 kata.** Target ini berada
  **di dalam** pita korpus terukur: median Pendahuluan IR **893 kata**
  (min 90, maks 3322; N=41) dan median Sinta **539 kata** (min 176, maks
  1208; N=29) ([`docs/bab1-corpus-stats.md`](bab1-corpus-stats.md) §2.1) —
  artikel HI cenderung lebih panjang daripada artikel komputasi Sinta,
  sehingga ~700–900 kata adalah titik tengah yang aman.

### C. Berlaku untuk Keduanya (ragam bahasa & integritas)

- **C1 — Ragam impersonal: tanpa kata ganti orang I/II.** `saya`, `aku`,
  `kami`, `kita`, `anda`, `kamu`, `kalian`. Sumber:
  [`docs/skripsi-pedoman.md`](skripsi-pedoman.md) §"Ragam Bahasa";
  [`docs/conversion-skripsi-to-article.md`](conversion-skripsi-to-article.md)
  §"No-pronoun rule"; penegak `tools/check-bahasa.sh`.
- **C2 — Diksi baku EYD Edisi V.** Tanpa `analisa`, `praktek`, `standard`,
  `dimana`, `dikarenakan`, `mempengaruhi`, dst. Sumber:
  [`docs/skripsi-pedoman.md`](skripsi-pedoman.md) §"Ragam Bahasa" (tabel
  padanan baku); [`assets/bahasa/kamus-id.yaml`](../assets/bahasa/kamus-id.yaml)
  §`kosakata_baku`; penegak `tools/check-bahasa.sh`.
- **C3 — Tanpa frasa pengisi AI generik.** Daftar di
  [`assets/bahasa/kamus-id.yaml`](../assets/bahasa/kamus-id.yaml)
  §`frasa_ai_generik` (`pada era digital saat ini`, `seiring dengan
  perkembangan zaman`, `dalam rangka untuk`, `sangat krusial`, `sebagai
  kesimpulan`, …). Sumber: kamus idem; penegak `tools/check-bahasa.sh`.
- **C4 — Setiap sitasi dalam teks punya entri di daftar pustaka (APA
  name-year).** Sumber: [`docs/sinta-reference.md`](sinta-reference.md)
  §"Article anatomy" ("References — complete, consistent, and cited in text");
  penegak `tools/validate.py papers` (72 sitasi ↔ 72 entri pada draf repo).
- **C5 — Urutan bagian tetap; tidak ada bagian yang dihilangkan.** Untuk
  skripsi: lima subbagian A1 berurutan; untuk artikel: empat beat B1 berurutan.
  Sumber: [`docs/skripsi-pedoman.md`](skripsi-pedoman.md);
  [`docs/conversion-skripsi-to-article.md`](conversion-skripsi-to-article.md).

---

## 3. Frame (Model Gerak dan Administrasi)

Frame menggabungkan **model gerak argumen** (CARS/Swales yang disesuaikan HI)
dengan **frame administratif skripsi** (lima subbagian).

### 3.1 Frame gerak argumen (CARS/Swales disesuaikan HI)

Model *Create a Research Space* (CARS) Swales menyusun Pendahuluan artikel
ilmiah dalam tiga gerak besar: **(1) Establishing a territory** →
**(2) Establishing a niche** → **(3) Occupying the niche** (Swales, 2014;
Choe & Hwang, 2014 — §10). Pada HI, gerak tersebut terwujud sebagai urutan
teramati `konteks/objek → masalah → kajian terdahulu → celah/tujuan`
([`docs/kamus-riset-korpus-hi.md`](kamus-riset-korpus-hi.md) §7). Artikel
bergenre sosial/HI menggeser aksen: gerak "celah" dan "tujuan" menjadi penanda
paling eksplisit (Arsyad & Zainil, 2023; Acob & Nugroho, 2026 — §10).

### 3.2 Frame administratif skripsi (lima subbagian)

Skripsi HI memecah frame gerak menjadi lima subbagian tetap
([`docs/skripsi-pedoman.md`](skripsi-pedoman.md)):

1. **Latar Belakang** — gerak 1–3 (konteks → masalah → kajian terdahulu →
   celah) + tujuan.
2. **Rumusan Masalah** — pertanyaan bernomor (lazimnya 3).
3. **Batasan Masalah** — lima batas (waktu, objek, kerangka, data,
   pengecualian).
4. **Tujuan** — butir bernomor, 1:1 dengan Rumusan Masalah.
5. **Manfaat** — teoretis + praktis.

### 3.3 Tabel pemetaan: gerak → pertanyaan → formula/penanda teramati

| Gerak (CARS) | Subbagian skripsi | Pertanyaan yang dijawab | Formula / penanda teramati | Sumber bukti |
|---|---|---|---|---|
| 1. Establish territory (konteks/objek) | Latar Belakang | Mengapa objek ini penting? | `Penelitian ini dilatarbelakangi oleh …`; mulai dari konteks kebijakan luar negeri/hubungan bilateral | `kamus-id.yaml` §`formula`; `kamus-riset-korpus-hi.md` §7 |
| 1b. Masalah | Latar Belakang | Apa masalah yang muncul? | `Meskipun demikian, terdapat celah …`; bandingkan kondisi ideal vs nyata | `kamus-bahasa-artikel.md` §"Pendahuluan" (gerak Masalah) |
| 2. Establish niche (kajian terdahulu) | Latar Belakang | Apa yang sudah dikerjakan? | `Kajian mengenai … cenderung terpusat pada …` | draf `content/skripsi/10-bab-01-pendahuluan.md` |
| 2b. Celah | Latar Belakang | Apa yang belum dikerjakan? | `terdapat celah dalam literatur …`; `Studi ini berupaya mengisi kekosongan tersebut dengan meneliti …` (`hi-jsgs-korean-cuisine`) | `kamus-riset-korpus-hi.md` §7; `kamus-bahasa-artikel.md` §"Pendahuluan" |
| 3. Occupy niche (tujuan) | Latar Belakang + Tujuan | Apa yang hendak dicapai? | `Penelitian ini bertujuan untuk …`; `Artikel ini bertujuan menjelaskan …` (`hi-padjir-desa-wisata`); `This article examines …` (`hi-reinvention-vaccine`) | `kamus-id.yaml` §`formula`; `kamus-riset-korpus-hi.md` §7 |
| Administratif | Rumusan Masalah | Pertanyaan apa yang dijawab? | pertanyaan bernomor (lazimnya 3) | `skripsi-pedoman.md` |
| Administratif | Batasan Masalah | Sejauh mana ruang lingkupnya? | lima batas: waktu, objek, kerangka, data, pengecualian | `skripsi-pedoman.md` |
| Administratif | Tujuan | Capaian apa yang ditargetkan? | butir bernomor, 1:1 ke Rumusan Masalah | `skripsi-pedoman.md` |
| Administratif | Manfaat | Siapa yang diuntungkan? | `Secara teoretis, …` / `Secara praktis, …` | draf `content/skripsi/10-bab-01-pendahuluan.md` |

---

## 4. Scope

**Apa yang dicakup BAB I / Pendahuluan.** (a) **Konteks/objek** — definisi
objek dan domain penelitian, umumnya dimulai dari kebijakan luar negeri /
hubungan bilateral pada HI; (b) **masalah** — kesenjangan kondisi ideal vs
nyata; (c) **kajian terdahulu** — ringkasan penelitian relevan bersitasi;
(d) **celah & tujuan** — pernyataan celah, rumusan masalah, dan tujuan
([`docs/kamus-bahasa-artikel.md`](kamus-bahasa-artikel.md) §"Rangkai Argumen →
Pendahuluan").

**Apa yang dikecualikan.** (a) **Definisi teori rinci** — pada artikel, teori
dilipat ke Pendahuluan + Pembahasan, bukan bagian tersendiri
([`docs/conversion-skripsi-to-article.md`](conversion-skripsi-to-article.md)
§"Mapping table": BAB II "folded into Pendahuluan + Pembahasan"); (b) **metode
rinci** — milik bagian Metode, bukan Pendahuluan; (c) **hasil** — tidak
diungkap di Pendahuluan (kecuali sebagai janji); (d) **aspek di luar dimensi
yang diteliti** — dinyatakan eksplisit di Batasan Masalah (mis. efektivitas
klinis vaksin atau kinerja keuangan perusahaan farmasi pada draf repo).

**Lima batas scope (skripsi, A5).** rentang waktu, objek, kerangka analisis,
sumber data, dan hal yang dikecualikan
([`docs/skripsi-pedoman.md`](skripsi-pedoman.md)).

**Perbedaan scope skripsi vs artikel.**

| Aspek scope | Skripsi HI | Artikel HI |
|---|---|---|
| Bentuk | lima subbagian administratif (A1) | satu bagian kontinu, empat beat (B1) |
| Batasan | dinyatakan eksplisit di Batasan Masalah | menyatu dalam kalimat celah/tujuan |
| Teori | ditinjau di BAB II terpisah | dilipat ke Pendahuluan + Pembahasan |
| Sumber: | [`docs/skripsi-pedoman.md`](skripsi-pedoman.md); [`docs/conversion-skripsi-to-article.md`](conversion-skripsi-to-article.md) | idem |

---

## 5. Model Komponen dan Varian Struktural

### 5.1 Set subbagian skripsi (A1) vs set beat artikel (B1)

| Model | Komponen (berurutan) | Sumber |
|---|---|---|
| **Skripsi HI** (A1) | `Latar Belakang` → `Rumusan Masalah` → `Batasan Masalah` → `Tujuan` → `Manfaat` | [`docs/skripsi-pedoman.md`](skripsi-pedoman.md) |
| **Artikel HI** (B1) | konteks → penelitian terdahulu → celah → tujuan (kontinu, tanpa subbagian) | [`docs/conversion-skripsi-to-article.md`](conversion-skripsi-to-article.md) |

### 5.2 Varian judul kepala Pendahuluan yang teramati di korpus

Frekuensi keluarga "Pendahuluan" = **28/43** paper pada
`docs/ir-corpus/` ([`docs/kamus-riset-korpus-hi.md`](kamus-riset-korpus-hi.md)
§2). Varian judul kepala yang teramati (verbatim):

- `PENDAHULUAN` — mis. `hi-dinamika-bali-democracy`, `hi-jhi-umy-konstruktivis`,
  `hi-jhi-umy-malaysia`, `hi-padjir-asian-games`, `hi-padjir-desa-wisata`,
  `hi-padjir-wisatawan`.
- `Introduction` / `INTRODUCTION` — mis. `hi-cjas-southeast-asia`,
  `hi-ijss-vtuber`, `hi-jelajah-tourism`, `hi-jsps-aviation`.
- `1. Introduction` (bernomor) — mis. `hi-atlantis-china-asea-pd`,
  `hi-irscs-bahasa`, `hi-mdpi-health-silk-road`, `hi-richtmann-japan-vaccine`.
- `1.0 INTRODUCTION` (desimal) — `hi-jpr-nation-branding` (`1.0`–`5.0`).
- `Latar Belakang` (varian non-kanonik) — `hi-sentris-asian-games` (memakai
  `Latar Belakang`/`Landasan Teori`/`Analisis`, bukan
  Pendahuluan/Tinjauan/Hasil).

**Kanon repositori.** Kepala kanonik untuk artikel repositori adalah
`Pendahuluan` (id `pendahuluan`), dengan varian `Pendahuluan`, `PENDAHULUAN`,
`Introduction`, `INTRODUCTION`
([`assets/bahasa/kamus-id.yaml`](../assets/bahasa/kamus-id.yaml)
§`kepala_bagian.pendahuluan`).

**Implikasi.** Untuk artikel HI Indonesia, pilih `PENDAHULUAN` atau
`Pendahuluan`; untuk jurnal berbahasa Inggris, `Introduction`; bila jurnal
sasaran memakai penomoran, ikuti skema `N.` (8/43 paper) atau `N.0` (1/43)
([`docs/kamus-riset-korpus-hi.md`](kamus-riset-korpus-hi.md) §1 "Catatan
struktur penting").

Selain varian judul kepala di atas, **mutu judul** skripsi/artikel (direktif,
berlingkup terkendali, dan menyatakan masalah atau solusi/kontribusi) ditegakkan
oleh `tools/validators/judul.py` (JD1–JD6); rincian `docs/judul-framework.md`.

---

## 6. Pita Panjang per Bagian

Angka di bawah **terukur** dari
[`docs/bab1-corpus-stats.md`](bab1-corpus-stats.md) (Langkah 1; N=85 paper =
29 Sinta + 41 IR + 15 LibGen; panjang = token kata bagian Pendahuluan saja,
dibatasi judul Pendahuluan hingga judul seksi berikutnya).

### 6.1 Panjang kata Pendahuluan (terukur) — dasar empiris

| Korpus | N | min | median | maks | Sumber |
|---|---:|---:|---:|---:|---|
| **Sinta 1–6** | 29 | 176 | **539** | 1208 | `bab1-corpus-stats.md` §2.1 |
| **IR (`ir-corpus`)** | 41 | 90 | **893** | 3322 | `bab1-corpus-stats.md` §2.1 |
| **LibGen** (buku/artikel) | 15 | 344 | 6602 | 16181 | `bab1-corpus-stats.md` §2.1 |
| **Semua** | 85 | 90 | 778 | 16181 | `bab1-corpus-stats.md` §2.1 |

Aritmetika median (dari berkas statistik): Sinta N=29 → nilai ke-15 = 539; IR
N=41 → nilai ke-21 = 893; LibGen N=15 → nilai ke-8 = 6602. Ekstrem: Sinta min
176 (`s4-jsi`), maks 1208 (`s4-transformatika`); IR min 90
(`hi-atlantis-china-asea-pd`), maks 3322 (`hi-david-palestinian-nation-branding`,
bab-1 gaya skripsi).

### 6.2 Penanda gerak dan sitasi (terukur)

| Ukuran | Sinta | IR | LibGen | Semua | Sumber |
|---|---:|---:|---:|---:|---|
| Penanda **tujuan** | 19/29 (65.5%) | 26/41 (63.4%) | 6/15 (40.0%) | 51/85 (60.0%) | `bab1-corpus-stats.md` §2.2 |
| Penanda **celah** | 16/29 (55.2%) | 14/41 (34.1%) | 8/15 (53.3%) | 38/85 (44.7%) | `bab1-corpus-stats.md` §2.2 |
| **Sitasi** di Pendahuluan (median) | 11 (maks 48) | 7 (maks 44) | 4 (maks 68) | — | `bab1-corpus-stats.md` §2.4 |
| Modus **jumlah paragraf** | 4 paragraf (10 artikel) | 7–10 paragraf (9 artikel) | > 10 paragraf (11/15) | — | `bab1-corpus-stats.md` §2.3 |

Implikasi: penanda **tujuan** dan **celah** tidak universal (60.0% dan 44.7%)
— karena itu keduanya dinyatakan sebagai **aturan wajib** (A3/B1), bukan
sekadar deskripsi korpus: kerangka menutup celah kepatuhan yang tidak
dipenuhi mayoritas artikel.

### 6.3 Pita target dan konsistensinya dengan korpus

| Bagian | Pita target | Basis empiris |
|---|---|---|
| **Latar Belakang skripsi (A3)** | ~700–1300 kata | **di dalam** pita IR (median **893**) dan **≤** maks Sinta (**1208**) — `bab1-corpus-stats.md` §2.1; draf repo `content/skripsi/10-bab-01-pendahuluan.md` terukur **1206 kata** (di dalam pita) |
| **Pendahuluan artikel (B3)** | ~700–900 kata | berada **di dalam** pita IR (median **893**) dan di atas median Sinta (**539**) — `bab1-corpus-stats.md` §2.1 |
| **Rumusan Masalah** | ringkas: pengantar + pertanyaan bernomor (lazimnya 3) | kualitatif — korpus memuat **bagian Pendahuluan artikel**, bukan subbagian skripsi; **tidak ada angka per-subbagian** yang diukur (lihat catatan di bawah) |
| **Batasan Masalah** | ringkas: lima batas eksplisit | kualitatif (idem) |
| **Tujuan** | ringkas: butir bernomor 1:1 | kualitatif (idem) |
| **Manfaat** | 2 paragraf (teoretis + praktis) | kualitatif (idem) |

**Catatan penting tentang subbagian skripsi.** Tiga korpus mengukur **bagian
Pendahuluan artikel** (dan bab-1 buku), **bukan** subbagian administratif
skripsi (`Rumusan Masalah`, `Batasan Masalah`, `Tujuan`, `Manfaat`). Karena
itu **tidak ada angka kata per-subbagian skripsi yang dikarang** di sini; pita
untuk keempat subbagian tersebut tetap **kualitatif** ("ringkas", 2 paragraf),
mengikuti [`docs/skripsi-pedoman.md`](skripsi-pedoman.md) (A1, A4–A7). Satu
berkas bergaya skripsi teramati di korpus (`hi-david-palestinian-nation-
branding`, `Chapter 1: A Theoretical Framework`) hanya mengukur panjang **bab
utuh** (3322 kata), bukan subbagiannya.

### 6.4 Konteks tambahan yang sudah tersedia di repositori

- **Abstrak (bukan Pendahuluan):** Sinta n=29, min 137 / median 206 / maks 292
  kata; internasional n=38, min 91 / median 192 / maks 356 kata
  ([`docs/abstrak-corpus-stats.md`](abstrak-corpus-stats.md) §2.1) — patokan
  bahwa bagian pembuka jurnal berpusat pada ratusan kata.
- **Panjang artikel utuh (Sinta):** 3.000–8.000 kata / 10–20 halaman
  ([`docs/sinta-reference.md`](sinta-reference.md) §"Technical spec table").
- **BAB I–VI skripsi:** total ≥ 50 halaman
  ([`docs/skripsi-pedoman.md`](skripsi-pedoman.md) §"References & length").

---

## 7. Matriks Kepatuhan per-Tingkat

Legenda sel: **wajib** = harus ada; **disarankan** = praktik baik, bukan
syarat keras; **tidak berlaku** = aturan tidak relevan untuk tingkat itu.
Sel Scopus yang menyatakan klaim spesifik di luar bar struktural ditandai
`unverified — confirm first` (tidak ada status indeksasi jurnal yang
dikarang).

| Aturan | Sinta 3–6 | Sinta 1–2 | Scopus | Skripsi HI | Artikel HI |
|---|---|---|---|---|---|
| **A1** lima subbagian urut tetap | tidak berlaku | tidak berlaku | tidak berlaku | wajib | tidak berlaku |
| **A2** baris formula `kamus:f` | tidak berlaku | tidak berlaku | tidak berlaku | wajib | tidak berlaku |
| **A3** Latar Belakang 5 gerak, ~700–1200 kata, ≥ 15 sitasi | disarankan (gerak); pita `unverified — confirm first` | disarankan (gerak); pita `unverified — confirm first` | disarankan (gerak CARS; pita per-jurnal — `unverified — confirm first`) | wajib | disarankan (gerak) |
| **A4** Rumusan Masalah bernomor 1:1 | tidak berlaku | tidak berlaku | tidak berlaku | wajib | tidak berlaku |
| **A5** Batasan Masalah lima batas | tidak berlaku | tidak berlaku | tidak berlaku | wajib | tidak berlaku |
| **A6** Tujuan bernomor 1:1 | tidak berlaku | tidak berlaku | tidak berlaku | wajib | tidak berlaku |
| **A7** Manfaat teoretis + praktis | tidak berlaku | tidak berlaku | tidak berlaku | wajib | tidak berlaku |
| **A8** APA, ≥ 20 ref, ≥ 30% intl, ≤ 5 tahun (jendela vs `periode`, bawaan `2020–2025`; penegak `evidence_recency.py`) | disarankan | disarankan | disarankan (gaya sitasi per jurnal — `unverified — confirm first`) | wajib | disarankan (APA wajib di build repo) |
| **B1** empat beat kontinu | disarankan | disarankan | disarankan (CARS/Swales) | tidak berlaku | wajib |
| **B2** kalimat tujuan kanonik `Penelitian ini bertujuan untuk …` | disarankan | disarankan | tidak berlaku (jurnal EN lazim memakai `This article examines …`) | tidak berlaku | wajib |
| **B3** Pendahuluan artikel ~700–900 kata | disarankan; pita `unverified — confirm first` | disarankan; pita `unverified — confirm first` | disarankan (gerak CARS; pita per-jurnal — `unverified — confirm first`) | tidak berlaku | disarankan |
| **C1** impersonal (tanpa kata ganti orang I/II) | disarankan | disarankan | disarankan | wajib | wajib |
| **C2** diksi baku EYD Edisi V | disarankan | disarankan | tidak berlaku (naskah Inggris) | wajib | wajib |
| **C3** tanpa frasa AI generik | disarankan | disarankan | tidak berlaku (daftar khusus Indonesia) | wajib | wajib |
| **C4** setiap sitasi punya entri daftar pustaka | wajib | wajib | wajib | wajib | wajib |
| **C5** urutan tetap, tanpa bagian dihilangkan | disarankan | disarankan | disarankan | wajib | wajib |

**Catatan.** Kolom **Scopus** hanya menyatakan **bar struktural** yang lazim
diminta jurnal terindeks (model gerak CARS/Swales, abstrak Inggris,
pendahuluan kontinu tanpa subbagian) dengan sitasi literatur metodologis nyata
(Swales, 2014; Wardat & AlAli, 2025 — §10). **Status indeksasi Scopus sebuah
jurnal tertentu tidak dinyatakan**; klaim apa pun yang menyangkut syarat
spesifik jurnal terindeks ditandai `unverified — confirm first` dan harus
dikonfirmasi dari *Author Guidelines* jurnal sasaran.

---

## 8. Daftar Periksa Do / Don't

| ✔ Lakukan | ✘ Hindari |
|---|---|
| (Skripsi) Lima subbagian urut: Latar Belakang → Rumusan Masalah → Batasan Masalah → Tujuan → Manfaat | Mengubah urutan atau menghilangkan subbagian |
| (Artikel) Empat beat kontinu: konteks → terdahulu → celah → tujuan | Menyisipkan subbagian administratif ke Pendahuluan artikel |
| Nyatakan **celah** secara eksplisit (`terdapat celah dalam literatur …`) | Melompat dari konteks ke tujuan tanpa celah |
| Akhiri dengan tujuan kanonik `Penelitian ini bertujuan untuk …` | Tujuan tersirat / tanpa rumusan |
| Rumusan Masalah ↔ Tujuan **1:1** | Pertanyaan yang tak terjawab butir Tujuan (atau sebaliknya) |
| Batasan Masalah menyebut lima batas (waktu, objek, kerangka, data, pengecualian) | Batasan implisit / tidak menyebut pengecualian |
| Manfaat dua bagian: teoretis **dan** praktis | Hanya satu jenis manfaat |
| Sitasi APA name-year, ≥ 20 referensi, ≥ 30% internasional, ≤ 5 tahun | Gaya sitasi campur; referensi usang (> 5 tahun) |
| Ragam impersonal & pasif (`dilakukan`, `digunakan`, `dianalisis`) | Kata ganti orang (`saya`, `kami`, `kita`, `anda`) |
| Diksi baku EYD Edisi V (`analisis`, `praktik`, `standar`) | Bentuk tidak baku (`analisa`, `praktek`, `standard`) |
| Prosa lugas mulai dari fakta/objek | Frasa AI generik (`pada era digital saat ini`, `dalam rangka untuk`) |
| Setiap sitasi punya entri daftar pustaka | Sitasi tanpa entri (atau entri tanpa sitasi) |
| Pertahankan baris formula `kamus:f` verbatim (dikelola mesin) | Menyunting baris formula dengan tangan |

---

## 9. Rubrik Penilaian

Skor **0–2** per komponen; **6 komponen × 2 = maksimum 12**.

| Komponen | 0 | 1 | 2 |
|---|---|---|---|
| **Latar Belakang** | Tidak ada / tanpa gerak | Ada konteks, tetapi masalah/celah/tujuan tidak lengkap | Lima gerak lengkap (konteks → masalah → terdahulu → celah → tujuan) |
| **Rumusan Masalah** | Tidak ada | Pertanyaan ada tetapi tidak bernomor / tidak memetakan | Pertanyaan bernomor, 1:1 ke Tujuan |
| **Batasan Masalah** | Tidak ada | Menyebut sebagian batas | Lima batas eksplisit (waktu, objek, kerangka, data, pengecualian) |
| **Tujuan** | Tidak ada | Butir tidak 1:1 ke Rumusan Masalah | Butir bernomor, 1:1 ke Rumusan Masalah |
| **Manfaat** | Tidak ada | Hanya satu jenis (teoretis **atau** praktis) | Dua bagian: teoretis **dan** praktis |
| **Kepatuhan bahasa** | Ada kata ganti orang / diksi tak baku / frasa AI | Satu pelanggaran ringan | Nol pelanggaran (C1–C3) |

**Tafsiran skor total (0–12):**

- **11–12** — siap (BAB I / Pendahuluan memenuhi seluruh aturan absolut).
- **8–10** — revisi ringan (perkuat gerak celah/tujuan atau batas).
- **≤ 7** — tulis ulang bagian yang lemah sebelum melanjutkan ke bab berikutnya.

---

## 10. Sumber

### 10.1 Berkas repositori (bukti utama)

- [`docs/skripsi-pedoman.md`](skripsi-pedoman.md) — §"BAB structure with
  required sub-sections" (A1: lima subbagian BAB I); §"References & length"
  (A8: ≥ 20 referensi, ≥ 30% internasional, ≤ 5 tahun diukur terhadap `periode`
  dokumen (bawaan `2020–2025`); penegak `tools/validators/evidence_recency.py`;
  BAB I–VI ≥ 50 halaman);
  §"Ragam Bahasa" (C1–C2).
- [`docs/conversion-skripsi-to-article.md`](conversion-skripsi-to-article.md) —
  §"Rewrite rules" (B1: Introduction in 4 beats); §"Three core formulas"
  (B2: `Penelitian ini bertujuan untuk …`); §"No-pronoun rule" (C1).
- [`docs/kamus-riset-korpus-hi.md`](kamus-riset-korpus-hi.md) — §1 (43 PDF
  `docs/ir-corpus/`, tabel per-paper, varian judul kepala); §2 (Pendahuluan
  28/43, Simpulan 29/43, Metode 13/43); §4 (APA 34/43); §7 ("Argument moves"
  HI: konteks/objek → masalah → kajian terdahulu → celah/tujuan; penanda tujuan
  `Artikel ini bertujuan menjelaskan …`, `Penelitian ini bertujuan untuk …`,
  `This article examines …`; kolokasi `kepentingan nasional` 62× di 7 paper,
  `kebijakan luar negeri` 19× di 10 paper).
- [`docs/kamus-bahasa-artikel.md`](kamus-bahasa-artikel.md) — §"Rangkai
  Argumen → Pendahuluan" (empat gerak: konteks/objek, masalah, kajian
  terdahulu, celah & tujuan; penanda celah teramati; varian tujuan).
- [`docs/kamus-riset-korpus.md`](kamus-riset-korpus.md) — §7 (konvensi
  Pendahuluan korpus Sinta: subbagian `Research Gap` eksplisit `s2-jiki` 2.3,
  `s3-juti` 2.5; varian tujuan `s4-scan`, `s4-transformatika`; 29 PDF
  `docs/sinta-corpus/`).
- [`docs/sinta-reference.md`](sinta-reference.md) — §"ARJUNA 8 indicators +
  weights" (Substansi Artikel bobot 39); §"Article anatomy" (body IMRaD,
  referensi lengkap & konsisten); §"Technical spec table" (panjang artikel
  3.000–8.000 kata).
- [`assets/bahasa/kamus-id.yaml`](../assets/bahasa/kamus-id.yaml) —
  §`kepala_bagian.pendahuluan` (varian judul); §`formula` (rumus tujuan);
  §`kosakata_baku` (C2); §`frasa_ai_generik` (C3); §`abstrak`.
- [`docs/abstrak-corpus-stats.md`](abstrak-corpus-stats.md) — §2.1 (panjang
  abstrak terukur; dipakai sebagai konteks §6.2).
- [`docs/libgen-corpus/MANIFEST.md`](libgen-corpus/MANIFEST.md) — 15 PDF
  (10 buku + 5 artikel) korpus tambahan; rujukan ruang lingkup.
- Penegak: [`tools/check-bahasa.sh`](../tools/check-bahasa.sh) (C1–C3),
  [`tools/gen_kamus.py`](../tools/gen_kamus.py) (A2), `tools/validate.py papers`
  (C4).
- Draf rujukan: `content/skripsi/10-bab-01-pendahuluan.md` (lima `##`
  berurutan; 5 tag `kamus:f`; lima gerak Latar Belakang; lima batas Batasan
  Masalah; Manfaat teoretis + praktis).
- Statistik Langkah 1: [`docs/bab1-corpus-stats.md`](bab1-corpus-stats.md) —
  §2.1 (panjang kata Pendahuluan: Sinta N=29 min 176 / median 539 / maks 1208;
  IR N=41 min 90 / median 893 / maks 3322; LibGen N=15 min 344 / median 6602 /
  maks 16181); §2.2 (penanda gerak: tujuan 51/85 = 60.0%; celah 38/85 = 44.7%);
  §2.3 (modus paragraf); §2.4 (sitasi Pendahuluan: median Sinta 11, IR 7,
  LibGen 4); §1 (tabel per-paper 85 baris). Dikutip penuh di §6.

### 10.2 Literatur eksternal (rekaman nyata `scholar.py`)

- Swales, J. (2014). *Create a research space (CARS) model of research
  introductions*. In *Writing about writing: A college reader*.
  <https://marymount.edu/academics/wp-content/uploads/sites/3/2021/08/CARS-Model-of-Research-Introductions.pdf>
- Choe, H., & Hwang, B. H. (2014). *A Genre Analysis of Introductions in
  Theses, Dissertations and Research Articles Based on Swales' CARS Model*.
  응용언어학.
  <https://www.researchgate.net/profile/Hohsung-Choe/publication/284467438_A_Genre_Analysis_of_Introductions_in_Theses_Dissertations_and_Research_Articles_Based_on_Swales'CARS_Model/links/667c439dd21e220d89d4c867/A-Genre-Analysis-of-Introductions-in-Theses-Dissertations-and-Research-Articles-Based-on-SwalesCARS-Model.pdf>
- Adika, G. S. K. (2014). *Swales' Cars Model and the Metaphor of Research
  Space*. Legon Journal of the Humanities. <https://www.jstor.org/stable/48816124>
- Samraj, B. (2008). *A discourse analysis of master's theses across
  disciplines with a focus on introductions*. Journal of English for Academic
  Purposes. <https://www.sciencedirect.com/science/article/pii/S1475158508000052>
- Bunton, D. (2014). *Generic moves in Ph.D. thesis introductions*. In
  *Academic discourse*.
  <https://api.taylorfrancis.com/content/chapters/edit/download?identifierName=doi&identifierValue=10.4324/9781315838069-11&type=chapterpdf>
- Starfield, S., & Ravelli, L. J. (2006). *Self and structure in New
  Humanities research theses*. Journal of English for Academic Purposes.
  <https://www.sciencedirect.com/science/article/pii/S1475158506000270>
- Cortes, V. (2013). *The purpose of this study is to: Connecting lexical
  bundles and moves in research article introductions*. Journal of English for
  Academic Purposes.
  <https://www.sciencedirect.com/science/article/pii/S1475158512000756>
- Arsyad, S., & Zainil, Y. (2023). *Research gap strategies in article
  introductions of different rank applied linguistics journals*. Studies in
  English Language and Education.
  <https://www.researchgate.net/profile/Safnil_Arsyad2/publication/367561409_Research_gap_strategies_in_article_introductions_of_different_rank_applied_linguistics_journals/links/63d8f1a9c465a873a271c1df/Research-gap-strategies-in-article-introductions-of-different-rank-applied-linguistics-journals.pdf>
- Acob, J. R. U., & Nugroho, H. S. W. (2026). *State of the Art: Making the
  Research Gap Explicit in the Background of Research Articles*. Health
  Notions. <http://www.heanoti.com/index.php/hn/article/download/hn10201/10201>
- Kurniawan, E., & Nabilla, S. N. (2024). *Introduction in social science
  research articles by Indonesian authors: A comparative move analysis*. LLT
  Journal. <https://e-journal.usd.ac.id/index.php/LLT/article/view/8191/0>
- Nabilla, S., Kurniawan, E., & Gunawan, W. (2021). *Rhetorical move structure
  of soft and hard science research article introductions by novice Indonesian
  authors*. Bahasa dan Seni: Jurnal Bahasa, Sastra, Seni, dan Pengajarannya.
  <https://citeus.um.ac.id/jbs/vol49/iss2/1/>
- Setiawati, D., Nabilla, S. N., & Suherdi, D. (2021). *A move analysis of
  research article introduction written by Indonesian authors: The case of
  soft and hard sciences*. Thirteenth Conference on Applied Linguistics
  (CONAPLIN 2020), Atlantis Press.
  <https://www.atlantis-press.com/proceedings/conaplin-20/125956078>
- Rochma, A. F. (2025). *Rhetorical analysis in scholarly texts: Insights into
  introduction and literature review patterns*. Journal on English as a
  Foreign Language.
  <https://e-journal.iain-palangkaraya.ac.id/jefl/article/view/9095>
- Wardat, Y., & AlAli, R. (2025). *How to Publish Research Papers in
  SCOPUS-Indexed General and Educational Journals*. Educational Process:
  International Journal.
  <https://www.ceeol.com/search/article-detail?id=1338844>
- Bakry, U. S. (2016). *Pedoman Penulisan Skripsi Hubungan Internasional*.
  <https://books.google.com/books?hl=en&lr=&id=t39UEQAAQBAJ&oi=fnd&pg=PR6&dq=panduan+penulisan+pendahuluan+skripsi+hubungan+internasional>
- Jatmika, S. (2016). *SKRIPSI: Metodologi & Romantikanya*.
  <https://books.google.com/books?hl=en&lr=&id=Qw5LEQAAQBAJ&oi=fnd&pg=PP1&dq=panduan+penulisan+pendahuluan+skripsi+hubungan+internasional>
- Wæver, O. (1998). *The sociology of a not so international discipline:
  American and European developments in international relations*.
  International Organization.
  <https://www.cambridge.org/core/journals/international-organization/article/sociology-of-a-not-so-international-discipline-american-and-european-developments-in-international-relations/6EBD754B6D0E9D5EACE3F25F5E15A04F>
- Kristensen, P. M. (2012). *Dividing discipline: structures of communication
  in international relations*. International Studies Review.
  <https://academic.oup.com/isr/article-abstract/14/1/32/1832161>
- IMRaD. *Introduction — CARS model*.
  <https://imrad.se/index.php/cars>
- ARJST. *Optimized Manuscript Template (Scopus Standard)*.
  <https://publications.ngmc.ac.in/optimized-manuscript-template-scopus-standard>

### 10.3 Kueri `scholar.py` yang dipakai

```sh
python3 .claude/skills/nykripsi/scripts/scholar.py search "research article introduction move analysis CARS model" --limit 6 --json
python3 .claude/skills/nykripsi/scripts/scholar.py search "international relations journal introduction structure" --limit 6 --json
python3 .claude/skills/nykripsi/scripts/scholar.py search "panduan penulisan pendahuluan skripsi hubungan internasional" --limit 6 --json
python3 .claude/skills/nykripsi/scripts/scholar.py search "Scopus indexed journal author guidelines introduction" --limit 6 --json
python3 .claude/skills/nykripsi/scripts/scholar.py search "thesis chapter one introduction structure social science" --limit 6 --json
python3 .claude/skills/nykripsi/scripts/scholar.py search "Swales genre analysis academic introductions CARS creating a research space" --limit 6 --json
python3 .claude/skills/nykripsi/scripts/scholar.py search "rhetorical moves introduction qualitative research article Indonesian journal" --limit 6 --json
python3 .claude/skills/nykripsi/scripts/scholar.py search "panduan penulisan skripsi bab pendahuluan latar belakang rumusan masalah tujuan manfaat" --limit 6 --json
python3 .claude/skills/nykripsi/scripts/scholar.py search "introduction section research article structure context gap objective" --limit 6 --json
```

**Catatan integritas.** Seluruh rekaman di §10.2 berasal dari keluaran nyata
`scholar.py` (backend `scholar`); tidak ada judul, penulis, tahun, venue, URL,
atau DOI yang dikarang. Klaim status indeksasi Scopus tidak dinyatakan di
dokumen ini.
