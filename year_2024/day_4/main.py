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

def part_1_state_machine():
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

def part_1():
    res = 0
    combinations = ['XMAS', 'SAMX']

    with open(file_path, 'r') as f:
        buffer = []
        for line in f:
            input_entry = line.strip()

            # Horizontal pattern
            for y in range(len(input_entry) - 3):
                if input_entry[y:y + 4] in combinations:
                    res += 1

            buffer.append(input_entry)

            if len(buffer) == 4:
                for y in range(len(input_entry)):
                    # Vertical pattern
                    if buffer[0][y] + buffer[1][y] + buffer[2][y] + buffer[3][y] in combinations:
                        res += 1
                    # Diagonal (\)
                    if y < len(input_entry) - 3 and buffer[0][y] + buffer[1][y + 1] + buffer[2][y + 2] + buffer[3][y + 3] in combinations:
                        res += 1
                    # Diagonal (/)
                    if y >= 3 and buffer[0][y] + buffer[1][y - 1] + buffer[2][y - 2] + buffer[3][y - 3] in combinations:
                        res += 1

                buffer = buffer[1:]

    return res

def part_2():
    res = 0
    combinations = ['MAS', 'SAM']

    with open(file_path, 'r') as f:
        buffer = []
        for line in f:
            input_entry = line.strip()

            buffer.append(input_entry)

            if len(buffer) >= 3:
                for y in range(len(input_entry) - 2):
                    # Cross (X)
                    if buffer[0][y] + buffer[1][y + 1] + buffer[2][y + 2] in combinations and buffer[0][y + 2] + buffer[1][y + 1] + buffer[2][y] in combinations:
                        res += 1
                buffer = buffer[1:]

    return res


def main():
    return part_1(), part_2()

if __name__ == '__main__':
    print(main())