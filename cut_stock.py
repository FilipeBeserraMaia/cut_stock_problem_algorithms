from math import ceil
from random import randint, uniform
import numpy as np
import random


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
            selected_c = random.uniform(0, len(rlc) - 1)
            selected_c = rlc[int(selected_c)]
        else:
            break

        solution = calc_solution(solution, cut_list[selected_c], base_bar)
        indexs.pop(indexs.index(selected_c))

    return solution


def flips():
    pass


def tabu_search(first_solution, remainder_of_first_solution, dict_of_neighbours, iters, size):
    count = 1
    solution = first_solution
    best_cost = remainder_of_first_solution
    best_solution_ever = solution
    tabu_list = list()

    while count <= iters:
        # return possibles solutions
        flipados = flips(solution, dict_of_neighbours)
        index_of_best_solution = 0
        best_solution = flipados[index_of_best_solution]
        best_cost_index = len(best_solution) - 1

        found = False
        while not found:
            for i in range(len(best_solution)):
                if best_solution[i] != solution[i]:
                    first_exchange = best_solution[i]
                    second_exchange = solution[i]
                    break

            # verifica se  a troca ja esta salva na lista tabu
            if [first_exchange, second_exchange] not in tabu_list and [second_exchange, first_exchange] not in tabu_list:
                found = True
                tabu_list.append([first_exchange, second_exchange])
                solution = best_solution[:-1]
                cost = flipados[index_of_best_solution][best_cost_index]
                if cost < best_cost:
                    best_cost = cost
                    best_solution_ever = solution
            else:
                index_of_best_solution = index_of_best_solution + 1
                best_solution = flipados[index_of_best_solution]

        if len(tabu_list) >= size:
            tabu_list.pop(0)

        count = count + 1

    return best_solution_ever, best_cost


def cut_stock(list_bars, size_base):
    amt_used = 1
    cut_list = {}
    current_bar = size_base

    list_bars.sort(reverse=True)

    while list_bars:
        best_item = search_best_item(list_bars, current_bar)

        if best_item is None or current_bar < list_bars[best_item]:
            amt_used += 1
            current_bar = size_base
            best_item = 0

        current_bar -= list_bars[best_item]
        cut_list = save_cut(cut_list, amt_used, list_bars[best_item])
        list_bars.pop(best_item)

    return cut_list, (current_bar, amt_used)


# salva a ordem e a barra que o index foi cortado
def save_cut(cut_list, bar_id, new_item):
    if not bar_id in cut_list.keys():
        cut_list[str(bar_id)] = []

    cut_list[str(bar_id)].append(new_item)

    return cut_list


def search_best_item(cut_list=[], rest=0):
    best_index = list(filter(lambda x: x[1] <= rest, enumerate(cut_list)))

    return best_index[0][0] if best_index else None


def main():
    pass


if __name__ == '__main__':
    print()
