plots = f1_0.pdf f1_100.pdf f1_2500.pdf f2_0.pdf f2_100.pdf f2_2500.pdf a1_0.pdf a1_100.pdf a1_2500.pdf a2_0.pdf a2_100.pdf a2_2500.pdf p1_0.pdf p1_100.pdf p1_2500.pdf p2_0.pdf p2_100.pdf p2_2500.pdf prom1.pdf prom2.pdf 

Resultados_hw4.pdf : Resultados_hw4.tex $(plots)
	pdflatex $<

$(plots) : Plots_Temperatura.py
	python $<

*.txt : a.out
	./$<

a.out : DifusionTemperatura.c
	cc $<
