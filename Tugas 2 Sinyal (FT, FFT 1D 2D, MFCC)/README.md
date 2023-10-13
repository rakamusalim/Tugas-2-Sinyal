# Signal Class Assignment 2 (aDDED ASSIGNMENT)

There are several assignments, There are FFT 1D, FFT 2D, and MMPC From 3 graph 

# FFT 1D CODING
So here i assume that A has a value of 1

```python
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

```

## FFT 1D RESULT
FIRST IS FROM -A TO A
![FFT1D_-A SAMPAI A](https://github.com/rakamusalim/Tugas-2-Sinyal/assets/113959958/b9789e28-c1a8-4892-bab9-8f128191cd27)

SECOND IS FROM -A/2 TO A/2
![FFT1D_-A2 SAMPAI A2](https://github.com/rakamusalim/Tugas-2-Sinyal/assets/113959958/6cc2e10e-2fe7-4312-9c80-784ca1454ca9)

THIRD IS FROM -3A TO 3A
![FFT1D_3A SAMPAI 3A](https://github.com/rakamusalim/Tugas-2-Sinyal/assets/113959958/186bf5ee-ec7a-494a-8302-f77fe412b5f0)

# FFT 2D CODING
So here i assume that A has a value of 1

```python
import numpy as np
import matplotlib.pyplot as plt

# Definisikan Sinyal
N = 128  # Jumlah Sinyal
A = 1
x = np.linspace(-A, A, N)  # Signal values range from -A to A
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


```

## FFT 1D RESULT
FIRST IS FROM -A TO A
![FFT2D_-A SAMPAI A](https://github.com/rakamusalim/Tugas-2-Sinyal/assets/113959958/e9aeb3a8-de6b-4cf2-a5bc-20c9218eca5f)


SECOND IS FROM -A/2 TO A/2
![FFT2D_-A2 SAMPAI A2](https://github.com/rakamusalim/Tugas-2-Sinyal/assets/113959958/2414eb8b-8df9-402f-8e59-73421d38c142)


THIRD IS FROM -3A TO 3A
![FFT2D_-3A SAMPAI 3A](https://github.com/rakamusalim/Tugas-2-Sinyal/assets/113959958/45971b7e-fdd7-4682-abfb-520836b12f7a)
