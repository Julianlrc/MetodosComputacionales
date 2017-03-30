import numpy as np
import matplotlib.pyplot as plt

#Carga y asignacion de datos
datos = np.loadtxt("RotationCurve_F571-8.txt")
v_observada = datos[:,5]
radio = datos[:,1]
suma_vel_esperadas = datos[:,2]+datos[:,3]+datos[:,4]

#Graficas de las velocidades en funcion al radio
plt.scatter(radio, v_observada, c='black', label="$V_{observada}$")
plt.scatter(radio, suma_vel_esperadas, c='g', label="$\sum{V_{esperadas}}$")
plt.title(r"$Velocidad$ $en$ $funci\'on$ $del$ $radio$")
plt.xlabel("$Radio$ $(kpc)$", fontsize=18)
plt.ylabel("$Velocidades$ $(km/s)$", fontsize=18)
plt.legend(loc=0)
plt.savefig('RotationCurvePlot.pdf')
plt.close()
