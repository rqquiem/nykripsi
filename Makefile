PANDOC      := pandoc
SKRIPSI_SRC := $(sort $(wildcard content/skripsi/*.md))
DRAFTS_SRC  := $(wildcard content/drafts/*.md)
ARTIKEL_SRC := content/artikel/artikel-sinta.md
BIB         := assets/refs.bib
CSL         := assets/csl/apa.csl
OUT         := out

.PHONY: all setup skripsi artikel clean check corpus corpus-hi corpus-libgen kamus validate validate-agent validate-offline check-drafts promote sources research

all: skripsi artikel

$(OUT):
	@mkdir -p $(OUT)

setup:
	sudo pacman -S --needed --noconfirm pandoc-cli
	python3 -m ensurepip --upgrade
	python3 -m pip install --user --break-system-packages python-docx
	python3 -m pip install --user --break-system-packages pyyaml
	python3 tools/make_reference_docx.py

skripsi: $(OUT)
	$(PANDOC) $(SKRIPSI_SRC) \
	  --from=markdown+raw_attribute+pipe_tables+footnotes \
	  --top-level-division=chapter \
	  --number-sections \
	  --pdf-engine=xelatex \
	  -V documentclass=book -V fontsize=12pt -V indent=true \
	  --include-in-header=templates/skripsi-preamble.tex \
	  --citeproc --bibliography=$(BIB) --csl=$(CSL) \
	  -o $(OUT)/skripsi.pdf

artikel: $(OUT)
	$(PANDOC) $(ARTIKEL_SRC) \
	  --from=markdown+raw_attribute+pipe_tables \
	  --metadata-file=templates/artikel-meta.yaml \
	  --reference-doc=templates/journal-reference.docx \
	  --citeproc --bibliography=$(BIB) --csl=$(CSL) \
	  -o $(OUT)/artikel-sinta.docx
	$(PANDOC) $(ARTIKEL_SRC) \
	  --metadata-file=templates/artikel-meta.yaml \
	  --pdf-engine=xelatex \
	  --include-in-header=templates/artikel-preamble.tex \
	  --citeproc --bibliography=$(BIB) --csl=$(CSL) \
	  -o $(OUT)/artikel-sinta.pdf

kamus:
	python3 tools/gen_kamus.py --emit --doc

check: all
	bash tools/check.sh
	bash tools/check-bahasa.sh
	python3 tools/gen_kamus.py --check
	python3 tools/validate.py

validate:
	python3 tools/validate.py

validate-agent:
	python3 tools/validate.py --agent

validate-offline:
	python3 tools/validate.py --offline

corpus:
	bash tools/fetch_corpus.sh

corpus-hi:
	bash tools/fetch_corpus_ir.sh

corpus-libgen:
	python3 tools/libgen.py fetch

check-drafts:
	@files="$(DRAFTS_SRC)"; if [ -z "$$files" ]; then echo "TIDAK ADA DRAFT: content/drafts kosong"; else bash tools/check-bahasa.sh $$files; fi

promote:
	python3 tools/promote.py --draft "$(DRAFT)"

sources:
	python3 .claude/skills/nykripsi/scripts/search.py render

research:
	python3 .claude/skills/nykripsi/scripts/research_gap.py render

clean:
	rm -rf $(OUT)
