import re
import os
from collections import defaultdict

script_dir = os.path.dirname(os.path.abspath(__file__))
relative_path = "input.txt"
file_path = os.path.join(script_dir, relative_path)

def part1():
    pattern = re.compile(r"^(\d+)\s+(\d+)$")

    l, r = [], []
    with open(file_path, 'r') as f:
        for line in f:
            left, right = pattern.fullmatch(line.strip()).groups()
            l.append(int(left))
            r.append(int(right))

    l.sort()
    r.sort()

    return sum(max(a, b) - min(a, b) for a, b in zip(l, r, strict=True))


def part2():
    pattern = re.compile(r"^(\d+)\s+(\d+)$")

    l_occur, r_occur = defaultdict(lambda: 0), defaultdict(lambda: 0)
    with open(file_path, 'r') as f:
        for line in f:
            left, right = pattern.fullmatch(line.strip()).groups()
            l, r = int(left), int(right)
            l_occur[l] += 1
            r_occur[r] += 1

    return sum(k * r_occur[k] * v for k, v in l_occur.items())


def main():
    return part1(), part2()

if __name__ == '__main__':
    main()