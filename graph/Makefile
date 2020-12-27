all: Makefile *.tex 
	pdflatex main
	bibtex main -min-crossrefs=5
	pdflatex main

clean:
	rm -f *.aux *.bbl *.blg *.log *.out *.rel comment.cut main.pdf

.PHONY: all clean
