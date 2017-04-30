plots = f1_0.pdf f1_100.pdf f1_2500.pdf f2_0.pdf f2_100.pdf f2_2500.pdf a1_0.pdf a1_100.pdf a1_2500.pdf a2_0.pdf a2_100.pdf a2_2500.pdf p1_0.pdf p1_100.pdf p1_2500.pdf p2_0.pdf p2_100.pdf p2_2500.pdf prom1.pdf prom2.pdf 

files = fijas_caso1_0.txt fijas_caso1_100.txt fijas_caso1_2500.txt fijas_caso2_0.txt fijas_caso2_100.txt fijas_caso2_2500.txt abiertas_caso1_0.txt abiertas_caso1_100.txt abiertas_caso1_2500.txt abiertas_caso2_0.txt abiertas_caso2_100.txt abiertas_caso2_2500.txt periodicas_caso1_0.txt periodicas_caso1_100.txt periodicas_caso1_2500.txt periodicas_caso2_0.txt periodicas_caso2_100.txt periodicas_caso2_2500.txt fijas_caso1_prom.txt fijas_caso2_prom.txt abiertas_caso1_prom.txt abiertas_caso2_prom.txt periodicas_caso1_prom.txt periodicas_caso2_prom.txt

Resultados_hw4.pdf : $(plots) Resultados_hw4.tex
	pdflatex Resultados_hw4.tex

$(plots) : Plots_Temperatura.py $(files)
	python Plots_Temperatura.py

$(files) : a.out
	./a.out

a.out : DifusionTemperatura.c
	cc -lm DifusionTemperatura.c
