import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

#Se realiza la carga, manejo y asignacion de los datos
#Primero lo hacemos para el archivo de anomalias de temperatura
data_anomalias = np.loadtxt("Heat_content_index.txt")
an1 = data_anomalias[:,2]
an2 = data_anomalias[:,3]
an3 = data_anomalias[:,4]

#Ahora, se realiza la carga del archivo de SOI
data_soi = np.loadtxt("soi.txt")

#Organizamos los datos
indices = []
for i in range(0, len(data_soi[:,0])):
	for j in range(1, len(data_soi[0,:])):
		indices.append(float(data_soi[i,j]))
indices.append(1.3)

#Se genera un arreglo que contenga el numero de meses de los anios en cuestion
t = np.linspace(1, len(indices)+1, len(indices)+1)

#Generamos listas donde se guarden los anios (anios) y las posiciones (loc) de cada uno de ellos para realizar el xticks de la grafica posterior
anios = []
loc = []
it = 0
for i in range(0, len(indices),12):
		loc.append(i)
		anios.append(str(1876+it))
		it+=1

#Se generan las graficas de las anomalias y el SOI en funcion del tiempo. Se realizaron en la isma figura pero con dos ejes verticales distintos, para visualizar mejor las posibles correlaciones.

#plt.figure(figsize=(80,100))
plt.title(r"$Anomal\'ias$ $de$ $temperatura$ $y$ $SOI$ $en$ $funci\'on$ $del$ $tiempo$")
plt.plot(t[1236:-1], indices[1236:], label=r"$SOI$", color='orange')
plt.ylabel(r"$SOI$", fontsize=16)
plt.xlabel(r"$Tiempo$ $(meses$ $por$ $a\~no)$")
plt.xticks(loc, anios, size='small', rotation=90)
plt.legend(loc=0)
plt.twinx()
plt.plot(t[1236:],an1, label=r"$130E$-$80W$", color='r')
plt.plot(t[1236:],an2, label=r"$160E$-$80W$", c='g')
plt.plot(t[1236:],an3, label=r"$180W$-$100W$", color='b')
plt.minorticks_on()
plt.ylabel(r"$Temperatura$ $(^{\circ}C)$")
plt.legend(loc=0)
plt.savefig("Anomalies_SOI_Plot.pdf")
plt.close()

#plt.plot(t[1236:-1], indices[1236:], label=r"$SOI$", color='orange')
#plt.ylabel(r"$SOI$", fontsize=16)
#plt.xlabel(r"$Tiempo$ $(meses$ $por$ $a\~no)$")
#plt.plot(t[1236:],an1, label=r"$130E$-$80W$", color='r')
#plt.plot(t[1236:],an2, label=r"$160E$-$80W$", c='g')
#plt.plot(t[1236:],an3, label=r"$180W$-$100W$", color='b')
#plt.legend(loc=0)
#plt.savefig("xx.pdf")
#plt.close()



#Se guardan las variables relevantes (el SOI y las tres anomalias de temperatura). No se tiene en cuenta el dato para el segundo mes del anio 2017 y solo se toman los datos para los anios de 1979 en adelante.
datos = np.zeros((457,4), dtype=float)
datos[:,0] = indices[1236:]
datos[:,1] = an1[:-1]
datos[:,2] = an2[:-1]
datos[:,3] = an3[:-1]

#Se le resta la media para que queden centrados en cero
datos[:,0] = datos[:,0]-np.mean(datos[:,0])
datos[:,1] = datos[:,1]-np.mean(datos[:,1])
datos[:,2] = datos[:,2]-np.mean(datos[:,2])
datos[:,3] = datos[:,3]-np.mean(datos[:,3])

#print datos

#Se calcula la matriz de covarianza
cov_matrix = np.cov(datos.T)
print "COV", cov_matrix
#Se hallan los valores y los vectores propios a partir de la matriz de covarianza
valores, vectores = np.linalg.eig(cov_matrix)
print valores, vectores
#Tras la visualizacion de los valores y vectores propios se observa que estan en orden, por lo cual no es necesario organizarlos. Esto se podria comprobar con el siguiente comando comentado.
#pos = valores.argsort()
#print pos

#Se imprimen las dos componentes principales (la primera se relaciona con el SOI y la segunda, con la correlacion de las tres anomalias de temperatura)
print "Las dos componentes principales son los vectores propios:", vectores[:,0], vectores[:,1], ",con valores propios", valores[0], "y", valores[1],",respectivamente."

#Se generan los datos en el sistema de referencia de las dos componentes principales halladas (se rotan).
datos_pca = np.dot(vectores.T, datos.T)
print datos_pca
#print datos_pca[0,:]
#print datos_pca[1,:]

#Se genera la grafica de los datos en el sistema de referencia de las dos componentes principales.
plt.figure(figsize=(10,5))
plt.title(r"$Componentes$ $principales$", fontsize=18)
plt.scatter(datos_pca[0,:], datos_pca[1,:]) 
plt.xlabel(r"$Componente$ $principal$ $1$", fontsize=16)
plt.ylabel(r"$Componente$ $principal$ $2$", fontsize=16)
plt.savefig("PCA_Anomalies_SOI_Plot.pdf")
plt.close()
