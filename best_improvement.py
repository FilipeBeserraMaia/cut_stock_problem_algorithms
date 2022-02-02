from random import uniform

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


def best_improvment(cut_list, limit, iter):
    initial_solution = grasp(cut_list=cut_list, base_bar=limit)
    best_solution = initial_solution
    minimum_cost = get_cost(initial_solution, limit)

    tabu = []

    count = 0
    while count <= iter:
        local_solutions = search(best_solution, limit, iter)

        for solution in local_solutions:
            if solution not in tabu:

                current_cost = get_cost(solution, limit)
                if current_cost[1] < minimum_cost[1] and current_cost[0] <= minimum_cost[0]:
                    best_solution = solution
                    minimum_cost = current_cost

                    tabu.append(best_solution)
                    break

        if len(tabu) >= len(initial_solution):
            tabu.pop(0)
        count += 1

    return best_solution


def search(solution, bar_size, amt_trade=10):
    cost = get_cost(solution, bar_size)
    current_cost = (float('+inf'), float('+inf'))

    solutions = []
    for _ in range(amt_trade):
        count = 0
        while not (current_cost[1] < cost[1] and current_cost[0] <= cost[0]):

            if count > 1000:
                return solutions

            current_solution = permutation(solution, bar_size)
            current_solution = fill_bar(current_solution, bar_size)
            current_cost = get_cost(current_solution, bar_size)
            count += 1

        solutions.append(current_solution)

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
    def uni(s): return int(uniform(0, len(s)))

    b1 = uni(solution)
    p1 = uni(solution[b1])

    b2 = uni(solution)
    p2 = uni(solution[b2])

    if solution[b1] and solution[b2]:
        if (sum(solution[b1]) - (solution[b1][p1]) + solution[b2][p2]) <= bar_size and (sum(solution[b2]) - solution[b2][p2] + solution[b1][p1]) <= bar_size:
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
    base_bar = 200

    si = grasp(cut_list=cut_list, base_bar=base_bar)
    print(f'{si}')
    print(f'{get_cost(si, base_bar)=}')

    result = search(si, base_bar, 100)
    print(result)


if __name__ == '__main__':
    main()
