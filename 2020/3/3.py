#!/bin/python3
import os

filename = os.path.join(os.path.dirname(__file__), '3_input.txt')
with open(filename,mode='r') as f:
   terrain = [line.rstrip() for line in f]

tree = '#'
column = 0
answer1, answer2 = 0,0
vertical = len(terrain)
horizontal = len(terrain[0])

for y in range(vertical):
   if terrain[y][column] == tree:
      answer1 = answer1 + 1
   column = (column + 3) % horizontal

print(str(answer1))
increments = [[1,1],[3,1],[5,1],[7,1],[1,2]]
trees_hit = []
for increment in increments:
   hit = 0
   column = 0
   right = increment[0]
   down = increment[1]
   for y in vertical[::down]:
      if terrain[y][column] == tree:
         hit = hit + 1
      column = (column + right) % horizontal
   trees_hit.append(hit)
