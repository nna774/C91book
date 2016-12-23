all: pdf

TERGET=C91Book
TEX=xelatex -halt-on-error -interaction=nonstopmode -file-line-error

pdf:
	${TEX} ${TERGET}
	${TEX} ${TERGET}

clean:
	rm -f *.log *.pdf *.aux *.out
