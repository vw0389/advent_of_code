#!/bin/python3
import os
filename = os.path.basename(__file__).replace('.py', '_input.txt')
filepath = os.path.join(os.path.dirname(__file__), filename)


def get_input(file):
    with open(file, mode='r') as f:
        text = [line.rstrip() for line in f]
    text.append('')
    return text


def part_one(lines):
    answer = 0
    alphabet = set()
    for line in lines:
        if line == '':
            answer = answer + len(alphabet)
            alphabet.clear()
        else:
            for char in line:
                alphabet.add(char)
    return answer


def part_two(lines):
    answer = 0
    alphabet = set()
    for line in lines:
        if line == '':
            answer = answer + len(alphabet)
            alphabet.clear()
        else:
            if len(alphabet) == 0:
                for char in line:
                    alphabet.add(char)
            else:
                ghost = set()
                for char in line:
                    ghost.add(char)
                alphabet = alphabet.intersection(ghost)

    return answer


text = get_input(filepath)

print("Part 1:", str(part_one(text)))
print("Part 2:", str(part_two(text)))
