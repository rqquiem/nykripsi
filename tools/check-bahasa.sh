#!/usr/bin/env bash
# Linter ragam bahasa ilmiah Indonesia untuk artikel + bab skripsi.
# Menolak kata ganti orang pertama/kedua dan kosakata tidak baku (EYD Edisi V),
# serta memastikan kepala bagian artikel memakai himpunan autentik.
set -euo pipefail
cd "$(dirname "$0")/.."

# Catatan: berkas 00-*.md s.d. 03-*.md sengaja dikecualikan (surat pernyataan
# memakai orang pertama "karya saya sendiri"); 06-*.md dan 90-*.md hanya LaTeX mentah.
if [ "$#" -gt 0 ]; then
  FILES="$*"
else
  FILES=$(ls content/skripsi/0[45]-*.md content/skripsi/1[0-5]-*.md content/artikel/*.md)
fi

PRONOUNS='saya|aku|kami|kita|anda|kamu|kalian'
NONBAKU=$(python3 tools/gen_kamus.py --pattern kosakata_baku)

status=0

if grep -nEwi "$PRONOUNS" $FILES; then
  echo "GAGAL: ditemukan kata ganti orang pertama/kedua (ragam tidak impersonal)."
  status=1
fi

if grep -nEwi "$NONBAKU" $FILES; then
  echo "GAGAL: ditemukan kosakata tidak baku (lihat EYD Edisi V)."
  status=1
fi

AI_GENERIK=$(python3 tools/gen_kamus.py --pattern frasa_ai_generik)
if grep -niE "$AI_GENERIK" $FILES; then
  echo "GAGAL: ditemukan frasa pengisi bergaya AI generik (lihat kamus)."
  status=1
fi

for id in pendahuluan metode hasil simpulan ucapan pustaka; do
  if ! grep -q "<!-- kamus:h id=$id -->" content/artikel/artikel-sinta.md; then
    echo "GAGAL: kepala bagian '$id' tidak ditemukan di artikel"
    status=1
  fi
done

EXPECTED_ORDER=$'<!-- kamus:h id=pendahuluan -->\n<!-- kamus:h id=metode -->\n<!-- kamus:h id=hasil -->\n<!-- kamus:h id=simpulan -->\n<!-- kamus:h id=ucapan -->\n<!-- kamus:h id=pustaka -->'
ACTUAL_ORDER=$(grep -oE '<!-- kamus:h id=[a-z0-9_]+ -->' content/artikel/artikel-sinta.md || true)
if [ "$ACTUAL_ORDER" != "$EXPECTED_ORDER" ]; then
  echo "GAGAL: urutan kepala bagian tidak sesuai kamus"
  status=1
fi

if ! python3 tools/gen_kamus.py --check; then
  status=1
fi

if [ "$status" -eq 0 ]; then
  echo "RAGAM BAHASA: LULUS."
fi

exit "$status"
