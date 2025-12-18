import os
from collections import *
from functools import *
from itertools import *
from math import *
from typing import *

def discretise(values: list[int]) -> list[int]:
    values = sorted(set(values))
    
    ret = [0]
    for value, next_value in zip(values, values[1:]):
        ret.append(value)
        if value != next_value:
            ret.append(value + 1)
    
    ret.append(values[-1])
    return ret

def binary_search(values: list[int], target: int) -> int:
    low = 0
    high = len(values) - 1
    
    while low != high:
        mid = (low + high) // 2
        
        if values[mid] > target:
            high = mid - 1
        elif values[mid] == target:
            return mid
        else:
            low = mid + 1
    
    return low

def main_part_1(inp: Sequence[str]) -> int:
    red_tiles = [
        list(map(int, row.split(",")))
        for row in inp
        if row
    ]

    size = len(red_tiles)
    
    largest = 0
    for i, j in combinations(range(size), 2):
        x1, y1 = red_tiles[i]
        x2, y2 = red_tiles[j]
        area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)

        largest = max(largest, area)
    
    return largest

def main_part_2(inp: Sequence[str]) -> int:
    red_tiles = [
        list(map(int, row.split(",")))
        for row in inp
        if row
    ]

    size = len(red_tiles)

    x_values = discretise([x for x, _ in red_tiles])
    y_values = discretise([y for _, y in red_tiles])

    grid = [[0 for _ in x_values] for _ in y_values]
    for (x1, y1), (x2, y2) in zip(red_tiles, chain(red_tiles[1:], [red_tiles[0]])):
        rx1 = binary_search(x_values, x1)
        ry1 = binary_search(y_values, y1)
        rx2 = binary_search(x_values, x2)
        ry2 = binary_search(y_values, y2)

        lx, hx = min(rx1, rx2), max(rx1, rx2)
        ly, hy = min(ry1, ry2), max(ry1, ry2)

        for xi, yi in product(range(lx, hx + 1), range(ly, hy + 1)):
            grid[yi][xi] = 1
    
    for row in grid:
        cur = 0
        for index, value in enumerate(row):
            if value == 1:
                cur = 1 - cur
            else:
                row[index] = cur
    
    partial_sum = [[0 for _ in x_values] for _ in y_values]

    for yi, xi in product(range(1, len(y_values)), range(1, len(x_values))):
        partial_sum[yi][xi] += partial_sum[yi - 1][xi]
        partial_sum[yi][xi] += partial_sum[yi][xi - 1]
        partial_sum[yi][xi] -= partial_sum[yi - 1][xi - 1]
        partial_sum[yi][xi] += grid[yi][xi]
    
    largest = 0
    for i, j in combinations(range(size), 2):
        x1, y1 = red_tiles[i]
        x2, y2 = red_tiles[j]
        area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)

        lx, hx = min(x1, x2), max(x1, x2)
        ly, hy = min(y1, y2), max(y1, y2)

        lxi = binary_search(x_values, lx) - 1
        hxi = binary_search(x_values, hx)
        lyi = binary_search(y_values, ly) - 1
        hyi = binary_search(y_values, hy)
        fake_area = abs(hxi - lxi) * abs(hyi - lyi)

        points = 0
        points += partial_sum[hyi][hxi]
        points += partial_sum[lyi][lxi]
        points -= partial_sum[hyi][lxi]
        points -= partial_sum[lyi][hxi]

        if points == fake_area:
            largest = max(largest, area)
    
    return largest

def main() -> None:
    test_input = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""
    test_input_parsed = test_input.splitlines()
    test_output_part_1_expected = 50
    test_output_part_2_expected = 24

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
