#!/bin/python3
import os

filename = os.path.basename(__file__).replace('.py', '_input.txt')
filepath = os.path.join(os.path.dirname(__file__), filename)


def get_input(file):
    with open(file, mode='r') as f:
        text = [line.rstrip() for line in f]
    text.append("")
    return text


def part_one(text):
    answer = 0
    field_to_value = {}
    for line in text:
        if line == '':
            if part_one_checker(field_to_value):
                answer = answer + 1
            field_to_value = {}
        else:
            things = line.split(' ')
            for thing in things:
                stuff = thing.split(':')
                field_to_value[stuff[0]] = stuff[1]
    return answer


def part_two(text):
    answer = 0
    field_to_value = {}
    for line in text:
        if line == '':
            if part_one_checker and part_two_checker(field_to_value):
                answer = answer + 1
            field_to_value = {}
        else:
            things = line.split(' ')
            for thing in things:
                stuff = thing.split(':')
                field_to_value[stuff[0]] = stuff[1]
    return answer


def part_one_checker(k_t_v):
    for field in fields:
        if field not in k_t_v:
            return False
    return True


def part_two_checker(k_t_v):
    if not part_one_checker(k_t_v):
        return False

    if not 1920 <= int(k_t_v.get('byr')) <= 2002:
        return False

    if not 2010 <= int(k_t_v.get('iyr')) <= 2020:
        return False

    if not 2020 <= int(k_t_v.get('eyr')) <= 2030:
        return False

    hgt = k_t_v.get('hgt')
    if 'in' in hgt and 'cm' in hgt:
        return False
    elif 'in' in hgt:
        hgt = hgt.rstrip('in')
        if not 59 <= int(hgt) <= 76:
            return False
    elif 'cm' in hgt:
        hgt = hgt.rstrip('cm')
        if not 150 <= int(hgt) <= 193:
            return False
    else:
        return False

    hcl = k_t_v.get('hcl')
    if not hcl[0] == '#':
        return False
    hcl = hcl.lstrip('#')
    if not len(hcl) == 6:
        return False
    try:
        int(hcl, 16)
    except ValueError:
        return False

    ecl = k_t_v.get('ecl')
    if ecl not in ecls:
        return False

    pid = k_t_v.get('pid')
    if not len(pid) == 9:
        return False
    try:
        int(pid, 10)
    except ValueError:
        return False
    return True


ecls = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
fields = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
lines = get_input(filepath)
print("Part 1:", str(part_one(lines)))
print("Part 2:", str(part_two(lines)))
