from utils.api import get_input


def parse(s):
    a, b = s.strip().split()
    return a, int(b)


def move(x, y, dx, dy):
    return (x + dx, y + dy)


def need_to_move(hx, hy, tx, ty):
    return abs(hx - tx) > 1 or abs(hy - ty) > 1


input_str = map(parse, get_input(9).splitlines())


deltas = {"R": (0, 1), "L": (0, -1), "U": (1, 0), "D": (-1, 0)}

rope_len = 9
rope = [(0, 0) for _ in range(rope_len)]
prev_rope = [e for e in rope]

visited = set()
visited.add(rope[0])

for direction, steps in input_str:
    delta = deltas[direction]
    print(rope)
    for _ in range(steps):
        prev_rope = [e for e in rope]
        rope[-1] = move(*rope[-1], *delta)
        for i in range(rope_len - 2, -1, -1):
            if need_to_move(*rope[i], *rope[i + 1]):
                rope[i] = prev_rope[i + 1]
        visited.add(rope[0])

print(len(visited))
