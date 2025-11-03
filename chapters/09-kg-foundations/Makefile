MAIN = main
TEXFILE = $(MAIN).tex

pdf:
	latexmk -pdf -pdflatex="pdflatex -interaction=nonstopmode -halt-on-error" $(TEXFILE)

clean:
	latexmk -C

validate:
	@grep -n "LaTeX Warning.*undefined" $(MAIN).log || echo "No undefined refs"
	@grep -n "LaTeX Warning.*citation" $(MAIN).log || echo "No citation warnings"

