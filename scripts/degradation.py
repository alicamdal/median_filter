import soundfile as sf
import numpy as np
from random import randint
from scipy.io.wavfile import write

if __name__ == "__main__":
    data, Fs = sf.read("clean.wav", dtype="float32")    # read clean sound
    data = np.delete(data, 1, 1)                        # change stereo to mono
    data = data.T[0]                                    # take transpose and reduce dimension

    noise_length = 1000                                 # noise number of 1000

    for i in range(noise_length):
        noise = randint(0, len(data))                   # randomly determine the position of noise
        data[noise] = 1                                 # add noise of 1
    
    write("degraded.wav", Fs, data.astype(np.float32))  # write wav file with the same sampling frequency and data type
