import os
import re

script_dir = os.path.dirname(os.path.abspath(__file__))
relative_path = "input.txt"
file_path = os.path.join(script_dir, relative_path)

def part1():
    pattern = re.compile(r"mul\((\d+),(\d+)\)")
    res = 0

    with open(file_path, 'r') as f:
        for line in f:
            matches = [(int(l), int(r)) for l, r in pattern.findall(line.strip())]
            for l, r in matches:
                res += l * r

    return res

def part2():
    pattern = re.compile(r"(do)\(\)|(don't)\(\)|mul\((\d+),(\d+)\)")
    enable_mult = True
    res = 0

    with open(file_path, 'r') as f:
        for line in f:
            matches = [(True if enable == 'do' else None, True if disable == "don't" else None, int(l) if l != '' else None, int(r) if r != '' else None) for enable, disable, l, r in pattern.findall(line.strip())]
            for enable, disable, l, r in matches:
                if enable is True:
                    enable_mult = True
                elif disable is True:
                    enable_mult = False
                else:
                    res += l * r if enable_mult else 0

    return res


def main():
    return part1(), part2()

if __name__ == '__main__':
    print(main())