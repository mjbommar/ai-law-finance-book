# ============================================================================
# Makefile for LaTeX Document Compilation
# ============================================================================
# A comprehensive, user-friendly Makefile for building LaTeX documents
# with beautiful output and smart dependency handling.
# ============================================================================

# Document settings
MAIN = main
TEXFILE = $(MAIN).tex
PDFFILE = $(MAIN).pdf
BIBFILE = bib/refs.bib

# Commands
LATEX = pdflatex
BIBER = biber
LATEXMK = latexmk
VIEWER = xdg-open
PDFTOPPM = pdftoppm

# Compilation flags
LATEX_FLAGS = -interaction=nonstopmode -file-line-error -halt-on-error
LATEXMK_FLAGS = -pdf -pdflatex="$(LATEX) $(LATEX_FLAGS)" -use-make

# Output directories
PNG_DIR = png_pages

# ANSI color codes for beautiful output
BOLD = \033[1m
RED = \033[31m
GREEN = \033[32m
YELLOW = \033[33m
BLUE = \033[34m
MAGENTA = \033[35m
CYAN = \033[36m
RESET = \033[0m

# Icons for visual feedback
CHECK = ✓
CROSS = ✗
ARROW = ➜
STAR = ★

# ============================================================================
# Main Targets
# ============================================================================

.PHONY: all pdf quick clean cleanall view help watch wordcount png zip validate

# Default target
all: pdf
	@echo "$(GREEN)$(BOLD)$(CHECK) Build complete!$(RESET)"

# Build PDF using smart method (latexmk if available, manual otherwise)
pdf:
	@echo "$(CYAN)$(BOLD)════════════════════════════════════════════════════════$(RESET)"
	@echo "$(CYAN)$(BOLD)  Building: $(MAIN).pdf$(RESET)"
	@echo "$(CYAN)$(BOLD)════════════════════════════════════════════════════════$(RESET)"
	@if command -v $(LATEXMK) >/dev/null 2>&1; then \
		echo "$(BLUE)$(ARROW) Using latexmk for smart compilation...$(RESET)"; \
		$(MAKE) pdf-latexmk; \
	else \
		echo "$(BLUE)$(ARROW) Using manual compilation...$(RESET)"; \
		$(MAKE) pdf-manual; \
	fi
	@$(MAKE) show-summary

# Smart compilation with latexmk (automatically handles dependencies)
pdf-latexmk:
	@echo "$(YELLOW)$(ARROW) Running latexmk...$(RESET)"
	@$(LATEXMK) $(LATEXMK_FLAGS) $(TEXFILE) 2>&1 | grep -v "^Latexmk:" || true
	@if [ -f $(PDFFILE) ]; then \
		echo "$(GREEN)$(CHECK) PDF generated successfully$(RESET)"; \
	else \
		echo "$(RED)$(CROSS) PDF generation failed$(RESET)"; \
		exit 1; \
	fi

# Manual compilation (full build: pdflatex -> biber -> pdflatex -> pdflatex)
pdf-manual:
	@echo "$(YELLOW)$(ARROW) Pass 1/4: Initial pdflatex run...$(RESET)"
	@$(LATEX) $(LATEX_FLAGS) $(TEXFILE) > compile1.log 2>&1 || (cat compile1.log && exit 1)
	@echo "$(GREEN)  $(CHECK) Pass 1 complete$(RESET)"
	@if [ -f $(MAIN).bcf ]; then \
		echo "$(YELLOW)$(ARROW) Pass 2/4: Running biber for bibliography...$(RESET)"; \
		$(BIBER) $(MAIN) > biber.log 2>&1 || (cat biber.log && exit 1); \
		echo "$(GREEN)  $(CHECK) Bibliography processed$(RESET)"; \
	fi
	@echo "$(YELLOW)$(ARROW) Pass 3/4: Second pdflatex run (resolve citations)...$(RESET)"
	@$(LATEX) $(LATEX_FLAGS) $(TEXFILE) > compile2.log 2>&1 || (cat compile2.log && exit 1)
	@echo "$(GREEN)  $(CHECK) Pass 2 complete$(RESET)"
	@echo "$(YELLOW)$(ARROW) Pass 4/4: Final pdflatex run (resolve references)...$(RESET)"
	@$(LATEX) $(LATEX_FLAGS) $(TEXFILE) > compile3.log 2>&1 || (cat compile3.log && exit 1)
	@echo "$(GREEN)  $(CHECK) Pass 3 complete$(RESET)"

# Quick compile (single pdflatex run, for minor edits)
quick:
	@echo "$(CYAN)$(BOLD)$(ARROW) Quick compile (single pass)...$(RESET)"
	@$(LATEX) $(LATEX_FLAGS) $(TEXFILE)
	@if [ -f $(PDFFILE) ]; then \
		echo "$(GREEN)$(CHECK) Quick compile complete$(RESET)"; \
		$(MAKE) show-summary; \
	fi

# Watch mode (continuous compilation on file changes)
watch:
	@if ! command -v $(LATEXMK) >/dev/null 2>&1; then \
		echo "$(RED)$(CROSS) Error: latexmk is required for watch mode$(RESET)"; \
		echo "$(YELLOW)  Install with: sudo apt-get install latexmk$(RESET)"; \
		exit 1; \
	fi
	@echo "$(CYAN)$(BOLD)$(STAR) Watch mode: Compiling on file changes...$(RESET)"
	@echo "$(YELLOW)  Press Ctrl+C to stop$(RESET)"
	@$(LATEXMK) $(LATEXMK_FLAGS) -pvc $(TEXFILE)

# ============================================================================
# Utility Targets
# ============================================================================

# Show document summary
show-summary:
	@if [ -f $(PDFFILE) ]; then \
		echo ""; \
		echo "$(CYAN)$(BOLD)════════════════════════════════════════════════════════$(RESET)"; \
		echo "$(GREEN)$(BOLD)  $(STAR) Document Summary$(RESET)"; \
		echo "$(CYAN)════════════════════════════════════════════════════════$(RESET)"; \
		pages=$$(pdfinfo $(PDFFILE) 2>/dev/null | grep "Pages:" | awk '{print $$2}'); \
		size=$$(du -h $(PDFFILE) | cut -f1); \
		echo "$(BOLD)  File:$(RESET)  $(PDFFILE)"; \
		echo "$(BOLD)  Pages:$(RESET) $$pages"; \
		echo "$(BOLD)  Size:$(RESET)  $$size"; \
		echo "$(CYAN)════════════════════════════════════════════════════════$(RESET)"; \
		echo ""; \
	fi

# Word count (approximate, from LaTeX source)
wordcount:
	@echo "$(CYAN)$(BOLD)$(ARROW) Counting words...$(RESET)"
	@if command -v detex >/dev/null 2>&1; then \
		words=$$(detex $(TEXFILE) sections/*.tex 2>/dev/null | wc -w); \
		echo "$(GREEN)  Approximate word count: $$words words$(RESET)"; \
	else \
		echo "$(YELLOW)  Note: Install 'detex' for accurate word count$(RESET)"; \
		words=$$(cat $(TEXFILE) sections/*.tex 2>/dev/null | grep -v "^%" | wc -w); \
		echo "$(YELLOW)  Rough estimate: $$words words$(RESET)"; \
	fi

# Validate references and citations
validate:
	@echo "$(CYAN)$(BOLD)$(ARROW) Validating document...$(RESET)"
	@echo "$(BLUE)  Checking for undefined references...$(RESET)"
	@if grep -n "LaTeX Warning.*undefined" $(MAIN).log 2>/dev/null; then \
		echo "$(RED)$(CROSS) Found undefined references$(RESET)"; \
	else \
		echo "$(GREEN)$(CHECK) All references defined$(RESET)"; \
	fi
	@echo "$(BLUE)  Checking for citation warnings...$(RESET)"
	@if grep -n "LaTeX Warning.*citation" $(MAIN).log 2>/dev/null; then \
		echo "$(RED)$(CROSS) Found citation warnings$(RESET)"; \
	else \
		echo "$(GREEN)$(CHECK) All citations OK$(RESET)"; \
	fi

# View the PDF
view: $(PDFFILE)
	@echo "$(CYAN)$(ARROW) Opening PDF viewer...$(RESET)"
	@$(VIEWER) $(PDFFILE) &

# Convert PDF pages to PNG images (useful for presentations/previews)
png: $(PDFFILE)
	@echo "$(CYAN)$(BOLD)$(ARROW) Converting PDF to PNG images...$(RESET)"
	@mkdir -p $(PNG_DIR)
	@$(PDFTOPPM) -png -r 300 $(PDFFILE) $(PNG_DIR)/page
	@count=$$(ls $(PNG_DIR)/*.png 2>/dev/null | wc -l); \
	echo "$(GREEN)$(CHECK) Created $$count PNG images in $(PNG_DIR)/$(RESET)"

# Create distributable ZIP (like Overleaf package)
zip:
	@echo "$(CYAN)$(BOLD)$(ARROW) Creating distribution package...$(RESET)"
	@zip_name="$(MAIN)-$$(date +%Y%m%d).zip"; \
	zip -r ../$$zip_name \
		$(TEXFILE) \
		$(BIBFILE) \
		sections/ \
		figures/ \
		*.cls *.sty \
		-x "*.aux" "*.log" "*.bbl" "*.bcf" "*.blg" "*.out" "*.toc" "*.run.xml" \
		2>/dev/null || true; \
	echo "$(GREEN)$(CHECK) Created ../$$zip_name$(RESET)"

# ============================================================================
# Cleaning Targets
# ============================================================================

# Clean auxiliary files (keep PDF)
clean:
	@echo "$(YELLOW)$(ARROW) Cleaning auxiliary files...$(RESET)"
	@rm -f *.aux *.log *.bbl *.bcf *.blg *.out *.toc *.lof *.lot \
	       *.fls *.fdb_latexmk *.synctex.gz *.run.xml *.xdv \
	       compile*.log biber.log
	@rm -f sections/*.aux
	@echo "$(GREEN)$(CHECK) Cleaned auxiliary files$(RESET)"

# Clean everything including PDF
cleanall: clean
	@echo "$(YELLOW)$(ARROW) Removing all generated files...$(RESET)"
	@rm -f $(PDFFILE)
	@rm -rf $(PNG_DIR)
	@echo "$(GREEN)$(CHECK) Cleaned all generated files$(RESET)"

# Deep clean (reset to pristine state)
distclean: cleanall
	@echo "$(YELLOW)$(ARROW) Deep cleaning...$(RESET)"
	@rm -f *~ *.backup
	@rm -rf auto/
	@echo "$(GREEN)$(CHECK) Repository reset to pristine state$(RESET)"

# ============================================================================
# Help Target
# ============================================================================

help:
	@echo "$(CYAN)$(BOLD)════════════════════════════════════════════════════════$(RESET)"
	@echo "$(CYAN)$(BOLD)  LaTeX Document Build System$(RESET)"
	@echo "$(CYAN)$(BOLD)════════════════════════════════════════════════════════$(RESET)"
	@echo ""
	@echo "$(BOLD)Main Targets:$(RESET)"
	@echo "  $(GREEN)make$(RESET) or $(GREEN)make pdf$(RESET)    Build the PDF document (full compilation)"
	@echo "  $(GREEN)make quick$(RESET)           Quick compile (single pass, for minor edits)"
	@echo "  $(GREEN)make watch$(RESET)           Watch mode: auto-recompile on changes"
	@echo "  $(GREEN)make view$(RESET)            Open the PDF in your default viewer"
	@echo ""
	@echo "$(BOLD)Utility Targets:$(RESET)"
	@echo "  $(GREEN)make wordcount$(RESET)       Show approximate word count"
	@echo "  $(GREEN)make validate$(RESET)        Check for undefined references/citations"
	@echo "  $(GREEN)make png$(RESET)             Convert PDF pages to PNG images"
	@echo "  $(GREEN)make zip$(RESET)             Create distributable ZIP package"
	@echo ""
	@echo "$(BOLD)Cleaning Targets:$(RESET)"
	@echo "  $(GREEN)make clean$(RESET)           Remove auxiliary files (keep PDF)"
	@echo "  $(GREEN)make cleanall$(RESET)        Remove all generated files (including PDF)"
	@echo "  $(GREEN)make distclean$(RESET)       Deep clean (reset to pristine state)"
	@echo ""
	@echo "$(BOLD)Help:$(RESET)"
	@echo "  $(GREEN)make help$(RESET)            Show this help message"
	@echo ""
	@echo "$(CYAN)════════════════════════════════════════════════════════$(RESET)"

# ============================================================================
# Dependencies
# ============================================================================

# PDF depends on all source files
$(PDFFILE): $(TEXFILE) $(BIBFILE) sections/*.tex figures/*.tex
	@$(MAKE) pdf-manual
