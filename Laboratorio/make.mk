a.out: caminata.c
	cc caminata.c
rand_walks.txt: a.out
	./a.out
graficas.py: rand_walks.txt
	python graficas.py
