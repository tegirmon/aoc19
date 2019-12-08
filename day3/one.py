import csv


def get_key_val(x, y):
    return str(x)+"_"+str(y), abs(x) + abs(y)


def left_or_right(direction):
    return 0 if direction not in ['R', 'L'] else 1 if direction == 'R' else -1


def up_or_down(direction):
    return 0 if direction not in ['U', 'D'] else 1 if direction == 'U' else -1


def path_for(last_pos, direction, steps):
    next_pos = last_pos + (steps * direction)
    return next_pos, [] if direction == 0 else range(last_pos + direction, (next_pos + direction), direction)


def get_wire(paths):
    wire, last_x, last_y = {}, 0, 0
    for path in paths:
        direction, steps = path[0], int(path[1:])
        last_x, rg = path_for(last_x, left_or_right(direction), steps)
        wire.update([get_key_val(x, last_y) for x in rg])
        last_y, rg = path_for(last_y, up_or_down(direction), steps)
        wire.update([get_key_val(last_x, y) for y in rg])
    return wire


with open('in.txt') as input_file:
    first_wire = get_wire(next(csv.reader(input_file)))
    second_wire = get_wire(next(csv.reader(input_file)))
print(min([first_wire[point] for point in set(first_wire).intersection(set(second_wire))]))
