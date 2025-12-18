from __future__ import annotations

import os
from collections import *
from functools import *
from itertools import *
from math import *
from typing import *

class Ranges:  # stole this code from last year!
    def __init__(self, *ranges: tuple[int, int]) -> None:
        self.ranges: list[tuple[int, int]] = []
        for number_range in ranges:
            self.ranges.append(number_range)

        self.fix_everything()

    def __str__(self) -> str:
        return str(self.ranges)
    
    def __contains__(self, item: int) -> bool:
        for low, high in self.ranges:
            if low <= item <= high:
                return True
        
        return False

    def clean_up(self) -> None:
        while self.one_step_clean_up():
            pass

    def one_step_clean_up(self) -> bool:
        for range_index in range(len(self.ranges)):
            for other_range_index in range(range_index):
                new = self.combine(
                    self.ranges[range_index],
                    self.ranges[other_range_index]
                )
                if len(new) == 1:
                    self.ranges.pop(range_index)
                    self.ranges.pop(other_range_index)
                    self.ranges.append(new[0])
                    return True
        return False

    def remove_invalid_ranges(self) -> None:
        self.ranges = [
            number_range
            for number_range
            in self.ranges
            if number_range[1] >= number_range[0]
        ]

    def combine(self, interval_1: tuple[int, int], interval_2: tuple[int, int]) -> list[tuple[int, int]]:
        if interval_1[0] < interval_2[0]:
            if interval_1[1] < interval_2[0]:
                return [interval_1, interval_2]
            elif interval_2[1] <= interval_1[1]:
                return [interval_1]
            else:
                return [(interval_1[0], interval_2[1])]
        elif interval_1[0] == interval_2[0]:
            return [(interval_1[0], max(interval_1[1], interval_2[1]))]
        else:
            return self.combine(interval_2, interval_1)

    def sort(self) -> None:
        from functools import cmp_to_key

        def compare(left: tuple[int, int], right: tuple[int, int]):
            if right[1] <= left[0]:
                return 1
            else:
                return -1

        self.ranges.sort(key=cmp_to_key(compare))

    def fix_everything(self) -> None:
        self.remove_invalid_ranges()
        self.clean_up()
        self.sort()

    def length(self) -> int:
        return sum(upper - lower + 1 for lower, upper in self.ranges)

    def add(self, *ranges: Ranges | tuple[int, int]) -> None:
        for number_range in ranges:
            if isinstance(number_range, Ranges):
                for sub_interval in number_range.ranges:
                    self.ranges.append(sub_interval)
            elif isinstance(number_range, tuple):
                self.ranges.append(number_range)

        self.fix_everything()

    def remove(self, removal_interval: tuple[int, int]) -> Ranges:
        new_ranges: list[tuple[int, int]] = []
        removed_ranges: list[tuple[int, int]] = []
        for interval in self.ranges:
            if interval[1] <= removal_interval[1] and interval[0] >= removal_interval[0]:
                removed_ranges.append(interval)

            elif interval[1] > removal_interval[1] and interval[0] < removal_interval[0]:
                new_ranges.append((interval[0], removal_interval[0] - 1))
                new_ranges.append((removal_interval[1] + 1, interval[1]))
                removed_ranges.append(removal_interval)

            elif interval[1] <= removal_interval[1] and interval[1] >= removal_interval[0]:
                new_ranges.append((interval[0], removal_interval[0] - 1))
                removed_ranges.append((removal_interval[0], interval[1]))

            elif interval[0] >= removal_interval[0] and interval[0] <= removal_interval[1]:
                new_ranges.append((removal_interval[1] + 1, interval[1]))
                removed_ranges.append((interval[0], removal_interval[1]))

            else:
                new_ranges.append(interval)

        self.ranges = new_ranges

        ret: Ranges = Ranges()
        for interval in removed_ranges:
            ret.add(interval)

        return ret

    def shift(self, amount: int) -> None:
        new_ranges: list[tuple[int, int]] = []
        for start, end in self.ranges:
            new_ranges.append((start + amount, end + amount))
        self.ranges = new_ranges

def main_part_1(inp: Sequence[str]) -> int:
    line = 0
    
    ranges = Ranges()
    while inp[line] != "":
        low, high = map(int, inp[line].split("-"))
        ranges.add((low, high))
        
        line += 1
    
    line += 1
    total = 0
    while line < len(inp):
        if int(inp[line]) in ranges:
            total += 1
        line += 1

    return total

def main_part_2(inp: Sequence[str]) -> int:
    line = 0
    
    ranges = Ranges()
    while inp[line] != "":
        low, high = map(int, inp[line].split("-"))
        ranges.add((low, high))
        
        line += 1
    
    return ranges.length()

def main() -> None:
    test_input = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""
    test_input_parsed = test_input.splitlines()
    test_output_part_1_expected = 3
    test_output_part_2_expected = 14

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
