import os
from collections import *
from functools import *
from itertools import *
from math import *
from typing import *

class DSU:
    def __init__(self, size: int) -> None:
        self.__par: list[int] = list(range(size))
        self.__size: list[int] = [1 for _ in range(size)]
        self.__regions: int = size

    @property
    def regions(self) -> int:
        return self.__regions

    def get_par(self, node: int) -> int:
        if self.__par[node] == node:
            return node

        par = self.get_par(self.__par[node])
        self.__par[node] = par
        return par

    def connect(self, node_1: int, node_2: int) -> None:
        node_1 = self.get_par(node_1)
        node_2 = self.get_par(node_2)

        if node_1 == node_2:
            return
        elif self.__size[node_1] < self.__size[node_2]:
            node_1, node_2 = node_2, node_1
        
        self.__par[node_2] = node_1
        self.__size[node_1] += self.__size[node_2]

        self.__regions -= 1
    
    def is_connected(self, node_1: int, node_2: int) -> bool:
        return self.get_par(node_1) == self.get_par(node_2)
    
    def get_region_sizes(self) -> list[int]:
        return [
            size 
            for index, (size, par) 
            in enumerate(zip(self.__size, self.__par))
            if index == par
        ]


def main_part_1(inp: Sequence[str], num: int = 1000) -> int:
    locations = [
        list(map(int, row.split(",")))
        for row in inp
        if row
    ]

    size = len(locations)
    
    distances = []
    for i, j in combinations(range(size), 2):
        x1, y1, z1 = locations[i]
        x2, y2, z2 = locations[j]
        dist = (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2

        distances.append((dist, i, j))
    
    distances.sort()
    dsu = DSU(size)

    for _, node_1, node_2 in distances[:num]:
        dsu.connect(node_1, node_2)
    
    sizes = dsu.get_region_sizes()
    sizes.sort(reverse=True)

    return sizes[0] * sizes[1] * sizes[2]

def main_part_2(inp: Sequence[str]) -> int:
    locations = [
        list(map(int, row.split(",")))
        for row in inp
        if row
    ]

    size = len(locations)
    
    distances = []
    for node_1, node_2 in combinations(range(size), 2):
        x1, y1, z1 = locations[node_1]
        x2, y2, z2 = locations[node_2]
        dist = (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2

        distances.append((dist, node_1, node_2))
    
    distances.sort()
    dsu = DSU(size)

    x1 = 0
    x2 = 0

    for _, node_1, node_2 in distances:
        dsu.connect(node_1, node_2)
    
        x1 = locations[node_1][0]
        x2 = locations[node_2][0]

        if dsu.regions == 1:
            break

    return x1 * x2




def main() -> None:
    test_input = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""
    test_input_parsed = test_input.splitlines()
    test_output_part_1_expected = 40
    test_output_part_2_expected = 25272

    file_location = os.path.dirname(os.path.realpath(__file__))
    file_location = file_location + "/input.txt"
    with open(file_location, "r") as file:
        input_file = file.read().splitlines()

    test_output_part_1 = main_part_1(test_input_parsed, 10)
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
