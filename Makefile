all: pdf

TERGET=C91Book

pdf:
	xelatex ${TERGET}
	xelatex ${TERGET}

clean:
	rm -f *.log *.pdf *.aux *.out
