import random
import time
import numpy as np

def fft_rec(x):
    n = len(x)
    if n == 1:
        # If the length of the input array is 1, the FFT is just the array itself
        return x
    else:
        # Calculate the midpoint of the array
        m = n // 2

        # FFT of the even-indexed elements
        y_top = fft_rec(x[::2])   

        # FFT of the odd-indexed elements   
        y_bottom = fft_rec(x[1::2])  

        # Compute the complex exponential factor used in the FFT algorithm
        # The complex exponential factor is of the form exp(-2*pi*j/n)^(0:m-1),
        # where n is the length of the input array and m is half the length of the array
        complex_exp = np.exp(-2j*np.pi/n)    # Calculate the complex exponential e^(-2*pi*j/n)
        d = complex_exp**(np.arange(m))    # Raise the complex exponential sequence to the power of 0 through m-1

        
        # Multiply the FFT of the bottom half with the complex exponential factor
        z = d * y_bottom

        # Combine the FFTs of the top and bottom halves. 
        y = np.concatenate([y_top + z, y_top - z])
    
    re = np.real(y)
    im = np.imag(y)
    phase = np.angle(y)
    magnitude = np.abs(y)

    # Print results for each element in the FFT
    #print("\n**********************************************************************") 
    #for k in range(n):
    #    print(f"X[{k}] = {re[k]:.4f} + {im[k]:.4f}j (mag = {magnitude[k]:.4f}, phase = {phase[k]:.4f})")
    #print("**********************************************************************\n") 

    return y

#x = np.array([1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0])
#y = fft_rec(x)

# Create the original array
original_arr = np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0])

# Resize the array to a larger size
larger_arr = np.resize(original_arr, (1048576,))
fft_rec(larger_arr)

start_time = time.time()
for i in range(10):
    fft_rec(larger_arr)
end_time = time.time()

# Print the execution time
print(f"Execution time: {end_time - start_time:.6f} seconds")
