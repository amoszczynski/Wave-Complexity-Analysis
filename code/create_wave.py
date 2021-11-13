import numpy as np
import math


def make_sine(mx, ln):
    sinx = list(range(ln)) #array of x values
    adj_x = []
    for i in sinx:
        v1 = sinx[i] * ((2 * math.pi) / (ln - 1))
        adj_x.append(v1)
    siny = []
    for j in sinx:
        v2 = mx * math.sin(adj_x[j])
        siny.append(v2)
    sine_wave = np.array([sinx, siny])
    return sine_wave

def make_cmp(sig, zeroes):
    mx = max(sig[0]) #amplitude of sine wave
    ln = int(zeroes[1] - zeroes[0])  #length of complete wave, number of samples in computing
    z1, z2 = int(zeroes[0]), int(zeroes[1])
    cmp_wave = sig[0][z1:z2] #new wave starting at 0
    return cmp_wave
