files = walk.txt walk1.txt

Resultado_hw5.pdf : *.png *.jpg Resultados_hw5.tex
	pdflatex Resultados_hw5.tex

*.jpg : $(files) plots_canal_ionico.py
	python plots_canal_ionico.py

*.png : circuitoRC.py
	python circuitoRC.py

$(files) : a.out
	./a.out

a.out : canal_ionico.c
	gcc canal_ionico.c -lm

clean:
	rm a.out
