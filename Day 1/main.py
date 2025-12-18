import os
from collections import *
from functools import *
from itertools import *
from math import *
from typing import *


def main_part_1(inp: Sequence[str]) -> int:
    position = 50
    password = 0

    for line in inp:
        movement = int(line[1:])

        if line[0] == "L":
            movement *= -1
        
        position += movement
        if position % 100 == 0:
            password += 1
    
    return password

def main_part_2(inp: Sequence[str]) -> int:
    position = 50
    password = 0

    for line in inp:
        movement = int(line[1:])

        if line[0] == "L":
            movement *= -1
        
        new_position = position + movement
        
        password += abs(new_position // 100 - position // 100)
        if new_position < position:
            if position % 100 == 0:
                password -= 1
            
            if new_position % 100 == 0:
                password += 1
        
        position = new_position
    
    return password

def main() -> None:
    test_input: str = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""
    test_input_parsed = test_input.splitlines()
    test_output_part_1_expected = 3
    test_output_part_2_expected = 6

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
