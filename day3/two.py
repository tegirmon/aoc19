import csv
from common.Wire import Wire

with open('in.txt') as input_file:
    first_wire = Wire().walk(next(csv.reader(input_file)))
    second_wire = Wire().walk(next(csv.reader(input_file)))

print(min([int(first_wire[point] + second_wire[point]) for point in set(first_wire).intersection(set(second_wire))]))
