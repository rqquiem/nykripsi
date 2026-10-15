# Bahasa Artikel — Ragam Bahasa Ilmiah Indonesia

Sourced rules for the **authentic Indonesian academic register** used by
Sinta-indexed journals. Every rule below is tied to a source URL (see
[`## Sumber`](#sumber)). This document is enforced by the register linter
(`tools/check-bahasa.sh`, run via `make check`).

> Struktur, rangkai argumen, dan leksikon diturunkan dari korpus: lihat [docs/kamus-bahasa-artikel.md](kamus-bahasa-artikel.md).

## Ragam Bahasa Ilmiah Indonesia

Academic Indonesian is **impersonal and objective**: the writing reports what was
done and found, not who did it.

- **Passive preference.** Prefer passive verb forms for methods and findings:
  `dilakukan`, `digunakan`, `dikumpulkan`, `dianalisis`. Instead of "peneliti
  mengumpulkan data" write "data dikumpulkan".
- **No first/second person pronouns.** Do not use `saya`, `aku`, `kami`, `kita`,
  `anda`, `kamu`, `kalian` in body text.
- **Impersonal self-reference.** `penulis` and `peneliti` are allowed as
  impersonal self-reference (e.g. "peneliti berasumsi bahwa …").
- **Hedging.** Qualify claims with `cenderung`, `dapat dikatakan`, `kemungkinan`,
  `diduga` rather than absolute assertions.

Sources: https://mplk.politanikoe.ac.id/images/pdf/BA_Kuliah_Teknik_Penulisan/001.Hakikat_dan_Karakteristik_Karya_Ilmiah.pdf ,
https://ojs.unm.ac.id/Insani/article/download/3986/2345

## Kosakata Baku (EYD Edisi V)

Use standard (baku) diction per **EYD Edisi V** (Badan Bahasa). Common
non-standard → standard pairs:

| Tidak baku | Baku |
|------------|------|
| analisa | analisis |
| praktek | praktik |
| merubah | mengubah |
| aktifitas | aktivitas |
| hipotesa | hipotesis |
| sistim | sistem |
| standard | standar |
| jadual | jadwal |
| obyek | objek |
| metoda | metode |

Sources: EYD Edisi V — https://ejaan.kemendikdasmen.go.id/eyd/ ; Badan Bahasa
(PUEBI) — https://badanbahasa.kemendikdasmen.go.id/resource/doc/files/Salinan_RKKB_PUEBI.pdf ;
https://lmsspada.kemdiktisaintek.go.id/pluginfile.php/648755/mod_folder/content/0/Artikel%20Ilmiah/ANALISIS_PENGGUNAAN_TATA_BAHASA_INDONESIA_DALAM_PENULISAN_KARYA_TULIS_ILMIAH.pdf?forcedownload=1

## Kepala Bagian Standar

**Canonical five** (IMRaD-style):

> `Pendahuluan; Metode (Penelitian); Hasil dan Pembahasan; Simpulan (dan Saran);
> Daftar Pustaka`

**Chosen authentic majority set** (used by this repo's article template):

> `Pendahuluan / Metode Penelitian / Hasil dan Pembahasan / Simpulan dan Saran /
> Ucapan Terima Kasih / Daftar Pustaka`

**Observed variants** across journals: `Kesimpulan`, `Penutup`, `Bahan dan
Metode`, `Materi dan Metode`.

Sources: https://jurnal.unikastpaulus.ac.id/index.php/jpkm/guidelines ,
https://ejurnal.fapetkan.untad.ac.id/index.php/agrisains/authorguidelines ,
https://cdn.undiksha.ac.id/wp-content/uploads/sites/10/2022/03/19222330/JPPMI_Template.pdf

## Formula Kalimat

Verbatim sentence templates sourced from Indonesian journals:

| Fungsi | Formula |
|--------|---------|
| Tujuan (purpose) | `Penelitian ini bertujuan untuk …` |
| Metode (method) | `Penelitian ini menggunakan pendekatan …` |
| Hasil (results) | `Hasil penelitian menunjukkan bahwa …` ; `Berdasarkan hasil pengujian …` |
| Simpulan (conclusion) | `Berdasarkan hasil penelitian dan pembahasan, dapat disimpulkan bahwa …` |
| Keterbatasan (limitation) | `Meskipun penelitian ini …, masih terdapat beberapa keterbatasan.` |

Sources: https://jurnal.uin-palangkaraya.ac.id/mipa/article/download/10351/3254/32674 ,
https://jurnal.stie-aas.ac.id/index.php/jap/article/download/6632/pdf/25938 ,
https://jurnal.poliupg.ac.id/index.php/snp2m/article/download/494/421/1398

## Kutipan dalam Teks (APA name-year)

Narrative and parenthetical citation phrasing:

- Narrative: `Menurut X (2020), …` ; `X (2020) menyatakan bahwa …` ;
  `penelitian oleh X (2020) menunjukkan bahwa …`
- Parenthetical: `(X, 2020)`
- Multiple: `(X, 2020; Y, 2021)`
- Two authors: join with `dan` in Indonesian narrative and `&` inside parentheses.
- Three or more authors: use `et al.`

Sources: https://sevima.com/inilah-5-cara-mengutip-dari-jurnal-yang-umum-digunakan ,
https://ejurnal.fapetkan.untad.ac.id/index.php/agrisains/authorguidelines

## Abstrak dan Kata Kunci

- Label: **`Abstrak`**.
- **One continuous paragraph**; no citations, abbreviations, or footnotes.
- Component order: **latar belakang → tujuan → metode → hasil → simpulan**.
- Length: **100–250 words** (journals vary **100–300**).
- Followed by **`Kata Kunci:`**.
- **Bilingual (ID + EN)** is near-universal.

Sources: https://pskp.kemendikdasmen.go.id/assets_front/uploads/pengumuman/01_PanduanPenulisanJurnalPuslitjak.pdf ,
https://ejournal.brin.go.id/jmi/about/submissions ,
https://journal.ipb.ac.id/index.php/jtanah/article/download/25680/16711

## Daftar Periksa

Mirrors the register linter (`tools/check-bahasa.sh`) run by `make check`:

- [ ] No first/second person pronouns (`saya`, `aku`, `kami`, `kita`, `anda`, `kamu`, `kalian`).
- [ ] Baku diction only — none of the non-standard words in the table above.
- [ ] The six authentic article headings are present (`Pendahuluan`, `Metode Penelitian`,
      `Hasil dan Pembahasan`, `Simpulan dan Saran`, `Ucapan Terima Kasih`, `Daftar Pustaka`).
- [ ] Core formulas used: `Penelitian ini bertujuan untuk …`,
      `Hasil penelitian menunjukkan bahwa …`,
      `Berdasarkan hasil penelitian dan pembahasan, dapat disimpulkan bahwa …`.
- [ ] Tidak ada em dash `—` atau hyphen berspasi ` - ` di prosa; en dash `–` hanya untuk rentang angka (LT8; `assets/bahasa/kamus-id.yaml` §`tanda_pisah`).
- [ ] Setiap istilah teknis §`istilah_teknis` diikuti padanan Inggris dalam kurung pada kemunculan prosa pertama, miring bila padanannya istilah asing (LT9; `assets/bahasa/kamus-id.yaml` §`istilah_teknis`).

## Register Anti-AI (Gaya Korpus)

Bagian ini merangkum bukti dari dua korpus repo ini: korpus HI/IR
(`docs/ir-corpus/`, 43 berkas) dan korpus Sinta SI
(`docs/sinta-corpus/`, 29 berkas). Hitungan lengkap ada di
[`docs/kamus-riset-korpus-hi.md`](kamus-riset-korpus-hi.md) §10–14 dan
[`docs/kamus-riset-korpus.md`](kamus-riset-korpus.md) §12–16.

**Prinsip**: tulis dengan **pemarkah, kolokasi, dan pembuka yang benar-benar
dipakai penulis jurnal** (terattestasi di korpus), **hindari frasa AI generik**
yang absen dari korpus, dan **pertahankan hedging** ilmiah. Register yang
diajarkan linter (`tools/check-bahasa.sh`) sudah selaras dengan korpus; tabel
di bawah memberi padanan konkret "pakai ini / jangan ini".

### Do / Don't (dengan sitasi korpus)

| Pakai (terattestasi) | Jangan (absen/generik) | Bukti korpus |
|---|---|---|
| `Hal ini …` (68× HI; 33× SI) | `dalam era digital saat ini` (0×) | HI §11.2, SI §13.2 |
| `Selain itu …` (52× HI; 19× SI) | `seiring dengan perkembangan zaman` (0×) | HI §11.1, SI §13.1 |
| `Dengan demikian …` (17× HI; 8× SI) | `tidak dapat dipungkiri` (HI 2×, SI 0×) | HI §11.1, SI §13.1 |
| `Berdasarkan hasil …` (28× HI; 75× SI) | `perlu dicatat bahwa` (0×) | HI §11.1, SI §13.1 |
| `Hasil penelitian …` (HI 6×; SI 27×) | `penting untuk dicatat bahwa` (0×) | HI §11.2, SI §13.1 |
| `menunjukkan bahwa` (HI 22×; SI 35×) | `memainkan peran penting` (HI 3×, SI 1×) | HI §10.3, SI §12.3 |
| `menggunakan metode …` (SI 50×) | `memiliki peran penting` (0×) | SI §12.3 |
| `menghasilkan akurasi` (SI 24×) | `dalam rangka untuk` (0×) | SI §12.3 |
| `membangun citra` (HI 4×) | `sangat krusial` (0×) | HI §10.3 |
| `kepentingan nasional` (HI 62×) | `kompleks dan beragam` (0×) | HI §10.1 |
| `cenderung` / `berpotensi` / `dapat dikatakan` (hedging) | `pasti` / `wajib` / `mutlak` (≈0×) | HI §12, SI §14 |
| `guna` (kata utuh, HI/SI 6× each) | `dalam konteks ini` (HI 2×, SI 0×) | HI §11.1, SI §13.1 |

### Aturan ringkas

1. **Pembuka & konektor**: pakai pemarkah korpus — `Hal ini`, `Selain itu`,
   `Dengan demikian`, `Berdasarkan hasil`, `Hasil penelitian`,
   `menunjukkan bahwa`. Semua terattestasi lintas dua korpus.
2. **Kolokasi**: ikuti pola korpus — `menggunakan metode/algoritma <X>`,
   `melatih model`, `menghasilkan/memperoleh akurasi` (SI); `membangun citra`,
   `meningkatkan citra positif`, `kepentingan nasional`, `diplomasi publik`
   (HI).
3. **Hindari frasa AI generik**: `dalam era digital saat ini`,
   `seiring dengan perkembangan zaman`, `tidak dapat dipungkiri`,
   `perlu dicatat bahwa`, `penting untuk dicatat bahwa`,
   `memiliki peran penting`, `dalam rangka untuk`, `sangat krusial`,
   `kompleks dan beragam`, `sebagai kesimpulan` — semuanya **0×** di kedua
   korpus (beberapa hanya 1–4× terpusat pada satu artikel).
4. **Pertahankan hedging**: `cenderung`, `dapat dikatakan`, `berpotensi`,
   `umumnya`, `relatif` — jauh lebih lazim daripada booster absolut.
5. **Tipografi**: simbol `%` menempel angka dengan koma desimal
   (`73,57%`, `12,92%`); istilah asing teknis dibiarkan verbatim
   (`soft power`, `dataset`); kutipan memakai tanda melengkung `“…”`.

## Tipografi: Tanda Pisah dan Istilah Teknis Dwibahasa

Dua kaidah tipografi tambahan ditegakkan mesin oleh
`tools/validators/layout_typography.py` (lihat juga
[`docs/layout-framework.md`](layout-framework.md) LT8 dan LT9).

**Tanda pisah (LT8).** Pada prosa akademik:

- **EM DASH `—` (U+2014) dilarang.** Gantikan dengan koma, titik dua, atau
  titik, mis. `kebijakan ini, yang diambil pada 2020, terbukti …` bukan
  `kebijakan ini — yang diambil pada 2020 — terbukti …`.
- **HYPHEN ASCII BERSPASI ` - ` dilarang.** Gantikan dengan koma, titik dua,
  atau titik.
- **EN DASH `–` (U+2013) hanya untuk rentang angka**, mis. `2020–2022`,
  `hlm. 15–20`, `[7]–[9]`. Jangan pakai en dash sebagai penghubung klausa.
- **Hyphenasi otomatis ditekan.** Kedua preamble
  (`templates/skripsi-preamble.tex`, `templates/artikel-preamble.tex`) memuat
  `\hyphenpenalty=10000` dan `\exhyphenpenalty=10000`, sehingga tidak ada
  hyphen yang muncul pada kata yang terpotong di ujung baris.

Sumber: `assets/bahasa/kamus-id.yaml` §`tanda_pisah` (konvensi "tanda pisah");
`templates/skripsi-preamble.tex`; `templates/artikel-preamble.tex`.

**Istilah teknis dwibahasa (LT9).** Setiap istilah teknis Indonesia tingkat
lanjut yang terdaftar di `assets/bahasa/kamus-id.yaml` §`istilah_teknis`
**wajib** diikuti padanan bahasa Inggrisnya dalam tanda kurung pada
**kemunculan prosa pertama**: `istilah (english gloss)`. Bila padanan itu
sendiri istilah asing yang terdaftar di §`istilah_asing`, tulis padanannya
miring: `istilah (*english gloss*)` (EYD Edisi V G.3). Dikecualikan: blok
abstrak, tabel, *caption*, label kata kunci, *fence* kode, dan komentar.

Sumber: `assets/bahasa/kamus-id.yaml` §`istilah_teknis` dan §`istilah_asing`;
[`docs/layout-framework.md`](layout-framework.md) LT9.

## Korpus Studi

The verified journals behind these rules — 17 journals across Sinta 1–6, with
downloaded article PDFs — live in
[`docs/sinta-corpus/MANIFEST.md`](sinta-corpus/MANIFEST.md).

| # | Slug | Sinta | Journal | Publisher | Article (year) | Language | PDF URL |
|---|------|-------|---------|-----------|----------------|----------|---------|
| 1 | `s1-register` | 1 | Register: Jurnal Ilmiah Teknologi Sistem Informasi | Unipdu Jombang | Robust Classification of Beef and Pork Images… (2025) | English | https://journal.unipdu.ac.id/index.php/register/article/view/4045/1901 |
| 2 | `s1-telkomnika` | 1 | TELKOMNIKA | Universitas Ahmad Dahlan | Optimization of MSMEs promotion strategy using GIS… (2026) | English | https://www.telkomnika.uad.ac.id/index.php/TELKOMNIKA/article/download/26692/12359 |
| 3 | `s2-resti` | 2 | Jurnal RESTI | IAII | Reliable Indonesian Academic Service Chatbot… (2026) | English | https://jurnal.iaii.or.id/index.php/RESTI/article/download/8018/1340 |
| 4 | `s2-jtiik` | 2 | JTIIK | Universitas Brawijaya | Evaluasi Adopsi Sistem Informasi Pemilu Digital… (2026) | Indonesian | resolve from article page: https://jtiik.ub.ac.id/index.php/jtiik/en/article/view/11619 |
| 5 | `s2-ijccs` | 2 | IJCCS | IndoCEISS / UGM | Predicting Resale Prices using Random Forests… (2025) | English | https://journal.ugm.ac.id/ijccs/article/download/103967/42783 |
| 6 | `s2-jisebi` | 2 | JISEBI | Universitas Airlangga | Information Quality of Business Intelligence Systems… (2023) | English | https://e-journal.unair.ac.id/JISEBI/article/download/45098/26591 |
| 7 | `s3-sinkron` | 3 | Sinkron | Politeknik Ganesha Medan | Evaluating the Sensitivity–Specificity Trade-off… (2026) | English | https://jurnal.polgan.ac.id/index.php/sinkron/article/view/16797/4353 |
| 8 | `s3-sistemasi` | 3 | Sistemasi: Jurnal Sistem Informasi | Universitas Islam Indragiri | Heart Disease Prediction using Cost-sensitive Random Forest… (2026) | English | https://sistemasi.ftik.unisi.ac.id/index.php/stmsi/article/view/6482/1373 |
| 9 | `s4-zonasi` | 4 | ZONAsi: Jurnal Sistem Informasi | Universitas Lancang Kuning | PENGARUH KEAMANAN DAN PRIVASI… (2026) | Indonesian | https://journal.unilak.ac.id/index.php/zn/article/view/34847/9850 |
| 10 | `s4-jsi` | 4 | Jurnal Sains dan Informatika (JSI) | Politeknik Negeri Tanah Laut | Klasifikasi Sampah Plastik di Laut… (2026) | Indonesian | https://jsi.politala.ac.id/index.php/JSI/article/view/1606/220 |
| 11 | `s4-jusifor` | 4 | JUSIFOR | Universitas Islam Raden Rahmat | Penilaian Kinerja Layanan TI SIPP… (2026) | Indonesian | https://ejournal.uniramalang.ac.id/jusifor/en/article/view/8532/5871 |
| 12 | `s5-jatisi` | 5 | JATISI | Universitas Multi Data Palembang | Penerapan Machine Learning Algoritma Random Forest… (2025) | Indonesian | https://jurnal.mdp.ac.id/index.php/jatisi/article/download/10917/2477 |
| 13 | `s5-misi` | 5 | MISI | STMIK Lombok | Implementasi Chatbot pada Telegram… (2025) | Indonesian | http://e-journal.stmiklombok.ac.id/index.php/misi/article/download/1681/467 |
| 14 | `s5-nuansa` | 5 | Nuansa Informatika | Universitas Kuningan | Development of a VR Metaverse System… (2026) | English | https://journal.fkom.uniku.ac.id/ilkom/article/download/445/141 |
| 15 | `s5-intek` | 5 | INTEK | Universitas Muhammadiyah Purworejo | Pengembangan Multimedia Pembelajaran Interaktif… (2024) | Indonesian | https://jurnal.umpwr.ac.id/index.php/intek/article/view/5251/2390 |
| 16 | `s6-jutik` | 6 | JuTIK | Universitas Dhyana Pura | Penerapan SimpleQueue pada Bandwidth Management… (2026) | Indonesian | https://jurnal.undhirabali.ac.id/index.php/jutik/article/download/3792/4550 |
| 17 | `s6-jupiter` | 6 | JUPITER | Universitas Komputer Indonesia | Sistem Penilaian Kinerja Pegawai dengan AHP… (2025) | Indonesian | https://ojs.unikom.ac.id/index.php/jupiter/article/download/17612/5296 |

## Sumber

- Register / karakteristik karya ilmiah:
  https://mplk.politanikoe.ac.id/images/pdf/BA_Kuliah_Teknik_Penulisan/001.Hakikat_dan_Karakteristik_Karya_Ilmiah.pdf ,
  https://ojs.unm.ac.id/Insani/article/download/3986/2345
- EYD Edisi V: https://ejaan.kemendikdasmen.go.id/eyd/ ,
  https://badanbahasa.kemendikdasmen.go.id/resource/doc/files/Salinan_RKKB_PUEBI.pdf ,
  https://lmsspada.kemdiktisaintek.go.id/pluginfile.php/648755/mod_folder/content/0/Artikel%20Ilmiah/ANALISIS_PENGGUNAAN_TATA_BAHASA_INDONESIA_DALAM_PENULISAN_KARYA_TULIS_ILMIAH.pdf?forcedownload=1
- Heading set: https://jurnal.unikastpaulus.ac.id/index.php/jpkm/guidelines ,
  https://ejurnal.fapetkan.untad.ac.id/index.php/agrisains/authorguidelines ,
  https://cdn.undiksha.ac.id/wp-content/uploads/sites/10/2022/03/19222330/JPPMI_Template.pdf
- Formula kalimat: https://jurnal.uin-palangkaraya.ac.id/mipa/article/download/10351/3254/32674 ,
  https://jurnal.stie-aas.ac.id/index.php/jap/article/download/6632/pdf/25938 ,
  https://jurnal.poliupg.ac.id/index.php/snp2m/article/download/494/421/1398
- Kutipan APA: https://sevima.com/inilah-5-cara-mengutip-dari-jurnal-yang-umum-digunakan ,
  https://ejurnal.fapetkan.untad.ac.id/index.php/agrisains/authorguidelines
- Abstrak + kata kunci:
  https://pskp.kemendikdasmen.go.id/assets_front/uploads/pengumuman/01_PanduanPenulisanJurnalPuslitjak.pdf ,
  https://ejournal.brin.go.id/jmi/about/submissions ,
  https://journal.ipb.ac.id/index.php/jtanah/article/download/25680/16711
- Sinta / ARJUNA provenance: https://sinta.kemdiktisaintek.go.id ,
  https://arjuna.kemdiktisaintek.go.id
