files = walk.txt walk1.txt
plotsCanal = canal.pdf canal1.pdf x_hist.pdf y_hist.pdf x1_hist.pdf y1_hist.pdf
plotsRC = carga.pdf r_verosimilitud.pdf c_verosimilitud.pdf r_hist.pdf c_hist.pdf

Resultado_hw5.pdf : Resultados_hw5.tex $(plotsCanal) $(plotsRC)
	pdflatex $<

$(plotsCanal) : plots_canal_ionico.py $(files)
	python $<

$(files) : a.out
	./$<

a.out : canal_ionico.c Canal_ionico.txt Canal_ionico1.txt
	gcc $< -lm

$(plotsRC) : circuitoRC.py CircuitoRC.txt
	python $<
