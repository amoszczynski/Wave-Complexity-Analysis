import numpy as np

#finds one revolution of wave
def find_zeroes(sig):
    a = np.array([])
    mx = max(sig[0])
    mx_index = np.where(sig[0] == mx)[0][0]
    br1 = False
    #goes backwards
    i = mx_index
    while br1 == False:
        
        if sig[0][i] == 0:
            a = np.append(a, i)
            br1 = True
            break
        elif sig[0][i + 1] > 0 and sig[0][i] < 0:
            a = np.append(a, i)
            br1 = True
            break
        i = i - 1

    #goes forward and finds second zero ( think sine wave goes through x-axis and then comes back up)
    # only really need to check when value goes from negative to positive
    br2 = False
    chk1 = 0 #makes sure value == 0 isnt the first one
    mx_chk = max(sig[0]) / 4
    i = mx_index + 1 #artifically inflate length here (+ 100 or so)
    chk2 = False
    while br2 == False:
        
        if sig[0][i] < -mx_chk and not chk2:
            chk2 = True
        if sig[0][i] == 0 and chk1 == 0 and chk2:
            chk1 = chk1 + 1
        elif sig[0][i] == 0 and chk1 == 1 and chk2:
            a = np.append(a, i)
            br2 = True
            break
        elif sig[0][i] > 0 and sig[0][i - 1] < 0 and chk2:
            a = np.append(a, i)
            br2 = True
            break
        i = i + 1
    return a

