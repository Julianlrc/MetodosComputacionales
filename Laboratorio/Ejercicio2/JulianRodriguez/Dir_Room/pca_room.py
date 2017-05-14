import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('room-temperature.csv', delimiter=",", skiprows=1, usecols=(1,2,3,4))
frontleft = data[:,0]
frontright = data[:,1]
backleft = data[:,2]
backright = data[:,3]

x = np.linspace(1, len(data[:,0]), len(data[:,0]))

f, (ax1, ax2, ax3, ax4) = plt.subplots(4, sharex=True, sharey=True)
ax1.plot(x, frontleft, label='Fron left')
ax1.set_title('Temperatura de las cuatro esquinas de la habitacion')
ax1.legend()
ax2.plot(x, frontright, label='Front right')
ax2.legend()
ax3.plot(x, backleft, label='Back left')
ax3.set_ylabel('Temperatura')
ax3.legend()
ax4.plot(x, backright, label='Back right')
f.subplots_adjust(hspace=0)
ax4.legend()
plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)
plt.savefig('room.pdf')
#plt.show()

frontleft = (data[:,0]- np.mean(data[:,0]))/np.std(data[:,0])
frontright = (data[:,1]- np.mean(data[:,1]))/np.std(data[:,1])
backleft = (data[:,2]- np.mean(data[:,2]))/np.std(data[:,2])
backright = (data[:,3]- np.mean(data[:,3]))/np.std(data[:,3])

cov_matrix = np.cov(data.T)
print "La matriz de covarianza es:" , cov_matrix

values, vectors = np.linalg.eig(cov_matrix)
print values, vectors
