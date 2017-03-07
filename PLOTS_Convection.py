import numpy as np	
import matplotlib.pyplot as plt
from scipy import interpolate

#Descarga y asignacion de datos
datos = np.loadtxt("TempHeight.txt")
altura = datos[:,0]
temperatura = datos[:,1]

#Conversion de la altura de metros a kilometros
altura_k = altura/1000

#Grafica de temperatura respecto a la altura
plt.title(r'$Temperatura$ $en$ $funci\'on$ $de$ $la$ $altura$')
plt.scatter(altura_k, temperatura, c='r', label="$Temperatura$")
plt.xlabel("$Altura$ $(km)$", fontsize=18)
plt.ylabel("$Temperatura$ $(^{\circ}C)$", fontsize=18)
plt.legend(loc=0)
plt.savefig("TemperaturePlot.pdf")
plt.close()

#Interpolacion
tck = interpolate.splrep(altura, temperatura, k=5)
altura_regular = np.linspace(2500, 25000, 150)
temperatura_i = interpolate.splev(altura_regular, tck)

#Conversion de la altura regular de metros a kilometros
altura_km = altura_regular/1000

#Derivada de T respecto a la altura (Gradiente vertical de temperatura)
grad_vert = (temperatura_i[2:-1] - temperatura_i[0:-3])/((altura_km[2:-1]-altura_km[0:-3]))

#Se guardan los datos del gradiente vertical que en valor absoluto son mayores al gradiente adiabatico
grad_temp = []
altura_conv = []
for i in range(len(grad_vert)):
	if abs(grad_vert[i])>(9.8):
		grad_temp.append(grad_vert[i])
		altura_conv.append(altura_km[i])

#Grafica de puntos de conveccion
plt.title(r'$Puntos$ $que$ $cumplen$ $con$ $criterio$ $de$ $convecci\'on$')
plt.scatter(altura_conv, grad_temp, label=r'$Convecci\'on$', c='lime')
plt.xlabel('$Altura$ $(km)$', fontsize=18)
plt.ylabel(r'$\nabla{T_{vertical}}$ $\left(\frac{^\circ C}{km}\right)$', fontsize=18)
plt.legend(loc=0)
plt.savefig('ConvectionPLOT.pdf')
plt.close()

#Se genera el gradiente adiabatico
grad_adiabatico = []
for i in range(len(altura_regular)):
	grad_adiabatico.append(-9.8)

#Grafica de los gradientes
plt.title('$Gradientes$')
plt.plot(altura_km, grad_adiabatico, label=r'$Gradiente$ $adiab\'atico$', c='orange', ls='--')
plt.scatter(altura_km[1:-2], grad_vert, label='$Gradiente$ $vertical$ $de$ $temperatura$')
plt.ylabel(r'$\nabla{T}$ $\left(\frac{^\circ C}{km}\right)$', fontsize=18)
plt.xlabel('$Altura$ $(km)$', fontsize=18)
plt.legend(loc=0)
plt.savefig('GradientsPlot.pdf')
plt.close()
