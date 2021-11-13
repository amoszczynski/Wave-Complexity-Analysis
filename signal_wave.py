import matplotlib.pyplot as plt
import numpy as np
import wave
import sys

#returns array representation of entire .wav file
def sig_array(file):
    spf = wave.open(file, "r")

    # Extract Raw Audio from Wav File
    signal = spf.readframes(-1)
    signal = np.fromstring(signal, "int16")
    fs = spf.getframerate() 

    if spf.getnchannels() == 2:
        print("mono only")
        sys.exit(0)

    Time = np.linspace(0, len(signal) / fs, num=len(signal))

    return [signal, Time]


