#!/bin/python3
import os

filename = os.path.join(os.path.dirname(__file__), '4_input.txt')
with open(filename,mode='r') as f:
   text = [line.rstrip() for line in f]

records = []
answer1,answer2 = 0,0
# cid is optional therefore irrelevant
fields = ('byr:','iyr:','eyr:','hgt:','hcl:','ecl:','pid:')
found = [False]*7

for y in text:
    if y == '':
        valid = True
        for i in found:
            if i == False:
                valid = False
                break
        if valid:
            answer1 = answer1 +  1
        found = [False]*7
    for i in range(7):
        if fields[i] in y:
            found[i] = True

valid = True
for i in found:
    if i == False:
        valid = False
        break
if valid:
    answer1 = answer1 +  1

print(str(answer1))
print(str(answer2))