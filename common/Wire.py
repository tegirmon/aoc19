
class Wire:
    def __init__(self, distance=False):
        self.total = 0
        self.wire = {}
        self.distance = distance

    @staticmethod
    def dist(x, y):
        return abs(x) + abs(y)

    @staticmethod
    def left_or_right(direction):
        return 0 if direction not in ['R', 'L'] else 1 if direction == 'R' else -1

    @staticmethod
    def up_or_down(direction):
        return 0 if direction not in ['U', 'D'] else 1 if direction == 'U' else -1

    @staticmethod
    def path_for(last_pos, direction, steps):
        next_pos = last_pos + (steps * direction)
        return next_pos, [] if direction == 0 else range(last_pos + direction, (next_pos + direction), direction)

    def inc(self):
        self.total += 1
        return self.total

    def val(self, x, y):
        if self.distance:
            return self.dist(x, y)
        else:
            return self.inc()

    def get_key_val(self, x, y):
        return str(x) + "_" + str(y), self.val(x, y)

    def walk(self, paths):
        last_x, last_y = 0, 0
        for path in paths:
            direction, steps = path[0], int(path[1:])
            last_x, rg = self.path_for(last_x, self.left_or_right(direction), steps)
            self.wire.update([self.get_key_val(x, last_y) for x in rg])
            last_y, rg = self.path_for(last_y, self.up_or_down(direction), steps)
            self.wire.update([self.get_key_val(last_x, y) for y in rg])
        return self.wire
