import numpy as np

def fft_it(x):
    # Length of input signal
    n = len(x)

    # Convert input to complex numpy array
    x = np.array(x, dtype=complex)

    # Reorder input using bit reversal
    x = x[np.bitwise_xor(np.arange(n), np.arange(n)[::-1])]

    # Compute number of stages required for FFT
    q = int(np.round(np.log2(n)))

    # Perform FFT using iterative algorithm
    for j in range(1, q+1):

        # Size of subproblems at this stage
        m = 2**(j-1)

        # Twiddle factors
        d = np.exp(-np.pi*1j/m * np.arange(m))

        # Perform butterfly operations
        for k in range(1, 2**(q-j)+1):
            s = (k-1) * 2*m
            e = k * 2*m
            r = s + m
            y_top = x[s:r]
            y_bottom = x[r:e]
            z = d * y_bottom
            y = np.concatenate([y_top + z, y_top - z])
            x[s:e] = y

    # Print real and imaginary parts of output
    print("\n**********************************************************************")
    print("Real part: ", np.real(y))
    print("Imaginary part: ", np.imag(y))

    # Print phase and magnitude of output
    mag = np.abs(y)
    phase = np.angle(y)
    print("Magnitude: ", mag)
    print("Phase: ", phase)
    print("**********************************************************************\n")
    
    # Return FFT of input
    return x

#x = [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0]
x = [1, 2, 3, 4, 5, 6, 7, 8]
o = fft_it(x)
#print(o)


