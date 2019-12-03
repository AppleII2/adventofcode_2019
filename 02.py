from operator import add, mul
functions = {1:add, 2:mul}

# Part 1

program = []

with open('02-input', 'r') as raw:
    intcode = [int(x) for x in raw.readline().strip().split(',')]
def part1():
    intcode[1] = 12
    intcode[2] = 2
    return compute(intcode)

def compute(program):
    """Executes the intcode program
    >>> compute([1,0,0,0,99])
    [2,0,0,0,99]
    >>> compute([2,3,0,3,99])
    [2,3,0,6,99]
    >>> compute([2,4,4,5,99,0])
    [2,4,4,5,99,9801]
    >>> compute([1,1,1,4,99,5,6,0,99])
    [30,1,1,4,2,5,6,0,99]
    """
    while True:
        for i in range(0, len(program), 4):
            if program[i] == 99:
                return program[0]
            elif program[i] in functions.keys(): 
                function = functions[program[i]]
                o1, o2 = program[program[i+1]], program[program[i+2]]
                output = program[i+3]
                program[output] = function(o1, o2)
            else:
                raise ValueError("Unknown operator provided")

# Part 2

def bruteforce():
    for x in range(100):
        for y in range(100):
            program = intcode.copy()
            program[1] = x
            program[2] = y
            result = compute(program)
            if result == 19690720:
                return 100 * x + y

