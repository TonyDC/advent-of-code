import os
from collections import defaultdict
from operator import sub, add

script_dir = os.path.dirname(os.path.abspath(__file__))
relative_path = "input.txt"
file_path = os.path.join(script_dir, relative_path)

def is_within_map(hiking_map, position) -> int:
    x, y = position

    return all([x >= 0, y >= 0, x < len(hiking_map), y < len(hiking_map)])

def score_map(hiking_map, visit_map, start_position) -> int:
    if not is_within_map(hiking_map, start_position):
        return 0

    x, y = start_position
    height = hiking_map[x][y]
    if height == 9:
        return 1
    
    res = 0
    for new_x, new_y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if is_within_map(hiking_map, (new_x, new_y)) and not visit_map[new_x][new_y] and hiking_map[new_x][new_y] - height == 1:
            visit_map[new_x][new_y] = True
            res += score_map(hiking_map, visit_map, (new_x, new_y))

    return res

def rate_map(hiking_map, start_position) -> int:
    if not is_within_map(hiking_map, start_position):
        return 0

    x, y = start_position
    height = hiking_map[x][y]
    if height == 9:
        return 1
    
    res = 0
    for new_x, new_y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if is_within_map(hiking_map, (new_x, new_y)) and hiking_map[new_x][new_y] - height == 1:
            res += rate_map(hiking_map, (new_x, new_y))

    return res


def part_1():
    res = 0

    with open(file_path, 'r') as f:
        hiking_map = [[int(p) for p in l.strip()] for l in f]

        for x, line in enumerate(hiking_map):
            for y, height in enumerate(line):
                if height == 0:
                    visit_map = [[False for _ in l] for l in hiking_map]
                    res += score_map(hiking_map, visit_map, (x, y))

    return res


def part_2():
    res = 0

    with open(file_path, 'r') as f:
        hiking_map = [[int(p) for p in l.strip()] for l in f]

        for x, line in enumerate(hiking_map):
            for y, height in enumerate(line):
                if height == 0:
                    res += rate_map(hiking_map, (x, y))

    return res


def main():
    return part_1(), part_2()


if __name__ == '__main__':
    print(main())

