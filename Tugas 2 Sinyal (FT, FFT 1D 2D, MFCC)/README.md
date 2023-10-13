# Signal Class Assignment 2

There are two files in this repository (Source Code & Screenshot of Spyder) 

## Convolution of two 1D array signals 

There are two array signals, The first one is a signal that wants to be convoluted, and the second one is the signal that becomes a kernel or signal 2.

```python
signal = [2, 5, 4, 4, 5]
kernel = [0.5, 0.5]
```

## CODING

Define the convolution function that takes two signals, signal and kernel, as its inputs. 

Then calculate the length of the resulting convolution signal. In convolution, the resulting signal has a length equal to the sum of the lengths of the input signals minus 1.

```python
def convolve(signal, kernel):
    output_length = len(signal) + len(kernel) - 1
    output = [0] * output_length
```
I use nested loops to perform the convolution. The outer loop iterates through each element of the signal.

Inside the outer loop, the inner loop iterates through each element of the kernel.

For each pair of elements from signal and kernel, we multiply them and add the result to the corresponding position in the output 
```python
 for i in range(len(signal)):
        for j in range(len(kernel)):
            output[i + j] += signal[i] * kernel[j]

    return output
```
Then After the loops are complete, we return the output as the resulting convolution. Then print the result or output of convolve (signal, kernel)

```python
result = convolve(signal, kernel)
print(result) 
```

We can put our name and NRP before print the result 
```python
print ("Implementation of Convolution")
print ("Rakan Akmal Musalim")
print ("5009201016")
```

# OUTPUT
These are the output of the program 


