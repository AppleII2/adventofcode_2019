with open('03-input', 'r') as raw:
    w1, w2 = raw.readlines()
    w1, w2 = w1.strip().split(','), w2.strip().split(',')

def directions_to_coords(wire):
    """Converts directions into set of integer coordinates wire crosses"""
    breadcrumbs = set()
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
        breadcrumbs.update(gen_intermediate(current_pos, next_pos))
        current_pos = next_pos
    return breadcrumbs

def gen_intermediate(start,finish):
    t = int(start[0] == finish[0])
    lbound, ubound = sorted([start[t], finish[t]])
    ubound += 1
    if t == 1:
        coords = [(start[0], i) for i in range(lbound, ubound)]
    else:
        coords = [(i, start[1]) for i in range(lbound, ubound)]
    return coords, len(coords-1)

def part1():
    s1, s2 = directions_to_coords(w1), directions_to_coords(w2)
    common = s1.intersection(s2)
    common.remove((0,0))
    distances = [sum([abs(x) for x in i]) for i in common]
    print("Shortest Manhattan distance:", min(distances))
    return common
    
