from random import uniform
from copy import deepcopy

import numpy as np


def grasp(cut_list=[], base_bar=0):
    ALPHA = 0.4

    indexs = list(range(len(cut_list)))
    solution = []

    while indexs:
        rlc = []
        maxim = max(cut_list[indexs])
        minim = min(cut_list[indexs])

        b = minim + ALPHA * (maxim - minim)

        for i in indexs:
            if (cut_list[i]) <= b:
                rlc.append(i)

        if rlc:
            selected_c = uniform(0, len(rlc) - 1)
            selected_c = rlc[int(selected_c)]
        else:
            break

        solution = calc_solution(solution, cut_list[selected_c], base_bar)
        indexs.pop(indexs.index(selected_c))

    return solution


def best_improvment(cut_list, bar_size, unprovement_limit):
    # minimum_cost = get_cost(initial_solution, limit)
    # tabu = []

    global_solution = (float('inf'), [])
    times_not_improved = 0
    new_solution = []
    # gerar solução inicial até não melhorar considerando um limite de naomelhoria
    while times_not_improved <= unprovement_limit:  # enquanto não parar de melhorar
        new_solution = grasp(cut_list=cut_list, base_bar=bar_size)
        local_solution = search(new_solution, bar_size)

        if len(local_solution) < global_solution[0]:  # caso melhore reseta se não incrementa
            global_solution = (len(local_solution), local_solution)
            times_not_improved = 0
        else:
            times_not_improved += 1

    return global_solution


def search(solution, bar_size):
    cost = get_cost(solution, bar_size)
    current_cost = (float('+inf'), float('+inf'))

    for b in range(len(solution)):
        bar = solution[b]
        sub_solution = deepcopy(solution[b + 1:])

        for it in range(len(bar)):
            item = bar[it]

            for b_aux in range(len(sub_solution)):
                if sum(sub_solution[b_aux]) + item <= bar_size:
                    sub_solution[b_aux].append(item)
                    break
            else:
                break
        else:
            solution = solution[:b] + sub_solution
            break

    return solution

    # for _ in range(amt_trade):
    #     count = 0
    #     while not (current_cost[1] < cost[1] and current_cost[0] <= cost[0]):
    #
    #         if count > 1000:
    #             return solutions
    #
    #         current_solution = permutation(solution, bar_size)
    #         current_solution = fill_bar(current_solution, bar_size)
    #         current_cost = get_cost(current_solution, bar_size)
    #         count += 1
    #
    #     solutions.append(current_solution)

    return solutions


def calc_solution(solution, cut_value, base_bar):
    if solution:
        current_bar = sum(solution[-1])
    else:
        current_bar = 0
        solution = [[]]

    if current_bar + cut_value <= base_bar:
        solution[-1] += [cut_value]
    else:
        solution.append([cut_value])

    return solution


def fill_bar(solution, bar_size):
    menor_barra = np.argmin((*map(lambda x: sum(x), solution),))
    menor_barra = solution.pop(menor_barra)

    for index, barra in enumerate(solution):
        elements = []
        for el in range(len(barra)):
            if sum(menor_barra) + barra[el] <= bar_size:
                elements.append(el)
                menor_barra.append(barra[el])

        if elements:
            solution[index] = [*map(
                lambda el: el[1],
                filter(lambda e: e[0] not in elements, enumerate(solution[index]))), ]

    solution.append(menor_barra)
    return solution


def permutation(solution, bar_size):
    def uni(s):
        return int(uniform(0, len(s)))

    b1 = uni(solution)
    p1 = uni(solution[b1])

    b2 = uni(solution)
    p2 = uni(solution[b2])

    if solution[b1] and solution[b2]:
        if (sum(solution[b1]) - (solution[b1][p1]) + solution[b2][p2]) <= bar_size and (
                sum(solution[b2]) - solution[b2][p2] + solution[b1][p1]) <= bar_size:
            aux = solution[b1][p1]
            solution[b1][p1] = solution[b2][p2]
            solution[b2][p2] = aux
    else:
        if solution[b1] and (sum(solution[b2]) + solution[b1][p1]) <= bar_size:
            solution[b2].append(solution[b1][p1])
        if solution[b2] and (sum(solution[b1]) + solution[b2][p2]) <= bar_size:
            solution[b1].append(solution[b2][p2])

    return solution


def get_cost(solution: list, limitt: int) -> int:
    sums = []
    for s in solution:
        rest = limitt - sum(s)
        if s and (rest > 0):
            sums.append(rest)

    return sum(sums), len(sums)


def main():
    np.random.seed(2)
    cut_list = np.random.randint(low=40, high=50, size=12)
    base_bar = 100

    # si = grasp(cut_list=cut_list, base_bar=base_bar)
    # print(f'{si}')
    # print(f'{get_cost(si, base_bar)=}')

    result = best_improvment(cut_list, base_bar, 1000)
    print(result)


if __name__ == '__main__':
    main()
