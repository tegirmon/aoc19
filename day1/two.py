import math


def fuel(weight):
    return math.floor(weight / 3) - 2


sum_fuel = 0
with open('in.txt') as inp:
    for row in inp:
        req_fuel = fuel(int(row))
        total_fuel = req_fuel
        while req_fuel > 0:
            req_fuel = fuel(req_fuel)
            if req_fuel > 0:
                total_fuel += req_fuel
        sum_fuel += total_fuel

print(sum_fuel)
