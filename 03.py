with open('03-input', 'r') as raw:
    w1, w2 = raw.readlines()
    w1, w2 = w1.strip().split(','), w2.strip().split(',')

def directions_to_coords(wire):
    """Converts directions into set of integer coordinates wire crosses"""
    breadcrumbs = []
    current_pos = [0,0]
    for instruction in wire:
        mag, direct = int(instruction[1:]), instruction[:1]
        if direct == 'L':
            next_pos = [current_pos[0] - mag, current_pos[1]]
        elif direct == 'R':
            next_pos = [current_pos[0] + mag, current_pos[1]]
        elif direct == 'D':
            next_pos = [current_pos[0], current_pos[1] - mag]
        elif direct == 'U':
            next_pos = [current_pos[0], current_pos[1] + mag]
        breadcrumbs += gen_intermediate(current_pos, next_pos)
        current_pos = next_pos
    breadcrumbs += [tuple(next_pos)]
    return breadcrumbs

def gen_intermediate(start,finish):
    t = int(start[0] == finish[0])
    lbound, ubound = sorted([start[t], finish[t]])
    if start[t] > finish[t]:
        lbound += 1
        ubound += 1
    if t == 1:
        coords = [(start[0], i) for i in range(lbound, ubound)]
    else:
        coords = [(i, start[1]) for i in range(lbound, ubound)]
    if start[t] > finish[t]:
        coords = coords[::-1]
    return coords

def part1(w1=w1, w2=w2):
    s1, s2 = set(directions_to_coords(w1)), set(directions_to_coords(w2))
    common = s1.intersection(s2)
    common.remove((0,0))
    distances = [sum([abs(x) for x in i]) for i in common]
    print("Shortest Manhattan distance:", min(distances))
    return common

def part2(w1=w1, w2=w2):
    common = part1(w1, w2)
    a,b = directions_to_coords(w1), directions_to_coords(w2)
    steps = {}
    for pair in common:
        steps[pair] = 0
    for key in steps.keys():
        steps[key] = a.index(key) + b.index(key)
    min_value = min(steps.items(), key = lambda x: x[1])
    return min_value

