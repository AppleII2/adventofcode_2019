import re
lower = 138241
upper = 674034


def part1(lower, upper):
    matches = []
    for n in range(lower, upper+1):
        n = str(n)
        if list(n) == sorted(list(n)):
            if re.search(r"(\d)\1", n):
                matches.append(n)
    print(len(matches))
    return matches
