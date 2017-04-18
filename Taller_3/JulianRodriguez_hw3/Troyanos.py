#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np

#PROBLEMA DE TRES CUERPOS

#Creamos la clase Planetas, que define las propiedades de un cuerpo celeste.
class Planetas: 
    #Constante gravitacional
    G = 1.0
    def __init__(self, m, x, y, vx, vy):
        self.m = m
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.ax=0
        self.ay=0
        
    #Calcula la aceleracion a causa de las fuerzas de los demas planetas con los que interactua en un punto determinado    
    def aceleracion(self, planetas):
        self.ax=0
        self.ay=0
        for i in range(0,len(planetas)):
            if(planetas[i]!=self):
                xp = planetas[i].x-self.x
                yp = planetas[i].y-self.y
                rx = xp/np.sqrt(xp**2.0+yp**2.0)
                ry = yp/np.sqrt(xp**2.0+yp**2.0)
                rr = (xp**2.0+yp**2.0)
                self.ax += self.G*planetas[i].m*rx/rr
                self.ay += self.G*planetas[i].m*ry/rr
    
    #Se resuelven las ecuaciones diferenciales mediante el metodo Leap-Frog (Simplectico)
    def leapFrog(self, h, planetas):
        self.aceleracion(planetas)
        vx_mitad = self.vx + 0.5*h*self.ax
        vy_mitad = self.vy + 0.5*h*self.ay
        
        self.x = self.x + h*vx_mitad
        self.y = self.y + h*vy_mitad
        
        self.aceleracion(planetas)
        self.vx = vx_mitad + 0.5*h*self.ax
        self.vy = vy_mitad + 0.5*h*self.ay    

#Se define una funcion que itera sobre los tres cuerpos, hallando las velocidades y las posiciones.
def iteradorTresCuerpos(h, planetas, it):
    x_troyano = np.zeros(it+1)
    x_troyano[0] = planetas[0].x
    y_troyano = np.zeros(it+1)
    y_troyano[0] = planetas[0].y
    x_planeta = np.zeros(it+1)
    x_planeta[0] = planetas[1].x
    y_planeta = np.zeros(it+1)
    y_planeta[0] = planetas[1].y
    x_estrella = np.zeros(it+1)
    x_estrella[0] = planetas[2].x
    y_estrella = np.zeros(it+1)
    y_estrella[0] = planetas[2].y

    for i in range(1, it+1):
        planetas[0].leapFrog(h, planetas)
        planetas[1].leapFrog(h, planetas)
        planetas[2].leapFrog(h, planetas)
    
        x_troyano[i] = planetas[0].x
        y_troyano[i] = planetas[0].y
        x_planeta[i] = planetas[1].x
        y_planeta[i] = planetas[1].y
        x_estrella[i] = planetas[2].x
        y_estrella[i] = planetas[2].y
    
    return x_troyano, y_troyano, x_planeta, y_planeta, x_estrella, y_estrella

#Se define una funcion que actualiza las condiciones iniciales cada vez que se requiera.
def actualizarCondicionesIniciales(m):
    x_planet = 100.0-100.0/1048
    x_star = -100.0/1048
    x_trojan = np.cos(60*np.pi/180)*x_planet
    y_trojan = np.sin(60*np.pi/180)*x_planet
    m_star = 1047.0
    m_trojan = 0.005
    m_planet = m
    m_red = np.sqrt(abs((m_planet+m_star)/(x_planet+x_star)**3.0))
    vy_planet = m_red*abs(x_planet)
    vy_star = -m_red*abs(x_star)
    vx_trojan = -vy_planet*np.sin(60*np.pi/180)
    vy_trojan = vy_planet*np.cos(60*np.pi/180)
    
    return m_trojan, x_trojan, y_trojan, vx_trojan, vy_trojan, m_planet,x_planet,vy_planet, m_star,x_star,vy_star

#Se crean los cuerpos celestes con las condiciones iniciales apropiadas
m_trojan, x_trojan, y_trojan, vx_trojan, vy_trojan, m_planet,x_planet,vy_planet, m_star,x_star,vy_star = actualizarCondicionesIniciales(1.0)
troyano = Planetas(m_trojan, x_trojan, y_trojan, vx_trojan, vy_trojan)
planeta = Planetas(m_planet,x_planet,0,0,vy_planet)
estrella = Planetas(m_star,x_star,0,0,vy_star)
planets = [troyano, planeta, estrella]

#Se itera sobre los cuerpos celestes creados previamente para obtener sus posiciones.
h=0.01
it=23000
x_troyano, y_troyano, x_planeta, y_planeta, x_estrella, y_estrella = iteradorTresCuerpos(h, planets, it)

#Se grafican las orbitas de los tres cuerpos
fig, (ax1, ax2, ax3) = plt.subplots(3, figsize=(6,8))
ax1.plot(x_troyano, y_troyano, label=r"$Troyano$", c="g")
ax1.set_title(r"$\'Orbitas$ $de$ $los$ $tres$ $cuerpos$", fontsize=20)
ax1.set_xlabel(r"$x$")
ax1.set_ylabel(r"$y$")
ax1.legend()
ax1.set_xlim([-150, 150])
ax1.set_ylim([-150, 150])
ax2.plot(x_planeta, y_planeta, label=r"$Planeta$", c="b")
ax2.set_xlabel(r"$x$")
ax2.set_ylabel(r"$y$")
ax2.legend()
ax2.set_xlim([-150, 150])
ax3.plot(x_estrella, y_estrella, label=r"$Estrella$", c="r")
ax3.set_xlabel(r"$x$")
ax3.set_ylabel(r"$y$")
ax3.set_xlim([-0.15, 0.15])
ax3.set_ylim([-0.15, 0.15])
ax3.legend()
fig.subplots_adjust(hspace=0.4)
plt.savefig("OrbitsPLOT.pdf")
plt.close()

#Se crea una nueva lista de planetas con las condiciones iniciales perturbadas
m_trojan, x_trojan, y_trojan, vx_trojan, vy_trojan, m_planet,x_planet,vy_planet, m_star,x_star,vy_star = actualizarCondicionesIniciales(1.0)
troyanop = Planetas(m_trojan, x_trojan+50, y_trojan+50, vx_trojan+50, vy_trojan+50)
planetap = Planetas(m_planet,x_planet+50,50,50,vy_planet+50)
estrellap = Planetas(m_star,x_star+50,50,50,vy_star+50) 
pp = [troyanop, planetap, estrellap]
x_troyanop, y_troyanop, x_planetap, y_planetap, x_estrellap, y_estrellap = iteradorTresCuerpos(h, pp, it)

#Se grafica la orbita del troyano en el sistema de referencia del planeta, con las condiciones iniciales que se piden y con una pequena perturbacion
plt.plot(x_troyano-x_planeta, y_troyano-y_planeta, label=r"$Sin$ $perturbar$")
plt.plot(x_troyanop-x_planetap, y_troyanop-y_planetap, label=r"$Perturbadas$", c="r")
plt.title(r"$\'Orbitas$ $del$ $troyano$ $respecto$ $al$ $planeta$",fontsize=15)
plt.ylabel(r"$y$", fontsize=15)
plt.xlabel(r"$x$", fontsize=15)
plt.legend(loc=0)
plt.savefig("Troyano.pdf")
plt.close()

#Se crean los nuevos objetos con las condiciones iniciales pertinentes, cambiando la masa del planeta. Se hace para m2 igual a 10, 20, 30 y 40.
m_trojan, x_trojan, y_trojan, vx_trojan, vy_trojan, m_planet,x_planet,vy_planet, m_star,x_star,vy_star = actualizarCondicionesIniciales(10.0)
troyano10 = Planetas(m_trojan, x_trojan, y_trojan, vx_trojan, vy_trojan)
planeta10 = Planetas(m_planet,x_planet,0,0,vy_planet)
estrella10 = Planetas(m_star,x_star,0,0,vy_star) 
p10 = [troyano10, planeta10, estrella10]

m_trojan, x_trojan, y_trojan, vx_trojan, vy_trojan, m_planet,x_planet,vy_planet, m_star,x_star,vy_star = actualizarCondicionesIniciales(20.0)
troyano20 = Planetas(m_trojan, x_trojan, y_trojan, vx_trojan, vy_trojan)
planeta20 = Planetas(m_planet,x_planet,0,0,vy_planet)
estrella20 = Planetas(m_star,x_star,0,0,vy_star)
p20 = [troyano20, planeta20, estrella20]

m_trojan, x_trojan, y_trojan, vx_trojan, vy_trojan, m_planet,x_planet,vy_planet, m_star,x_star,vy_star = actualizarCondicionesIniciales(30.0)
troyano30 = Planetas(m_trojan, x_trojan, y_trojan, vx_trojan, vy_trojan)
planeta30 = Planetas(m_planet,x_planet,0,0,vy_planet)
estrella30 = Planetas(m_star,x_star,0,0,vy_star) 
p30 = [troyano30, planeta30, estrella30]

m_trojan, x_trojan, y_trojan, vx_trojan, vy_trojan, m_planet,x_planet,vy_planet, m_star,x_star,vy_star = actualizarCondicionesIniciales(40.0)
troyano40 = Planetas(m_trojan, x_trojan, y_trojan, vx_trojan, vy_trojan)
planeta40 = Planetas(m_planet,x_planet,0,0,vy_planet)
estrella40 = Planetas(m_star,x_star,0,0,vy_star)
p40 = [troyano40, planeta40, estrella40]

#Se itera sobre los nuevos cuerpos creados
x_troyano10, y_troyano10, x_planeta10, y_planeta10, x_estrella10, y_estrella10 = iteradorTresCuerpos(h, p10, it)
x_troyano20, y_troyano20, x_planeta20, y_planeta20, x_estrella20, y_estrella20 = iteradorTresCuerpos(h, p20, it)
x_troyano30, y_troyano30, x_planeta30, y_planeta30, x_estrella30, y_estrella30 = iteradorTresCuerpos(h, p30, it)
x_troyano40, y_troyano40, x_planeta40, y_planeta40, x_estrella40, y_estrella40 = iteradorTresCuerpos(h, p40, it)

#Se grafican las orbitas del troyano en el sistema de referencia del planeta para los casos anteriores.
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, figsize=(6,11))
ax1.plot(x_troyano10-x_planeta10, y_troyano10-y_planeta10, label=r"$m_2=10$", c="b")
ax1.set_title(r"$\'Orbitas$ $del$ $troyano$ $respecto$ $al$ $planeta$" , fontsize=18)
ax1.set_xlabel(r"$x$")
ax1.set_ylabel(r"$y$")
ax1.legend()
ax2.plot(x_troyano20-x_planeta20, y_troyano20-y_planeta20, label=r"$m_2=20$", c="g")
ax2.set_xlabel(r"$x$")
ax2.set_ylabel(r"$y$")
ax2.legend()
ax3.plot(x_troyano30-x_planeta30, y_troyano30-y_planeta30, label=r"$m_2=30$", c="r")
ax3.set_xlabel(r"$x$")
ax3.set_ylabel(r"$y$")
ax3.legend()
ax4.plot(x_troyano40-x_planeta40, y_troyano40-y_planeta40, label=r"$m_2=40$", c="k")
ax4.set_xlabel(r"$x$")
ax4.set_ylabel(r"$y$")
ax4.legend()
fig.subplots_adjust(hspace=0.7)
plt.savefig("MassPLOT.pdf")
plt.close()
