import math


sum_fuel = 0
with open('in.txt') as inp:
    for row in inp:
        sum_fuel += math.floor(int(row) / 3) - 2

print(sum_fuel)
