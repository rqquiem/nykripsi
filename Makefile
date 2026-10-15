PANDOC      := pandoc
SKRIPSI_SRC := $(sort $(wildcard content/skripsi/*.md))
DRAFTS_SRC  := $(wildcard content/drafts/*.md)
ARTIKEL_SRC := content/artikel/artikel-sinta.md
BIB         := assets/refs.bib
CSL         := assets/csl/apa.csl
OUT         := out

.PHONY: all setup skripsi artikel artikel-kyt artikel-arai artikel-datacenter artikel-hi artikel-hi-en check-kyt check-bab1 check-alur diagrams tables check-figures check-layout check-citations clean check corpus corpus-hi corpus-libgen kamus validate validate-agent validate-offline check-drafts promote sources research fulltext subjects scrape webgrab webdiscover check-web

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
	  --lua-filter=tools/pandoc_filters/figure_table.lua \
	  --lua-filter=tools/pandoc_filters/table.lua \
	  --lua-filter=tools/pandoc_filters/bilingual.lua \
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
	  --lua-filter=tools/pandoc_filters/figure_table.lua \
	  --lua-filter=tools/pandoc_filters/table.lua \
	  --lua-filter=tools/pandoc_filters/bilingual.lua \
	  --lua-filter=tools/pandoc_filters/sinta_layout.lua \
	  --from=markdown+raw_attribute+pipe_tables \
	  --metadata-file=templates/artikel-meta.yaml \
	  --reference-doc=templates/journal-reference.docx \
	  --citeproc --bibliography=$(BIB) --csl=$(CSL) \
	  -o $(OUT)/artikel-sinta.docx
	$(PANDOC) $(ARTIKEL_SRC) \
	  --lua-filter=tools/pandoc_filters/figure_table.lua \
	  --lua-filter=tools/pandoc_filters/table.lua \
	  --lua-filter=tools/pandoc_filters/bilingual.lua \
	  --lua-filter=tools/pandoc_filters/sinta_layout.lua \
	  --metadata-file=templates/artikel-meta.yaml \
	  --pdf-engine=xelatex \
	  --include-in-header=templates/artikel-preamble.tex \
	  --citeproc --bibliography=$(BIB) --csl=$(CSL) \
	  -o $(OUT)/artikel-sinta.pdf

artikel-kyt: $(OUT)
	$(PANDOC) content/artikel/artikel-kyt.md \
	  --lua-filter=tools/pandoc_filters/figure_table.lua \
	  --lua-filter=tools/pandoc_filters/table.lua \
	  --lua-filter=tools/pandoc_filters/bilingual.lua \
	  --lua-filter=tools/pandoc_filters/sinta_layout.lua \
	  --from=markdown+raw_attribute+pipe_tables \
	  --metadata-file=templates/artikel-kyt-meta.yaml \
	  --reference-doc=templates/journal-reference.docx \
	  --citeproc --bibliography=$(BIB) --csl=$(CSL) \
	  -o $(OUT)/artikel-kyt.docx
	$(PANDOC) content/artikel/artikel-kyt.md \
	  --lua-filter=tools/pandoc_filters/figure_table.lua \
	  --lua-filter=tools/pandoc_filters/table.lua \
	  --lua-filter=tools/pandoc_filters/bilingual.lua \
	  --lua-filter=tools/pandoc_filters/sinta_layout.lua \
	  --metadata-file=templates/artikel-kyt-meta.yaml \
	  --pdf-engine=xelatex \
	  --include-in-header=templates/artikel-preamble.tex \
	  --citeproc --bibliography=$(BIB) --csl=$(CSL) \
	  -o $(OUT)/artikel-kyt.pdf

artikel-arai: $(OUT)
	$(PANDOC) content/artikel/artikel-arai.md \
	  --lua-filter=tools/pandoc_filters/figure_table.lua \
	  --lua-filter=tools/pandoc_filters/table.lua \
	  --lua-filter=tools/pandoc_filters/bilingual.lua \
	  --lua-filter=tools/pandoc_filters/sinta_layout.lua \
	  --from=markdown+raw_attribute+pipe_tables \
	  --metadata-file=templates/artikel-arai-meta.yaml \
	  --reference-doc=templates/journal-reference.docx \
	  --citeproc --bibliography=$(BIB) --csl=$(CSL) \
	  -o $(OUT)/artikel-arai.docx
	$(PANDOC) content/artikel/artikel-arai.md \
	  --lua-filter=tools/pandoc_filters/figure_table.lua \
	  --lua-filter=tools/pandoc_filters/table.lua \
	  --lua-filter=tools/pandoc_filters/bilingual.lua \
	  --lua-filter=tools/pandoc_filters/sinta_layout.lua \
	  --metadata-file=templates/artikel-arai-meta.yaml \
	  --pdf-engine=xelatex \
	  --include-in-header=templates/artikel-preamble.tex \
	  --citeproc --bibliography=$(BIB) --csl=$(CSL) \
	  -o $(OUT)/artikel-arai.pdf

artikel-datacenter: $(OUT)
	$(PANDOC) content/artikel/artikel-datacenter.md \
	  --lua-filter=tools/pandoc_filters/figure_table.lua \
	  --lua-filter=tools/pandoc_filters/table.lua \
	  --lua-filter=tools/pandoc_filters/bilingual.lua \
	  --lua-filter=tools/pandoc_filters/sinta_layout.lua \
	  --from=markdown+raw_attribute+pipe_tables \
	  --metadata-file=templates/artikel-datacenter-meta.yaml \
	  --reference-doc=templates/journal-reference.docx \
	  --citeproc --bibliography=$(BIB) --csl=$(CSL) \
	  -o $(OUT)/artikel-datacenter.docx
	$(PANDOC) content/artikel/artikel-datacenter.md \
	  --lua-filter=tools/pandoc_filters/figure_table.lua \
	  --lua-filter=tools/pandoc_filters/table.lua \
	  --lua-filter=tools/pandoc_filters/bilingual.lua \
	  --lua-filter=tools/pandoc_filters/sinta_layout.lua \
	  --metadata-file=templates/artikel-datacenter-meta.yaml \
	  --pdf-engine=xelatex \
	  --include-in-header=templates/artikel-preamble.tex \
	  --citeproc --bibliography=$(BIB) --csl=$(CSL) \
	  -o $(OUT)/artikel-datacenter.pdf

artikel-hi: $(OUT)
	$(PANDOC) content/artikel/artikel-hi.md \
	  --lua-filter=tools/pandoc_filters/figure_table.lua \
	  --lua-filter=tools/pandoc_filters/table.lua \
	  --lua-filter=tools/pandoc_filters/bilingual.lua \
	  --lua-filter=tools/pandoc_filters/sinta_layout.lua \
	  --from=markdown+raw_attribute+pipe_tables \
	  --metadata-file=templates/artikel-hi-meta.yaml \
	  --reference-doc=templates/journal-reference.docx \
	  --citeproc --bibliography=$(BIB) --csl=$(CSL) \
	  -o $(OUT)/artikel-hi.docx
	$(PANDOC) content/artikel/artikel-hi.md \
	  --lua-filter=tools/pandoc_filters/figure_table.lua \
	  --lua-filter=tools/pandoc_filters/table.lua \
	  --lua-filter=tools/pandoc_filters/bilingual.lua \
	  --lua-filter=tools/pandoc_filters/sinta_layout.lua \
	  --metadata-file=templates/artikel-hi-meta.yaml \
	  --pdf-engine=xelatex \
	  --include-in-header=templates/artikel-preamble.tex \
	  --citeproc --bibliography=$(BIB) --csl=$(CSL) \
	  -o $(OUT)/artikel-hi.pdf

artikel-hi-en: $(OUT)
	$(PANDOC) content/artikel-en/artikel-hi-en.md \
	  --lua-filter=tools/pandoc_filters/figure_table.lua \
	  --lua-filter=tools/pandoc_filters/table.lua \
	  --lua-filter=tools/pandoc_filters/bilingual.lua \
	  --lua-filter=tools/pandoc_filters/sinta_layout.lua \
	  --from=markdown+raw_attribute+pipe_tables \
	  --metadata-file=templates/artikel-hi-en-meta.yaml \
	  --reference-doc=templates/journal-reference.docx \
	  --citeproc --bibliography=$(BIB) --csl=$(CSL) \
	  -o $(OUT)/artikel-hi-en.docx
	$(PANDOC) content/artikel-en/artikel-hi-en.md \
	  --lua-filter=tools/pandoc_filters/figure_table.lua \
	  --lua-filter=tools/pandoc_filters/table.lua \
	  --lua-filter=tools/pandoc_filters/bilingual.lua \
	  --lua-filter=tools/pandoc_filters/sinta_layout.lua \
	  --metadata-file=templates/artikel-hi-en-meta.yaml \
	  --pdf-engine=xelatex \
	  --include-in-header=templates/artikel-preamble.tex \
	  --citeproc --bibliography=$(BIB) --csl=$(CSL) \
	  -o $(OUT)/artikel-hi-en.pdf

check-kyt:
	python3 tools/validate.py article_framework

check-bab1:
	python3 tools/validate.py bab1_framework

check-alur:
	python3 tools/validate.py argument_flow

check-figures:
	python3 tools/validate.py figures_tables sintesa_diagram bagan_diagram && python3 tools/table.py --check

check-layout:
	python3 tools/validate.py layout_typography

check-citations:
	python3 tools/validate.py citation_framework

diagrams:
	python3 tools/diagrams.py render

tables:
	python3 tools/table.py --check

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

subjects:
	python3 tools/scrape.py render

scrape:
	python3 tools/scrape.py sweep "$(S)"

fulltext:
	python3 tools/fulltext.py verify $(F)

webgrab:
	python3 tools/webgrab.py fetch "$(URL)"

webdiscover:
	python3 tools/webgrab.py discover "$(Q)" --fetch

check-web:
	python3 tools/validate.py web_corpus

research:
	python3 .claude/skills/nykripsi/scripts/research_gap.py render

clean:
	rm -rf $(OUT)
