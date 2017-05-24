files = walk.txt walk1.txt

Resultado_hw5.pdf : Resultados_hw5.tex *.jpg *.png
	pdflatex $<

*.jpg : plots_canal_ionico.py $(files)
	python $<

$(files) : a.out
	./$<

a.out : canal_ionico.c Canal_ionico.txt Canal_ionico1.txt
	gcc $< -lm

*.png : circuitoRC.py CircuitoRC.txt
	python $<

clean :
	rm a.out *.png *.jpg *.log *.aux
