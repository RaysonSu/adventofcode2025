import os
from collections import *
from functools import *
from itertools import *
from math import *
from random import *
from typing import *

def main_part_1(inp: Sequence[str]) -> int:
    graph = {row[:3]: [] for row in inp}
    graph["out"] = []

    for row in inp:
        source, *dests = row.replace(":", "").split()
        for dest in dests:
            graph[dest].append(source)

    @lru_cache
    def solve(node: str) -> int:
        if node == "you":
            return 1
        
        return sum(solve(source) for source in graph[node])

    return solve("out")

def main_part_2(inp: Sequence[str]) -> int:
    graph = {row[:3]: [] for row in inp}
    graph["out"] = []

    for row in inp:
        source, *dests = row.replace(":", "").split()
        for dest in dests:
            graph[dest].append(source)

    @lru_cache
    def solve(node: str, goal: str) -> int:
        if node == goal:
            return 1
        
        return sum(solve(source, goal) for source in graph[node])

    ret = 0
    ret += solve("dac", "svr") * solve("fft", "dac") * solve("out", "fft")
    ret += solve("fft", "svr") * solve("dac", "fft") * solve("out", "dac")
    # print(solve("out", "svr"))

    return ret

def main() -> None:
    test_input_1 = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out"""

    test_input_2 = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out"""
    test_input_1_parsed = test_input_1.splitlines()
    test_input_2_parsed = test_input_2.splitlines()
    test_output_part_1_expected = 5
    test_output_part_2_expected = 2

    file_location = os.path.dirname(os.path.realpath(__file__))
    file_location = file_location + "/input.txt"
    with open(file_location, "r") as file:
        input_file = file.read().splitlines()

    test_output_part_1 = main_part_1(test_input_1_parsed)
    test_output_part_2 = main_part_2(test_input_2_parsed)

    if test_output_part_1_expected != test_output_part_1:
        print(f"Part 1 testing error: ")
        print(f"Test input: {test_input_1}")
        print(f"Expected output: {test_output_part_1_expected}")
        print(f"Got: {test_output_part_1}")
        print()

    if test_output_part_2_expected != test_output_part_2:
        print(f"Part 2 testing error: ")
        print(f"Test input: {test_input_2}")
        print(f"Expected output: {test_output_part_2_expected}")
        print(f"Got: {test_output_part_2}")
        print()

    if test_output_part_1_expected == test_output_part_1:
        print(f"Part 1: {main_part_1(input_file)}")
    
    if test_output_part_2_expected == test_output_part_2:
        print(f"Part 2: {main_part_2(input_file)}")


if __name__ == "__main__":
    main()
