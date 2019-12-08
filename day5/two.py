import csv
from common.IntCode import IntCode

with open('in.txt') as input_file:
    data = next(csv.reader(input_file))
    print(IntCode(1, data, 0).exec(5, 0))
