import os
from collections import defaultdict
from operator import sub, add

script_dir = os.path.dirname(os.path.abspath(__file__))
relative_path = "input.txt"
file_path = os.path.join(script_dir, relative_path)


def is_within_map(point, map_size) -> bool:
    x, y = point

    return x >= 0 and x < map_size and y >= 0 and y < map_size

def debug(antinode_locations, antenna_locations, map_size):
    for x in range(map_size):
        for y in range(map_size):
            if (x, y) in antinode_locations:
                print('#', end='')
            elif (x, y) in antenna_locations:
                print('A', end='')
            else:
                print('.', end='')

        print()

def part_1():
    with open(file_path, 'r') as f:
        map_size = -1
        antennas = defaultdict(list)
        antenna_locations = set()
        antinode_locations = set()
        
        for x, l in enumerate(f):
            line = l.strip()
            
            if map_size < 0:
                map_size = len(line)

            for y, antenna_id in enumerate(line):
                if antenna_id == '.':
                    continue
                
                location = (x, y)
                antennas[antenna_id].append(location)
                antenna_locations.add(location)

        for antenna_id, locations in antennas.items():
            for i, l1 in enumerate(locations):
                for l2 in locations[i + 1:]:
                    direction = tuple(map(sub, l2, l1))

                    antinode = tuple(map(add, l2, direction))
                    if is_within_map(antinode, map_size):
                        antinode_locations.add(antinode)
                    
                    antinode = tuple(map(sub, l1, direction))
                    if is_within_map(antinode, map_size):
                        antinode_locations.add(antinode)

    return len(antinode_locations)


def part_2():
    with open(file_path, 'r') as f:
        map_size = -1
        antennas = defaultdict(list)
        antenna_locations = set()
        antinode_locations = set()
        
        for x, l in enumerate(f):
            line = l.strip()
            
            if map_size < 0:
                map_size = len(line)

            for y, antenna_id in enumerate(line):
                if antenna_id == '.':
                    continue
                
                location = (x, y)
                antennas[antenna_id].append(location)
                antenna_locations.add(location)

        for antenna_id, locations in antennas.items():
            for i, l1 in enumerate(locations):
                for l2 in locations[i + 1:]:
                    direction = tuple(map(sub, l2, l1))

                    # Antennas themselves are antinodes
                    antinode = l2
                    while is_within_map(antinode, map_size):
                        antinode_locations.add(antinode)
                        antinode = tuple(map(add, antinode, direction))

                    antinode = l1
                    while is_within_map(antinode, map_size):
                        antinode_locations.add(antinode)
                        antinode = tuple(map(sub, antinode, direction))

    return len(antinode_locations)


def main():
    return part_1(), part_2()


if __name__ == '__main__':
    print(main())