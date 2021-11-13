
from signal_wave import *
from wave_m import *
from wave_graph import *
from create_wave import *
from complexity import *
import matplotlib.pyplot as plt

file = #your .wav file here
signal = sig_array(file)
#plt.figure(1)
#plt.title("Signal Wave...")
#plt.plot(signal)
zeroes = find_zeroes(signal)

cmp = make_cmp(signal, zeroes)
sine = make_sine(max(signal[0]), int(zeroes[1] - zeroes[0]))

#case = 0 by default, 1 for just sine, 2 form just cmp
wave_graph(cmp, sine)

#print(pt_complexity(sine[1][16], sine[1][17], cmp[16], cmp[17]))

print(complexity(cmp, sine))
print(avg_others(cmp, sine))
