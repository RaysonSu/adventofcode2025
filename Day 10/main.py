import os
from collections import *
from functools import *
from itertools import *
from math import *
from random import *
from typing import *

def main_part_1(inp: Sequence[str]) -> int:
    total = 0
    for line in inp:
        light_diagram, *wiring_schematics, _ = line.split(" ")

        final_state = 0
        for light in light_diagram[1:-1][::-1]:
            final_state <<= 1

            if light == "#":
                final_state += 1
        
        vectors = []
        for schematic in wiring_schematics:
            vector = 0
            
            for connection in schematic[1:-1].split(","):
                vector += 1 << int(connection)
            vectors.append(vector)
        
        num_vectors = len(vectors)
        res = -1
        for amt in range(num_vectors + 1):
            for used in combinations(range(num_vectors), amt):
                state = 0
                for vec in used:
                    state ^= vectors[vec]
                
                if state == final_state:
                    res = amt
                    break

            if res != -1:
                break
        
        total += res

    return total

def gaussian_elimination(matrix: list[list[float]]) -> None:
    m, n = len(matrix), len(matrix[0])
    h, k = 0, 0
    while h < m and k < n:
        _, i_max = max((abs(matrix[i][k]), i) for i in range(h, m))
        if abs(matrix[i_max][k]) < 1e-8:
            k += 1
            continue
        
        matrix[h], matrix[i_max] = matrix[i_max], matrix[h]
        for i in range(h + 1, m):
            f = matrix[i][k] / matrix[h][k]
            matrix[i][k] = 0.0
            
            for j in range(k + 1, n):
                matrix[i][j] -= f * matrix[h][j]
        
        h += 1
        k += 1

def fix_columns(matrix: list[list[float]]) -> None:
    m, n = len(matrix), len(matrix[0])
    pops = []
    for h in range(m):
        i = 0
        for i in range(n - 1):
            if abs(matrix[h][i]) > 1e-8:
                break
        else:
            pops.append(h)
            continue

        for j in range(m):
            matrix[j][i], matrix[j][h] = matrix[j][h], matrix[j][i]
    
    for row in pops[::-1]:
        matrix.pop(row)

def back_subsitute(matrix: list[list[float]]) -> None:
    m, n = len(matrix), len(matrix[0])
    
    for h in range(m):
        d = matrix[h][h]
        for i in range(n):
            matrix[h][i] /= d
        
        for j in range(h):
            f = matrix[j][h]

            for i in range(n):
                matrix[j][i] -= f * matrix[h][i]

def gauss_jordan_elimination(matrix: list[list[float]]) -> None:
    gaussian_elimination(matrix)
    fix_columns(matrix)
    back_subsitute(matrix)

def create_matrix(buttons: list[tuple[int, ...]], joltages: list[int]) -> list[list[float]]:
    size = len(joltages)
    button_count = len(buttons)

    equalities = [[0.0 for _ in range(button_count + 1)] for _ in range(size)]

    for button_index, button in enumerate(buttons):
        for light in button:
            equalities[light][button_index] += 1
    
    for light, joltage in enumerate(joltages):
        equalities[light][-1] = joltage

    return equalities

def display_matrix(matrix: list[list[float]]) -> None:
    for row in matrix:
        for value in row[:-1]:
            print(f"{value:7.2f}", end=" ")
        
        print(f"| {row[-1]:7.2f}")

def display_imatrix(imatrix: list[list[int]]) -> None:
    for row in imatrix:
        for value in row[:-1]:
            print(f"{value:>7}", end=" ")
        
        print(f"| {row[-1]:>7}")

def solve(buttons: list[tuple[int, ...]], joltages: list[int]) -> int:
    matrix = create_matrix(buttons, joltages)

    gauss_jordan_elimination(matrix)
    # display_matrix(matrix)

    matrix_size = len(matrix)
    matrix = [row[matrix_size:] for row in matrix]
    guess_variables = len(matrix[0]) - 1

    max_jolt = max(joltages)
    scale = lcm(*range(1, 12))
    
    imatrix = [
        [round(value * scale) for value in row]
        for row in matrix
    ]

    result = 10000000000
    for guess in product(range(max_jolt + 1), repeat=guess_variables):
        fixed_variables = [
            values[-1] - sum(x * y for x, y in zip(values[:-1], guess))
            for values in imatrix
        ]

        if any(variable < 0 or variable % scale != 0
                for variable in fixed_variables):
            continue

        fixed_variables = [
            variable // scale for variable in fixed_variables
        ]
        
        result = min(result, round(sum(chain(guess, fixed_variables))))

    return result

def main_part_2(inp: Sequence[str]) -> int:
    total = 0
    for line in inp:
        _, *wiring_schematics, joltages_raw = line.split(" ")

        buttons = []
        for schematic in wiring_schematics:
            buttons.append(list(map(int, schematic[1:-1].split(","))))
        
        joltages = list(map(int, joltages_raw[1:-1].split(",")))

        total += solve(buttons, joltages)

    return total

def main() -> None:
    test_input = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""
    test_input_parsed = test_input.splitlines()
    test_output_part_1_expected = 7
    test_output_part_2_expected = 33

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
