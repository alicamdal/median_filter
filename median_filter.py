"""
    Applies median filter for sounds. Developed for Computational Methods module of Trinity College Dublin.
    Author: Ali Camdal
"""

from scipy import ndimage
from scipy.io.wavfile import write
import sounddevice as sd
import numpy as np
import soundfile as sf
import sys
import unittest
import math

# Progress Bar for filter process
def printProgressBar(iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    if iteration == total: 
        print()


def median(real_data, data, filter_size, detection):
    output = np.zeros((len(data), 1))
    data_length = len(data)
    printProgressBar(0, data_length, prefix = "Progress:", suffix = "Complete", length = 50)
    for i in range(data_length - 1):
        if detection[i] == 0:                                       # if there is no distortion copy real data
            output[i] = real_data[i]
        else:                                                       # else copy median data for sequence
            sorted_data = np.sort(data[i])
            output[i] = sorted_data[filter_size // 2]
        if i % 20 == 0:                                             # update progress bar for every 20 cycle
            printProgressBar(i + 1, data_length, prefix = 'Progress:', suffix = 'Complete', length = 50)
    print()
    output = np.transpose(output)
    output = output[0]
    return output


def medianFilter(data, filter_size, detection):
    filter_size = (filter_size * 2) + 1                             # filter size must be odd
    indexer = filter_size // 2                                      # index variable for filter
    output = np.zeros((len(data), filter_size), dtype=data.dtype)   # output variable
    output[:, indexer] = data
    for i in range(indexer):
        j = indexer - i
        output[j:, i] = data[:-j]
        output[:j, i] = data[0]
        output[:-j, -(i + 1)] = data[j:]
        output[-j:, -(i + 1)] = data[-1]
    return median(data, output, filter_size, detection)

if __name__ == "__main__":
    """
        input arguments list:
            1 -> input file
            2 -> detection file
            3 -> filter size
            4 -> output file
    """
    try:
        if len(sys.argv) == 5:
            print("Script Starts")
            input_file = sys.argv[1]
            detection_file = sys.argv[2]
            filter_size = int(sys.argv[3])
            output_file = sys.argv[4]
            print("Input file playing...")
            input_data, Fs = sf.read(input_file, dtype='float32')
            sd.play(input_data, Fs)
            sd.wait()
            print("Input file playing done...")
            print("Starting median filter...")
            detection = np.fromfile(detection_file, dtype = np.uint8)
            output_data = medianFilter(input_data, filter_size, detection)
            write(output_file, Fs, output_data.astype(np.float32))
            print("Playing output file...")
            output_data, Fs = sf.read(output_file, dtype='float32')
            sd.play(output_data, Fs)
            sd.wait()
            print("Script Done")
        else:
            print("Missing Argument")
    except Exception as excp:
        print(excp)
