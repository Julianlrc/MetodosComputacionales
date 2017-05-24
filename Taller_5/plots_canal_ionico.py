import numpy as np
import matplotlib.pyplot as plt

canal = np.loadtxt("Canal_ionico.txt")
walk = np.loadtxt("walk.txt")

rmax = np.amax(walk[:,2])
imax = np.argmax(walk[:,2])
theta = np.linspace(0, 2*np.pi, 1000)
circulo_x = rmax*np.cos(theta) + walk[imax,0]
circulo_y = rmax*np.sin(theta) + walk[imax,1]


fig = plt.figure(figsize=(4,5))
plt.scatter(canal[:,0], canal[:,1])
plt.scatter(walk[imax,0], walk[imax,1], c="r")
plt.plot(circulo_x, circulo_y, c="r")
plt.xlabel(r"$x(\AA)$")
plt.ylabel(r"$y(\AA)$")
plt.title(r"$x=%f\AA$, $y=%f\AA$, $r=%f\AA$" % (walk[imax,0], walk[imax,1], rmax)) 
fig.savefig("canal.jpg")
plt.close()


canal1 = np.loadtxt("Canal_ionico1.txt")
walk1 = np.loadtxt("walk1.txt")

rmax1 = np.amax(walk1[:,2])
imax1 = np.argmax(walk1[:,2])
theta1 = np.linspace(0, 2*np.pi, 1000)
circulo_x1 = rmax1*np.cos(theta1) + walk1[imax1,0]
circulo_y1 = rmax1*np.sin(theta1) + walk1[imax1,1]


fig = plt.figure(figsize=(4,5))
plt.scatter(canal1[:,0], canal1[:,1])
plt.scatter(walk1[imax1,0], walk1[imax1,1], c="r")
plt.plot(circulo_x1, circulo_y1, c="r")
plt.xlabel(r"$x(\AA)$")
plt.ylabel(r"$y(\AA)$")
plt.title(r"$x=%f\AA$, $y=%f\AA$, $r=%f\AA$" % (walk1[imax1,0], walk1[imax1,1], rmax1)) 
plt.savefig("canal1.jpg")
plt.close()
