# ============================================================================
# Makefile — Foundations: Conversations & Reasoning
# ============================================================================

# Reuse the same build script by including or copying; keep self-contained.

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

.PHONY: all pdf quick clean cleanall view help watch wordcount png zip overleaf validate

all: pdf
	@echo "$(GREEN)$(BOLD)$(CHECK) Build complete!$(RESET)"

pdf:
	@echo "$(CYAN)$(BOLD) Building: $(MAIN).pdf$(RESET)"
	@if command -v $(LATEXMK) >/dev/null 2>&1; then $(MAKE) pdf-latexmk; else $(MAKE) pdf-manual; fi
	@$(MAKE) show-summary

pdf-latexmk:
	@$(LATEXMK) $(LATEXMK_FLAGS) $(TEXFILE) 2>&1 | grep -v "^Latexmk:" || true
	@if [ -f $(PDFFILE) ]; then echo "$(GREEN)$(CHECK) PDF generated$(RESET)"; else echo "$(RED)$(CROSS) Failed$(RESET)"; exit 1; fi

pdf-manual:
	@$(LATEX) $(LATEX_FLAGS) $(TEXFILE) > compile1.log 2>&1 || (cat compile1.log && exit 1)
	@if [ -f $(MAIN).bcf ]; then $(BIBER) $(MAIN) > biber.log 2>&1 || (cat biber.log && exit 1); fi
	@$(LATEX) $(LATEX_FLAGS) $(TEXFILE) > compile2.log 2>&1 || (cat compile2.log && exit 1)
	@$(LATEX) $(LATEX_FLAGS) $(TEXFILE) > compile3.log 2>&1 || (cat compile3.log && exit 1)

show-summary:
	@if [ -f $(PDFFILE) ]; then pages=$$(pdfinfo $(PDFFILE) 2>/dev/null | grep "Pages:" | awk '{print $$2}'); size=$$(du -h $(PDFFILE) | cut -f1); echo "PDF: $(PDFFILE) — $$pages pages — $$size"; fi

validate:
	@grep -n "LaTeX Warning.*undefined" $(MAIN).log 2>/dev/null || echo "No undefined refs"
	@grep -n "LaTeX Warning.*citation" $(MAIN).log 2>/dev/null || echo "No citation warnings"

clean:
	@rm -f *.aux *.log *.bbl *.bcf *.blg *.out *.toc *.fls *.fdb_latexmk *.run.xml compile*.log biber.log sections/*.aux

cleanall: clean
	@rm -f $(PDFFILE)

