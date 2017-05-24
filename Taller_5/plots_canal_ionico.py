import numpy as np
import matplotlib.pyplot as plt

canal = np.loadtxt("Canal_ionico.txt")
walk = np.loadtxt("walk1.txt")

rmax = np.amax(walk[:,2])
imax = np.argmax(walk[:,2])
theta = np.linspace(0, 2*np.pi, 1000)
circulo_x = rmax*np.cos(theta) + walk[imax,0]
circulo_y = rmax*np.sin(theta) + walk[imax,1]


fig = plt.figure(figsize=(6,6))
plt.scatter(canal[:,0], canal[:,1], s = 10, alpha = 0.5)
plt.scatter(walk[imax,0], walk[imax,1], c="r")
plt.plot(circulo_x, circulo_y, c="r")
plt.xlabel(r"$x(\AA)$")
plt.ylabel(r"$y(\AA)$")
plt.title(r"$x=%f\AA$, $y=%f\AA$, $r=%f\AA$" % (walk[imax,0], walk[imax,1], rmax)) 
plt.show()
#fig.savefig("canal_ionico_1.pdf")
#plt.close(fig)
