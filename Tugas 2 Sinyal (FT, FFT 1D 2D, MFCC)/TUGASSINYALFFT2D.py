import numpy as np
import matplotlib.pyplot as plt

# Definisikan Sinyal
N = 128  # Jumlah Sinyal
A = 1
x = np.linspace(-3*A, 3*A, N)  # Signal values range from -A to A
y = np.zeros((N, N))  #  2D array for the signal

# Amplitude values to the signal
for i in range(N):
    for j in range(N):
        if x[i] >= -1 and x[i] <= 1:
            y[i, j] = 1
        else:
            y[i, j] = 0

# 2D FFT on the signal
Y = np.fft.fft2(y)

# Shift the zero frequency component to the center of the spectrum
Y_shifted = np.fft.fftshift(Y)

# Compute the magnitude spectrum
mag_spectrum = np.abs(Y_shifted)

# Display the magnitude spectrum
plt.imshow(mag_spectrum, cmap='jet')
plt.colorbar()
plt.title('2D FFT Magnitude Spectrum')
plt.xlabel('Frequency (kx)')
plt.ylabel('Frequency (ky)')
plt.show()

