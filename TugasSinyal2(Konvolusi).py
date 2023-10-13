def convolve(signal, kernel):
    output_length = len(signal) + len(kernel) - 1
    output = [0] * output_length

    for i in range(len(signal)):
        for j in range(len(kernel)):
            output[i + j] += signal[i] * kernel[j]

    return output

print ("Implementation of Convolution")
print ("Rakan Akmal Musalim")
print ("5009201016")

# Test the function
signal = [2, 5, 4, 4, 5]
kernel = [0.5, 0.5]

result = convolve(signal, kernel)
print(result)


