import soundfile as sf
import numpy as np

if __name__ == "__main__":    
    data, Fs = sf.read("degraded.wav", dtype="float32")     # read degraded sound file
    detection_vector = np.zeros((1, len(data)))[0]          # create detection vector with zeros
    for i,dat in enumerate(data):                           # iterate data
        if dat > 0.8:                                       # if data greater than 0.8 it is distortion
            detection_vector[i] = 1                         # change distortion position as 1
        else:
            pass

    with open("detection.raw", 'wb') as f:                  # write detection vector to binary file
        f.write(detection_vector.astype(np.uint8))


