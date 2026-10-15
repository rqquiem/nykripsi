# Kerangka Mutu Judul — Skripsi HI dan Artikel (Sinta/HI)

Kerangka ini menetapkan **mutu judul** penelitian agar setiap judul — judul
skripsi Hubungan Internasional maupun judul artikel (Sinta/HI) — bersifat
**direktif** (memuat tindakan/tujuan penelitian), **berlingkup terkendali**
(tidak menumpuk objek, variabel, wilayah, atau rentang waktu), dan
**menyatakan masalah atau solusi/kontribusi**. Prinsipnya: **judul adalah janji
penelitian** — ia harus dapat dibaca sebagai tindakan atas sebuah masalah atau
penawaran sebuah kontribusi, bukan sebagai label topik. Karena itu judul
**diperiksa mesin**: setiap pelanggaran menutup `make check` melalui validator
`judul` (`tools/validators/judul.py`, aturan **JD1–JD6**).

Kerangka ini **melengkapi** kerangka yang sudah ada dan tidak menggantikannya.
`docs/research-gap.md` menetapkan **ketersediaan** judul (duplikat/terlalu
mirip) dan celah penelitian; `docs/article-framework.md` dan
`docs/argument-framework.md` menetapkan anatomi artikel serta pita panjang judul
(`≤ 12–16` kata); `docs/sinta-reference.md` menetapkan anatomi dan spesifikasi
artikel Sinta; `docs/bab1-framework.md` menetapkan kerangka BAB I. Kerangka mutu
judul **tidak menggantikan** kelimanya: ia hanya menetapkan **bagaimana** sebuah
judul dinilai **direktif**, **terkendali lingkupnya**, dan **menyatakan
masalah/kontribusi**, lalu menegakkannya secara reprodusibel dan dapat diperiksa
mesin.

**Dasar normatif.** Judul akademik diarahkan oleh tiga kaidah. Pertama,
**EYD Edisi V** menetapkan penulisan judul (huruf kapital pada kata penting,
ungkapan asing dimiringkan) — lihat
<https://ejaan.kemendikdasmen.go.id/eyd/>. Kedua, panduan gaya **APA Edisi 7**
menuntut judul yang **ringkas, spesifik, dan informatif** serta menghindari
frasa berlebih (*wordiness*) — lihat
<https://apastyle.apa.org/style-grammar-guidelines/paper-format/title-page>.
Ketiga, struktur **IMRaD** menuntut judul mencerminkan tindakan penelitian
(What was done) dan kontribusinya — lihat <https://imrad.se/index.php/cars>.
Registri repositori ini menurunkan ketiga kaidah itu ke daftar konkret pada
`assets/bahasa/kamus-id.yaml` §`judul`, dan `docs/sinta-reference.md`
(§"Article anatomy") menambahkan batas panjang `≤ 12–16` kata.

---

## 1. Definisi dan Fungsi

**Definisi.** *Judul* adalah satuan teks terpendek yang menyatakan **apa yang
diteliti** (objek), **bagaimana diteliti** (tindakan/tujuan), **seberapa luas**
(lingkup), dan **mengapa penting** (masalah/kontribusi). Judul yang bermutu
adalah judul yang **direktif**: ia memuat verba aksi/tujuan yang jelas, lingkup
yang dapat dijangkau satu penelitian, serta penanda masalah atau
solusi/kontribusi.

**Fungsi kerangka.** Pertama, **menjadikan mutu judul dapat diperiksa mesin**:
JD1–JD6 menolak judul non-direktif, terlalu luas, dan tanpa masalah/kontribusi.
Kedua, **menyeragamkan penilaian lintas-venue**: judul skripsi, artikel Sinta,
artikel Scopus, dan proposal memakai rubrik yang sama. Ketiga, **mengaitkan
judul dengan celah penelitian**: judul yang baik adalah ringkasan satu kalimat
dari celah (`docs/research-gap.md`) dan tujuannya (`docs/bab1-framework.md`).

**Objek yang ditegakkan.** Validator `judul` memeriksa **setiap** judul berikut:

| Sumber | Bidang | Catatan |
|---|---|---|
| `research/judul.json` | `judul` tiap catatan | seluruh status (`selected`/`candidate`/`rejected`) |
| `templates/artikel-*-meta.yaml` | `title:` | placeholder (`Judul Artikel`, `≤`, `<`, `…`) dilewati |
| `content/skripsi/00-halaman-judul.md` | isi `{\large\bfseries …\par}` | judul skripsi, diambil via regex lalu dibersihkan dari LaTeX |

---

## 2. Tiga Mode Kegagalan Judul

Tiga mode kegagalan berikut adalah **target langsung** kerangka ini; masing-masing
memetakan ke aturan absolut di §3.

### 5a — Non-direktif (judul hanya topik)

**Cacat.** Judul berupa **frasa nomina murni** tanpa tindakan/objek penelitian:
tidak ada verba aksi yang menyatakan apa yang dilakukan peneliti.

- **Salah:** `Diplomasi Publik Tiongkok terhadap Indonesia melalui Diplomasi Vaksin pada Masa Pandemi Covid-19 Tahun 2020–2022` — menyebut topik, tetapi tidak menyatakan tindakan penelitian.
- **Benar:** `Analisis Strategi Diplomasi Publik Tiongkok terhadap Indonesia melalui Diplomasi Vaksin pada Masa Pandemi Covid-19 Tahun 2020–2022` — menambahkan penanda aksi (`Analisis`) dan solusi (`Strategi`).

**Penangkal:** **JD1** (wajib ≥ 1 penanda dari `judul_verba_aksi`).

### 5b — Lingkup terlalu luas

**Cacat.** Judul **menumpuk** banyak objek/variabel/wilayah/waktu sekaligus,
sehingga tidak dapat dijangkau satu penelitian.

- **Salah:** `Analisis Pengaruh Kebijakan Fiskal dan Moneter serta Pariwisata terhadap Pertumbuhan dan Ketimpangan di Asia dan Eropa pada Tahun 2019, 2021, dan 2023` — tiga objek, dua wilayah, tiga rentang waktu, empat penanda lingkup.
- **Benar:** `Analisis Pengaruh Kebijakan Fiskal terhadap Pertumbuhan Ekonomi di Asia Tenggara Tahun 2021` — satu objek, satu wilayah, satu waktu.

**Penangkal:** **JD2** (jumlah penanda lingkup ≤ 2, wilayah/venue ≤ 1, rentang waktu ≤ 1).

### 5c — Tanpa masalah / tanpa solusi

**Cacat.** Judul menyebut metode dan objek, tetapi **tidak** menyatakan masalah
yang diteliti maupun kontribusi yang ditawarkan.

- **Salah:** `Analisis Sentimen Publik pada Media Sosial X` — ada aksi dan objek, tetapi tidak ada masalah/kontribusi.
- **Benar:** `Analisis Sentimen Publik pada Media Sosial X untuk Pemetaan Kesenjangan Layanan` (menyatakan masalah: `kesenjangan`) atau `Kerangka Analisis Sentimen Publik pada Media Sosial X` (menyatakan kontribusi: `kerangka`).

**Penangkal:** **JD3** (wajib ≥ 1 penanda dari `judul_penanda_masalah` **atau**
`judul_penanda_solusi`).

---

## 3. Aturan Absolut (JD1–JD6)

Enam aturan berikut bersifat **absolut**: setiap pelanggaran adalah `fail` dan
menutup `make check`. Setiap butir menyebut definisi, penegak, dan sumbernya.

| Aturan | Pernyataan | Menangkal | Penegak |
|---|---|---|---|
| **JD1** | Judul **wajib** memuat ≥ 1 penanda aksi/tujuan (`judul_verba_aksi`). | 5a | `tools/validators/judul.py` |
| **JD2** | Jumlah penanda lingkup (`judul_penanda_lingkup`) ≤ 2; wilayah/venue (`judul_penanda_wilayah`) ≤ 1; rentang waktu ≤ 1. | 5b | idem |
| **JD3** | Judul **wajib** memuat ≥ 1 penanda masalah (`judul_penanda_masalah`) **atau** solusi/kontribusi (`judul_penanda_solusi`). | 5c | idem |
| **JD4** | Panjang judul dalam pita **6–16 kata**. | 5a/5b | idem |
| **JD5** | Judul **bukan** bentuk tanya (tanpa `?`) dan **tanpa** penanda kabur (`judul_terlarang`). | 5a/5c | idem |
| **JD6** | Judul **seluruhnya Indonesia** atau **seluruhnya Inggris**, tidak campuran/dwibahasa. | — | idem |

**Catatan JD3 (kebijakan repo lebih ketat daripada norma korpus).** Pada korpus
Sinta yang dikalibrasi (§6), **tidak satu pun** dari 33 judul menyatakan masalah
atau kontribusi secara eksplisit — mayoritas hanya menyatakan aksi + objek
(IMRaD-style). JD3 sengaja **lebih ketat** daripada norma itu: repositori ini
mewajibkan judul mengaitkan diri dengan celah/kontribusi (`docs/research-gap.md`),
sehingga judul yang hanya menyebut aksi + objek **tetap** `fail`. Konsekuensinya
JD3 adalah aturan yang paling mungkin menolak judul gaya Sinta yang lazim.

**Catatan JD6 (deteksi bahasa).** Bahasa dideteksi dari dua himpunan yang saling
lepas: **kata fungsi** (sinyal kuat) dan **kata khas-judul** (sinyal lemah, karena
banyak istilah dipinjam lintas bahasa). Judul dinilai **campuran** dan `fail`
bila (a) memuat kata fungsi kedua bahasa, (b) memuat kata fungsi satu bahasa
**dan ≥ 2** kata khas bahasa lain, atau (c) memuat **≥ 2 kata khas dari kedua
bahasa** sekaligus (mis. `Analisis Strategi vaccine diplomacy Tiongkok` yang
tanpa kata fungsi). Dengan begitu judul Indonesia yang memuat istilah asing
serapan (mis. `Penerapan Green Supply Chain Management …`) tetap lolos,
sedangkan judul dwibahasa sejati ditolak. Judul tanpa penanda apa pun (mis.
seluruhnya nama diri) dinilai netral dan **lolos**.

**Normalisasi.** Sebelum pencocokan, judul dinormalkan: huruf kecil, lipat-ASCII
(`é → e`, `– → spasi`), non-alfanumerik menjadi spasi; penanda dicari sebagai
token/frasa **utuh**. Panjang dihitung dari token spasi.

---

## 4. Frame (Alur Penjudulan)

Alur berikut dijalankan **sebelum** judul dimasukkan ke `research/judul.json`,
`templates/artikel-*-meta.yaml`, dan `content/skripsi/00-halaman-judul.md`.

1. **Tentukan aksi/tujuan.** Pilih verba aksi (`Analisis`, `Strategi`,
   `Evaluasi`, `Pengaruh`, `Perbandingan`, `Penerapan`, …). Ini menentukan JD1.
2. **Tentukan objek tunggal.** Satu objek/variabel utama. Hindari menyambung
   dua objek dengan `dan`/`serta`/`atau` (JD2).
3. **Tetapkan lingkup.** Satu wilayah/venue (`di Asia Tenggara`, `di Indonesia`)
   dan satu rentang waktu (satu tahun atau satu rentang) (JD2).
4. **Rumuskan masalah atau kontribusi.** Tambahkan penanda masalah
   (`kesenjangan`, `tantangan`) atau solusi/kontribusi (`kerangka`, `model`,
   `strategi`, `rekomendasi`) (JD3).
5. **Pilih satu bahasa.** Seluruh Indonesia **atau** seluruh Inggris (JD6).
6. **Uji panjang.** Hitung kata; pastikan 6–16 (JD4) dan bukan bentuk tanya (JD5).
7. **Jalankan penegak.** `python3 tools/validate.py judul`, lalu `make check`;
   lengkapi celah di `docs/research-gap.md`.

---

## 5. Model Komponen

Judul yang patuh dapat dimodelkan sebagai rangkaian komponen berikut:

| # | Komponen | Fungsi | Contoh | Aturan |
|---|---|---|---|---|
| 1 | **Penanda aksi** | menyatakan tindakan/tujuan | `Analisis`, `Strategi`, `Evaluasi` | JD1 |
| 2 | **Objek** | apa yang diteliti | `Diplomasi Publik Tiongkok` | JD2 |
| 3 | **Konteks lingkup** | wilayah/venue + waktu | `di Asia Tenggara Tahun 2021` | JD2 |
| 4 | **Penanda masalah/solusi** | mengapa penting | `untuk Pemetaan Kesenjangan` | JD3 |

**Pola ringkas:** `[Penanda Aksi] + [Objek] + [Konteks Lingkup] + [Penanda Masalah/Solusi]`.
Komponen 1 dan 4 bersifat **wajib**; komponen 3 **opsional** tetapi bila ada
dibatasi JD2. Contoh lengkap: `Analisis Strategi Diplomasi Publik Tiongkok
terhadap Indonesia melalui Diplomasi Vaksin Tahun 2020–2022`.

---

## 6. Pita dan Ambang

Ambang berikut **dikalibrasi pada korpus Sinta** (`docs/sinta-corpus/MANIFEST.md`,
kolom *Article title*, **33 judul** yang lolos verifikasi) dan pada pita dokumen
repo. Statistik korpus: **median 7 kata, rata-rata 8,3, minimum 4, maksimum 16**;
**seluruh** judul memuat kepala aksi/tujuan; **tidak satu pun** menyatakan
masalah/kontribusi secara eksplisit; **15 dari 33** judul memuat penanda
lingkup (dan **3** di antaranya memuat **2** penanda lingkup — maksimum teramati).

| Komponen | Ambang | Sumber / bukti |
|---|---|---|
| Panjang judul (JD4) | **6–16 kata** | korpus: min 4, maks 16, median 7; pita dokumen `≤ 12–16` kata (`docs/sinta-reference.md`; `docs/article-framework.md` §6) |
| Penanda lingkup (JD2) | **≤ 2** | korpus: maksimum teramati = 2 |
| Wilayah/venue (JD2) | **≤ 1** | korpus: judul terkalibrasi memakai ≤ 1 wilayah |
| Rentang waktu (JD2) | **≤ 1** | konvensi skripsi/artikel HI (satu rentang observasi) |
| Penanda aksi (JD1) | **≥ 1** | korpus: 33/33 memuat kepala aksi/tujuan |
| Penanda masalah/solusi (JD3) | **≥ 1** | **kebijakan repo** (korpus: 0/33 menyatakan masalah/kontribusi) |
| Penanda kabur (JD5) | **0** | konvensi kejelasan (APA 7) |

**Pita bawah 6 kata** dipilih meski korpus mencapai 4 kata: judul 4 kata
(`Evaluating the Sensitivity–Specificity Trade-off…`) hanya mungkin bila
memuat istilah teknis padat; pada konteks skripsi/artikel HI, judul 4–5 kata
biasanya menjadi **non-direktif** (5a). **Pita atas 16 kata** menjaga judul tetap
di dalam batas dokumen (`≤ 12–16`) sekaligus mengizinkan judul HI yang memuat
aktor + konteks + rentang waktu.

**Kalibrasi terhadap judul repo.** Keenam judul yang ditegakkan saat ini lolos:
`Strategi Pemasaran KYT …` (13 kata), `Strategi Ekspor–Impor Helm Arai …`
(8 kata), `Kerangka Baru Analisis Citra Negara 98765` (6 kata), dan judul
skripsi `Analisis Strategi Diplomasi Publik Tiongkok …` (16 kata). Judul
skripsi **gagal JD1 dan JD3** sebelum diperbaiki (lihat §10 dan
"TITLE CHANGES" pada laporan pekerjaan).

---

## 7. Matriks Kepatuhan per-Venue

Seluruh aturan bersifat **`fail`** (non-negotiable) di semua venue; yang
bervariasi hanyalah **penekanan** (aturan yang paling sering menolak).

| Aturan | Sinta 1–2 | Sinta 3–6 | Scopus | Skripsi HI | Proposal |
|---|---|---|---|---|---|
| JD1 direktif | fail | fail | fail | fail | fail |
| JD2 lingkup | fail | fail | fail | fail | fail |
| JD3 masalah/solusi | fail | fail | fail | fail | fail |
| JD4 panjang 6–16 | fail | fail | fail | fail | fail |
| JD5 bukan tanya/kabur | fail | fail | fail | fail | fail |
| JD6 satu bahasa | fail | fail | fail | fail | fail |
| **Penekanan** | JD1, JD3 | JD1, JD3 | JD1, JD4 | JD1, JD3 | JD1, JD3 |

Catatan: judul Scopus yang lazim ringkas (4–6 kata) tetap harus lolos JD1–JD3;
pita JD4 (6–16) diterapkan seragam. Untuk artikel dwibahasa (ID + EN) pada
abstrak, **judul tetap satu bahasa** (JD6) — dwibahasa hanya berlaku pada
abstrak, bukan judul.

---

## 8. Daftar Periksa Do/Don't

**Do**

- [ ] Mulai judul dengan penanda aksi/tujuan (`Analisis`, `Strategi`, `Evaluasi`).
- [ ] Pilih **satu** objek utama; sebut aktor/kepentingan nasional secara eksplisit untuk judul HI.
- [ ] Batasi ke **satu** wilayah dan **satu** rentang waktu.
- [ ] Sertakan penanda masalah (`kesenjangan`, `tantangan`) atau kontribusi (`kerangka`, `model`, `rekomendasi`).
- [ ] Pertahankan judul 6–16 kata dan satu bahasa (ID atau EN).
- [ ] Jalankan `python3 tools/validate.py judul` sebelum `make check`.

**Don't**

- [ ] Jangan memakai frasa nomina murni tanpa verba aksi (5a).
- [ ] Jangan menyambung banyak objek/wilayah/waktu dengan `dan`/`serta`/`atau` (5b).
- [ ] Jangan berhenti pada metode + objek tanpa masalah/kontribusi (5c).
- [ ] Jangan memakai penanda kabur (`berbagai aspek`, `secara umum`, `dll`, `dsb`).
- [ ] Jangan menulis judul berbentuk tanya (`?`).
- [ ] Jangan mencampur bahasa Indonesia dan Inggris dalam satu judul.

---

## 9. Rubrik Penilaian (0–2 × JD1–JD6)

Skor tiap aturan: **0** = tidak terpenuhi, **1** = terpenuhi sebagian,
**2** = terpenuhi penuh. Skor maksimum **12**. Validator `judul` menegakkan
ambang **biner** (pelanggaran = `fail`); rubrik ini untuk penilaian manusia atas
draf sebelum dijalankan.

| Aturan | 0 | 1 | 2 |
|---|---|---|---|
| JD1 direktif | tanpa penanda aksi | aksi implisit/lemah | penanda aksi eksplisit |
| JD2 lingkup | > 2 lingkup atau > 1 wilayah/waktu | tepat pada batas | satu objek, satu wilayah, satu waktu |
| JD3 masalah/solusi | tanpa keduanya | penanda samar | penanda masalah **atau** solusi eksplisit |
| JD4 panjang | < 6 atau > 16 kata | 6 atau 16 kata | 7–15 kata |
| JD5 bukan tanya/kabur | berbentuk tanya atau kabur | kabur ringan | lugas, tanpa kabur |
| JD6 bahasa | campuran | dominan satu bahasa | seluruhnya satu bahasa |

**Interpretasi:** **12** = siap submit; **10–11** = perbaikan kecil;
**≤ 9** = revisi judul sebelum `make check`.

---

## 10. Sumber

### 10.1 Berkas repositori

- `research/judul.json` — registri judul (objek yang ditegakkan; JD1–JD6).
- `tools/validators/judul.py` — penegak JD1–JD6 (validator `judul`).
- `assets/bahasa/kamus-id.yaml` §`judul` — registri penanda
  (`judul_verba_aksi`, `judul_penanda_lingkup`, `judul_penanda_wilayah`,
  `judul_penanda_masalah`, `judul_penanda_solusi`, `judul_terlarang`).
- `docs/research-gap.md` — ketersediaan judul & perumusan celah penelitian.
- `docs/sinta-reference.md` — anatomi artikel Sinta; pita judul `≤ 12–16` kata.
- `docs/article-framework.md` — anatomi & pita judul artikel (`≤ 15` kata).
- `docs/argument-framework.md` — konvensi anatomi (judul `≤ 12–16` kata).
- `docs/bab1-framework.md` — kerangka BAB I (tujuan/celah).
- `docs/sinta-corpus/MANIFEST.md` — korpus kalibrasi (33 judul, kolom *Article title*).

### 10.2 Literatur eksternal

- EYD Edisi V — penulisan judul dan huruf miring: <https://ejaan.kemendikdasmen.go.id/eyd/>.
- APA Edisi 7 — judul ringkas, spesifik, informatif: <https://apastyle.apa.org/style-grammar-guidelines/paper-format/title-page>.
- IMRaD — judul mencerminkan tindakan dan kontribusi: <https://imrad.se/index.php/cars>.

### 10.3 Venue

- Sinta 1–6 (Indonesia) — `docs/sinta-reference.md`.
- Skripsi HI (STMIK Triguna Dharma) — `docs/skripsi-pedoman.md`.
- Scopus — `docs/article-framework.md` (profil terdokumentasi).
