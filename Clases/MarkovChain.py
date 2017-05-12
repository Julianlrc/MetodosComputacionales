import numpy as np
import matplotlib.pyplot as plt

def nasty_function(x):
	x_0 = 3.
	a = 0.01
	return np.exp(-(x**2))/((x-x_0)**2+a**2)

x = np.linspace(-4.0, 4.0, 1000)
f = nasty_function(x)
#plt.plot(y,f)
#plt.show()

x_walk = np.empty((0))
x_0 = 8.0*((np.random.random())-0.5)
x_walk = np.append(x_walk, x_0)
#print x_walk

n_iterations = 200000

for i in range(n_iterations):
	x_prime = np.random.normal(x_walk[i], 0.1)

	alpha = nasty_function(x_prime)/nasty_function(x_walk[i])
	if(alpha >= 1.0):
		x_walk = np.append(x_walk, x_prime)
	else:
		beta = np.random.random()
		if(beta <= alpha):
			x_walk = np.append(x_walk, x_prime)
		else:
			x_walk = np.append(x_walk, x_walk[i])

print x_walk
norm = sum(f*(x[1]-x[0]))
plt.plot(x, f/norm, lw=1, c='r')
count, bins, ignored = plt.hist(x_walk, 1000, normed=True)
plt.show()



