import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("random_walks.txt")

plt.hist(data, bins=100)
plt.xlabel(r"$Valor$")
plt.ylabel(r"$Frecuencia$")
plt.title(r"$Caminatas$ $aleatorias$")
plt.savefig("rand.png")
plt.close()
