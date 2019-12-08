import csv
import itertools
from common.IntCode import IntCode


with open('in.txt') as input_file:
    data = next(csv.reader(input_file))
    amplifier_list = list(["A", "B", "C", "D", "E"])

    list_of_outputs = list()
    for setting_list in itertools.permutations(range(5, 10)):
        intcode_list = []
        for i in amplifier_list:
            intcode_list.append(IntCode(i, data[:], 0))

        output = 0
        for i in range(len(intcode_list)):
            output = intcode_list[i].exec(setting_list[i], output)
            list_of_outputs.append(output)

        while output != -1:
            for i in range(len(intcode_list)):
                output = intcode_list[i].exec(output, output)
                list_of_outputs.append(output)

    print(max(list_of_outputs))
