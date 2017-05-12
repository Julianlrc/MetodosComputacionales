import numpy as np


#PROMEDIOS
n = 2

matrix = np.zeros((n,n), dtype=float)
mean_filas = np.zeros(n)
mean_columnas = np.zeros(n)

matrix[0,0]=10
matrix[0,1]=30
matrix[1,0]=20
matrix[1,1]=60

for i in range(n):
	meanf = np.mean(matrix[:,i])
	mean_filas[i] = meanf

for j in range(n):
	meanc = np.mean(matrix[j,:])
	mean_columnas[j] = meanc

#print matrix, mean_filas, mean_columnas


#CREA ARRAY RANDOM CON 100 ELEMENTOS Y HALLA MEDIA, VARIANZA, DESVIACION.

array_random = np.zeros(1000)

for k in range(1000):
	array_random[k]= np.random.randn()

media = np.mean(array_random)
varianza = np.var(array_random)
desviacion = np.std(array_random)	

#print media, varianza, desviacion
