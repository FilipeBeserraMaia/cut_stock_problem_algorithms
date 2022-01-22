import numpy as np
import math

def main():
    bottom_up(10, [1, 2, 3, 4, 5, 6, 7, 8, 9])

def dynamic(cut_list=[], len_bar=10):
    matrix = np.zeros((len(cut_list), len(len_bar)))
    cut_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for cut in cut_list:
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                if cut <= j:
                    pass  # fazer o paranaue

    return matrix[-1][-1]

def bottom_up(n, p):
    size_bar = 7
    items = [1,2,3,4,5,6]

    max_amt_bar = int(math.ceil(sum(items) / size_bar))

    shape = (len(items) + 1, size_bar + 1, max_amt_bar+1)
    matrix = np.zeros(shape=shape)
    next_index = 1

    for curr_cut in range(1, matrix.shape[0]):
        for curr_lim_bar in range(1, matrix.shape[1]):
            best_local_bar = (0, 0)

            for curr_bar in range(1, matrix.shape[2]):


                local_bar = 0

                if items[curr_cut-1] <= curr_lim_bar:
                    local_bar = items[curr_cut-1] + matrix[curr_cut - 1, curr_lim_bar - curr_cut, curr_bar]

                previous = matrix[curr_cut - 1, curr_lim_bar, curr_bar]
                aux = max(local_bar, previous)

                if aux > best_local_bar[1]:
                    best_local_bar = (curr_bar, aux)
            matrix[curr_cut, curr_lim_bar, best_local_bar[0]] = best_local_bar[1]

    for i in range(matrix.shape[2]):
        print(matrix[-1][-1][i])
    return matrix[-1][-1][-1]


if __name__ == '__main__':
    main()
