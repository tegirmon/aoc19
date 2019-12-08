import csv
from common.IntCode import IntCode

with open('in.txt') as input_file:
    data = next(csv.reader(input_file))
    data[1] = 12
    data[2] = 2
    IntCode(1, data, 0).exec(0, 0)
    print(data[0])
