#!/usr/bin/env bash
# Fetch the Sinta corpus PDFs described by docs/sinta-corpus/manifest.tsv.
#
# Exits 0 even when some rows fail: the requirement is >= 10 PDFs, not all 17.
set -uo pipefail
cd "$(dirname "$0")/.."

MANIFEST="docs/sinta-corpus/manifest.tsv"
OUTDIR="docs/sinta-corpus"
UA='Mozilla/5.0 (X11; Linux x86_64)'

ok=0
failed=0

# Download <url> to <dest> with the standard UA. Returns curl's exit code.
download() {
  local url="$1" dest="$2"
  curl -fsSL -A "$UA" --max-time 60 -o "$dest" "$url"
}

# Normalize a possibly-relative href against the page it came from.
abs_url() {
  local href="$1" page="$2"
  case "$href" in
    http*) printf '%s\n' "$href" ;;
    /*)    printf '%s\n' "$(printf '%s' "$page" | sed -E 's#(https?://[^/]+).*#\1#')$href" ;;
    *)     printf '%s\n' "$(dirname "$page")/$href" ;;
  esac
}

# Print every article/download/... href in an HTML page (one per line).
first_download_all() {
  grep -oE 'href="[^"]*article/download/[^"]*"' \
    | sed -E 's/^href="//; s/"$//'
}

# Resolve candidate PDF URLs from an article page: every article/download/...
# href on the page, plus download links found by descending into each view/...
# PDF galley page (OJS "view" viewer). Prints one URL per line.
resolve_pdf() {
  local page="$1" html g gh h
  html=$(curl -fsSL -A "$UA" --max-time 60 "$page") || return 1
  printf '%s' "$html" | first_download_all | while read -r h; do
    abs_url "$h" "$page"
  done
  printf '%s' "$html" | grep -oE 'href="[^"]*article/view/[^"]*"' \
    | sed -E 's/^href="//; s/"$//' | while read -r g; do
      g=$(abs_url "$g" "$page")
      gh=$(curl -fsSL -A "$UA" --max-time 60 "$g") || continue
      printf '%s' "$gh" | first_download_all | while read -r h; do
        abs_url "$h" "$g"
      done
    done
}

# Try a single URL; return 0 on success and leave a valid PDF at $dest.
try_url() {
  local url="$1" dest="$2"
  [ -n "$url" ] || return 1
  download "$url" "$dest" || return 1
  file "$dest" | grep -q 'PDF' || return 1
  return 0
}

while IFS=$'\t' read -r slug sinta journal year article_url pdf_url; do
  [ "$slug" = "slug" ] && continue          # skip header
  [ -n "$slug" ] || continue                # skip blank lines

  dest="$OUTDIR/$slug.pdf"
  rm -f "$dest"
  status=1

  # 1. Direct pdf_url (if any).
  if try_url "$pdf_url" "$dest"; then
    status=0
  fi

  # 2. Resolve from the article page (also used when pdf_url was empty).
  if [ "$status" -ne 0 ]; then
    while IFS= read -r resolved; do
      [ -n "$resolved" ] || continue
      if try_url "$resolved" "$dest"; then
        status=0
        break
      fi
    done < <(resolve_pdf "$article_url")
  fi

  # 3. Retry via r.jina.ai text proxy.
  if [ "$status" -ne 0 ] && [ -n "$pdf_url" ]; then
    try_url "https://r.jina.ai/$pdf_url" "$dest" && status=0
  fi

  # 4. Retry via Wayback Machine.
  if [ "$status" -ne 0 ] && [ -n "$pdf_url" ]; then
    try_url "https://web.archive.org/web/2025/$pdf_url" "$dest" && status=0
  fi

  if [ "$status" -eq 0 ]; then
    echo "$slug OK"
    ok=$((ok + 1))
  else
    rm -f "$dest"
    echo "$slug FAILED"
    failed=$((failed + 1))
  fi
done < "$MANIFEST"

echo "OK=$ok FAILED=$failed"
exit 0
