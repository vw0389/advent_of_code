#!/bin/python3
import os
filename = os.path.basename(__file__).replace('.py', '_input.txt')
filepath = os.path.join(os.path.dirname(__file__), filename)


def get_input(file):
    with open(file, mode='r') as f:
        input_lines = [line.rstrip() for line in f]
    return input_lines


def part_one(terrain):
    answer = 0
    column = 0
    for y in range(vertical):
        if terrain[y][column] == tree:
            answer = answer + 1
        column = (column + 3) % horizontal
    return answer


def part_two(terrain):
    answer = 1
    column = 0
    for increment in increments:
        hit = 0
        column = 0
        right = increment[0]
        down = increment[1]
        for y in range(0, vertical, down):
            if terrain[y][column] == tree:
                hit = hit + 1
            column = (column + right) % horizontal
        answer = answer * hit
    return answer


lines = get_input(filepath)
tree = '#'
vertical = len(lines)
horizontal = len(lines[0])
increments = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
print("Part 1:", str(part_one(lines)))
print("Part 2:", str(part_two(lines)))
