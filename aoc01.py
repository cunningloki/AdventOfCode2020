#Advent of Code 2020 - Day 2 - solution

import itertools

#Solution for part 1

for (a,b) in itertools.combinations([int(n) for n in open('aoc01.txt')], 2):
    if a+b == 2020:
        print(a*b)

#Solution for part 2
for (a,b,c) in itertools.combinations([int(n) for n in open('aoc01.txt')], 3):
    if a+b+c == 2020:
        print(a*b*c)