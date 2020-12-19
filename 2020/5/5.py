#!/bin/python3
import os
filename = os.path.basename(__file__).replace('.py', '_input.txt')
filepath = os.path.join(os.path.dirname(__file__), filename)


def get_input(file):
    with open(file, mode='r') as f:
        text = [line.rstrip() for line in f]
    return text


def part_one(text):
    values = []
    biggest = 0
    for line in text:
        row_line = line[:7]
        column_line = line[-3:]
        row_line = row_line.replace('F', '0')
        row_line = row_line.replace('B', '1')
        column_line = column_line.replace('L', '0')
        column_line = column_line.replace('R', '1')
        row = int(row_line, 2)
        column = int(column_line, 2)
        values.append(row * 8 + column)

    for value in values:
        if biggest < value:
            biggest = value

    return biggest


def part_two(text):
    values = []
    biggest = 0
    for line in text:
        row_line = line[:7]
        column_line = line[-3:]
        row_line = row_line.replace('F', '0')
        row_line = row_line.replace('B', '1')
        column_line = column_line.replace('L', '0')
        column_line = column_line.replace('R', '1')
        row = int(row_line, 2)
        column = int(column_line, 2)
        values.append(row * 8 + column)

    sorted_values = sorted(values)

    index = 0
    last_seat = len(sorted_values) - 1
    while index < last_seat - 1:
        if sorted_values[index] - sorted_values[index+1] == -2:
            return sorted_values[index]+1
        index = index + 1


lines = get_input(filepath)

print("Part 1:", str(part_one(lines)))
print("Part 2:", str(part_two(lines)))