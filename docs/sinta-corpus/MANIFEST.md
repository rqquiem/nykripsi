# Sinta Corpus — Manifest

33 verified Sinta 1–6 journals (Indonesian computing/IS field) gathered as a local
studyable corpus of article PDFs. Files live in `docs/sinta-corpus/<slug>.pdf`;
`manifest.tsv` is the machine-readable source used by `tools/fetch_corpus.sh`
(`make corpus`).

Status after `bash tools/fetch_corpus.sh`: **OK=29 FAILED=4** (requirement is ≥ 10).

## Journals

| # | Slug | Sinta | Journal | Publisher | Article title | Year | Article URL | PDF URL | Local file | Status |
|---|------|-------|---------|-----------|---------------|------|-------------|---------|------------|--------|
| 1 | `s1-register` | 1 | Register: Jurnal Ilmiah Teknologi Sistem Informasi | Unipdu Jombang | Robust Classification of Beef and Pork Images… | 2025 | https://journal.unipdu.ac.id/index.php/register/article/view/4045 | https://journal.unipdu.ac.id/index.php/register/article/view/4045/1901 | `s1-register.pdf` | OK |
| 2 | `s1-telkomnika` | 1 | TELKOMNIKA | Universitas Ahmad Dahlan | Optimization of MSMEs promotion strategy using GIS… | 2026 | https://www.telkomnika.uad.ac.id/index.php/TELKOMNIKA/article/view/26692 | https://www.telkomnika.uad.ac.id/index.php/TELKOMNIKA/article/download/26692/12359 | `s1-telkomnika.pdf` | OK |
| 3 | `s2-resti` | 2 | Jurnal RESTI | IAII | Reliable Indonesian Academic Service Chatbot… | 2026 | https://jurnal.iaii.or.id/index.php/RESTI/article/view/8018 | https://jurnal.iaii.or.id/index.php/RESTI/article/download/8018/1340 | `s2-resti.pdf` | OK |
| 4 | `s2-jtiik` | 2 | JTIIK | Universitas Brawijaya | Evaluasi Adopsi Sistem Informasi Pemilu Digital… | 2026 | https://jtiik.ub.ac.id/index.php/jtiik/en/article/view/11619 | _(resolved from article page)_ | — | FAILED |
| 5 | `s2-ijccs` | 2 | IJCCS | IndoCEISS / UGM | Predicting Resale Prices using Random Forests… | 2025 | https://journal.ugm.ac.id/ijccs/article/view/103967 | https://journal.ugm.ac.id/ijccs/article/download/103967/42783 | `s2-ijccs.pdf` | OK |
| 6 | `s2-jisebi` | 2 | JISEBI | Universitas Airlangga | Information Quality of Business Intelligence Systems… | 2023 | https://e-journal.unair.ac.id/JISEBI/article/view/45098 | https://e-journal.unair.ac.id/JISEBI/article/download/45098/26591 | `s2-jisebi.pdf` | OK |
| 7 | `s3-sinkron` | 3 | Sinkron | Politeknik Ganesha Medan | Evaluating the Sensitivity–Specificity Trade-off… | 2026 | https://jurnal.polgan.ac.id/index.php/sinkron/article/view/16797 | https://jurnal.polgan.ac.id/index.php/sinkron/article/view/16797/4353 | `s3-sinkron.pdf` | OK |
| 8 | `s3-sistemasi` | 3 | Sistemasi: Jurnal Sistem Informasi | Universitas Islam Indragiri | Heart Disease Prediction using Cost-sensitive Random Forest… | 2026 | https://sistemasi.ftik.unisi.ac.id/index.php/stmsi/article/view/6482 | https://sistemasi.ftik.unisi.ac.id/index.php/stmsi/article/view/6482/1373 | `s3-sistemasi.pdf` | OK |
| 9 | `s4-zonasi` | 4 | ZONAsi: Jurnal Sistem Informasi | Universitas Lancang Kuning | PENGARUH KEAMANAN DAN PRIVASI… | 2026 | https://journal.unilak.ac.id/index.php/zn/article/view/34847 | https://journal.unilak.ac.id/index.php/zn/article/view/34847/9850 | — | FAILED |
| 10 | `s4-jsi` | 4 | Jurnal Sains dan Informatika (JSI) | Politeknik Negeri Tanah Laut | Klasifikasi Sampah Plastik di Laut… | 2026 | https://jsi.politala.ac.id/index.php/JSI/article/view/1606 | https://jsi.politala.ac.id/index.php/JSI/article/view/1606/220 | `s4-jsi.pdf` | OK |
| 11 | `s4-jusifor` | 4 | JUSIFOR | Universitas Islam Raden Rahmat | Penilaian Kinerja Layanan TI SIPP… | 2026 | https://ejournal.uniramalang.ac.id/jusifor/en/article/view/8532 | https://ejournal.uniramalang.ac.id/jusifor/en/article/view/8532/5871 | — | FAILED |
| 12 | `s5-jatisi` | 5 | JATISI | Universitas Multi Data Palembang | Penerapan Machine Learning Algoritma Random Forest… | 2025 | https://jurnal.mdp.ac.id/index.php/jatisi/article/view/10917 | https://jurnal.mdp.ac.id/index.php/jatisi/article/download/10917/2477 | `s5-jatisi.pdf` | OK |
| 13 | `s5-misi` | 5 | MISI | STMIK Lombok | Implementasi Chatbot pada Telegram… | 2025 | http://e-journal.stmiklombok.ac.id/index.php/misi/article/view/1681 | http://e-journal.stmiklombok.ac.id/index.php/misi/article/download/1681/467 | `s5-misi.pdf` | OK |
| 14 | `s5-nuansa` | 5 | Nuansa Informatika | Universitas Kuningan | Development of a VR Metaverse System… | 2026 | https://journal.fkom.uniku.ac.id/ilkom/article/view/445 | https://journal.fkom.uniku.ac.id/ilkom/article/download/445/141 | `s5-nuansa.pdf` | OK |
| 15 | `s5-intek` | 5 | INTEK | Universitas Muhammadiyah Purworejo | Pengembangan Multimedia Pembelajaran Interaktif… | 2024 | https://jurnal.umpwr.ac.id/index.php/intek/article/view/5251 | https://jurnal.umpwr.ac.id/index.php/intek/article/view/5251/2390 | — | FAILED |
| 16 | `s6-jutik` | 6 | JuTIK | Universitas Dhyana Pura | Penerapan SimpleQueue pada Bandwidth Management… | 2026 | https://jurnal.undhirabali.ac.id/index.php/jutik/article/view/3792 | https://jurnal.undhirabali.ac.id/index.php/jutik/article/download/3792/4550 | `s6-jutik.pdf` | OK |
| 17 | `s6-jupiter` | 6 | JUPITER | Universitas Komputer Indonesia | Sistem Penilaian Kinerja Pegawai dengan AHP… | 2025 | https://ojs.unikom.ac.id/index.php/jupiter/article/view/17612 | https://ojs.unikom.ac.id/index.php/jupiter/article/download/17612/5296 | `s6-jupiter.pdf` | OK |
| 18 | `s3-sisfokom` | 3 | Sisfokom: Jurnal Sistem Informasi dan Komputer | ISB Atma Luhur | Land Suitability Assessment with TOPSIS in the Agrarian Sector | 2026 | https://jurnal.atmaluhur.ac.id/index.php/sisfokom/article/view/2606 | https://jurnal.atmaluhur.ac.id/index.php/sisfokom/article/download/2606/1436 | `s3-sisfokom.pdf` | OK |
| 19 | `s3-juti` | 3 | JUTI: Jurnal Ilmiah Teknologi Informasi | Institut Teknologi Sepuluh Nopember | Tail latency, throughput, and memory overhead of monolithic and microservices architectures… | 2026 | https://juti.if.its.ac.id/index.php/juti/article/view/1516 | https://juti.if.its.ac.id/index.php/juti/article/download/1516/600 | `s3-juti.pdf` | OK |
| 20 | `s2-jiki` | 2 | Jurnal Ilmu Komputer dan Informasi (JIKI) | Universitas Indonesia | Performance Evaluation of TabPFN for Student Depression Prediction Across Varying Sample Sizes | 2026 | https://jiki.cs.ui.ac.id/index.php/jiki/article/view/1716 | https://jiki.cs.ui.ac.id/index.php/jiki/article/download/1716/565 | `s2-jiki.pdf` | OK |
| 21 | `s4-transformatika` | 4 | Jurnal Transformatika | Universitas Semarang | Analisis Sentimen Publik Pada Media Sosial X Terhadap Pembentukan Danantara… | 2026 | https://journals.usm.ac.id/index.php/transformatika/en/article/view/14327 | https://journals.usm.ac.id/index.php/transformatika/article/download/14327/7363 | `s4-transformatika.pdf` | OK |
| 22 | `s4-scan` | 4 | SCAN: Jurnal Teknologi Informasi dan Komunikasi | UPN "Veteran" Jawa Timur | Arsitektur Hybrid Pengenalan Alfabet BISINDO Berbasis Web Real-Time… | 2026 | https://ejournal.upnjatim.ac.id/index.php/scan/article/view/5582 | http://ejournal.upnjatim.ac.id/index.php/scan/article/download/5582/pdf | `s4-scan.pdf` | OK |
| 23 | `s2-jti` | 2 | Jurnal Teknik Informatika (JTI) | UIN Syarif Hidayatullah Jakarta | Efficiency vs. Accuracy: MobileNetV2 vs VGG16 for Brain Tumor MRI Classification… | 2026 | https://journal.uinjkt.ac.id/index.php/ti/article/view/45002 | https://journal.uinjkt.ac.id/index.php/ti/article/download/45002/19042 | `s2-jti.pdf` | OK |
| 24 | `s2-ilkom` | 2 | ILKOM Jurnal Ilmiah | Universitas Muslim Indonesia | Ensemble Association Analysis on Kalla Toyota's Employee Data Using Apriori, FP-Growth, and ECLAT | 2026 | https://jurnal.fikom.umi.ac.id/index.php/ILKOM/article/view/2550 | https://jurnal.fikom.umi.ac.id/index.php/ILKOM/article/download/2550/pdf | `s2-ilkom.pdf` | OK |
| 25 | `s3-coreit` | 3 | Jurnal CoreIT | UIN Sultan Syarif Kasim Riau | Analysis of Combined Local and Global Pooling Layers in CNNs for CIFAR-10 Classification | 2026 | https://ejournal.uin-suska.ac.id/index.php/coreit/article/view/35089 | https://ejournal.uin-suska.ac.id/index.php/coreit/article/download/35089/15915 | `s3-coreit.pdf` | OK |
| 26 | `s3-jsi-ui` | 3 | Jurnal Sistem Informasi (JSI) | Universitas Indonesia | Factor Analysis of Practical Cybersecurity Learning Through Gamified Visual Novel Platform | 2026 | https://jsi.cs.ui.ac.id/index.php/jsi/article/view/1533 | https://jsi.cs.ui.ac.id/index.php/jsi/article/download/1533/463 | `s3-jsi-ui.pdf` | OK |
| 27 | `s2-jsinbis` | 2 | Jurnal Sistem Informasi Bisnis (JSINBIS) | Universitas Diponegoro | Penerapan Green Supply Chain Management Untuk Peningkatan Kinerja Keuangan Perusahaan | 2017 | https://ejournal.undip.ac.id/index.php/jsinbis/article/view/10894 | https://ejournal.undip.ac.id/index.php/jsinbis/article/download/10894/pdf | `s2-jsinbis.pdf` | OK |
| 28 | `s4-sitekin` | 4 | SITEKIN: Jurnal Sains, Teknologi dan Industri | UIN Sultan Syarif Kasim Riau | Comparative Sentiment Analysis of Provider X Application Reviews Using SVM, RF, and Naïve Bayes… | 2026 | https://ejournal.uin-suska.ac.id/index.php/sitekin/article/view/40021 | https://ejournal.uin-suska.ac.id/index.php/sitekin/article/download/40021/15918 | `s4-sitekin.pdf` | OK |
| 29 | `s2-sji` | 2 | Scientific Journal of Informatics (SJI) | Universitas Negeri Semarang | E-Dharmagita Learning Model Innovation with Mobile and Multimedia Technology | 2024 | https://journal.unnes.ac.id/nju/sji/article/view/46653 | https://journal.unnes.ac.id/nju/sji/article/download/46653/pdf | `s2-sji.pdf` | OK |
| 30 | `s2-jtie` | 2 | JTIE: Journal of Technology Informatics and Engineering | University of Science and Computer Technology | Development and Usability Evaluation of an AI-Powered English Vocabulary Learning Application | 2026 | https://jtie.stekom.ac.id/index.php/jtie/article/view/383 | https://jtie.stekom.ac.id/index.php/jtie/article/download/383/360 | `s2-jtie.pdf` | OK |
| 31 | `s3-jsce` | 3 | Journal of System and Computer Engineering (JSCE) | Universitas Pancasakti Makassar | Attention-Driven Contrastive Learning for the Identification of Rare Partial Discharge Signal in GIS | 2026 | https://journal.unpacti.ac.id/index.php/JSCE/article/view/2664 | https://journal.unpacti.ac.id/index.php/JSCE/article/download/2664/1409 | `s3-jsce.pdf` | OK |
| 32 | `s2-jptk` | 2 | Jurnal Pendidikan Teknologi dan Kejuruan (JPTK) | Universitas Negeri Yogyakarta | Enhancing learning and character through NHT model in grade x culinary class at SMKN 4 Yogyakarta | 2025 | https://journal.uny.ac.id/index.php/jptk/article/view/77489 | https://journal.uny.ac.id/index.php/jptk/article/download/77489/25067 | `s2-jptk.pdf` | OK |
| 33 | `s3-mib` | 3 | Jurnal Media Informatika Budidarma (MIB) | Universitas Budi Darma | Efek Transformasi Wavelet Diskrit Pada Klasifikasi Aritmia Dari Data Elektrokardiogram… | 2023 | https://ejurnal.stmik-budidarma.ac.id/index.php/mib/article/view/4859 | https://ejurnal.stmik-budidarma.ac.id/index.php/mib/article/download/4859/3201 | `s3-mib.pdf` | OK (via Wayback) |

## Notes

- **Sinta levels confirmed off-portal.** `https://sinta.kemdiktisaintek.go.id` returns
  HTTP 403 to automated fetchers, so the Sinta 1–6 levels above were confirmed on each
  journal's own site and/or from Wayback Machine snapshots of the official SINTA profile
  URLs, not by scraping SINTA directly.
- **Permendiktisaintek No. 9/2026 removes Sinta 5 and 6.** The regulation simplifies
  journal accreditation by dropping the Sinta 5 and Sinta 6 tiers; existing accreditation
  stands until its expiry date. Source:
  https://suarausu.or.id/kemendiktisaintek-sederhanakan-akreditasi-jurnal-sinta-5-dan-6-resmi-dihapus/
- **FAILED rows (4).** `s2-jtiik`, `s4-zonasi`, `s4-jusifor`, and `s5-intek` could not be
  retrieved: `s2-jtiik` (JTIIK) 403s automated fetchers, `s4-zonasi` 403s, `s4-jusifor`
  redirect-loops (max redirects exceeded), and `s5-intek` serves an incomplete TLS chain
  (curl SSL verify failure). Direct download, article-page resolution, the `r.jina.ai`
  proxy, and the Wayback fallback were all attempted; no snapshot/source was reachable.
  These rows remain listed here and in `manifest.tsv`. The requirement (≥ 10 PDFs) is met
  with OK=29.
- **Expansion (16 new journals, rows 18–33).** The corpus was expanded with 16 further
  DIFFERENT Sinta 2–4 journals in the Indonesian computing/IS field. All 16 article URLs
  were verified HTTP 200 before being added. 15 downloaded on the first attempt
  (`s3-sisfokom`, `s3-juti`, `s2-jiki`, `s4-transformatika`, `s4-scan`, `s2-jti`,
  `s2-ilkom`, `s3-coreit`, `s3-jsi-ui`, `s2-jsinbis`, `s4-sitekin`, `s2-sji`, `s2-jtie`,
  `s3-jsce`, `s2-jptk`); `s3-mib` (MIB) served a 404 for its `/article/download/...`
  link, so its `pdf_url` was kept and the script's Wayback fallback retrieved the PDF.
- **Candidates that could not be added (dead/unreachable, not listed).** `s2-jtiik`
  (JTIIK) still 403s; JEPIN (Untan) and JIP Polinema returned no working OJS article page,
  and the legacy `jsi.ui.ac.id` host was unreachable (JSI UI was added instead via its
  live `jsi.cs.ui.ac.id` host); JTMI (UB), Jurnal Teknoinfo (Unila/Teknokrat), Jurnal
  Ilmiah SINUS, Jurnal Generic, and Jurnal Buana Informatika (UBD) resolved to no working
  OJS article page from here, so they were not added (dead links are excluded by policy).
- **Provenance.** Journal provenance and accreditation data originate from
  `https://sinta.kemdiktisaintek.go.id` and `https://arjuna.kemdiktisaintek.go.id`.

## Reproduce

```sh
make corpus              # or: bash tools/fetch_corpus.sh
ls docs/sinta-corpus/*.pdf | wc -l
file docs/sinta-corpus/*.pdf | grep -vc 'PDF document'   # -> 0
```
