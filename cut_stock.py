from math import ceil
from random import uniform


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


#salva a ordem e a barra que o index foi cortado
def save_cut(cut_list,bar_id,new_item):
    if not bar_id in cut_list.keys():
        cut_list[str(bar_id)] = []

    cut_list[str(bar_id)].append(new_item)

    return cut_list

    
def search_best_item(items=[], rest=0):
    """
    Search the largest 
    """

    best_index = list(filter(lambda x: x[1] <= rest, enumerate(items)))

    return best_index[0][0] if best_index else None


def main():
    list_bars = [9,2]
    size_base = 10

    print(sum(list_bars)/size_base)
   
    s0 = cut_stock(list_bars,size_base)

    print(s0)

if __name__ == '__main__':
    main()