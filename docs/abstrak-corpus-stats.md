# Abstract conventions in the local journal corpora

**Purpose.** Measure the abstract conventions actually used in the local journal corpora — `docs/sinta-corpus/` (Sinta 1–6, Indonesian computing/IS) and `docs/ir-corpus/` (international HI/IR) — as raw evidence for the abstract framework being written elsewhere.

**Method / tool.** Poppler `pdftotext` (`/usr/bin/pdftotext`) extracts each PDF to a plain-text file under `/tmp`; the abstract block is located by its label (`Abstrak`/`Abstract`, any case), the prose captured up to the first keyword line or next section heading, and each field is read off that block. Word count = whitespace tokens of the extracted abstract prose. Language (ID vs EN) is detected by counting common Indonesian vs English function words in the abstract. Structured = ≥2 inline headings (e.g. `Background:`/`Methods:`/`Results:`/`Conclusion:` or `Latar Belakang:`/`Tujuan:`/`Metode:`/`Hasil:`) in the block; otherwise unstructured prose.

All 72 PDFs (29 Sinta + 43 international) yielded extractable text; **none was UNREADABLE**. Five international PDFs carry an abstract that is *not preceded by any label* (editorial/Forum or repository front matter) and are recorded in the failures list rather than the table. Because many Sinta and IR papers print **both** an Indonesian and an English abstract, each such paper is counted **once** (on its first block) so the row counts reflect papers, not abstract blocks.

## 1. Per-paper table

Sinta column = level from the filename / `docs/sinta-corpus/MANIFEST.md`; `—` for `ir-corpus`. Component columns: `Y` = cue present, `–` = not detected. `#Kw` = number of items after `Kata Kunci:`/`Keywords:`.

| # | File | Sinta | Lang | Label | Structure | Words | Bg | Obj | Meth | Res | Concl | #Kw | Word limit |
|---|------|:-----:|:----:|:-----:|:---------:|------:|:--:|:---:|:----:|:---:|:-----:|:---:|:----------:|
| 1 | `s1-register.pdf` | 1 | EN | ABSTRACT | unstruct | 213 | Y | Y | Y | Y | Y | 5 | — |
| 2 | `s1-telkomnika.pdf` | 1 | EN | ABSTRACT | unstruct | 169 | Y | Y | – | Y | Y | 5 | — |
| 3 | `s2-ijccs.pdf` | 2 | ID | Abstrak | unstruct | 179 | Y | Y | Y | Y | – | 5 | — |
| 4 | `s2-ilkom.pdf` | 2 | EN | Abstract | unstruct | 202 | Y | Y | Y | Y | – | 5 | — |
| 5 | `s2-jiki.pdf` | 2 | EN | Abstract | unstruct | 263 | Y | Y | Y | Y | Y | 5 | — |
| 6 | `s2-jisebi.pdf` | 2 | EN | Abstract | struct | 193 | Y | Y | Y | Y | Y | 5 | — |
| 7 | `s2-jptk.pdf` | 2 | EN | ABSTRACT | unstruct | 240 | – | Y | Y | Y | Y | 4 | — |
| 8 | `s2-jsinbis.pdf` | 2 | EN | Abstract | unstruct | 238 | – | Y | Y | Y | – | 4 | — |
| 9 | `s2-jti.pdf` | 2 | EN | ABSTRACT | unstruct | 210 | – | Y | Y | Y | Y | 6 | — |
| 10 | `s2-jtie.pdf` | 2 | EN | Abstract | unstruct | 222 | Y | – | Y | Y | – | 5 | — |
| 11 | `s2-resti.pdf` | 2 | EN | Abstract | unstruct | 181 | Y | Y | Y | Y | – | 5 | — |
| 12 | `s2-sji.pdf` | 2 | EN | Abstract | struct | 213 | Y | Y | Y | Y | – | 5 | — |
| 13 | `s3-coreit.pdf` | 3 | EN | Abstract | unstruct | 215 | Y | Y | Y | Y | – | 6 | — |
| 14 | `s3-jsce.pdf` | 3 | EN | Abstract | unstruct | 206 | Y | Y | Y | Y | – | 4 | — |
| 15 | `s3-jsi-ui.pdf` | 3 | EN | Abstract | unstruct | 151 | Y | – | Y | Y | – | 5 | — |
| 16 | `s3-juti.pdf` | 3 | EN | ABSTRACT | unstruct | 263 | Y | Y | Y | Y | – | 5 | — |
| 17 | `s3-mib.pdf` | 3 | ID | Abstrak | unstruct | 225 | – | – | Y | Y | – | 5 | — |
| 18 | `s3-sinkron.pdf` | 3 | EN | Abstract | unstruct | 269 | Y | Y | Y | Y | – | 6 | — |
| 19 | `s3-sisfokom.pdf` | 3 | EN | Abstract | unstruct | 202 | Y | Y | Y | – | – | 5 | — |
| 20 | `s3-sistemasi.pdf` | 3 | ID | Abstrak | unstruct | 225 | – | – | Y | – | – | 5 | — |
| 21 | `s4-jsi.pdf` | 4 | ID | Abstrak | unstruct | 174 | Y | Y | Y | Y | – | 5 | — |
| 22 | `s4-scan.pdf` | 4 | ID | ABSTRAK | unstruct | 137 | – | Y | Y | Y | – | 4 | — |
| 23 | `s4-sitekin.pdf` | 4 | EN | ABSTRACT | unstruct | 174 | – | Y | Y | Y | – | 5 | — |
| 24 | `s4-transformatika.pdf` | 4 | ID | ABSTRACT | unstruct | 150 | – | Y | Y | Y | – | 5 | — |
| 25 | `s5-jatisi.pdf` | 5 | ID | Abstrak | unstruct | 168 | – | Y | Y | Y | – | 3 | — |
| 26 | `s5-misi.pdf` | 5 | EN | Abstract | unstruct | 292 | – | Y | Y | Y | – | 5 | — |
| 27 | `s5-nuansa.pdf` | 5 | EN | Abstract | unstruct | 200 | Y | Y | Y | Y | Y | 5 | — |
| 28 | `s6-jupiter.pdf` | 6 | ID | ABSTRAK | unstruct | 169 | Y | – | Y | Y | – | 3 | — |
| 29 | `s6-jutik.pdf` | 6 | ID | ABSTRAK | unstruct | 211 | Y | Y | Y | Y | – | 5 | — |
| 30 | `hi-atlantis-china-asea-pd.pdf` | — | EN | Abstract | unstruct | 109 | – | – | Y | – | – | 4 | — |
| 31 | `hi-bournemouth-nation-branding.pdf` | — | EN | Abstract | unstruct | 134 | Y | Y | – | Y | – | 0 | — |
| 32 | `hi-cjas-southeast-asia.pdf` | — | EN | Abstract | unstruct | 231 | Y | Y | Y | – | – | 7 | — |
| 33 | `hi-dinamika-bali-democracy.pdf` | — | EN | Abstract | unstruct | 147 | – | Y | Y | Y | – | 4 | — |
| 34 | `hi-gfpr-us-china-softpower.pdf` | — | EN | Abstract | unstruct | 143 | – | Y | Y | – | – | 7 | — |
| 35 | `hi-hrmars-vaccine-softpower.pdf` | — | EN | Abstract | unstruct | 297 | Y | – | Y | Y | Y | 4 | — |
| 36 | `hi-ieom-istanbul-vaccine.pdf` | — | EN | Abstract | unstruct | 182 | Y | Y | Y | Y | – | 5 | — |
| 37 | `hi-ieom-rome-vaccine.pdf` | — | EN | Abstract | unstruct | 191 | – | Y | Y | Y | – | 5 | — |
| 38 | `hi-ijss-vtuber.pdf` | — | EN | ABSTRACT | unstruct | 235 | – | Y | Y | Y | – | 5 | — |
| 39 | `hi-interaksi-g20.pdf` | — | ID | Abstrak | unstruct | 208 | Y | Y | Y | – | – | 5 | — |
| 40 | `hi-irscs-bahasa.pdf` | — | EN | Abstract | unstruct | 231 | – | Y | Y | – | Y | 5 | — |
| 41 | `hi-ivran-mask-diplomacy.pdf` | — | EN | Abstract | unstruct | 199 | Y | Y | – | Y | – | 5 | — |
| 42 | `hi-janus-health-diplomacy.pdf` | — | EN | Abstract | unstruct | 337 | Y | – | Y | Y | – | 4 | — |
| 43 | `hi-jelajah-tourism.pdf` | — | EN | Abstract | unstruct | 220 | Y | Y | Y | Y | Y | 4 | — |
| 44 | `hi-jgs-japan-pd.pdf` | — | EN | ABSTRACT | unstruct | 179 | Y | Y | Y | – | – | 6 | — |
| 45 | `hi-jhi-netherlands-vaccine.pdf` | — | ID | Abstrak | unstruct | 135 | – | Y | Y | Y | – | 4 | — |
| 46 | `hi-jhi-umy-free-active-vaccine.pdf` | — | ID | Abstrak | unstruct | 220 | Y | Y | Y | Y | – | 5 | — |
| 47 | `hi-jhi-umy-konstruktivis.pdf` | — | EN | Abstract | unstruct | 197 | Y | Y | Y | Y | – | 4 | — |
| 48 | `hi-jhi-umy-malaysia.pdf` | — | EN | Abstract | unstruct | 149 | Y | Y | Y | Y | – | 6 | — |
| 49 | `hi-jhi-umy-vaccine-politics.pdf` | — | ID | Abstrak | unstruct | 146 | – | Y | Y | Y | – | 6 | — |
| 50 | `hi-jhi-vanuatu.pdf` | — | ID | Abstrak | unstruct | 169 | – | Y | – | Y | – | 5 | — |
| 51 | `hi-jiir-uinsa.pdf` | — | EN | Abstract | unstruct | 200 | Y | Y | Y | – | – | 3 | — |
| 52 | `hi-jiwp-korea-week.pdf` | — | EN | Abstract | unstruct | 189 | – | Y | Y | Y | – | 5 | — |
| 53 | `hi-jpr-nation-branding.pdf` | — | EN | Abstract | struct | 356 | Y | Y | Y | Y | Y | 5 | — |
| 54 | `hi-jsgs-korean-cuisine.pdf` | — | EN | Abstract | unstruct | 249 | Y | – | Y | Y | Y | 5 | — |
| 55 | `hi-jsps-aviation.pdf` | — | EN | Abstract | unstruct | 202 | – | – | Y | – | – | 5 | — |
| 56 | `hi-mdpi-health-silk-road.pdf` | — | EN | Abstract | unstruct | 259 | Y | Y | Y | Y | Y | 4 | — |
| 57 | `hi-mgimo-health-silk-road.pdf` | — | EN | Abstract | unstruct | 190 | Y | – | Y | – | – | 8 | — |
| 58 | `hi-ndu-pakistan-nation-branding.pdf` | — | EN | Abstract | unstruct | 141 | – | – | Y | Y | – | 5 | — |
| 59 | `hi-padjir-asian-games.pdf` | — | EN | ABSTRACT | unstruct | 207 | – | Y | Y | Y | – | 6 | — |
| 60 | `hi-padjir-desa-wisata.pdf` | — | EN | ABSTRACT | unstruct | 147 | Y | Y | Y | Y | Y | 3 | — |
| 61 | `hi-padjir-wisatawan.pdf` | — | EN | ABSTRACT | unstruct | 137 | – | Y | Y | Y | – | 4 | — |
| 62 | `hi-ph-china-foreign-policy.pdf` | — | EN | Abstract | unstruct | 222 | – | Y | Y | – | Y | 4 | — |
| 63 | `hi-richtmann-japan-vaccine.pdf` | — | EN | Abstract | unstruct | 183 | Y | – | Y | – | – | 4 | — |
| 64 | `hi-sentris-asian-games.pdf` | — | ID | ABSTRAK | unstruct | 91 | – | – | Y | – | – | 5 | — |
| 65 | `hi-ssr-geopolitics-vaccine.pdf` | — | EN | Abstract | unstruct | 118 | Y | Y | – | – | – | 6 | — |
| 66 | `hi-stdjssh-health-silk-road-sea.pdf` | — | EN | ABSTRACT | unstruct | 208 | Y | Y | – | – | – | 5 | — |
| 67 | `hi-stdjssh-japan-vaccine.pdf` | — | EN | ABSTRACT | unstruct | 193 | Y | – | – | Y | – | 4 | — |

_Rows written: **67** = 29 Sinta papers + 38 international papers (each paper counted once). No stated abstract word limit was visible in any extracted PDF (the only `…words` figure found in the corpus, in `s2-resti`, refers to a 500-word sliding window inside the method, not an abstract limit), so the Word-limit column is `—` throughout._

## 2. Summary statistics

All figures below are derived from the per-paper table above. Median = middle value of the sorted list (for an even count, mean of the two middle values). Percentages are `count / N` for the relevant group.

### 2.1 Abstract word count (whitespace tokens)

| Group | N | min | median | max |
|-------|--:|----:|-------:|----:|
| Sinta (Sinta 1–6) | 29 | 137 | 206 | 292 |
| International (`ir-corpus`) | 38 | 91 | 192 | 356 |
| All | 67 | 91 | 200 | 356 |

Arithmetic: Sinta word counts sorted → min 137 (`s4-scan`), max 292 (`s5-misi`); with N=29 the median is the 15th value = 206. International → min 91 (`hi-sentris-asian-games`), max 356 (`hi-jpr-nation-branding`); with N=38 the median is the mean of the 19th and 20th values = (191+193)/2 = 192. All 67 → N=67, median = 34th value = 200.

### 2.2 Structured vs unstructured

| Group | Structured | Unstructured | % structured |
|-------|-----------:|-------------:|:------------:|
| Sinta | 2 | 27 | 6.9% |
| International | 1 | 37 | 2.6% |
| All | 3 | 64 | 4.5% |

Only three abstracts use inline section headings: `s2-jisebi` (Background/Objective/Methods/Results/Conclusion), `s2-sji` (Purpose/Methods/Results/Novelty) and `hi-jpr-nation-branding` (Purpose/Methodology/Findings). 6.9% Sinta = 2/29; 2.6% international = 1/38.

### 2.3 Component presence (cue-word detection)

| Group | Background/problem | Objective/purpose | Method | Results | Conclusion/implication |
|-------|:-----------------:|:-----------------:|:------:|:-------:|:----------------------:|
| Sinta (N=29) | 19 (65.5%) | 24 (82.8%) | 28 (96.6%) | 27 (93.1%) | 7 (24.1%) |
| International (N=38) | 22 (57.9%) | 28 (73.7%) | 32 (84.2%) | 24 (63.2%) | 8 (21.1%) |
| All (N=67) | 41 (61.2%) | 52 (77.6%) | 60 (89.6%) | 51 (76.1%) | 15 (22.4%) |

**Explicit objective sentence:** Sinta 82.8% (24/29); international 73.7% (28/38); all 77.6% (52/67).

**Explicit conclusion sentence:** Sinta 24.1% (7/29); international 21.1% (8/38); all 22.4% (15/67).

### 2.4 Keywords per abstract

| Group | median (all rows) | median (rows with ≥1 keyword) | rows with 0 keywords |
|-------|:-----------------:|:-----------------------------:|:--------------------:|
| Sinta | 5 | 5 | 0 |
| International | 5 | 5 | 1 |
| All | 5 | 5 | 1 |

Median keyword count is 5 in every group; the modal value is also 5. The single zero-keyword row is `hi-bournemouth-nation-branding` (an editorial with no keyword line); every Sinta row has ≥2 keywords.

### 2.5 Label variants

| Label | Sinta | International | All |
|-------|------:|--------------:|----:|
| `Abstract` | 14 | 25 | 39 |
| `ABSTRACT` | 7 | 7 | 14 |
| `Abstrak` | 5 | 5 | 10 |
| `ABSTRAK` | 3 | 1 | 4 |
| **Total** | 29 | 38 | 67 |

English label (`Abstract`/`ABSTRACT`): 53/67 = 79.1%; Indonesian label (`Abstrak`/`ABSTRAK`): 14/67 = 20.9%. Sinta uses the Indonesian label on 8/29 = 27.6% rows; international on 6/38 = 15.8%.

### 2.6 Language of the abstract

| Language | Sinta | International | All |
|----------|------:|--------------:|----:|
| Indonesian (ID) | 9 (31.0%) | 6 (15.8%) | 15 (22.4%) |
| English (EN) | 20 (69.0%) | 32 (84.2%) | 52 (77.6%) |

(23 of the 67 papers — 10 Sinta + 13 international — actually print **two** abstracts, one Indonesian and one English; each is counted once, on its first block, so the ID/EN split above is by *first* block. Counting every abstract block separately the corpus would contain 90 blocks.)

## 3. Extraction failures

**No file was UNREADABLE** — `pdftotext` returned non-empty text for all 72 PDFs (29 Sinta + 43 international), so no paper was skipped as a scan. The items below are papers that were **processed but not entered as a table row** because they have no label-led abstract to measure; they are recorded here rather than invented.

| File | Corpus | Reason not in table |
|------|--------|---------------------|
| `hi-bath-china-softpower.pdf` | ir | Repository/author pre-print front matter (University of Bath); the body starts at `Introduction` with **no `Abstract` heading** anywhere in the extracted text — no abstract block to measure. |
| `hi-brunel-softpower.pdf` | ir | Chinese-language essay (`软实力与国家品牌`, 北大商业评论 2007); no abstract label and no keyword line. |
| `hi-coventry-softpower-china.pdf` | ir | Author post-print (CURVE); body begins at `Introduction`, **no abstract heading** in the extracted text. |
| `hi-david-palestinian-nation-branding.pdf` | ir | Journal-of-Politics-and-Law layout: a ~511-word opening paragraph carries **no `Abstract` label**; only a `Keywords:` line follows. Excluded because the block cannot be delimited by a label. |
| `hi-reinvention-vaccine.pdf` | ir | Undergraduate journal article; no abstract section — the article opens directly with the body. |

_Note: the Sinta corpus had **no** retrieval gaps inside this task — the four PDFs that the manifest lists as FAILED (`s2-jtiik`, `s4-zonasi`, `s4-jusifor`, `s5-intek`) were never downloaded and are therefore not present under `docs/sinta-corpus/` at all; the 29 PDFs that do exist were all read successfully._

## 4. Reproduce

Run from the repository root:

```sh
# 1. Extract text from every PDF (poppler pdftotext).
mkdir -p /tmp/abs_txt
for f in docs/sinta-corpus/*.pdf docs/ir-corpus/*.pdf; do
  b=$(basename "$f" .pdf)
  pdftotext -q "$f" "/tmp/abs_txt/$b.txt"
done

# 2. Sanity check: every file produced text (no UNREADABLE).
for t in /tmp/abs_txt/*.txt; do
  printf "%s %s\n" "$(basename "$t")" "$(tr -d "[:space:]" < "$t" | wc -c)"
done | sort

# 3. Locate each abstract label and its keyword line.
grep -n -i -E '^[[:space:]]*(abstrak|abstract)\b' /tmp/abs_txt/*.txt
grep -n -i -E '^[[:space:]]*(kata[ -]*kunci|keywords?)\b' /tmp/abs_txt/*.txt
```

The per-paper fields (label, language, structure, word count, component cues, keyword count) were then read off each extracted block; word count = `len(block.split())` on the extracted abstract prose. The corpus counts were cross-checked against `docs/sinta-corpus/MANIFEST.md` (29 OK PDFs) and `docs/ir-corpus/MANIFEST.md` (43 OK PDFs).

