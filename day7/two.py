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


class IntCode:
    def __init__(self, name, in_list, p):
        self.name = name
        self.instruction_list = in_list
        self.pointer = p

    def exec(self, input_1, input_2):
        input_counter = 0
        while True:
            instruction = str(self.instruction_list[self.pointer])
            op_code = int(instruction[-2:])

            if op_code == 99:
                return -1

            mode_list = modes(instruction)
            if op_code in [3, 4]:
                p1 = int(self.instruction_list[self.pointer + 1])
                if op_code == 3:
                    self.instruction_list[p1] = input_1 if input_counter == 0 else input_2
                    input_counter += 1
                    self.pointer += 2
                elif op_code == 4:
                    self.pointer += 2
                    return self.instruction_list[p1]
            elif op_code in [5, 6]:
                self.pointer = three_op(self.pointer, op_code, self.instruction_list, mode_list)
            else:
                self.pointer = four_op(self.pointer, op_code, self.instruction_list, mode_list)


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
