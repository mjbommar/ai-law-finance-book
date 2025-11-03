# ============================================================================
# Makefile for LaTeX Document Compilation — Agents Part III
# ============================================================================

MAIN = main
TEXFILE = $(MAIN).tex
PDFFILE = $(MAIN).pdf

LATEX = pdflatex
BIBER = biber
LATEXMK = latexmk
VIEWER = xdg-open
PDFTOPPM = pdftoppm

LATEX_FLAGS = -interaction=nonstopmode -file-line-error -halt-on-error
LATEXMK_FLAGS = -pdf -pdflatex="$(LATEX) $(LATEX_FLAGS)" -use-make

PNG_DIR = png_pages

BOLD = \033[1m
RED = \033[31m
GREEN = \033[32m
YELLOW = \033[33m
BLUE = \033[34m
CYAN = \033[36m
RESET = \033[0m

CHECK = ✓
CROSS = ✗
ARROW = ➜
STAR = ★

.PHONY: all pdf quick clean cleanall view help watch wordcount png overleaf validate

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
		echo "$(YELLOW)$(ARROW) Pass 2/4: Running biber...$(RESET)"; \
		$(BIBER) $(MAIN) > biber.log 2>&1 || (cat biber.log && exit 1); \
		echo "$(GREEN)  $(CHECK) Bibliography processed$(RESET)"; \
	fi
	@echo "$(YELLOW)$(ARROW) Pass 3/4: Second pdflatex...$(RESET)"
	@$(LATEX) $(LATEX_FLAGS) $(TEXFILE) > compile2.log 2>&1 || (cat compile2.log && exit 1)
	@echo "$(YELLOW)$(ARROW) Pass 4/4: Final pdflatex...$(RESET)"
	@$(LATEX) $(LATEX_FLAGS) $(TEXFILE) > compile3.log 2>&1 || (cat compile3.log && exit 1)

quick:
	@$(LATEX) $(LATEX_FLAGS) $(TEXFILE)

watch:
	@$(LATEXMK) $(LATEXMK_FLAGS) -pvc $(TEXFILE)

show-summary:
	@if [ -f $(PDFFILE) ]; then \
		pages=$$(pdfinfo $(PDFFILE) 2>/dev/null | grep "Pages:" | awk '{print $$2}'); \
		size=$$(du -h $(PDFFILE) | cut -f1); \
		echo "$(CYAN)$(BOLD)════════════════════════════════════════════════════════$(RESET)"; \
		echo "$(GREEN)$(BOLD)  $(STAR) Document Summary$(RESET)"; \
		echo "  File: $(PDFFILE)"; \
		echo "  Pages: $$pages"; \
		echo "  Size: $$size"; \
		echo "$(CYAN)════════════════════════════════════════════════════════$(RESET)"; \
	fi

validate:
	@if grep -n "LaTeX Warning.*undefined" $(MAIN).log 2>/dev/null; then \
		echo "$(RED)$(CROSS) Found undefined references$(RESET)"; \
	else \
		echo "$(GREEN)$(CHECK) All references defined$(RESET)"; \
	fi
	@if grep -n "LaTeX Warning.*citation" $(MAIN).log 2>/dev/null; then \
		echo "$(RED)$(CROSS) Found citation warnings$(RESET)"; \
	else \
		echo "$(GREEN)$(CHECK) All citations OK$(RESET)"; \
	fi

view: $(PDFFILE)
	@$(VIEWER) $(PDFFILE) &

png: $(PDFFILE)
	@mkdir -p $(PNG_DIR)
	@$(PDFTOPPM) -png -r 300 $(PDFFILE) $(PNG_DIR)/page

clean:
	@rm -f *.aux *.log *.bbl *.bcf *.blg *.out *.toc *.lof *.lot *.fls *.fdb_latexmk *.synctex.gz *.run.xml *.xdv compile*.log biber.log
	@rm -f sections/*.aux

cleanall: clean
	@rm -f $(PDFFILE)
	@rm -rf $(PNG_DIR)

overleaf:
	@tmp_dir=$$(mktemp -d -p /tmp); \
	pkg_name="$(MAIN)-overleaf-$$(date +%Y%m%d-%H%M%S)"; \
	pkg_dir="$$tmp_dir/$$pkg_name"; \
	mkdir -p "$$pkg_dir"; \
	cp $(TEXFILE) "$$pkg_dir/"; \
	cp ../../preamble.tex "$$pkg_dir/"; \
	if [ -f ../../bib/refs.bib ]; then mkdir -p "$$pkg_dir/bib" && cp ../../bib/refs.bib "$$pkg_dir/bib/"; fi; \
	cp -r sections "$$pkg_dir/"; \
	cd "$$tmp_dir" && zip -r "$$pkg_name.zip" "$$pkg_name" >/dev/null 2>&1; \
	mv "$$tmp_dir/$$pkg_name.zip" . ; \
	rm -rf "$$tmp_dir"

$(PDFFILE): $(TEXFILE) sections/*.tex figures/*.tex
	@$(MAKE) pdf-manual

