#!/bin/pyton3
nums = []
answer = None
with open('1_input.txt',mode='r') as f:
   nums = [int(line.rstrip()) for line in f] 

for i in nums:
    for j in nums:
        if i + j == 2020:
            answer = i * j
            break
    if answer != None:
        break
print(str(answer))