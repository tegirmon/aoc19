import math

print(sum([math.floor(int(row) / 3) - 2 for row in open('in.txt')]))
