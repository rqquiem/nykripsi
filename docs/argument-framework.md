# Kerangka Alur Argumen & Kohesi Paragraf — Drafting Jurnal, Riset, dan Paper (Sinta, HI/IR, Skripsi, Proposal)

Kerangka ini menurunkan aturan agar sebuah tulisan ilmiah tidak **"melompat dari
topik A ke topik B"** tanpa kaitan. Setiap paragraf harus mengembangkan **satu
gagasan**, setiap transisi antarkalimat harus memiliki **kaitan leksikal** atau
**pemarkah transisi**, dan setiap batas paragraf harus menyiapkan paragraf
berikutnya. Setiap klaim dalam dokumen ini bersumber pada **berkas repositori
ini** (URL/berkas repo) atau **literatur akademik** yang terekam sesi ini — tidak
ada aturan tanpa sumber.

Kerangka ini **melengkapi** kerangka yang sudah ada dan tidak menggantikannya.
`docs/bab1-framework.md` mengatur gerak Pendahuluan (CARS/Swales) dan pita
panjangnya; `docs/abstrak-framework.md` mengatur anatomi abstrak 150–250 kata
dan 3–6 kata kunci; `docs/conversion-skripsi-to-article.md` mengatur konversi
skripsi menjadi artikel (kepala bagian kanonik + tiga rumus inti). Ketiga
kerangka itu menetapkan **apa** yang harus ada di setiap bagian; kerangka alur
argumen menetapkan **bagaimana** gagasan dirangkai antarkalimat dan antargraf
sehingga bagian-bagian itu terbaca sebagai satu argumen utuh.

---

## 1. Definisi dan Fungsi

**Alur argumen** adalah rantai gagasan antarkalimat dan antargraf yang setiap
langkahnya terkait dengan langkah sebelumnya. Prinsip pengikatnya adalah
***given-new***: **informasi lama diletakkan di awal** kalimat (sebagai titik
pijak pembaca), **informasi baru diletakkan di akhir** kalimat (sebagai muara
yang menarik pembaca ke kalimat berikutnya). Duke Graduate School merumuskannya
sebagai *"put new information last"* dan menegaskan bahwa **kalimat pertama dan
kalimat terakhir sebuah paragraf harus selaras**; Yale Poorvu Center menyebut
pola yang sama sebagai *"from old to new information"* dan menambahkan bahwa
transisi antargraf pun harus mengalir dari yang lama ke yang baru
(<https://sites.duke.edu/scientificwriting/lesson-2-cohesion-coherence-and-emphasis>;
<https://poorvucenter.yale.edu/sites/default/files/2024-12/Coherence%20and%20Flow%20From%20Old%20to%20New%20Information%20GWL%20Handout.pdf>).

**Kohesi vs koherensi.** Halliday & Hasan (1976) membedakan *kohesi* — peranti
**permukaan** yang mengikat kalimat secara eksplisit melalui lima jenis:
*reference* (rujukan: *hal ini, tersebut*), *substitution*, *ellipsis*,
*conjunction* (konjungsi/pemarkah transisi), dan *lexical cohesion*
(pengulangan kata isi/lemma) — dari *koherensi*, yaitu **kesatuan gagasan** yang
membuat paragraf terasa utuh
(<https://en.wikipedia.org/wiki/Cohesion_(linguistics)>;
<https://www.media.mit.edu/gnl/discourse/summaries/byhh.html>). Kohesi dapat
diperiksa mesin (ada/tidaknya kaitan leksikal atau pemarkah transisi); koherensi
menuntut penilaian manusia atas gagasan.

**Fungsi kerangka.** Pertama, **memandu pembaca**: alur lama → baru mengurangi
beban kognitif karena setiap kalimat berpijak pada kalimat sebelumnya. Kedua,
**mencegah lompatan topik**: aturan menolak paragraf yang berpindah gagasan
tanpa jembatan. Ketiga, **menjadikan kepatuhan dapat diperiksa mesin**: ambang
kuantitatif (Bagian 6) memungkinkan validator menolak naskah yang alurnya putus.
Lidwina (2013) menegaskan empat syarat paragraf ilmiah — **kesatuan,
pengembangan, kepaduan, kekompakan** — yang menjadi dasar K1–K5 di Bagian 3
(<https://media.neliti.com/media/publications/132320-ID-penulisan-paragraf-dalam-karya-ilmiah-ma.pdf>).

---

## 2. Lanskap Venue dan Konvensi Drafting

Alur argumen tidak berdiri di ruang hampa: ia dibentuk oleh **venue** tempat
naskah dikirim. Tabel 2.1 memetakan venue yang relevan beserta struktur wajib
dan panjangnya; Tabel 2.2 merangkum konvensi anatomi yang berlaku umum.

### Tabel 2.1 — Venue

|Jenis|Contoh|Struktur wajib|Panjang|Sumber|
|---|---|---|---|---|
|Jurnal Sinta S1–S6|Register, TELKOMNIKA (S1); IJCCS, JISEBI (S2); Sistemasi (S3); JSI, JUSIFOR (S4); JATISI, MISI (S5); JuTIK, JUPITER (S6)|IMRaD (Pendahuluan → Metode → Hasil dan Pembahasan → Simpulan → Daftar Pustaka)|3.000–8.000 kata / 10–20 halaman|`docs/sinta-reference.md`; `docs/sinta-corpus/MANIFEST.md`|
|Jurnal HI Indonesia|Jurnal Hubungan Internasional (UNAIR/UMY), Global: Jurnal Politik Internasional (UI), IJIR (AIHII), Mandala (UPNVJ), JHII (Unila), PADJIR|Pendahuluan → Metode → Hasil dan Pembahasan → Simpulan → Daftar Pustaka|5.000–7.000 kata (Global UI)|`docs/ir-corpus/MANIFEST.md`; <https://scholarhub.ui.ac.id/global/styleguide.html>|
|Jurnal akademik internasional/Scopus|(jurnal HI internasional)|IMRaD + gerak CARS|per *author guidelines*|`docs/bab1-framework.md` §10 (Swales); kolom Scopus `unverified — confirm first`|
|Skripsi HI|skripsi STMIK Triguna Dharma|BAB I lima subbagian → BAB II–VI|BAB I–VI ≥ 50 halaman; ≥ 20 referensi ≤ 5 tahun (ditegakkan pada sumber bukti via `tools/validators/evidence_recency.py`; jendela diukur terhadap `periode`, bawaan `2020–2025`)|`docs/skripsi-pedoman.md`; `docs/bab1-framework.md` A8|
|Proposal / paper riset|proposal penelitian HI|Latar Belakang → Rumusan Masalah → Tujuan & Manfaat → Tinjauan Pustaka → Metode|ringkas|`docs/skripsi-pedoman.md`; Global UI guidelines|

Global: Jurnal Politik Internasional (UI) menetapkan secara eksplisit bahwa
**Pendahuluan** memuat latar belakang, rumusan masalah (pertentangan *das sein*
vs *das sollen*), celah penelitian, kajian pustaka, kebaruan, argumen utama, dan
tujuan; badan artikel 5.000–7.000 kata; abstrak 150–200 kata ID+EN dengan 3–5
kata kunci; sitasi APA
(<https://scholarhub.ui.ac.id/global/styleguide.html>).

### Tabel 2.2 — Konvensi anatomi

|Aspek|Aturan|Sumber|
|---|---|---|
|Judul|≤ 12–16 kata|`docs/sinta-reference.md`|
|Abstrak|150–250 kata, ID + EN, tanpa sitasi|`docs/abstrak-framework.md` §4|
|Kata kunci|3–6 (idealnya 4–5)|`docs/abstrak-framework.md` §5|
|Kepala artikel kanonik|`Pendahuluan / Metode Penelitian / Hasil dan Pembahasan / Simpulan dan Saran / Ucapan Terima Kasih / Daftar Pustaka`|`docs/conversion-skripsi-to-article.md`|
|Sitasi|APA *name-year*|`docs/sinta-reference.md`; Global UI guidelines|
|Rumus inti|`Penelitian ini bertujuan untuk …`; `Hasil penelitian menunjukkan bahwa …`; `Berdasarkan hasil penelitian dan pembahasan, dapat disimpulkan bahwa …`|`docs/conversion-skripsi-to-article.md`|

Anatomi di atas menentukan **di mana** gagasan ditempatkan; aturan K1–K5 di
Bagian 3 menentukan **bagaimana** gagasan itu dirangkai agar terbaca sebagai
alur, bukan sebagai daftar.

---

## 3. Aturan Absolut (K1–K5)

Kelima aturan berikut bersifat **absolut**: naskah yang melanggarnya belum layak
disebut memiliki alur argumen. Setiap butir menyebut definisi, ambang (bila
ada), penegak, dan sumbernya.

1. **K1 — Satu gagasan per paragraf.** Setiap paragraf mengembangkan **satu**
   gagasan; **kalimat topik** berada pada **1–2 kalimat pertama**; seluruh
   kalimat lain relevan dengan gagasan itu. Sifat: **editorial** (menuntut
   penilaian gagasan), diperkuat oleh K4/K5. Sumber: Lidwina (2013) — syarat
   *kesatuan*; Risparyanto (2023); Yale.
2. **K2 — Transisi antarkalimat.** Setiap transisi antarkalimat **wajib**
   memiliki **kaitan leksikal** (pengulangan kata isi/lemma atau rujukan)
   **atau** **pemarkah transisi** terattestasi. Ambang: **≤ 30%** transisi tanpa
   kaitan. Penegak: `tools/validators/argument_flow.py`. Sumber: Halliday &
   Hasan (1976) — *lexical cohesion* & *conjunction*; daftar `konektor` di
   `assets/bahasa/kamus-id.yaml`; Duke.
3. **K3 — Batas paragraf.** Setiap batas paragraf **wajib** memiliki kaitan
   (kalimat penutup ↔ topik paragraf berikutnya) **atau** pemarkah transisi.
   Ambang: **≤ 25%** batas tanpa kaitan. Penegak: idem. Sumber: Duke (Prinsip 3
   — kalimat pertama & terakhir paragraf harus selaras); Yale (transisi
   antargraf).
4. **K4 — Larangan lompat topik.** Paragraf dengan **≥ 3 kalimat** yang **tidak
   memiliki satu pun** transisi terhubung **DILARANG**. Penegak: idem. Sumber:
   Lidwina (2013) — syarat *kepaduan*; Yale.
5. **K5 — Kepadatan paragraf.** Satu paragraf **maksimum 14 kalimat**;
   **peringatan** bila **> 50%** paragraf dalam satu berkas hanya satu kalimat.
   Penegak: idem. Sumber: pita korpus (`docs/bab1-corpus-stats.md` §2.3 modus
   4–10 paragraf/bagian); Risparyanto (2023).

K1 menuntut penilaian manusia atas **isi** gagasan, sehingga tidak dapat
diperiksa mesin; K2–K5 menuntut sifat **permukaan** (kaitan leksikal, pemarkah
transisi, jumlah kalimat) sehingga dapat ditegakkan otomatis. Karena itu K1
"diperkuat" K4/K5: paragraf yang melompat topik (K4) atau terlalu padat (K5)
hampir pasti juga melanggar kesatuan gagasan (K1).

---

## 4. Frame (Alur Drafting)

Menulis dengan alur argumen yang terjaga mengikuti prosedur lima langkah:

1. **Tetapkan tesis/tujuan.** Rumuskan satu kalimat yang menyatakan apa yang
   dibuktikan naskah. Untuk artikel, ini adalah kalimat tujuan kanonik
   `Penelitian ini bertujuan untuk …` (`docs/conversion-skripsi-to-article.md`).
2. **Susun rencana paragraf.** Sebelum menulis, buat daftar paragraf: satu
   gagasan per paragraf + kalimat topiknya. Ini memaksa K1 terpenuhi sejak
   tahap perencanaan, bukan saat revisi.
3. **Tulis dengan prinsip lama → baru.** Setiap kalimat dibuka dengan informasi
   yang sudah dikenal pembaca dan ditutup dengan informasi baru (Duke; Yale).
4. **Lakukan *reverse outline*.** Setelah draf selesai, tulis gagasan tiap
   paragraf di margin; periksa apakah urutannya logis dan tiap paragraf benar
   mengembangkan satu gagasan (Yale).
5. **Jalankan validator.** `python3 tools/validate.py argument_flow` untuk
   memastikan K2–K5 terpenuhi secara mesin.

Gerak per bagian harus mengikuti **rangkai argumen** yang terattestasi korpus di
`assets/bahasa/kamus-id.yaml` (`rangkai_argumen`): **Pendahuluan** — konteks →
masalah → kajian terdahulu → celah/tujuan; **Metode** — pendekatan → data →
prosedur; **Hasil dan Pembahasan** — temuan → tafsir → kaitan pustaka;
**Simpulan** — ringkasan temuan → jawaban tujuan → keterbatasan/saran. Urutan
kerja yang disarankan untuk konversi skripsi → artikel ada di
`docs/conversion-skripsi-to-article.md` (*recommended work order*).

---

## 5. Model Komponen (Anatomi Paragraf)

Sebuah paragraf ilmiah yang sehat tersusun dari tiga komponen fungsional:

- **Kalimat topik** (*topic sentence*) — menyatakan **klaim** paragraf,
  biasanya pada 1–2 kalimat pertama (mendukung K1).
- **Kalimat pengembang** (*supporting sentences*) — memberi **bukti,
  penjelasan, contoh, atau data** yang menopang klaim; dihubungkan ke kalimat
  topik melalui kaitan leksikal atau pemarkah transisi (mendukung K2).
- **Kalimat penutup** (*concluding sentence*) — menjembatani ke paragraf
  berikutnya, sering memakai prinsip lama → baru (mendukung K3).

**Pola pengembangan paragraf:** *deduktif* (klaim di awal, bukti menyusul),
*induktif* (bukti lebih dulu, klaim di akhir), dan *kombinasi* (klaim di awal
dan ditegaskan kembali di akhir). **Strategi pengembangan:** definisi, narasi,
data statistik, contoh, kutipan, sebab-akibat, proses, perbandingan, dan
klasifikasi. Risparyanto (2023) memetakan kesepuluh strategi ini sebagai pilihan
sadar penulis sesuai tujuan paragraf
(<https://journal.uii.ac.id/Buletin-Perpustakaan/article/download/28535/15104>);
Lidwina (2013) menekankan bahwa pilihan pola/strategi tidak mengubah kewajiban
kesatuan dan kepaduan.

---

## 6. Pita dan Ambang

### (a) Ambang yang diperiksa mesin

|Parameter|Nilai|Tingkat|
|---|---|---|
|Maksimum kalimat per paragraf|**14**|fail (K5)|
|Rasio paragraf satu-kalimat|**0.50**|warn (K5)|
|Rasio transisi antarkalimat tanpa kaitan|**0.30**|fail (K2)|
|Rasio batas paragraf tanpa kaitan|**0.25**|fail (K3)|

### (b) Pita panjang dari korpus

|Aspek|Pita|Sumber|
|---|---|---|
|Pendahuluan artikel|~700–900 kata|`docs/bab1-framework.md` B3|
|Abstrak|150–250 kata|`docs/abstrak-framework.md` §4|

Ambang pada (a) dikalibrasi pada **8 berkas** repositori ini
(`content/artikel/artikel-sinta.md`, `content/artikel/artikel-kyt.md`, dan enam
bab `content/skripsi/1[0-5]-*.md`) dan **lulus**; paragraf melompat buatan
gagal. Bila kelak muncul berkas sah yang melampaui ambang, konstanta di
`tools/validators/argument_flow.py` **dan** tabel (a) di dokumen ini harus
diubah **bersamaan** agar tetap selaras.

---

## 7. Matriks Kepatuhan per-Tingkat

|Aturan|Sinta 1–2|Sinta 3–6|Scopus|Skripsi HI|Proposal|
|---|---|---|---|---|---|
|K1 — Satu gagasan per paragraf|wajib|wajib|wajib|wajib|wajib|
|K2 — Transisi antarkalimat|wajib|wajib|wajib|wajib|wajib|
|K3 — Batas paragraf|wajib|wajib|wajib|wajib|wajib|
|K4 — Larangan lompat topik|wajib|wajib|wajib|wajib|wajib|
|K5 — Kepadatan paragraf|wajib|wajib|wajib|wajib|wajib|

K1–K5 **wajib** untuk semua kolom: alur argumen adalah syarat kelayakan dasar,
bukan pilihan gaya. Kolom **Scopus** ditandai **`unverified — confirm first`**:
status indeksasi venue internasional tidak dapat diverifikasi dari korpus lokal,
konsisten dengan sikap `docs/subject-framework.md` §8 yang menandai klaim tak
terverifikasi secara eksplisit.

---

## 8. Daftar Periksa Do/Don't

|Lakukan (Do)|Hindari (Don't)|
|---|---|
|Mulai kalimat dengan informasi lama|Mulai dengan konsep baru tanpa kaitan|
|Pakai pemarkah transisi terattestasi (Hal ini, Selain itu, Dengan demikian)|Lompat topik antarparagraf tanpa jembatan|
|Satu gagasan per paragraf|Menumpuk beberapa argumen dalam satu paragraf|
|Kalimat penutup menyiapkan paragraf berikutnya|Paragraf berhenti tanpa jembatan|
|Pakai konektor terattestasi korpus|Frasa AI generik|

Pemarkah transisi dan konektor pada kolom "Lakukan" harus berasal dari daftar
`konektor` di `assets/bahasa/kamus-id.yaml` (`sehingga, berdasarkan, karena, hal
ini, agar, adapun, sedangkan, namun, selain itu, guna, dengan demikian, oleh
karena itu, lebih lanjut, sejalan dengan, yaitu, kemudian, selanjutnya, pertama,
kedua, meskipun, meskipun demikian, namun demikian, misalnya, sebagai contoh,
akan tetapi, walaupun, oleh sebab itu, di sisi lain, sementara itu, …`) —
frasa di luar daftar terattestasi berisiko terbaca sebagai gaya generik.

---

## 9. Rubrik Penilaian

Nilai **0–2** untuk setiap komponen K1–K5; skor maksimum **10**.

|Komponen|0|1|2|
|---|---|---|---|
|K1 — Satu gagasan per paragraf|Banyak paragraf tanpa gagasan tunggal|Sebagian paragraf melanggar|Setiap paragraf satu gagasan + kalimat topik di awal|
|K2 — Transisi antarkalimat|> 30% transisi tanpa kaitan|20–30% tanpa kaitan|≤ 20% tanpa kaitan|
|K3 — Batas paragraf|> 25% batas tanpa kaitan|15–25% tanpa kaitan|≤ 15% tanpa kaitan|
|K4 — Larangan lompat topik|Ada paragraf ≥ 3 kalimat tanpa transisi|—|Tidak ada paragraf melompat|
|K5 — Kepadatan paragraf|Ada paragraf > 14 kalimat|Paragraf padat namun < 14|Setiap paragraf ≤ 14 kalimat|

**Tafsiran:** **10** = patuh penuh; **7–9** = revisi ringan; **4–6** = perlu
menulis ulang paragraf lemah; **≤ 3** = alur argumen belum layak.

---

## 10. Sumber

### 10.1 Berkas repositori

- `docs/bab1-framework.md` — gerak Pendahuluan (CARS/Swales) + pita panjang.
- `docs/bab1-corpus-stats.md` — statistik korpus Pendahuluan (§2.1, §2.3).
- `docs/abstrak-framework.md` — anatomi abstrak 150–250 kata + kata kunci (§4, §5).
- `docs/conversion-skripsi-to-article.md` — kepala kanonik + tiga rumus inti.
- `docs/sinta-reference.md` — Sinta S1–S6 + ARJUNA + anatomi artikel.
- `docs/skripsi-pedoman.md` — pedoman skripsi (BAB I lima subbagian; ≥ 20 referensi).
- `docs/subject-framework.md` — sikap klaim `unverified — confirm first` (§8).
- `assets/bahasa/kamus-id.yaml` — `konektor`, `rangkai_argumen`, `pembuka_kalimat`.
- `docs/kamus-bahasa-artikel.md` — ragam bahasa artikel.
- `docs/ir-corpus/MANIFEST.md` — venue HI Indonesia.
- `docs/sinta-corpus/MANIFEST.md` — venue Sinta.
- `tools/validators/argument_flow.py` — penegak K2–K5.

### 10.2 Literatur eksternal

- Halliday, M. A. K., & Hasan, R. (1976). *Cohesion in English*. Longman.
  <https://en.wikipedia.org/wiki/Cohesion_(linguistics)> ;
  <https://www.media.mit.edu/gnl/discourse/summaries/byhh.html>
- Duke Graduate School. *Lesson 2: Cohesion, Coherence, and Emphasis*.
  <https://sites.duke.edu/scientificwriting/lesson-2-cohesion-coherence-and-emphasis>
- Yale Poorvu Center. *Coherence and Flow: From Old to New Information*.
  <https://poorvucenter.yale.edu/sites/default/files/2024-12/Coherence%20and%20Flow%20From%20Old%20to%20New%20Information%20GWL%20Handout.pdf>
- Risparyanto, A. (2023). *Strategi Pengembangan Paragraf dalam Membuat Karya
  Tulis Ilmiah*. Buletin Perpustakaan UII, 6(1), 65–79.
  <https://journal.uii.ac.id/Buletin-Perpustakaan/article/download/28535/15104>
- Lidwina, S. (2013). *Penulisan Paragraf dalam Karya Ilmiah Mahasiswa*. Jurnal
  STIE Semarang, 5(1).
  <https://media.neliti.com/media/publications/132320-ID-penulisan-paragraf-dalam-karya-ilmiah-ma.pdf>
- Global: Jurnal Politik Internasional (UI). *Final Manuscript Preparation
  Guidelines*. <https://scholarhub.ui.ac.id/global/styleguide.html>
- Swales, J. M. — gerak CARS (via `docs/bab1-framework.md` §10).

### 10.3 Venue HI Indonesia

Jurnal Hubungan Internasional (UNAIR), Jurnal Hubungan Internasional (UMY),
Global: Jurnal Politik Internasional (UI), Indonesian Journal of International
Relations (AIHII), Mandala (UPNVJ), Jurnal Hubungan Internasional Indonesia
(Unila), Padjadjaran Jurnal Ilmu Hubungan Internasional (PADJIR), Jurnal
Interaksi, Jurnal Dinamika (Bali) — lihat Tabel 2.1 dan `docs/ir-corpus/MANIFEST.md`.
