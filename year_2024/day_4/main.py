import os
from enum import Enum, auto
from typing import Tuple, List

script_dir = os.path.dirname(os.path.abspath(__file__))
relative_path = "input.txt"
file_path = os.path.join(script_dir, relative_path)

#   x    m    a    s
# 0 -> 1 -> 2 -> 3 -> 4

# + -> y
# |
# v x

class Direction(Enum):
    HORIZONTAL = auto()
    VERTICAL = auto()
    DIAGONAL_RIGHT = auto()
    DIAGONAL_LEFT = auto()

class Flow(Enum):
    NORMAL = auto()
    REVERSED = auto()

TRANSITIONS = {
    Flow.NORMAL: {
        0: {
            'X': 1
        },
        1: {
            'M': 2
        },
        2: {
            'A': 3
        },
        3: {
            'S': 4
        }
    },
    Flow.REVERSED: {
        0: {
            'S': 1
        },
        1: {
            'A': 2
        },
        2: {
            'M': 3
        },
        3: {
            'X': 4
        }
    }
}

class XmasStateMachine():
    def __init__(self, start: Tuple[int, int], direction: Direction, flow: Flow):
        self.state = 0
        self.start_position = start
        self.position = start
        self.direction = direction
        self.flow = flow
        self.transitions = TRANSITIONS[flow]

    def process(self, input: str, position: Tuple[int, int]):
        if self.state < 0 or self.is_match():
            return
        
        position_diff = tuple(map(lambda x: x[0] - x[1], zip(position, self.position)))

        if self.state == 0 and position_diff == (0,0) or self.direction == Direction.HORIZONTAL and position_diff == (0,1) or self.direction == Direction.VERTICAL and position_diff == (1,0) or self.direction == Direction.DIAGONAL_LEFT and position_diff == (1,1) or self.direction == Direction.DIAGONAL_RIGHT and position_diff == (1,-1):
            next_state = self.transitions[self.state].get(input)
            self.state, self.position = (next_state, position) if next_state is not None else (-1, self.position)

    def is_match(self):
        return self.state == 4
    
    def is_stuck(self):
        return self.state == -1


def part1():
    res = 0
    states: List[XmasStateMachine] = []

    with open(file_path, 'r') as f:
        l_nr = 0
        for line in f:
            input = line.strip()

            states.extend([XmasStateMachine((l_nr, y), direction, flow) for flow in Flow for direction in Direction for y in range(len(input))])

            for letter_position, letter in enumerate(input):
                for state in states:
                    state.process(letter, (l_nr, letter_position))

            res += sum(1 for state in states if state.is_match())
            states = [state for state in states if not state.is_stuck() and not state.is_match()]
            l_nr += 1

    return res

def part2():
    res = 0

    with open(file_path, 'r') as f:
        line_x_minus_2 = ''
        line_x_minus_1 = ''
        for l_nr, line in enumerate(f):
            input = line.strip()

            if l_nr >= 2:
                for y in range(len(line_x_minus_1) - 2):
                    if line_x_minus_1[y + 1] == 'A' and (line_x_minus_2[y] == 'M' and line[y + 2] == 'S' or line_x_minus_2[y] == 'S' and line[y + 2] == 'M') and (line_x_minus_2[y + 2] == 'M' and line[y] == 'S' or line_x_minus_2[y + 2] == 'S' and line[y] == 'M'):
                        res += 1
            
            line_x_minus_2 = line_x_minus_1
            line_x_minus_1 = input

    return res


def main():
    return part1(), part2()

if __name__ == '__main__':
    print(main())