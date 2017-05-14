import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

archivo = np.loadtxt("red3_filtrado.txt", delimiter=' ')

x = archivo[:,0]
y = archivo[:,1]

plt.plot(x,y)
plt.title("Longitud de onda vs Intensidad")
plt.xlabel("Longitud de onda", fontsize=16)
plt.ylabel("Intensidad", fontsize=16)
plt.savefig("red3.png")

maximo = max(y)
indice = np.where(y==maximo)

print "la longitud de onda de maxima amplitud es:", float(x[indice]), "nm"


def gaussiana(x, a, b, c):
	return a*(np.exp((-(-x-b)**2)/c))


popt, pcov = curve_fit(gaussiana, x, y, [1,650,1])

y_opt = gaussiana(x, popt[0], popt[1], popt[2])
print y_opt
plt.plot(x,y)
plt.scatter(x, y_opt, label='fit')
plt.legend(loc=0)
plt.savefig("red3_fit.png")

maximo_opt = max(y_opt)
indice_opt = np.where(y_opt==maximo_opt)

print "La longitud de onda maximo segun el ajuste es:", float(x[indice_opt]), "nm"
