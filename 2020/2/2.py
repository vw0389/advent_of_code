#!/bin/python3
# Each line gives the password policy and then the password.
# The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid.
#  For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.
# In the above example, 2 passwords are valid. The middle password, cdefg, is not;
# it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

# How many passwords are valid according to their policies?
passwords = []
answer = 0
with open('2_input.txt',mode='r') as f:
   passwords = [line.rstrip() for line in f]
for i in passwords:
    things = i.split(' ')
    letter  = things[1].rstrip(':')
    password = things[2]
    things = things[0].split('-')
    min = int(things[0])
    max = int(things[1])

    number = password.count(letter)
    if number <=  max and number >= min:
        answer = answer + 1
print(str(answer))