#PLOTSSSSSSS

Resultado_hw5.pdf : $(plots) Resultados_hw5.tex
	pdflatex Resultados.tex

$(plots) : plots_canal_ionico.py $(files)
	python plots_canal_ionico.py

$(files) : a.out
	./a.out

a.out : canal_ionico.c
	gcc canal_ionico.c -lm
