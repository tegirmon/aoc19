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
                    c_list[wire_num][get_key(x, last_y)] = True
                    if wire_num == 1 and (get_key(x, last_y) in c_list[0].keys()):
                        cross_list.append(abs(x) + abs(last_y))
                last_x = next_x
            if dy != 0:
                next_y = last_y + (steps * dy)
                for y in range(last_y + dy, (next_y + dy), dy):
                    c_list[wire_num][get_key(last_x, y)] = True
                    if wire_num == 1 and (get_key(last_x, y) in c_list[0].keys()):
                        cross_list.append(abs(last_x) + abs(y))
                last_y = next_y
        wire_num += 1

print(min(cross_list))
