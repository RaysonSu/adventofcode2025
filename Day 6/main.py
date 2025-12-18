import os
from collections import *
from functools import *
from itertools import *
from math import *
from typing import *

def main_part_1(inp: Sequence[str]) -> int:
    values: list[list[int]] = []
    
    for row in inp[:-1]:
        values.append([])
        for number in row.split(" "):
            if not number:
                continue

            values[-1].append(int(number))
    
    operations: list[str] = []
    for operation in inp[-1].split(" "):
        if not operation:
            continue

        operations.append(operation)

    total = 0
    for operation, *numbers in zip(operations, *values):
        if operation == "*":
            total += reduce(lambda x, y: x * y, numbers)
        else:
            total += reduce(lambda x, y: x + y, numbers)

    return total

def main_part_2(inp: Sequence[str]) -> int:
    total = 0

    values: list[int] = []
    for row in list(zip(*inp))[::-1]:
        string = "".join(char for char in row[:-1] if char != " ")
        if string == "":
            values = []
            continue

        values.append(int(string))

        if row[-1] == "*":
            total += reduce(lambda x, y: x * y, values)
        elif row[-1] == "+":
            total += reduce(lambda x, y: x + y, values)
    
    return total

def main() -> None:
    test_input = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """
    test_input_parsed = test_input.splitlines()
    test_output_part_1_expected = 4277556
    test_output_part_2_expected = 3263827

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
