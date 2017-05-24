import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("CircuitoRC.txt")
t = data[:,0]
q = data[:,1]

V0=10

def likelihood(q_obs, q_model):
	chi_cuadrado = 0.5*sum(((q_obs-q_model)/100)**2)
	return np.exp(-chi_cuadrado)

def modelo(time, R, C):
	return V0*C*(1-np.exp(-time/(R*C)))

R_walk = np.empty((0))
C_walk = np.empty((0))
l_walk = np.empty((0))

R_walk = np.append(R_walk, 5.0)
C_walk = np.append(C_walk, 5.0)

q_init = modelo(t, R_walk[0], C_walk[0])
l_walk = np.append(l_walk, likelihood(q, q_init))

n = 20000

for i in range(n):
	R_prime = np.random.normal(R_walk[i], 0.1)
	C_prime = np.random.normal(C_walk[i], 0.1)

	q_init = modelo(t, R_walk[i], C_walk[i])
	q_prime = modelo(t, R_prime, C_prime)

	l_prime = likelihood(q, q_prime)
	l_init = likelihood(q, q_init)

	alpha = l_prime/l_init
	if(alpha>=1.0):
		R_walk = np.append(R_walk, R_prime)
		C_walk = np.append(C_walk, C_prime)
		l_walk = np.append(l_walk, l_prime)
	else:
		beta = np.random.random()
		if(beta<=alpha):
			R_walk = np.append(R_walk, R_prime) 	
                	C_walk = np.append(C_walk, C_prime)
                	l_walk = np.append(l_walk, l_prime)

		else:
			R_walk = np.append(R_walk, R_walk[i])
	        	C_walk = np.append(C_walk, C_walk[i])
                	l_walk = np.append(l_walk, l_init)

max_likelihood = np.argmax(l_walk)
best_R = R_walk[max_likelihood]
best_C = C_walk[max_likelihood]
best_q = modelo(t, best_R, best_C)

plt.figure()
plt.plot(t, q, label=r"Datos observados")
plt.plot(t, best_q, c="r", label=r"Modelo con $R=%f$ y $C=%F$" % (best_R, best_C))
plt.xlabel(r"tiempo(s)")
plt.ylabel(r"carga(c)")
plt.title(r"$Carga$ $en$ $funci\'on$ $del$ $tiempo$")
plt.legend()
plt.savefig("carga.pdf")
plt.close()

plt.figure()
plt.scatter(R_walk, -np.log(l_walk))
plt.xlabel(r"Resistencia (Ohm)")
plt.ylabel(r"Verosimilitud")
plt.title(r"$Resistencia$ $en$ $funci\'on$ $de$ $la$ $funci\'on$ $de$ $verosimilitud$")
plt.savefig("r_verosimilitud.pdf")
plt.close()

plt.figure()
plt.scatter(C_walk, -np.log(l_walk))
plt.xlabel(r"Capacitancia (F)")
plt.ylabel(r"Verosimilitud")
plt.title(r"$Capacitancia$ $en$ $funci\'on$ $de$ $la$ $funci\'on$ $de$ $verosimilitud$")
plt.savefig("c_verosimilitud.pdf")
plt.close()

plt.figure()
plt.hist(R_walk, 30, normed=True)
plt.xlabel(r"Resistencia (Ohm)")
plt.ylabel(r"Frecuencia (normalizada)")
plt.savefig("r_hist.pdf")
plt.close()

plt.figure()
plt.hist(C_walk, 30, normed=True)
plt.xlabel(r"Capacitancia (F)")
plt.ylabel(r"Frecuencia (normalizada)")
plt.savefig("c_hist.pdf")
plt.close()
