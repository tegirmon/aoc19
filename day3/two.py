import csv


def get_key(x, y):
    return str(x)+"."+str(y)


c_list = []
wire_num = 0
cross_list = []
with open('in.txt') as input_file:
    for row in csv.reader(input_file):
        last_x = 0
        last_y = 0
        c_list.append({})
        sum_steps = 0
        for move in row:
            dx = 0
            dy = 0
            if move[0] == 'U':
                dy = +1
            elif move[0] == 'D':
                dy = -1
            elif move[0] == 'R':
                dx = +1
            elif move[0] == 'L':
                dx = -1

            steps = int(move[1:])

            if dx != 0:
                next_x = last_x + (steps * dx)
                for x in range(last_x + dx, (next_x + dx), dx):
                    sum_steps += 1
                    key_x = get_key(x, last_y)
                    c_list[wire_num][key_x] = sum_steps
                    if wire_num == 1 and (key_x in c_list[0].keys()):
                        cross_list.append(key_x)
                last_x = next_x
            if dy != 0:
                next_y = last_y + (steps * dy)
                for y in range(last_y + dy, (next_y + dy), dy):
                    sum_steps += 1
                    key_y = get_key(last_x, y)
                    c_list[wire_num][key_y] = sum_steps
                    if wire_num == 1 and (key_y in c_list[0].keys()):
                        cross_list.append(key_y)
                last_y = next_y
        wire_num += 1

steps_list = []
for key in cross_list:
    steps_list.append((c_list[0][key] + c_list[1][key]))
print(min(steps_list))
