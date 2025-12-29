# ============================================================================
# MAKEFILE - LLM Essentials for Law and Finance (Mini-Book)
# ============================================================================
# Build system for the mini-book covering LLM foundations for legal and
# financial professionals.
#
# Usage:
#   make          - Build the complete mini-book PDF
#   make pdf      - Same as above
#   make quick    - Single-pass build (for minor edits)
#   make watch    - Continuous compilation on file changes
#   make validate - Check for undefined references
#   make clean    - Remove auxiliary files
#   make cleanall - Remove all generated files including PDF
#   make help     - Display this help message
# ============================================================================

# ----------------------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------------------

MAIN = main
TEXFILE = $(MAIN).tex
PDFFILE = $(MAIN).pdf
BIBFILE = bib/refs.bib
COVER = lulu-cover
COVER_TEX = $(COVER).tex
COVER_PDF = $(COVER).pdf
COVER_VARS = front-matter/cover/cover-vars.tex
COVER_FRONT_TEX = covers/cover-front.tex
COVER_BACK_TEX = covers/cover-back.tex
COVER_FRONT_PDF = covers/cover-front.pdf
COVER_BACK_PDF = covers/cover-back.pdf
INTERIOR_PDF = lulu-interior.pdf

# LaTeX tools - using XeLaTeX for fontspec support
LATEX = xelatex
BIBER = biber
LATEXMK = latexmk

# Latexmk options - use xelatex
LATEXMK_OPTS = -xelatex -interaction=nonstopmode -file-line-error -halt-on-error -recorder

# Manual compilation flags
LATEX_OPTS = -interaction=nonstopmode -file-line-error -halt-on-error

# Colors for output
BOLD = \033[1m
CYAN = \033[36m
GREEN = \033[32m
YELLOW = \033[33m
BLUE = \033[34m
RED = \033[31m
RESET = \033[0m

# Symbols
CHECK = ✓
CROSS = ✗
ARROW = ➜
STAR = ★

# ----------------------------------------------------------------------------
# Default target
# ----------------------------------------------------------------------------

.PHONY: all
all: pdf

# ----------------------------------------------------------------------------
# Main PDF build
# ----------------------------------------------------------------------------

.PHONY: pdf
pdf: $(PDFFILE)
	@echo ""
	@echo "$(BOLD)$(GREEN)$(CHECK) Build complete: $(PDFFILE)$(RESET)"
	@if command -v pdfinfo >/dev/null 2>&1; then \
		pages=$$(pdfinfo $(PDFFILE) 2>/dev/null | grep Pages | awk '{print $$2}'); \
		size=$$(du -h $(PDFFILE) | cut -f1); \
		echo "$(CYAN)   Pages: $$pages | Size: $$size$(RESET)"; \
	fi

# Dependencies: all tex files that could affect the PDF
TEX_DEPS = $(TEXFILE) $(BIBFILE) \
	preamble/*.tex \
	front-matter/*.tex \
	$(filter-out $(COVER_VARS),$(wildcard front-matter/*/*.tex)) \
	chapters/*/chapter.tex \
	chapters/*/sections/*.tex \
	chapters/*/figures/*.tex \
	back-matter/*.tex

$(PDFFILE): $(TEX_DEPS)
	@echo "$(BOLD)$(BLUE)$(ARROW) Building $(PDFFILE)...$(RESET)"
	@if command -v $(LATEXMK) >/dev/null 2>&1; then \
		echo "$(CYAN)   Using latexmk (smart compilation)$(RESET)"; \
		$(LATEXMK) $(LATEXMK_OPTS) $(TEXFILE); \
	else \
		echo "$(CYAN)   Using manual compilation (4-pass)$(RESET)"; \
		$(LATEX) $(LATEX_OPTS) $(TEXFILE) || exit 1; \
		$(BIBER) $(MAIN) || exit 1; \
		$(LATEX) $(LATEX_OPTS) $(TEXFILE) || exit 1; \
		$(LATEX) $(LATEX_OPTS) $(TEXFILE) || exit 1; \
	fi

# ----------------------------------------------------------------------------
# Quick build (single pass)
# ----------------------------------------------------------------------------

.PHONY: quick
quick:
	@echo "$(BOLD)$(BLUE)$(ARROW) Quick build (single pass)...$(RESET)"
	$(LATEX) $(LATEX_OPTS) $(TEXFILE)
	@echo "$(BOLD)$(GREEN)$(CHECK) Quick build complete$(RESET)"

# ----------------------------------------------------------------------------
# Watch mode (continuous compilation)
# ----------------------------------------------------------------------------

.PHONY: watch
watch:
	@echo "$(BOLD)$(BLUE)$(ARROW) Starting watch mode...$(RESET)"
	@if command -v $(LATEXMK) >/dev/null 2>&1; then \
		$(LATEXMK) -pvc $(LATEXMK_OPTS) $(TEXFILE); \
	else \
		echo "$(RED)$(CROSS) latexmk required for watch mode$(RESET)"; \
		exit 1; \
	fi

# ----------------------------------------------------------------------------
# Validation
# ----------------------------------------------------------------------------

.PHONY: validate
validate:
	@echo "$(BOLD)$(BLUE)$(ARROW) Validating references and citations...$(RESET)"
	@echo ""
	@# Check for undefined references
	@if grep -q "LaTeX Warning: Reference .* undefined" $(MAIN).log 2>/dev/null; then \
		echo "$(YELLOW)Undefined references:$(RESET)"; \
		grep "LaTeX Warning: Reference .* undefined" $(MAIN).log | sed 's/LaTeX Warning: /  /'; \
		echo ""; \
	else \
		echo "$(GREEN)$(CHECK) No undefined references$(RESET)"; \
	fi
	@# Check for undefined citations
	@if grep -q "LaTeX Warning: Citation .* undefined" $(MAIN).log 2>/dev/null; then \
		echo "$(YELLOW)Undefined citations:$(RESET)"; \
		grep "LaTeX Warning: Citation .* undefined" $(MAIN).log | sed 's/LaTeX Warning: /  /'; \
		echo ""; \
	else \
		echo "$(GREEN)$(CHECK) No undefined citations$(RESET)"; \
	fi
	@# Check for multiply defined labels
	@if grep -q "LaTeX Warning: Label .* multiply defined" $(MAIN).log 2>/dev/null; then \
		echo "$(YELLOW)Multiply defined labels:$(RESET)"; \
		grep "LaTeX Warning: Label .* multiply defined" $(MAIN).log | sed 's/LaTeX Warning: /  /'; \
		echo ""; \
	else \
		echo "$(GREEN)$(CHECK) No multiply defined labels$(RESET)"; \
	fi
	@echo ""
	@echo "$(BOLD)$(GREEN)$(CHECK) Validation complete$(RESET)"

# ----------------------------------------------------------------------------
# View PDF
# ----------------------------------------------------------------------------

.PHONY: view
view: $(PDFFILE)
	@echo "$(BOLD)$(BLUE)$(ARROW) Opening $(PDFFILE)...$(RESET)"
	@if command -v xdg-open >/dev/null 2>&1; then \
		xdg-open $(PDFFILE) &; \
	elif command -v open >/dev/null 2>&1; then \
		open $(PDFFILE); \
	else \
		echo "$(RED)$(CROSS) No PDF viewer found$(RESET)"; \
	fi

# ----------------------------------------------------------------------------
# Word count
# ----------------------------------------------------------------------------

.PHONY: wordcount
wordcount:
	@echo "$(BOLD)$(BLUE)$(ARROW) Counting words...$(RESET)"
	@total=0; \
	for f in front-matter/preface.tex chapters/*/sections/*.tex; do \
		if [ -f "$$f" ]; then \
			words=$$(detex "$$f" 2>/dev/null | wc -w); \
			total=$$((total + words)); \
		fi; \
	done; \
	echo "$(CYAN)   Approximate word count: $$total$(RESET)"

# ----------------------------------------------------------------------------
# Cleaning
# ----------------------------------------------------------------------------

.PHONY: clean
clean:
	@echo "$(BOLD)$(BLUE)$(ARROW) Cleaning auxiliary files...$(RESET)"
	@rm -f $(MAIN).aux $(MAIN).bbl $(MAIN).bcf $(MAIN).blg
	@rm -f $(MAIN).fdb_latexmk $(MAIN).fls $(MAIN).log $(MAIN).out
	@rm -f $(MAIN).run.xml $(MAIN).toc $(MAIN).lot $(MAIN).lof
	@rm -f $(MAIN).synctex.gz $(MAIN).synctex
	@rm -f $(MAIN).xdv
	@rm -f $(COVER).aux $(COVER).log $(COVER).out
	@rm -f $(COVER).fdb_latexmk $(COVER).fls $(COVER).toc
	@rm -f $(COVER).synctex.gz $(COVER).synctex $(COVER).xdv
	@rm -f covers/*.aux covers/*.log covers/*.out covers/*.fdb_latexmk
	@rm -f covers/*.fls covers/*.synctex.gz covers/*.synctex covers/*.xdv
	@rm -f covers/*.toc
	@rm -f texput.log
	@# Clean glossary files
	@rm -f $(MAIN).glo $(MAIN).gls $(MAIN).glg $(MAIN).ist
	@rm -f $(MAIN).acn $(MAIN).acr $(MAIN).alg
	@# Clean chapter auxiliary files
	@find chapters -name "*.aux" -delete 2>/dev/null || true
	@echo "$(GREEN)$(CHECK) Cleaned auxiliary files$(RESET)"

.PHONY: cleanall
cleanall: clean
	@echo "$(BOLD)$(BLUE)$(ARROW) Removing PDF...$(RESET)"
	@rm -f $(PDFFILE)
	@rm -f $(COVER_PDF) $(COVER_FRONT_PDF) $(COVER_BACK_PDF) $(INTERIOR_PDF)
	@echo "$(GREEN)$(CHECK) Removed $(PDFFILE)$(RESET)"

# ----------------------------------------------------------------------------
# Lulu interior (strip covers)
# ----------------------------------------------------------------------------

.PHONY: interior
interior: $(INTERIOR_PDF)

$(INTERIOR_PDF): $(PDFFILE)
	@echo "$(BOLD)$(BLUE)$(ARROW) Building Lulu interior (strip covers)...$(RESET)"
	@if ! command -v mutool >/dev/null 2>&1; then \
		echo "$(RED)$(CROSS) mutool not found (install mupdf-tools)$(RESET)"; \
		exit 1; \
	fi
	@pages=$$(if command -v pdfinfo >/dev/null 2>&1; then \
		pdfinfo $(PDFFILE) 2>/dev/null | awk '/^Pages:/ {print $$2}'; \
	else \
		mutool info -M $(PDFFILE) 2>/dev/null | awk '/^Pages:/ {print $$2}'; \
	fi); \
	if [ -z "$$pages" ]; then \
		echo "$(RED)$(CROSS) Could not determine page count$(RESET)"; \
		exit 1; \
	fi; \
	if [ $$pages -le 3 ]; then \
		echo "$(RED)$(CROSS) Not enough pages to strip covers$(RESET)"; \
		exit 1; \
	fi; \
	last=$$((pages-1)); \
	mutool merge -o $(INTERIOR_PDF) $(PDFFILE) 3-$$last
	@echo "$(BOLD)$(GREEN)$(CHECK) Interior built: $(INTERIOR_PDF)$(RESET)"

# ----------------------------------------------------------------------------
# Export targets
# ----------------------------------------------------------------------------

.PHONY: png
png: $(PDFFILE)
	@echo "$(BOLD)$(BLUE)$(ARROW) Converting PDF to PNG images...$(RESET)"
	@mkdir -p png
	@if command -v pdftoppm >/dev/null 2>&1; then \
		pdftoppm -png -r 300 $(PDFFILE) png/page; \
		echo "$(GREEN)$(CHECK) PNG images created in png/$(RESET)"; \
	else \
		echo "$(RED)$(CROSS) pdftoppm not found (install poppler-utils)$(RESET)"; \
	fi

.PHONY: zip
zip: $(PDFFILE)
	@echo "$(BOLD)$(BLUE)$(ARROW) Creating distribution ZIP...$(RESET)"
	@zip -r llm-essentials-law-finance.zip \
		$(PDFFILE) \
		$(TEXFILE) \
		front-matter/ \
		chapters/ \
		bib/ \
		Makefile \
		-x "*.aux" -x "*.log" -x "*.synctex*"
	@echo "$(GREEN)$(CHECK) Created llm-essentials-law-finance.zip$(RESET)"

# ----------------------------------------------------------------------------
# Help
# ----------------------------------------------------------------------------

.PHONY: help
help:
	@echo ""
	@echo "$(BOLD)LLM Essentials for Law and Finance - Build System$(RESET)"
	@echo ""
	@echo "$(BOLD)Usage:$(RESET)"
	@echo "  make [target]"
	@echo ""
	@echo "$(BOLD)Build Targets:$(RESET)"
	@echo "  $(CYAN)pdf$(RESET)              Build the complete mini-book PDF (default)"
	@echo "  $(CYAN)quick$(RESET)            Single-pass build for minor edits"
	@echo "  $(CYAN)watch$(RESET)            Continuous compilation on file changes"
	@echo "  $(CYAN)validate$(RESET)         Check for undefined references and citations"
	@echo ""
	@echo "$(BOLD)Lulu Publishing:$(RESET)"
	@echo "  $(CYAN)interior$(RESET)         Build Lulu interior PDF (strip covers)"
	@echo ""
	@echo "$(BOLD)Utilities:$(RESET)"
	@echo "  $(CYAN)view$(RESET)             Open the PDF in default viewer"
	@echo "  $(CYAN)wordcount$(RESET)        Approximate word count of content"
	@echo "  $(CYAN)clean$(RESET)            Remove auxiliary files (keep PDF)"
	@echo "  $(CYAN)cleanall$(RESET)         Remove all generated files including PDF"
	@echo "  $(CYAN)png$(RESET)              Convert PDF pages to PNG images"
	@echo "  $(CYAN)zip$(RESET)              Create distribution ZIP archive"
	@echo "  $(CYAN)help$(RESET)             Display this help message"
	@echo ""
