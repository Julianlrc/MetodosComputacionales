import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(10000)*2-1
y = np.random.rand(10000)*2-1

plt.figure(figsize=(6,6))
plt.scatter(x, y)
index = np. where(x**2+y**2 < 1)
xc = x[index]
yc = y[index]
plt.scatter(xc, yc, c='r')
plt.show()
pi = 4*float(len(xc))/float(len(x))
print pi, np.pi
print "error=", np.pi- pi
