#!/bin/python3
import os
filename = os.path.basename(__file__).replace('.py', '_input.txt')
filepath = os.path.join(os.path.dirname(__file__), filename)


def get_input(file):
    with open(file, mode='r') as f:
        nums = [int(line.rstrip()) for line in f]
    return nums


def part_two(nums):
    for i in nums:
        for j in nums:
            for k in nums:
                if i + j + k == 2020:
                    return i * j * k
    return -1


def part_one(nums):
    for i in nums:
        for j in nums:
            if i + j == 2020:
                return i * j
    return -1


values = get_input(filepath)

print("Part 1:" + str(part_one(values)))
print("Part 2:" + str(part_two(values)))
