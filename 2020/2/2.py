#!/bin/python3
import os
filename = os.path.basename(__file__).replace('.py', '_input.txt')
filepath = os.path.join(os.path.dirname(__file__), filename)

def get_input(file):
    with open(file, mode='r') as f:
        lines = [line.rstrip() for line in f]
    return lines


def part_one(lines):
    answer = 0
    for i in lines:
        things = i.split(' ')
        letter = things[1].rstrip(':')
        password = things[2]
        things = things[0].split('-')
        minimum = int(things[0])
        maximum = int(things[1])
        count = password.count(letter)
        if maximum >= count >= minimum:
            answer = answer + 1
    return answer


def part_two(lines):
    answer = 0
    for i in lines:
        things = i.split(' ')
        letter = things[1].rstrip(':')
        password = things[2]
        things = things[0].split('-')
        minimum = int(things[0])
        maximum = int(things[1])

        min_bool, max_bool = False, False
        if password[minimum - 1] == letter:
            min_bool = True
        if password[maximum - 1] == letter:
            max_bool = True
        if min_bool == max_bool:
            continue
        else:
            answer = answer + 1

    return answer


passwords = get_input(filepath)

print("Part 1:", str(part_one(passwords)))
print("Part 2:", str(part_two(passwords)))
