import numpy as np
import matplotlib.pyplot as plt

canal = np.loadtxt("Canal_ionico.txt")
walk = np.loadtxt("walk.txt")
rmax = np.amax(walk[:,2])
imax = np.argmax(walk[:,2])
xmax = walk[imax, 0]
ymax = walk[imax, 1]
theta = np.linspace(0, 2*np.pi, 1500)
x = rmax*np.cos(theta) + xmax
y = rmax*np.sin(theta) + ymax

plt.figure(figsize=(5.5,6))
plt.scatter(canal[:,0], canal[:,1])
plt.scatter(xmax, ymax, c="r")
plt.plot(x, y, c="r", lw=1.0)
plt.xlabel(r"$X (\AA)$")
plt.ylabel(r"$Y (\AA)$")
plt.title(r"$Par\'ametros:$ $X=%f\AA$, $Y=%f\AA$, $R=%f\AA$" % (xmax, ymax, rmax)) 
plt.savefig("canal.pdf")
plt.close()

canal1 = np.loadtxt("Canal_ionico1.txt")
walk1 = np.loadtxt("walk1.txt")
rmax1 = np.amax(walk1[:,2])
imax1 = np.argmax(walk1[:,2])
xmax1 = walk1[imax1, 0]
ymax1 = walk1[imax1, 1]
theta1 = np.linspace(0, 2*np.pi, 1500)
x1 = rmax1*np.cos(theta1) + xmax1
y1 = rmax1*np.sin(theta1) + ymax1

plt.figure(figsize=(5.5,6))
plt.scatter(canal1[:,0], canal1[:,1])
plt.scatter(xmax1, ymax1, c="r")
plt.plot(x1, y1, c="r", lw=1.0)
plt.xlabel(r"$X (\AA)$")
plt.ylabel(r"$Y (\AA)$")
plt.title(r"$Par\'ametros:$ $X=%f\AA$, $Y=%f\AA$, $R=%f\AA$" % (xmax1, ymax1, rmax1)) 
plt.savefig("canal1.pdf")
plt.close()

plt.figure()
plt.hist(walk[:,0], 30)
plt.xlabel(r"X $(\AA)$")
plt.ylabel(r"Frecuencia")
plt.title(r"Sampleo de la coordenada X")
plt.savefig("x_hist.pdf")
plt.close()

plt.figure()
plt.hist(walk[:,1], 30)
plt.xlabel(r"Y $(\AA)$")
plt.ylabel(r"Frecuencia")
plt.title(r"Sampleo de la coordenada Y")
plt.savefig("y_hist.pdf")
plt.close()

plt.figure()
plt.hist(walk1[:,0], 30)
plt.xlabel(r"X $(\AA)$")
plt.ylabel(r"Frecuencia")
plt.title(r"Sampleo de la coordenada X")
plt.savefig("x1_hist.pdf")
plt.close()

plt.figure()
plt.hist(walk1[:,1], 30)
plt.xlabel(r"Y $(\AA)$")
plt.ylabel(r"Frecuencia")
plt.title(r"Sampleo de coordenada Y")
plt.savefig("y1_hist.pdf")
plt.close()
