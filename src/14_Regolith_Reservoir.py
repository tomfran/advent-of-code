from utils.api import get_input
from copy import deepcopy

input_str = get_input(14)
lines = map(lambda s: [*map(eval, s.split("->"))], input_str.splitlines())

# fill the matrix with lines
Y_MAX = 0
matrix = [["." for _ in range(1000)] for _ in range(300)]
for line in lines:
    for (x1, y1), (x2, y2) in zip(line, line[1:]):
        Y_MAX = max([Y_MAX, y1, y2])
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1, 1):
                matrix[i][x1] = "#"
        else:
            for i in range(min(x1, x2), max(x1, x2) + 1, 1):
                matrix[y1][i] = "#"

# copy to solve both answers
matrix_copy = deepcopy(matrix)


def dfs(y, x, m):
    # stuck
    if m[y + 1][x] == m[y + 1][x - 1] == m[y + 1][x + 1] == "#":
        m[y][x] = "#"
        return 1
    # not stuck but deviated
    if m[y + 1][x] == "#":
        if m[y + 1][x - 1] == ".":
            return dfs(y + 1, x - 1, m)
        return dfs(y + 1, x + 1, m)
    # free
    return dfs(y + 1, x, m)


# decorator for the first answer
def limiter(f):
    def wrapper(*args, **kwargs):
        y, _, _ = args
        if y > Y_MAX:
            return -1
        return f(*args, **kwargs)

    return wrapper


# second answer
for i in range(1000):
    matrix_copy[Y_MAX + 2][i] = "#"

ans2 = 0
while matrix_copy[0][500] != "#":
    ans2 += 1
    dfs(0, 500, matrix_copy)

# first answer
dfs = limiter(dfs)
ans1 = 0
while dfs(0, 500, matrix) != -1:
    ans1 += 1

print(ans1, ans2)
