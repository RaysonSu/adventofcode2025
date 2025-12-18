import os
from collections import *
from functools import *
from itertools import *
from math import *
from typing import *

def main_part_1(inp: Sequence[str]) -> int:
    count = [[0 for _ in inp[0]] for _ in inp]
    
    for y, row in enumerate(inp):
        for x, char in enumerate(row):
            if char == ".":
                continue
            
            count[y][x] -= 1
            for dx, dy in product((-1, 0, 1), repeat = 2):
                if 0 <= y + dy < len(inp) and 0 <= x + dx < len(inp[0]):
                    count[y + dy][x + dx] += 1

    total = 0
    for y, row in enumerate(inp):
        for x, char in enumerate(row):
            if char == ".":
                continue
            
            if count[y][x] < 4:
                total += 1
    
    return total

def main_part_2(inp: Sequence[str]) -> int:
    count = [[0 for _ in inp[0]] for _ in inp]
    
    for y, row in enumerate(inp):
        for x, char in enumerate(row):
            if char == ".":
                continue
            
            count[y][x] -= 1
            for dx, dy in product((-1, 0, 1), repeat = 2):
                if 0 <= y + dy < len(inp) and 0 <= x + dx < len(inp[0]):
                    count[y + dy][x + dx] += 1

    total = 0
    queue: deque[tuple[int, int]] = deque()
    for y, row in enumerate(inp):
        for x, char in enumerate(row):
            if char == ".":
                continue
            
            if count[y][x] < 4:
                queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        total += 1

        for dx, dy in product((-1, 0, 1), repeat = 2):
            if not (0 <= y + dy < len(inp) and 0 <= x + dx < len(inp[0])):
                continue

            count[y + dy][x + dx] -= 1
            if count[y + dy][x + dx] == 3 and inp[y + dy][x + dx] == "@":
                queue.append((x + dx, y + dy))
        
    
    return total

def main() -> None:
    test_input = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""
    test_input_parsed = test_input.splitlines()
    test_output_part_1_expected = 13
    test_output_part_2_expected = 43

    file_location = os.path.dirname(os.path.realpath(__file__))
    file_location = file_location + "/input.txt"
    with open(file_location, "r") as file:
        input_file = file.read().splitlines()

    test_output_part_1 = main_part_1(test_input_parsed)
    test_output_part_2 = main_part_2(test_input_parsed)

    if test_output_part_1_expected != test_output_part_1:
        print(f"Part 1 testing error: ")
        print(f"Test input: {test_input}")
        print(f"Expected output: {test_output_part_1_expected}")
        print(f"Got: {test_output_part_1}")
        print()

    if test_output_part_2_expected != test_output_part_2:
        print(f"Part 2 testing error: ")
        print(f"Test input: {test_input}")
        print(f"Expected output: {test_output_part_2_expected}")
        print(f"Got: {test_output_part_2}")
        print()

    if test_output_part_1_expected == test_output_part_1:
        print(f"Part 1: {main_part_1(input_file)}")
    
    if test_output_part_2_expected == test_output_part_2:
        print(f"Part 2: {main_part_2(input_file)}")


if __name__ == "__main__":
    main()
