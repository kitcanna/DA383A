import numpy as np                
import matplotlib.pyplot as plt  

f = 800 # the frequency
N = 600 # the number of samples
T = 1/f # the time period
L = N*T # the length of the signal

# Creating an array x of N evenly spaced values between 0 and L, excluding the endpoint
x = np.linspace(0, L, N, endpoint=False)   

y = np.sin(50.0*(2.0*np.pi*x)) + 0.5*np.sin(80.0*(2.0*np.pi*x))   

# Applying FFT to the input signal y and dividing the result by N to obtain the normalized FFT coefficients
Y = np.fft.fft(y)/N          

# Computing the frequencies corresponding to the FFT coefficients using the fftfreq function from numpy.fft
freq = np.fft.fftfreq(N, T)      

plt.plot(freq, np.abs(Y))        
plt.title('FFT of y(x)')         
plt.xlabel('Frequency (Hz)')     
plt.ylabel('Amplitude')          
plt.show()                        

