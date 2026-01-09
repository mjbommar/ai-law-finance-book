# ============================================================================
# Makefile — Foundations: Structured Outputs, Tools, and Multimodal
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

.PHONY: all pdf quick clean cleanall validate

all: pdf

pdf:
	@if command -v $(LATEXMK) >/dev/null 2>&1; then $(LATEXMK) $(LATEXMK_FLAGS) $(TEXFILE); else $(MAKE) pdf-manual; fi

pdf-manual:
	@$(LATEX) $(LATEX_FLAGS) $(TEXFILE) > compile1.log 2>&1 || (cat compile1.log && exit 1)
	@if [ -f $(MAIN).bcf ]; then $(BIBER) $(MAIN) > biber.log 2>&1 || (cat biber.log && exit 1); fi
	@$(LATEX) $(LATEX_FLAGS) $(TEXFILE) > compile2.log 2>&1 || (cat compile2.log && exit 1)
	@$(LATEX) $(LATEX_FLAGS) $(TEXFILE) > compile3.log 2>&1 || (cat compile3.log && exit 1)

clean:
	@rm -f *.aux *.log *.bbl *.bcf *.blg *.out *.toc *.fls *.fdb_latexmk *.run.xml compile*.log biber.log sections/*.aux

cleanall: clean
	@rm -f $(PDFFILE)

validate:
	@grep -n "LaTeX Warning.*undefined" $(MAIN).log 2>/dev/null || echo "No undefined refs"
	@grep -n "LaTeX Warning.*citation" $(MAIN).log 2>/dev/null || echo "No citation warnings"

