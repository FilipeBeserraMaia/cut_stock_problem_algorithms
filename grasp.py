"""




                    RETIRAR!!!!!!!!!!!!!!



"""


from random import randint, uniform
import numpy as np
import random

def get_value_set(set, vw):
    total_value = 0
    total_weigth = 0

    for i in range(len(set)):
        if set[i] == 1:
            v = vw[i][0]
            w = vw[i][1]
            total_value += v
            total_weigth += w
    return total_value, total_weigth

def new_matrix(l, c, w, vw):
    new_m = np.full(c, 0)
    removed = []
    weigth = 0

    new_m = grasp(vw, removed, new_m, w)

    return new_m

def get_value(kps, items):
    valuer, weigth = 0
    for i, v in enumerate(items):
        if kps[i]:
            valuer += v[0]
            weigth += v[1]

def grasp(items, removed, m, w):
    MAX = 0.6
    MIN = 0.4
    ALPHA = MAX
   
    weigth = 0
    indexs = list(range(len(items)))
    rlc = []

    while weigth < w and indexs:
        rlc = []
        maxim = max(items[indexs], key=lambda x: (x[0] / x[1]))
        maxim = maxim[0] / maxim[1]
        minim = min(items[indexs], key=lambda x: (x[0] / x[1]))
        minim = minim[0] / minim[1]

        b = minim + ALPHA * (maxim - minim)

        for i in indexs:
            if (items[i][0] / items[i][1]) >= b:
                rlc.append(i)

        if rlc:
            selected_c = random.uniform(0, len(rlc) - 1)
            selected_c = rlc[int(selected_c)]
        else:
            break

        m[selected_c] = 1
        _, weigth = get_value_set(m, items)
        
        indexs.pop(indexs.index(selected_c))

    return m

def main():
    v_w = [[randint(600, 800), randint(30, 60)] for _ in range(10)]
    max_weight = 170

    v_w = sorted(v_w, key=lambda i: i[0] / i[1], reverse=True)

    v_w = np.array(v_w)

    print(new_matrix(len(v_w), len(v_w), max_weight, v_w))


if __name__ == '__main__':
    pass