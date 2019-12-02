import csv


def find(data, noun, verb):
    op_code = 0
    data[1] = noun
    data[2] = verb
    while True:
        action = int(data[op_code])
        if action == 99:
            break
        param1 = int(data[op_code + 1])
        param2 = int(data[op_code + 2])
        result = int(data[op_code + 3])
        if action == 1:
            data[result] = int(data[param1]) + int(data[param2])
        elif action == 2:
            data[result] = int(data[param1]) * int(data[param2])
        op_code += 4

    return data[0] == 19690720


with open('in.txt') as input_file:
    original = next(csv.reader(input_file))
    for noun in range(0, 100):
        for verb in range(0, 100):
            if find(original[:], noun, verb):
                print(100 * noun + verb)
                break
