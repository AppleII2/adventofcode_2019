from math import floor

# Part 1
def fuel_calc(filename='01-input'):
    with open(filename, 'r') as masses:
        return sum([floor(int(mass)/3) - 2 for mass in masses.readlines()])

# Part 2

def recursive_fuel(mass):
    req_fuel = floor(mass / 3) - 2
    if req_fuel <= 0:
        return 0
    else:
        return req_fuel + recursive_fuel(req_fuel)

def fuel_calc_with_recursion(filename='01-input'):
    with open(filename, 'r') as masses:
        return sum([recursive_fuel(int(mass)) for mass in masses.readlines()])
