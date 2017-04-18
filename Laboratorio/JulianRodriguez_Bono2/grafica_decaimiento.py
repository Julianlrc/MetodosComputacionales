import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("data_rand.txt")

tiempo = data[:,0]
decay = data[:,1]

plt.plot(tiempo, decay,)
plt.title(r"$Decaimiento$ $exponencial$")
plt.xlabel(r"$Tiempo$")
plt.ylabel(r"$N\'umero$ $de$ $part\'iculas$ $promedio$")
plt.savefig("decay.pdf")
plt.close()
