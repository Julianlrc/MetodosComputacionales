import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq, ifft
from scipy.io import wavfile

#Se hace la lectura de los datos
rateV, dataV = wavfile.read("violin.wav")
rateT, dataT = wavfile.read("trumpet.wav")

dtv = 1.0/rateV
dtt = 1.0/rateT

nT = len(dataT)
nV = len(dataV)

#Se halla la transformada de Fourier de los datos y se toma su parte real
ft_violin = fft(dataV)
ft_trumpet = fft(dataT)
ft_violin_real = ft_violin.real
ft_trumpet_real = ft_trumpet.real

#Se recuperan las frecuencias
freqV = fftfreq(nV, dtv)
freqT = fftfreq(nT, dtt)

#Se determina la mitad en la longitud de los datos
mitad_T =int(np.ceil(nT/2.0))
mitad_V = int(np.ceil(nV/2.0))

#Se toman solo los datos para las frecuencias positivas 
ft_violin_mitad = ft_violin_real[:mitad_V]
ft_trumpet_mitad = ft_trumpet_real[:mitad_T]
freqV_mitad = freqV[:mitad_V]
freqT_mitad = freqT[:mitad_T]

#Graficamos el valor absoluto de la parte real de la transformada de Fourier hallada en funcion de las frecuencias
fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(freqV_mitad, abs(ft_violin_mitad), label=r"$Viol\'in$", c='g')
ax1.set_title(r"$Transformadas$ $de$ $Fourier$")
ax1.set_xlim(0, 10500)
ax1.set_xlabel(r"$Frecuencia$ $(Hz)$")
ax1.set_ylabel(r"$Amplitud$")
ax1.legend(loc=0)
ax2.plot(freqT_mitad, abs(ft_trumpet_mitad), label="$Trompeta$", c='b')
ax2.set_xlabel(r"$Frecuencia$ $(Hz)$")
ax2.set_ylabel(r"$Amplitud$")
ax2.legend(loc=0)
ax2.set_xlim(0, 4000) 
fig.subplots_adjust(hspace=0.5)
plt.savefig("ViolinTrompeta.pdf")
plt.close()

#Se define una funcion que encuentra la frecuencia fundamental
def fundamental(ft, freq):
	amp = 0
	indx = 0
	for i in range(0, len(ft)):
		if(abs(ft[i])>amp):
			amp = ft[i]
			indx = i
	return abs(freq[indx])
	

#Se definen funciones que filtran los datos
def filtro_fundamental(ft, freq, rango):	
	fund = fundamental(ft, freq)
	for j in range(0, len(freq)):
		if(abs(freq[j])>(fund-rango) and abs(freq[j])<(fund+rango)):
			ft[j]=0
	return ft

def pasabajas(ft, freq, corte):
	ft[abs(freq) > corte]=0
	return ft

def pasaaltas(ft, freq, corte):
	ft[abs(freq) < corte] = 0
	return ft

def pasabandas(ft, freq, rango):
	fund = fundamental(ft, freq)	
	ft[abs(freq) >= (fund+rango)]= 0
	ft[abs(freq) <= (fund-rango)]= 0
	return ft

#Se le aplican los filtros a los datos del violin
ft = ft_violin.copy()
violin_fundamental = filtro_fundamental(ft, freqV, 100)
ft = ft_violin.copy()
violin_pasabajas = pasabajas(ft, freqV, 2000)
ft = ft_violin.copy()
violin_pasaaltas = pasaaltas(ft, freqV, 2000)
ft = ft_violin.copy()
violin_pasabandas = pasabandas(ft, freqV, 100)
ft = ft_violin.copy()

#Se grafican los datos originales y los filtros aplicados a estos (Normalizados) en funcion de las frecuencias (En la grafica solo le muestran los datos para las frecuencias en donde los datos son significativos)
f, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(5, sharey=True, figsize=(6,10))
ax1.plot(freqV, abs(ft_violin/nV), label=r"$Original$")
ax1.set_title(r"$Transformada$ $de$ $Fourier$ $original$ $y$ $filtros$")
ax1.set_xlabel(r"$Frecuencias$ $(Hz)$")
ax1.set_ylabel(r"$Amplitud$")
ax1.legend(loc=0)
ax1.set_xlim([-15000, 15000])
ax2.plot(freqV, abs(violin_fundamental/nV), label=r"$Fundamental$")
ax2.set_xlabel(r"$Frecuencias$ $(Hz)$")
ax2.set_ylabel(r"$Amplitud$")
ax2.legend(loc=0)
ax2.set_xlim([-15000, 15000])
ax3.plot(freqV, abs(violin_pasabajas/nV), label=r"$Pasa$ $bajas$")
ax3.set_ylabel(r"$Amplitud$")
ax3.set_xlabel(r"$Frecuencias$ $(Hz)$")
ax3.legend(loc=0)
ax3.set_xlim([-15000, 15000])
ax4.plot(freqV, abs(violin_pasaaltas/nV), label=r"$Pasa$ $altas$")
ax4.set_xlabel(r"$Frecuencias$ $(Hz)$")
ax4.set_ylabel(r"$Amplitud$")
ax4.legend(loc=0)
ax4.set_xlim([-15000, 15000])
ax5.plot(freqV, abs(violin_pasabandas/nV), label=r"$Pasabandas$")
ax5.set_xlabel(r"$Frecuencias$ $(Hz)$")
ax5.set_ylabel(r"$Amplitud$")
ax5.legend(loc=0)
ax5.set_xlim([-15000, 15000])
plt.savefig("ViolinFiltros.pdf")
f.subplots_adjust(hspace=1.0)
plt.close()

#Se reconstruyen los datos de la onda para cada uno de los filtros y se generan unos nuevos archivos de sonido .wav
wavfile.write("violin_pico.wav", rateV, np.fft.ifft(violin_fundamental).real)
wavfile.write("violin_pasabajos.wav", rateV, np.fft.ifft(violin_pasabajas).real)
wavfile.write("violin_pasaaltos.wav", rateV, np.fft.ifft(violin_pasaaltas).real)
wavfile.write("violin_pasabanda.wav", rateV, np.fft.ifft(violin_pasabandas).real)
