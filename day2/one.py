import csv


with open('in.txt') as input_file:
    data = next(csv.reader(input_file))
    op_code = 0
    data[1] = 12
    data[2] = 2
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

print(data[0])

