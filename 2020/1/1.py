#!/bin/pyton3
import os
filename = os.path.join(os.path.dirname(__file__), '1_input.txt')

nums = []
answer1 = answer2 = None
with open(filename,mode='r') as f:
   nums = [int(line.rstrip()) for line in f] 

for i in nums:
    for j in nums:
        if i + j == 2020:
            answer1 = i * j
            break
    if answer1 != None:
        break
for i in nums:
    for j in nums:
        for k in nums:
            if i + j + k == 2020:
                answer2 = i * j * k
                break
    if answer2 != None: 
        break
print("Part 1: " + str(answer1))
print("Part 2: " + str(answer2))