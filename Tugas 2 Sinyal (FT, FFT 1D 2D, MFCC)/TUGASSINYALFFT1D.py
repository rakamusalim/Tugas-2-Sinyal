import numpy as np
import matplotlib.pyplot as plt

# Parameter
N = 15000  # Jumlah sample 
T = 1.0 / 2000.0  # jarak antar sample
A = 1  # nilai A, diasumsikan 1

# Generate the signal
x = np.linspace(-N*T/2, N*T/2, N, endpoint=False)
y = np.where(np.abs(x) < 3*A, 1, 0)  # Fungsi box

# Compute FFT
yf = np.fft.fftshift(np.fft.fft(y))
xf = np.fft.fftshift(np.fft.fftfreq(N, T))

# Plot
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(x, y)
plt.title('Original Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(2, 1, 2)
plt.plot(xf, 2/N * np.abs(yf))
plt.title('Magnitude of FFT')
plt.xlabel('Frequency')
plt.ylabel('Magnitude')

plt.tight_layout()
plt.show()
