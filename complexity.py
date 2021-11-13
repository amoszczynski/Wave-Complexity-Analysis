import math


#okay so two methods, determine pt complexity and determine overall complexity

#pt complexity = difference of slope + logistic weighted height differential
def pt_complexity(sy1, sy2, cy1, cy2, mx): #assumes deltax is 1
    s_s = int(sy2) - int(sy1)
    s_c = int(cy2) - int(cy1)

    angle_s = math.atan(s_s)
    angle_c = math.atan(s_c)

    dif_a = angle_s - angle_c


    slope_val = abs(math.pow((2 * dif_a / math.pi), 2))

    #height complexity is difference in height, put into logistic equation
    #coincidentally the slope and height difference is the same
    h_s = (int(sy2) + int(sy1)) * .5
    h_c = (int(cy2) + int(cy1)) * .5
    dif_h = abs(h_s - h_c)
    m = mx

    height_val = 5 / (1 + math.pow(math.e, -(10 / m) * (dif_h - (m / 2))))

    return [slope_val + height_val, slope_val, height_val]

def complexity(cmp, sine):
    i_cmp = 0
    for i in range(1, len(sine[0])):
        i_cmp = i_cmp + (pt_complexity(sine[1][i-1], sine[1][i], cmp[i-1], cmp[i], max(sine[1])))[0]
    return i_cmp / len(sine[0])

def avg_others(cmp, sine):
    h_cmp = 0
    a_cmp = 0
    for i in range(1, len(sine[0])):
        h_cmp = h_cmp + (pt_complexity(sine[1][i-1], sine[1][i], cmp[i-1], cmp[i], max(sine[1])))[2]
    for i in range(1, len(sine[0])):
        a_cmp = a_cmp + (pt_complexity(sine[1][i-1], sine[1][i], cmp[i-1], cmp[i], max(sine[1])))[1]
    return [h_cmp / len(sine[0]), a_cmp / len(sine[0])]