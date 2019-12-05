import re
from collections import Counter
lower = 138241
upper = 674034


def part1(lower=lower, upper=upper):
    matches = []
    for n in range(lower, upper+1):
        n = str(n)
        if list(n) == sorted(list(n)):
            if re.search(r"(\d)\1", n):
                matches.append(n)
    print(len(matches))
    return matches

def part2(matches):
    # This may be a faster way to do part1 as well...
    filtered = []
    for match in matches:
        if 2 in Counter(list(match)).values():
            filtered.append(match)
    print(len(filtered))
    return filtered
