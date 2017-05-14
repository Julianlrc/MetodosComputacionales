import numpy as np
import matplotlib.pyplot as plt


h=0.01
min_x =0.0
max_x=4.0
puntos = int((max_x-min_x)/h)
t = np.zeros(puntos)
y1 = np.zeros(puntos)
y2 = np.zeros(puntos)

def d1(t,y1, y2):
	return y2

def d2(t, y1, y2):
	if(d1(t, y1, y2)>0):
		return -k*y1/m -u*g
	else:
		return k*y1/m -u*g 

k=42
g=9.8
m=0.25
u = 0.15

y1[0] = 0.2*m
y2[0] = 0.0
t[0]= 0.0

for i in range(0, puntos):
	t[i] = t[i-1]+ h
	dd1 = d1(t[i-1], y1[i-1], y2[i-1])
	dd2 = d2(t[i-1], y1[i-1], y2[i-1])
	y1[i] = y1[i-1] + h*dd1
	y2[i] = y2[i-1] + h*dd2

plt.plot(t, y1)
plt.show()
