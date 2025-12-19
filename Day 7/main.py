import os
from collections import *
from functools import *
from itertools import *
from math import *
from typing import *

def main_part_1(inp: Sequence[str]) -> int:
    width = len(inp[0])
    counts = [0 for _ in range(width)]
    counts[inp[0].index("S")] += 1

    total = 0
    for row in inp[1:]:
        new_counts = [0 for _ in range(width)]

        for index, char in enumerate(row):
            if char == ".":
                continue

            if counts[index] == 0:
                continue
            
            total += 1
            if index != 0:
                new_counts[index - 1] += counts[index]
            
            if index != width - 1:
                new_counts[index + 1] += counts[index]
            
            counts[index] = 0
        
        for index, count in enumerate(new_counts):
            counts[index] = min(1, count + counts[index])

    return total


def main_part_2(inp: Sequence[str]) -> int:
    width = len(inp[0])
    counts = [0 for _ in range(width)]
    counts[inp[0].index("S")] += 1

    for row in inp[1:]:
        new_counts = [0 for _ in range(width)]

        for index, char in enumerate(row):
            if char == ".":
                continue

            if index != 0:
                new_counts[index - 1] += counts[index]
            
            if index != width - 1:
                new_counts[index + 1] += counts[index]
            
            counts[index] = 0
        
        for index, count in enumerate(new_counts):
            counts[index] += count

    return sum(counts)

def main() -> None:
    test_input = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""
    test_input_parsed = test_input.splitlines()
    test_output_part_1_expected = 21
    test_output_part_2_expected = 40

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
