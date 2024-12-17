import os
from typing import List

script_dir = os.path.dirname(os.path.abspath(__file__))
relative_path = "input.txt"
file_path = os.path.join(script_dir, relative_path)

def is_valid_part_1(total: int, values: List[int]) -> bool:
    if len(values) == 1:
        return total == values[0]
    
    last_value = values[-1]
    if total % last_value == 0 and is_valid_part_1(total // last_value, values[:-1]):
        return True
    if total - last_value >= 0 and is_valid_part_1(total - last_value, values[:-1]):
        return True
    
    return False

def is_valid_part_2(total: int, values: List[int]) -> bool:
    if len(values) == 1:
        return total == values[0]
    
    last_value = values[-1]
    if total % last_value == 0 and is_valid_part_2(total // last_value, values[:-1]):
        return True
    if total - last_value >= 0 and is_valid_part_2(total - last_value, values[:-1]):
        return True
    if str(total).endswith(str(last_value)) and len(str(total)[:-len(str(last_value))]) > 0 and is_valid_part_2(int(str(total)[:-len(str(last_value))]), values[:-1]):
        return True
    
    return False

def part_1():
    res = 0

    with open(file_path, 'r') as f:
        for l in f:
            line = l.strip()
            test_value, values = line.split(': ')

            if is_valid_part_1(int(test_value), list(map(int, values.split(' ')))):
                res += int(test_value)

    return res

def part_2():
    res = 0

    with open(file_path, 'r') as f:
        for l in f:
            line = l.strip()
            test_value, values = line.split(': ')

            if is_valid_part_2(int(test_value), list(map(int, values.split(' ')))):
                res += int(test_value)

    return res


def main():
    return part_1(), part_2()


if __name__ == '__main__':
    print(main())