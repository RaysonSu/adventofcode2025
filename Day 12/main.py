import os
from collections import *
from functools import *
from itertools import *
from math import *
from random import *
from typing import *

def main_part_1(inp: Sequence[str]) -> int:
    values: list[int] = []
    tiles = inp.count("")
    for i in range(tiles):
        values.append("".join(inp[5 * i: 5 * i + 5]).count("#"))
    
    possible = 0
    for query in inp[5 * tiles:]:
        area_data, count_data = query.split(": ")
        w, h = map(int, area_data.split("x"))
        counts = list(map(int, count_data.split(" ")))

        area_req = sum(x * y for x, y in zip(counts, values))

        if (w // 3) * (h // 3) >= sum(counts):
            possible += 1
            continue
        
        if area_req > w * h:
            continue

        raise ValueError("oh crap!")

    return possible


def main() -> None:
    file_location = os.path.dirname(os.path.realpath(__file__))
    file_location = file_location + "/input.txt"
    with open(file_location, "r") as file:
        input_file = file.read().splitlines()

    print(f"Part 1: {main_part_1(input_file)}")


if __name__ == "__main__":
    main()
