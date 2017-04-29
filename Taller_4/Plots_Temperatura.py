import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fijas1_2500 = np.loadtxt("fijas_caso1_2500.txt")
fijas1_0 = np.loadtxt("fijas_caso1_0.txt")
fijas1_100 = np.loadtxt("fijas_caso1_100.txt")
fijas2_2500 = np.loadtxt("fijas_caso2_2500.txt")
fijas2_0 = np.loadtxt("fijas_caso2_0.txt")
fijas2_100 = np.loadtxt("fijas_caso2_100.txt")
abiertas1_2500 = np.loadtxt("abiertas_caso1_2500.txt")
abiertas1_0 = np.loadtxt("abiertas_caso1_0.txt")
abiertas1_100 = np.loadtxt("abiertas_caso1_100.txt")

t_fijas1_0 = np.zeros((100,100), dtype=float)
t_fijas1_100 = np.zeros((100,100), dtype=float)
t_fijas1_2500 = np.zeros((100,100), dtype=float)
t_fijas2_0 = np.zeros((100,100), dtype=float)
t_fijas2_100 = np.zeros((100,100), dtype=float)
t_fijas2_2500 = np.zeros((100,100), dtype=float)
t_abiertas1_0 = np.zeros((100,100), dtype=float)
t_abiertas1_100 = np.zeros((100,100), dtype=float)
t_abiertas1_2500 = np.zeros((100,100), dtype=float)

def linealizar(matriz, data):
	k=0
	for i in range(100):
		for j in range(100):
			matriz[j][i]= data[k]
			k+=1

linealizar(t_fijas1_0, fijas1_0)
linealizar(t_fijas1_2500, fijas1_2500)
linealizar(t_fijas1_100, fijas1_100)
linealizar(t_fijas2_0, fijas2_0)
linealizar(t_fijas2_2500, fijas2_2500)
linealizar(t_fijas2_100, fijas2_100)
linealizar(t_abiertas1_0, abiertas1_0)
linealizar(t_abiertas1_2500, abiertas1_2500)
linealizar(t_abiertas1_100, abiertas1_100)

plt.imshow(t_fijas1_0)
plt.colorbar()
plt.show()
plt.imshow(t_fijas1_100)
plt.colorbar()
plt.show()
plt.imshow(t_fijas1_2500)
plt.colorbar()
plt.show()
plt.imshow(t_fijas2_0)
plt.colorbar()
plt.show()
plt.imshow(t_fijas2_100)
plt.colorbar()
plt.show()
plt.imshow(t_fijas2_2500)
plt.colorbar()
plt.show()
plt.imshow(t_abiertas1_0)
plt.colorbar()
plt.show()
plt.imshow(t_abiertas1_100)
plt.colorbar()
plt.show()
plt.imshow(t_abiertas1_2500)
plt.colorbar()
plt.show()
