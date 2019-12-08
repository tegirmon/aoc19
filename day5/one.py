import csv
from common.IntCode import IntCode

with open('in.txt') as input_file:
    data = next(csv.reader(input_file))
    incode = IntCode(1, data, 0)
    output = 0
    while output != -1:
        output = incode.exec(1, 0)
        print(output)
