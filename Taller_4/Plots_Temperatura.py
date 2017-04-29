import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fijas_1_2500 = np.loadtxt("fijas_caso1_2500.txt")
fijas_1_0 = np.loadtxt("fijas_caso1_0.txt")
fijas_1_100 = np.loadtxt("fijas_caso1_100.txt")


t_inicial = np.zeros((100,100), dtype=float)
t_post2500 = np.zeros((100,100), dtype=float)
t_post100 = np.zeros((100,100), dtype=float)

def linealizar(matriz, data):
	k=0
	for i in range(100):
		for j in range(100):
			matriz[j][i]= data[k]
			k+=1

linealizar(t_inicial, fijas_1_0)
linealizar(t_post2500, fijas_1_2500)
linealizar(t_post100, fijas_1_100)
	
#f, (ax1, ax2) = plt.subplots(2)
#plt.figure()
plt.imshow(t_inicial)
plt.colorbar()
plt.show()
plt.imshow(t_post100)
plt.colorbar()
plt.show()
plt.imshow(t_post2500)
plt.colorbar()
plt.show()
