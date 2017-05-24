import numpy as np
import matplotlib.pyplot as plt

canal = np.loadtxt("Canal_ionico.txt")
walk = np.loadtxt("walk.txt")

rmax = np.amax(walk[:,2])
imax = np.argmax(walk[:,2])
theta = np.linspace(0, 2*np.pi, 1000)
x = rmax*np.cos(theta) + walk[imax,0]
y = rmax*np.sin(theta) + walk[imax,1]


plt.figure(figsize=(5,6))
plt.scatter(canal[:,0], canal[:,1])
plt.scatter(walk[imax,0], walk[imax,1], c="r")
plt.plot(x, y, c="r")
plt.xlabel(r"$x(\AA)$")
plt.ylabel(r"$y(\AA)$")
plt.title(r"$x=%f\AA$, $y=%f\AA$, $r=%f\AA$" % (walk[imax,0], walk[imax,1], rmax)) 
plt.savefig("canal.pdf")
plt.close()


canal1 = np.loadtxt("Canal_ionico1.txt")
walk1 = np.loadtxt("walk1.txt")

rmax1 = np.amax(walk1[:,2])
imax1 = np.argmax(walk1[:,2])
theta1 = np.linspace(0, 2*np.pi, 1000)
x1 = rmax1*np.cos(theta1) + walk1[imax1,0]
y1 = rmax1*np.sin(theta1) + walk1[imax1,1]


plt.figure(figsize=(5,6))
plt.scatter(canal1[:,0], canal1[:,1])
plt.scatter(walk1[imax1,0], walk1[imax1,1], c="r")
plt.plot(x1, y1, c="r")
plt.xlabel(r"$x(\AA)$")
plt.ylabel(r"$y(\AA)$")
plt.title(r"$x=%f\AA$, $y=%f\AA$, $r=%f\AA$" % (walk1[imax1,0], walk1[imax1,1], rmax1)) 
plt.savefig("canal1.pdf")
plt.close()

plt.figure()
plt.hist(walk[:,0])
plt.xlabel(r"x $(\AA)$")
plt.ylabel(r"Frecuencia")
plt.savefig("x_hist.pdf")
plt.close()

plt.figure()
plt.hist(walk[:,1])
plt.xlabel(r"y $(\AA)$")
plt.ylabel(r"Frecuencia")
plt.savefig("y_hist.pdf")
plt.close()


plt.figure()
plt.hist(walk1[:,0])
plt.xlabel(r"x $(\AA)$")
plt.ylabel(r"Frecuencia")
plt.savefig("x1_hist.pdf")
plt.close()

plt.figure()
plt.hist(walk1[:,1])
plt.xlabel(r"y $(\AA)$")
plt.ylabel(r"Frecuencia")
plt.savefig("y1_hist.pdf")
plt.close()
