import numpy as np
import matplotlib.pyplot as plt


obs_data = np.loadtxt("obs_data.dat")
x_obs = obs_data[:,0]
y_obs = obs_data[:,1]

def likelihood(y_obs, y_model):
    chi_squared = (1.0/2.0)*sum((y_obs-y_model)**2)
    return np.exp(-chi_squared)

def my_model(x_obs, m, b):
    return x_obs*m + b

m_walk = np.empty((0)) #this is an empty list to keep all the steps
b_walk = np.empty((0))
l_walk = np.empty((0))

m_walk = np.append(m_walk, np.random.random())
b_walk = np.append(b_walk, np.random.random())

y_init = my_model(x_obs, m_walk[0], b_walk[0])
l_walk = np.append(l_walk, likelihood(y_obs, y_init))

n_iterations = 20000 #this is the number of iterations I want to make
for i in range(n_iterations):
    m_prime = np.random.normal(m_walk[i], 0.1) 
    b_prime = np.random.normal(b_walk[i], 0.1)

    y_init = my_model(x_obs, m_walk[i], b_walk[i])
    y_prime = my_model(x_obs, m_prime, b_prime)
    
    l_prime = likelihood(y_obs, y_prime)
    l_init = likelihood(y_obs, y_init)
    
    alpha = l_prime/l_init
    if(alpha>=1.0):
        m_walk  = np.append(m_walk,m_prime)
        b_walk  = np.append(b_walk,b_prime)
        l_walk = np.append(l_walk, l_prime)
    else:
        beta = np.random.random()
        if(beta<=alpha):
            m_walk = np.append(m_walk,m_prime)
            b_walk = np.append(b_walk,b_prime)
            l_walk = np.append(l_walk, l_prime)
        else:
            m_walk = np.append(m_walk,m_walk[i])
            b_walk = np.append(b_walk,b_walk[i])
            l_walk = np.append(l_walk, l_init)

max_likelihood_id = np.argmax(l_walk)
best_m = m_walk[max_likelihood_id]
best_b = b_walk[max_likelihood_id]

best_y = my_model(x_obs, best_m, best_b)
plt.scatter(x_obs,y_obs)
plt.plot(x_obs, best_y)
plt.show()
