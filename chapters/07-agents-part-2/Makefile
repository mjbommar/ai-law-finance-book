# ============================================================================
# Makefile for LaTeX Document Compilation — Agents Part II
# ============================================================================
# Mirrors the Part I chapter build with latexmk/biber support.
# ============================================================================

# Document settings
MAIN = main
TEXFILE = $(MAIN).tex
PDFFILE = $(MAIN).pdf

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

# ANSI color codes for pretty output
BOLD = \033[1m
RED = \033[31m
GREEN = \033[32m
YELLOW = \033[33m
BLUE = \033[34m
MAGENTA = \033[35m
CYAN = \033[36m
RESET = \033[0m

# Icons
CHECK = ✓
CROSS = ✗
ARROW = ➜
STAR = ★

# ============================================================================
# Main Targets
# ============================================================================

.PHONY: all pdf quick clean cleanall view help watch wordcount png zip overleaf validate

all: pdf
	@echo "$(GREEN)$(BOLD)$(CHECK) Build complete!$(RESET)"

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

pdf-latexmk:
	@echo "$(YELLOW)$(ARROW) Running latexmk...$(RESET)"
	@$(LATEXMK) $(LATEXMK_FLAGS) $(TEXFILE) 2>&1 | grep -v "^Latexmk:" || true
	@if [ -f $(PDFFILE) ]; then \
		echo "$(GREEN)$(CHECK) PDF generated successfully$(RESET)"; \
	else \
		echo "$(RED)$(CROSS) PDF generation failed$(RESET)"; \
		exit 1; \
	fi

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

quick:
	@echo "$(CYAN)$(BOLD)$(ARROW) Quick compile (single pass)...$(RESET)"
	@$(LATEX) $(LATEX_FLAGS) $(TEXFILE)
	@if [ -f $(PDFFILE) ]; then \
		echo "$(GREEN)$(CHECK) Quick compile complete$(RESET)"; \
		$(MAKE) show-summary; \
	fi

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

view: $(PDFFILE)
	@echo "$(CYAN)$(ARROW) Opening PDF viewer...$(RESET)"
	@$(VIEWER) $(PDFFILE) &

png: $(PDFFILE)
	@echo "$(CYAN)$(BOLD)$(ARROW) Converting PDF to PNG images...$(RESET)"
	@mkdir -p $(PNG_DIR)
	@$(PDFTOPPM) -png -r 300 $(PDFFILE) $(PNG_DIR)/page
	@count=$$(ls $(PNG_DIR)/*.png 2>/dev/null | wc -l); \
	echo "$(GREEN)$(CHECK) Created $$count PNG images in $(PNG_DIR)/$(RESET)"

zip:
	@echo "$(CYAN)$(BOLD)$(ARROW) Creating distribution package...$(RESET)"
	@zip_name="$(MAIN)-$$(date +%Y%m%d).zip"; \
	zip -r ../$$zip_name \
		$(TEXFILE) \
		sections/ \
		figures/ \
		*.cls *.sty \
		-x "*.aux" "*.log" "*.bbl" "*.bcf" "*.blg" "*.out" "*.toc" "*.run.xml" \
		2>/dev/null || true; \
	echo "$(GREEN)$(CHECK) Created ../$$zip_name$(RESET)"

overleaf:
	@echo "$(CYAN)$(BOLD)$(ARROW) Creating Overleaf package...$(RESET)"
	@tmp_dir=$$(mktemp -d -p /tmp); \
	pkg_name="$(MAIN)-overleaf-$$(date +%Y%m%d-%H%M%S)"; \
	pkg_dir="$$tmp_dir/$$pkg_name"; \
	current_dir=$$(pwd); \
	mkdir -p "$$pkg_dir"; \
	echo "$(BLUE)  $(ARROW) Assembling files...$(RESET)"; \
	cp $(TEXFILE) "$$pkg_dir/" 2>/dev/null || true; \
	if [ -d sections ]; then cp -r sections "$$pkg_dir/"; fi; \
	if [ -d figures ]; then cp -r figures "$$pkg_dir/"; fi; \
	cp ../../preamble.tex "$$pkg_dir/" 2>/dev/null || true; \
	if [ -f ../../bib/refs.bib ]; then \
		mkdir -p "$$pkg_dir/bib"; \
		cp ../../bib/refs.bib "$$pkg_dir/bib/" 2>/dev/null || true; \
	fi; \
	find "$$pkg_dir" -type f \( \
		-name "*.aux" -o -name "*.log" -o -name "*.bbl" -o \
		-name "*.bcf" -o -name "*.blg" -o -name "*.out" -o \
		-name "*.toc" -o -name "*.run.xml" -o -name "*.fls" -o \
		-name "*.fdb_latexmk" -o -name "*.synctex.gz" -o \
		-name "*-SAVE-ERROR" \
	\) -delete 2>/dev/null || true; \
	cd "$$tmp_dir" && zip -r "$$pkg_name.zip" "$$pkg_name" > /dev/null 2>&1; \
	mv "$$tmp_dir/$$pkg_name.zip" "$$current_dir/$$pkg_name.zip"; \
	rm -rf "$$tmp_dir"; \
	if [ -f "$$current_dir/$$pkg_name.zip" ]; then \
		size=$$(du -h "$$current_dir/$$pkg_name.zip" | cut -f1); \
		echo "$(GREEN)$(CHECK) Created $$pkg_name.zip ($$size)$(RESET)"; \
		echo "$(CYAN)  $(ARROW) Ready for upload to Overleaf!$(RESET)"; \
	else \
		echo "$(RED)$(CROSS) Failed to create Overleaf package$(RESET)"; \
		exit 1; \
	fi

# ============================================================================
# Cleaning Targets
# ============================================================================

clean:
	@echo "$(YELLOW)$(ARROW) Cleaning auxiliary files...$(RESET)"
	@rm -f *.aux *.log *.bbl *.bcf *.blg *.out *.toc *.lof *.lot \
	       *.fls *.fdb_latexmk *.synctex.gz *.run.xml *.xdv \
	       compile*.log biber.log
	@rm -f sections/*.aux
	@echo "$(GREEN)$(CHECK) Cleaned auxiliary files$(RESET)"

cleanall: clean
	@echo "$(YELLOW)$(ARROW) Removing all generated files...$(RESET)"
	@rm -f $(PDFFILE)
	@rm -rf $(PNG_DIR)
	@echo "$(GREEN)$(CHECK) Cleaned all generated files$(RESET)"

distclean: cleanall
	@echo "$(YELLOW)$(ARROW) Deep cleaning...$(RESET)"
	@rm -f *~ *.backup
	@rm -rf auto/
	@echo "$(GREEN)$(CHECK) Repository reset to pristine state$(RESET)"

help:
	@echo "$(CYAN)$(BOLD)════════════════════════════════════════════════════════$(RESET)"
	@echo "$(CYAN)$(BOLD)  LaTeX Document Build System — Agents Part II$(RESET)"
	@echo "$(CYAN)$(BOLD)════════════════════════════════════════════════════════$(RESET)"
	@echo "  make / make pdf     Build the PDF"
	@echo "  make quick          Single-pass compile"
	@echo "  make watch          Watch mode with latexmk"
	@echo "  make validate       Check refs and citations"
	@echo "  make clean[all]     Clean artifacts"
	@echo "  make overleaf       Create Overleaf-ready ZIP"

# PDF depends on main + sections + figures
$(PDFFILE): $(TEXFILE) sections/*.tex figures/*.tex
	@$(MAKE) pdf-manual

