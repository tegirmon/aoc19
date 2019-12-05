import csv

with open('in.txt') as input_file:
    data = next(csv.reader(input_file))
    pointer = 0
    while True:
        instruction = str(data[pointer])
        mode1 = 0
        mode2 = 0
        if len(instruction) > 3:
            op_code = int(instruction[2:4])
            mode1 = int(instruction[1])
            mode2 = int(instruction[0])
        elif len(instruction) > 2:
            op_code = int(instruction[1:3])
            mode1 = int(instruction[0])
        else:
            op_code = int(instruction)

        if op_code == 99:
            break

        param1 = int(data[pointer + 1])
        if op_code == 3:
            data[param1] = 5
            pointer += 2
        elif op_code == 4:
            print(data[param1])
            pointer += 2
        else:
            param2 = int(data[pointer + 2])
            va1 = int(data[param1] if mode1 == 0 else param1)
            va2 = int(data[param2] if mode2 == 0 else param2)
            if op_code == 5:
                pointer = va2 if va1 > 0 else (pointer + 3)
            elif op_code == 6:
                pointer = va2 if va1 == 0 else (pointer + 3)
            else:
                result = int(data[pointer + 3])
                if op_code == 1:
                    data[result] = va1 + va2
                elif op_code == 2:
                    data[result] = va1 * va2
                elif op_code == 7:
                    data[result] = 1 if va1 < va2 else 0
                elif op_code == 8:
                    data[result] = 1 if va1 == va2 else 0
                pointer += 4
