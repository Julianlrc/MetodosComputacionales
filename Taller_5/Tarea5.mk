Resultado_hw5.pdf : *.png Resultados_hw5.tex
	pdflatex Resultados_hw5.tex

*.png : *.txt plots_canal_ionico.py
	python plots_canal_ionico.py

*.txt : a.out
	./a.out

a.out : canal_ionico.c
	gcc canal_ionico.c -lm
