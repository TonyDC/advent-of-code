import os

script_dir = os.path.dirname(os.path.abspath(__file__))
relative_path = "input.txt"
file_path = os.path.join(script_dir, relative_path)

def is_valid(deltas):
    return (all(d > 0 for d in deltas) or all(d < 0 for d in deltas)) and all(1 <= abs(d) <= 3 for d in deltas)

def part1():
    safe = 0
    with open(file_path, 'r') as f:
        for line in f:
            levels = [int(level) for level in line.strip().split(' ')]
            adjacent_levels = [(a, b) for a, b in zip(levels, levels[1:])]

            if (all(l2 > l1 for l1, l2, in adjacent_levels) or all(l2 < l1 for l1, l2, in adjacent_levels)) and all(1 <= abs(l1 - l2) <= 3 for l1, l2 in adjacent_levels):
                safe += 1

    return safe

def part2():
    safe = 0

    with open(file_path, 'r') as f:
        for line in f:
            levels = [int(level) for level in line.strip().split(' ')]
            adjacent_levels = [(a, b) for a, b in zip(levels, levels[1:])]
            deltas = [l2 - l1 for l1, l2 in adjacent_levels]

            if is_valid(deltas):
                safe += 1
            else:
                if is_valid(deltas[1:]) or is_valid(deltas[:-1]):
                    safe += 1
                else:
                    for n in range(len(deltas) - 1):
                        if is_valid(deltas[:n] + [sum(deltas[n:n + 2])] + deltas[n + 2:]):
                            safe += 1
                            break

    return safe


def main():
    return part1(), part2()

if __name__ == '__main__':
    print(main())