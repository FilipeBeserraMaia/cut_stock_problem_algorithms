def read_instances(path):
    with open(path ,'r') as f:
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


def get_cost(solution: list, limitt: int) -> tuple:
    sums = []
    for bar in solution:
        rest = limitt - sum(bar)
        if bar and (rest > 0):
            sums.append(rest)

    return len(solution), sum(sums)

