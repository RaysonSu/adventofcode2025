import os
from collections import *
from functools import *
from itertools import *
from math import *
from typing import *

def main_part_1(inp: Sequence[str]) -> int:
    total = 0
    
    for interval in inp[0].split(","):
        lb, ub = map(int, interval.split("-"))
        for n in range(lb, ub + 1):
            t = 10
            while t * t < n:
                t *= 10
            
            if (n % (t + 1) == 0) and (n // (t + 1) * 10 >= t):
                total += n

            
    return total

def main_part_2(inp: Sequence[str]) -> int:
    total = 0
    
    for interval in inp[0].split(","):
        lb, ub = map(int, interval.split("-"))
        for n in range(lb, ub + 1):
            exp = 2
            while n > pow(10, exp - 1):
                t = 10
                while pow(t, exp) < n:
                    t *= 10
                
                div = (pow(t, exp) - 1) // (t - 1)

                if (n % div == 0) and (n // div * 10 >= t):
                    total += n
                    break
            
                exp += 1

            
    return total

def main() -> None:
    test_input: str = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""
    test_input_parsed = test_input.splitlines()
    test_output_part_1_expected = 1227775554
    test_output_part_2_expected = 4174379265

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
