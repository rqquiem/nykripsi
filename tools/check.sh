#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

PNG_B64='iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mM48R8AApIByLuOOSgAAAAASUVORK5CYII='

echo "==> Memeriksa toolchain"
command -v pandoc
pandoc --version | head -1

echo "==> Memeriksa python-docx"
python3 -c "import docx"

echo "==> Memeriksa artefak keluaran"
test -s out/skripsi.pdf
test -s out/artikel-sinta.docx
test -s out/artikel-sinta.pdf

echo "==> Memeriksa halaman PDF skripsi"
pdfinfo out/skripsi.pdf | grep -q 'Pages'

echo "==> Memeriksa teks PDF skripsi"
grep -q 'PENDAHULUAN' <(pdftotext out/skripsi.pdf -)

echo "==> Memeriksa gaya DOCX artikel"
unzip -p out/artikel-sinta.docx word/styles.xml | grep -q 'Times New Roman'

echo "==> Memastikan gambar contoh tersedia"
test -e assets/figures/contoh.png || echo "$PNG_B64" | base64 -d > assets/figures/contoh.png

echo "==> Menghitung sisa penanda TODO: isi"
TODO_COUNT=$(grep -r -o 'TODO: isi' content/skripsi content/artikel 2>/dev/null | wc -l || true)
echo "Sisa penanda TODO: isi = ${TODO_COUNT}"

echo ""
echo "SEMUA PEMERIKSAAN LULUS."
exit 0
