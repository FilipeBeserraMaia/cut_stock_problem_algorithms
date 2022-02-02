from unittest import result
import numpy as np
import math

def main():
    bottom_up(10, [1, 2, 3, 4, 5, 6, 7, 8, 9])

def dynamic(items, size_bar):
    shape = (len(items) + 1, size_bar + 1)
    matrix = np.full(fill_value={'value': 0, 'cuts': []}, shape=shape)

    for curr_cut in range(1, matrix.shape[0]):
        for curr_lim_bar in range(1, matrix.shape[1]):
            local_bar = -1
            
            if items[curr_cut-1] <= curr_lim_bar :
                local_bar = items[curr_cut-1] + matrix[curr_cut - 1, curr_lim_bar - items[curr_cut-1]]['value']
                path = [curr_cut-1] + matrix[curr_cut - 1, curr_lim_bar - items[curr_cut-1]]['cuts']
            
            previous = matrix[curr_cut - 1, curr_lim_bar]['value']
            aux = max(local_bar, previous)

            if local_bar < previous:
                path = matrix[curr_cut - 1, curr_lim_bar]['cuts']

            matrix[curr_cut, curr_lim_bar] = {'value': aux, 'cuts': path}

    return matrix[-1][-1]


def bottom_up(items, size_bar):

    max_amt_bar = int(math.ceil(sum(items) / size_bar))
    
    result_list = []

    bars = [[size_bar, []] for i in range(max_amt_bar+1)]

    while len(items) > 0:
        local_results = []
        best_local = 0
        index = 0
        
        for i, bar in enumerate(bars):
            local_results.append(dynamic(items, bar[0]))
            
            if local_results[-1]['value'] > best_local:
                best_local = local_results[-1]['value']
                index = i


        bars[index][0] -= local_results[index]['value']
        bars[index][1] += local_results[index]['cuts']

        result_list.append([items[i] for i in local_results[index]['cuts']])
        items = np.delete(items, local_results[index]['cuts'])

    return result_list
 



def read_instances(path):
    with open(path, 'r') as f:
        data = f.read()
        data = data.split("\n")

    result = int(data.pop(0))
    size_bar = int(data.pop(0))

    cuts = []
    for lines in data:
        line = lines.split('\t')
        if len(line) > 1:
            cuts += [int(line[0])] * int(line[1])
    return cuts, size_bar, result


if __name__ == '__main__':
    cuts, size_bar, result = read_instances('instancias/Solutionsfaceis/Schwerin1_BPP100.txt')
    print(len(cuts))
    print(cuts)
    bottom_up(cuts, size_bar)
