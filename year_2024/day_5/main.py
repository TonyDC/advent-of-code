import os
from enum import Enum, auto
from typing import Iterable
from collections import defaultdict
from enum import Enum, auto

script_dir = os.path.dirname(os.path.abspath(__file__))
relative_path = "input.txt"
file_path = os.path.join(script_dir, relative_path)

class ProcessingStep(Enum):
    INGEST_ORDERING_RULES = auto()
    INGEST_PAGE_UPDATES = auto()

def part_1():
    res = 0
    violation_rules = defaultdict(set)
    processing_step = ProcessingStep.INGEST_ORDERING_RULES

    with open(file_path, 'r') as f:
        for l in f:
            line = l.strip()
            if processing_step == ProcessingStep.INGEST_ORDERING_RULES:
                if line == '':
                    processing_step = ProcessingStep.INGEST_PAGE_UPDATES
                else:
                    left, right = tuple(map(int, line.split('|')))
                    violation_rules[right].add(left)
            elif processing_step == ProcessingStep.INGEST_PAGE_UPDATES:
                sequence = list(map(int, line.split(',')))
                violation_sets = [violation_rules[s] for s in sequence]

                violation_found = False

                for position in range(len(sequence)):
                    for sm_position in range(position):
                        if sequence[position] in violation_sets[sm_position]:
                            violation_found = True
                            break
                    
                    if violation_found:
                        break
                
                if not violation_found:
                    res += sequence[len(sequence) // 2]

    return res

def part_2():
    res = 0
    violations = defaultdict(set)
    processing_step = ProcessingStep.INGEST_ORDERING_RULES

    with open(file_path, 'r') as f:
        for l in f:
            line = l.strip()
            if processing_step == ProcessingStep.INGEST_ORDERING_RULES:
                if line == '':
                    processing_step = ProcessingStep.INGEST_PAGE_UPDATES
                else:
                    left, right = tuple(map(int, line.split('|')))
                    violations[right].add(left)
            elif processing_step == ProcessingStep.INGEST_PAGE_UPDATES:
                sequence = list(map(int, line.split(',')))
                states = [violations[s] for s in sequence]

                violation_found = False
 
                for position in range(len(sequence)):
                    for sm_index in range(position):
                        if sequence[position] in states[sm_index]:
                            violation_found = True

                            sequence[sm_index], sequence[position] = sequence[position], sequence[sm_index]
                            states[sm_index], states[position] = states[position], states[sm_index]

                if violation_found:
                    res += sequence[len(sequence) // 2]

    return res


def main():
    return part_1(), part_2()


if __name__ == '__main__':
    print(main())