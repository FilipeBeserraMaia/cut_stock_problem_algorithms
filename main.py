from datetime import datetime

import numpy as np

from utils import read_instances, get_cost
from best_improvement import grasp, best_improvment
from dynamic_cut_stock import bottom_up
from greedy import greddy


def pipeline(algoritmo, *params):
    algoritmos = {
        'greddy': greddy,
        'grasp': grasp,
        'heuristic': best_improvment,
        'dynamic': bottom_up,
    }

    t_init = datetime.now()
    result = algoritmos[algoritmo](*params)
    t_diff = datetime.now() - t_init

    custom_print(algoritmo, result, t_diff)


def custom_print(algoritmo, result, time):
    print('='*35 + f' {algoritmo} ' + '='*35)

    for i, bar in enumerate(result):
        print(f'Barrra {i:2} - Toal {sum(bar)} - {bar}')

    print(f'\n\nTempo de execução: {time}')
    print(f'Results: {get_cost(result, size_bar)}\n')

    print('=' * 85)


if __name__ == '__main__':
    cuts, size_bar, result = read_instances('instancias/Solutionsfaceis/Schwerin1_BPP100.txt')
    cuts = np.array(cuts)

    pipeline('greddy', size_bar, cuts)
    pipeline('grasp', cuts, size_bar)
    pipeline('heuristic', cuts, size_bar, 100)
    pipeline('dynamic', cuts, size_bar)
