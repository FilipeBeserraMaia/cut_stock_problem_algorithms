import numpy as np
from random import uniform
import copy


def best_improvment(initial_solution, cut_list, iter):
    count = 0
    best_solution = initial_solution
    minimum_cost = get_cost(initial_solution)

    tabu = []

    while count <= iter:
        local_solutions = search(best_solution)
        index = 0
        permutation = local_solutions[index][-2:]

        found = False
        while not found:
            if permutation not in tabu:
                found = True
                tabu.append(permutation)
                solution = local_solutions[index][:-2]
                cost = get_cost(solution)
            else:
                index += 1
                best_solution = local_solutions[index]

        count += 1
 

def search(curr_solution):
    """
    :return best_improved_solution
    """
    best_solution = curr_solution[:]
    not_change = 10
    changes = 0 
    
    while changes < not_change:
    
        changes +=1
        
    
    return best_solution



def shuffle_solution():
    amt_trade = 1
    bar_size = 12

    s = [[1,1],[2,2],[3,3]]
    s_or = copy.deepcopy(s)
    c = get_cost(s_or, bar_size)
    n_c = -1
    count = 0

    while n_c <= c:
        if count > 20000: break   
        count += 1
        s = permutation(s, bar_size)
        n_c = get_cost(s, bar_size) 

    
def permutation(s, bar_size):
    uni = lambda s: int(uniform(0, len(s)))
        
    b1 = uni(s)
    p1 = uni(s[b1])
    
    b2 = uni(s)
    p2 = uni(s[b2])

    

    if (sum(s[b1]) - s[b1][p1] + s[b2][p2]) <= bar_size and (sum(s[b2]) - s[b2][p2] + s[b1][p1]) <= bar_size:
        aux = s[b1][p1]
        s[b1][p1] = s[b2][p2]
        s[b2][p2] = aux


    return s        

def valid_permutation(b1, p1, b2, p2):
    pass

def get_cost(solution: list, limit: int) -> int:
    sums = [sum(s) for s in solution]
    rest = 0
    for i in sums:
        rest += (limit- i)
    return  rest

def main():
    pass


if __name__ == '__main__':
    shuffle_solution()