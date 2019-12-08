import csv
import itertools
from common.IntCode import IntCode

with open('in.txt') as input_file:
    data = next(csv.reader(input_file))
    list_of_outputs = list()
    settings = list(range(0, 5))
    for setting_list in itertools.permutations(range(0, 5)):
        output = 0
        for setting in setting_list:
            output = IntCode(1, data[:], 0).exec(setting, output)
            list_of_outputs.append(output)
    print(max(list_of_outputs))
