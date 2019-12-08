import csv
import itertools


def modes(ins):
    m = [0] * 3
    if len(ins) > 3:
        m[0] = int(ins[1])
        m[1] = int(ins[0])
    elif len(ins) > 2:
        m[0] = int(ins[0])
    return m


def three_op(p, oc, in_l, m):
    p1 = int(in_l[p + 1])
    p2 = int(in_l[p + 2])
    v1 = int(in_l[p1] if m[0] == 0 else p1)
    v2 = int(in_l[p2] if m[1] == 0 else p2)
    if oc == 5 and v1 > 0:
        p = v2
    elif oc == 6 and v1 == 0:
        p = v2
    else:
        p += 3

    return p


def four_op(p, oc, in_l, m):
    p1 = int(in_l[p + 1])
    p2 = int(in_l[p + 2])
    r = int(data[p + 3])
    v1 = int(in_l[p1] if m[0] == 0 else p1)
    v2 = int(in_l[p2] if m[1] == 0 else p2)
    if oc == 1:
        in_l[r] = v1 + v2
    elif oc == 2:
        in_l[r] = v1 * v2
    elif oc == 7:
        in_l[r] = 1 if v1 < v2 else 0
    elif oc == 8:
        in_l[r] = 1 if v1 == v2 else 0

    return p + 4


def software(in_l, input_1, input_2):
    pointer = 0
    input_counter = 0
    while True:
        instruction = str(in_l[pointer])
        mode_list = modes(instruction)
        op_code = int(instruction[-2:])

        if op_code == 99:
            break

        if op_code in [3, 4]:
            p1 = int(in_l[pointer + 1])
            if op_code == 3:
                in_l[p1] = input_1 if input_counter == 0 else input_2
                input_counter += 1
            elif op_code == 4:
                return in_l[p1]
            pointer += 2
        elif op_code in [5, 6]:
            pointer = three_op(pointer, op_code, in_l, mode_list)
        else:
            pointer = four_op(pointer, op_code, in_l, mode_list)


with open('in.txt') as input_file:
    data = next(csv.reader(input_file))
    list_of_outputs = list()
    settings = list(range(0, 5))
    for setting_list in itertools.permutations(range(0, 5)):
        output = 0
        for setting in setting_list:
            output = software(data[:], setting, output)
            list_of_outputs.append(output)
    print(max(list_of_outputs))
