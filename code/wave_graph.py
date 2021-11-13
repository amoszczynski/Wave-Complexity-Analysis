import matplotlib.pyplot as plt
import math
import numpy as np

#graph the complex wave from 0, create sine wave with same max and length
def wave_graph(cmp, sine, case = 0):
    

    plt.figure(1)
    plt.title("Signal Wave...")
    if case == 0:
        plt.plot(sine[0], sine[1])
        plt.plot(cmp)
    if case == 1:
        plt.plot(sine[0], sine[1])
    if case == 2:
        plt.plot(cmp)
    plt.show()
