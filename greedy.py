from math import ceil
from random import uniform

def greddy(size_base, cut_list):
    amt_bars = 1
    size = size_base
    cut_list = reversed(cut_list)
    for cut in cut_list:
        if cut <= size:
            size -= cut
        else:
            amt_bars += 1
            size = size_base - cut
    return amt_bars

def main():
    list_bars = [9,2]
    size_base = 10

    print(sum(list_bars)/size_base)
   
    print(greddy(size_base, list_bars))

if __name__ == '__main__':
    main()