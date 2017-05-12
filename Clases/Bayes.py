import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("movimiento.dat")
x_obs = data[:,0]
y_obs = data[:,1]

#plt.scatter(x_obs, y_obs)
#plt.show()

def likelihood(y_obs, y_model):
	chi_cuadrado = 0.5*sum(((y_obs-y_model)/(100.0))**2)
	#print sum(y_obs-y_model)
	return np.exp(-chi_cuadrado)

def modelo(x_obs, a, b, c):
	return -(a*(x_obs**2)+b*x_obs+c)

a_walk = np.empty((0))
b_walk = np.empty((0))
c_walk = np.empty((0))
l_walk = np.empty((0))

a_walk = np.append(a_walk, 5.0)
b_walk = np.append(b_walk, -50.0)
c_walk = np.append(c_walk, -5.0)

y_init = modelo(x_obs, a_walk[0], b_walk[0], c_walk[0])
l_walk = np.append(l_walk, likelihood(y_obs, y_init))
print likelihood(y_obs, y_init)

n = 20000

for i in range(n):
	a_prime = np.random.normal(a_walk[i], 0.001)
	b_prime = np.random.normal(b_walk[i], 0.001)
	c_prime = np.random.normal(c_walk[i], 0.001)

	y_init = modelo(x_obs, a_walk[i], b_walk[i], c_walk[i])
	y_prime = modelo(x_obs, a_prime, b_prime, c_prime)

	l_prime = likelihood(y_obs, y_prime)
	l_init = likelihood(y_obs, y_init)

	alpha = l_prime/l_init
	if(alpha>=1.0):
		a_walk = np.append(a_walk, a_prime)
		b_walk = np.append(b_walk, b_prime)
		c_walk = np.append(c_walk, c_prime)
		l_walk = np.append(l_walk, l_prime)
	else:
		beta = np.random.random()
		if(beta<=alpha):
			a_walk = np.append(a_walk, a_prime)
			b_walk = np.append(b_walk, b_prime) 	
			c_walk = np.append(c_walk, c_prime)
                	l_walk = np.append(l_walk, l_prime)
		else:
			a_walk = np.append(a_walk, a_walk[i])
			b_walk = np.append(b_walk, b_walk[i])
			c_walk = np.append(c_walk, c_walk[i])
			l_walk = np.append(l_walk, l_init)

max_likelihood = np.argmax(l_walk)
best_a = a_walk[max_likelihood]
best_b = b_walk[max_likelihood]
best_c = c_walk[max_likelihood]

best_y = modelo(x_obs, best_a, best_b, best_c)
plt.scatter(x_obs, y_obs)
plt.plot(x_obs, best_y)
plt.show()
