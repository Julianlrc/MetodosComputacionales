import numpy as np
import matplotlib.pyplot as plt

#Numero de variables
n=9

#Empezamos con unos valores iniciales para las variables (guess)
#El orden de las variables en el arreglo es: [sin1, sin2, sin3, cos1, cos2, cos3, T1, T2, T3]
guess = np.array([0.5,0.3,0.7,0.8,0.9,0.6,13.,8.,18.])

#Criterio para aceptar una solucion
umbral = 0.001

#Definimos los valores conocidos
L1=3.0
L2=4.0
L3=4.0
L=8.0
W1=10.0
W2=20.0

#Definimos una funcion que nos plantee el sistema de ecuaciones
def F(vo):
	f = np.zeros((n,), dtype=float)
	f[0]=vo[6]*vo[0]-vo[7]*vo[1]-W1
	f[1]=vo[6]*vo[3]-vo[7]*vo[4]
	f[2]=vo[7]*vo[1]+vo[8]*vo[2]-W2
	f[3]=vo[7]*vo[4]-vo[8]*vo[5]
	f[4]=L1*vo[3]+L2*vo[4]+L3*vo[5]-L
	f[5]=L1*vo[0]+L2*vo[1]-L3*vo[2]
	f[6]=(vo[0])**2 + (vo[3])**2 -1
	f[7]=(vo[1])**2 + (vo[4])**2 -1
	f[8]=(vo[2])**2 + (vo[5])**2 -1
	return f

#Definamos las derivadas de la ecuacion_i respecto a la variable x_j
#Y agreguemoslas a la matriz declarada inicialmente
def Jacobiano(x,n):
	df = np.zeros((n,n), dtype=float)
	h=0.5
	for i in range(0, n):
		for j in range(0, n):
			cx = x.copy()
			cx[j]+=h
			fh=F(cx)
			fx=F(x)
			df[i,j] = (fh[i]-fx[i])/h
	return df

#Definamos los arrays donde iremos guardando los valores de los angulos y las tensiones que se van calculando en el Newton-Raphson
thetas = np.arcsin(guess[0:3])
tensiones = guess[6:]

#Realicemos la busqueda a traves de Newton-Raphson multidimensional para hallar los angulos y las tensiones en el estado de equilibrio
iteraciones=0
f=F(guess)
for i in range(0,n):
	while(np.linalg.norm(f[i])>umbral):
		Jb = Jacobiano(guess, n)
		d = np.linalg.solve(Jb, -f)
		guess =guess+d
		f = F(guess)
		thetas = np.concatenate((thetas, np.arcsin(guess[0:3])))
		tensiones = np.concatenate((tensiones, guess[6:]))
		iteraciones+=1

print "Los angulos 1,2 y 3 son respectivamente:", np.arcsin(guess[0:3]), "y las tensiones 1, 2 y 3 son respectivamente:", guess[6:]
print guess
#Generamos un arreglo con el numero de iteraciones
it = np.arange(iteraciones+1)

#Graficamos los valores intermedios de los angulos y las tensiones hasta llegar a la solucion del sistema.
c=['b','r','g']
plt.figure()
for i in range(0,3):
	plt.scatter(it, thetas[i::3], c=c[i], label=r'$\theta_{%d}$' %(i+1))
	plt.plot(it, thetas[i::3], c=c[i], linestyle='--')
plt.title(r"$\'Angulos$ $hallados$ $en$ $la$ $b\'usqueda$")
plt.xlabel(r"$Iteraciones$")
plt.ylabel(r"$\theta$ $(rad)$")
plt.legend(loc=0)
plt.savefig("AnglesPLOT.pdf")
plt.close()

plt.figure()
for i in range(0,3):
	plt.scatter(it, tensiones[i::3], c=c[i], label=r'$T_{%d}$' %(i+1))
	plt.plot(it, tensiones[i::3], c=c[i], linestyle='--')
plt.title(r"$Tensiones$ $halladas$ $en$ $la$ $b\'usqueda$")
plt.xlabel(r"$Iteraciones$")
plt.ylabel(r"$Tensi\'on$ $(N)$")
plt.legend(loc=0)
plt.savefig("TensionsPLOT.pdf")
plt.close()
