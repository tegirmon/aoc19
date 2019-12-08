import csv
from common.IntCode import IntCode

with open('in.txt') as input_file:
    original = next(csv.reader(input_file))
    for noun in range(0, 100):
        for verb in range(0, 100):
            data = original[:]
            data[1] = noun
            data[2] = verb
            IntCode(1, data, 0).exec(0, 0)
            if data[0] == 19690720:
                print(100 * noun + verb)
                break
