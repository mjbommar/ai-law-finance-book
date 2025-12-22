# ============================================================================
# MAKEFILE - Agents in Law and Finance (Mini-Book)
# ============================================================================
# Build system for the mini-book combining chapters on agent concepts,
# design, and governance.
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

# LaTeX tools - using XeLaTeX for fontspec support (works with standalone+tikz)
LATEX = xelatex
BIBER = biber
LATEXMK = latexmk

# Latexmk options - use xelatex
LATEXMK_OPTS = -xelatex -interaction=nonstopmode -file-line-error -halt-on-error

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

$(PDFFILE): $(TEXFILE) $(BIBFILE) preamble/*.tex front-matter/preface.tex chapters/*/chapter.tex
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
	@echo "$(GREEN)$(CHECK) Removed $(PDFFILE)$(RESET)"

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
	@zip -r agents-in-law-finance.zip \
		$(PDFFILE) \
		$(TEXFILE) \
		front-matter/ \
		chapters/ \
		bib/ \
		Makefile \
		-x "*.aux" -x "*.log" -x "*.synctex*"
	@echo "$(GREEN)$(CHECK) Created agents-in-law-finance.zip$(RESET)"

# ----------------------------------------------------------------------------
# Help
# ----------------------------------------------------------------------------

.PHONY: help
help:
	@echo ""
	@echo "$(BOLD)Agents in Law and Finance - Build System$(RESET)"
	@echo ""
	@echo "$(BOLD)Usage:$(RESET)"
	@echo "  make [target]"
	@echo ""
	@echo "$(BOLD)Targets:$(RESET)"
	@echo "  $(CYAN)pdf$(RESET)        Build the complete mini-book PDF (default)"
	@echo "  $(CYAN)quick$(RESET)      Single-pass build for minor edits"
	@echo "  $(CYAN)watch$(RESET)      Continuous compilation on file changes"
	@echo "  $(CYAN)validate$(RESET)   Check for undefined references and citations"
	@echo "  $(CYAN)view$(RESET)       Open the PDF in default viewer"
	@echo "  $(CYAN)wordcount$(RESET)  Approximate word count of content"
	@echo "  $(CYAN)clean$(RESET)      Remove auxiliary files (keep PDF)"
	@echo "  $(CYAN)cleanall$(RESET)   Remove all generated files including PDF"
	@echo "  $(CYAN)png$(RESET)        Convert PDF pages to PNG images"
	@echo "  $(CYAN)zip$(RESET)        Create distribution ZIP archive"
	@echo "  $(CYAN)help$(RESET)       Display this help message"
	@echo ""
