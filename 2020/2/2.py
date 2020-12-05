#!/bin/python3
import os
filename = os.path.join(os.path.dirname(__file__), '2_input.txt')
passwords = []
answer1, answer2 = 0, 0
with open(filename,mode='r') as f:
   passwords = [line.rstrip() for line in f]
for i in passwords:
    things = i.split(' ')
    letter  = things[1].rstrip(':')
    password = things[2]
    things = things[0].split('-')
    min = int(things[0])
    max = int(things[1])

    count = password.count(letter)
    if count <=  max and count >= min:
        answer1 = answer1 + 1
    minB, maxB = False, False
    if password[min-1] == letter:
        minB = True 
    if password[max-1] == letter:
        maxB = True
    if minB == maxB:
        continue
    else:
        answer2 = answer2 + 1
print(str(answer1))
print(str(answer2))