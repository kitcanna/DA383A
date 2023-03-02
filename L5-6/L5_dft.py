import time
import numpy as np
import random

def dft(x):
    # Length of input sequence
    N = len(x)              

    # Initialize an empty array to store DFT coefficients     
    X = np.zeros(N, dtype=np.complex_) 
    
    # Loop over frequency bins from 0 to N-1
    for k in range(N):              
        sum = 0           

        for n in range(N):  

            # Compute the DFT sum  
            sum += x[n] * np.exp(-2j * np.pi * n * k / N)  

        # Assign the sum to the kth frequency bin
        X[k] = sum                  
        
    # Print the DFT coefficients and their properties
    for k in range(N):
        # Real part of DFT coefficient
        re = np.real(X[k])    

        # Imaginary part of DFT coefficient      
        im = np.imag(X[k]) 

        # Magnitude of DFT coefficient         
        mag = np.abs(X[k])   

        # Phase of DFT coefficient       
        phase = np.angle(X[k])      

        # The :.4f format specifier rounds the floating-point numbers to 4 decimal places.
        # The angle function returns the phase angle in radians in the range [-pi, pi]
        #print("\n**********************************************************************") 
        #print(f"X[{k}] = {re:.4f} + {im:.4f}j (mag = {mag:.4f}, phase = {phase:.4f})")

        # Compare with FFT from the DFT library
        #X_fft = np.fft.fft(x)           
        #print("DFT = FFT:", np.allclose(X, X_fft)) 
        #print("**********************************************************************\n") 
    
    return X                        

#x = np.array([1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, ])

def randomize_values():
    values = []
    for i in range(1000000):
        values.append(random.random())
    return values

test_vals = np.array(randomize_values())

start_time = time.time()
for i in range(1000):
    #dft(test_vals)
    X_fft = np.fft.fft(test_vals) 
end_time = time.time()

# Print the execution time
print(f"Execution time: {end_time - start_time:.6f} seconds")
