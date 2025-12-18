import os
from collections import *
from functools import *
from itertools import *
from math import *
from typing import *

def calc_bank(bank: str, batteries: int) -> int:
    solution = bank[:batteries]

    for battery in bank[batteries:]:
        options = solution + battery

        for rem in range(batteries + 1):
            solution = max(solution, options[:rem] + options[rem + 1:])

    return int(solution)

def main_part_1(inp: Sequence[str]) -> int:
    total = 0
    
    for bank in inp:
        total += calc_bank(bank, 2)
            
    return total

def main_part_2(inp: Sequence[str]) -> int:
    total = 0
    
    for bank in inp:
        total += calc_bank(bank, 12)
            
    return total

def main() -> None:
    test_input: str = """987654321111111
811111111111119
234234234234278
818181911112111"""
    test_input_parsed = test_input.splitlines()
    test_output_part_1_expected = 357
    test_output_part_2_expected = 3121910778619

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
