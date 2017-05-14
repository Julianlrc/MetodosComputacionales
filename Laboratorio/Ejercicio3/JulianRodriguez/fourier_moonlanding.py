import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft2, fftfreq
from scipy.signal import convolve2d
from scipy import fftpack



def plot_spectrum(F):
    plt.imshow(np.log(5 + np.abs(F)))

imagen = plt.imread('moonlanding.png')

imagen_ft = fftpack.fft2(imagen)

ff = imagen_ft.copy()

r, c = ff.shape

ff[50:-50] = 0

ff[:, 50:-50] = 0

im_new = fftpack.ifft2(ff).real
plt.figure(figsize=(12,8))
plt.subplot(221)
plt.title('Imagen inicial')
plt.imshow(imagen, plt.cm.gray)
plt.subplot(222)
plt.title('Fourier')
plot_spectrum(imagen_ft)
plt.subplot(224)
plt.title('Espectro')
plot_spectrum(ff)
plt.subplot(223)
plt.title('Imagen modificada')
plt.imshow(im_new, plt.cm.gray)

plt.subplots_adjust(hspace=0.4)

plt.show()
