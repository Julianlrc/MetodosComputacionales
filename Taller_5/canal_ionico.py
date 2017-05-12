import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("Canal_ionico.txt")
x = data[:,0]
y = data[:,1]

plt.scatter(x,y)
plt.show()
