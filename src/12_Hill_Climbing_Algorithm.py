from utils.api import get_input
from functools import partial

input_str = get_input(12)

start = end = None
matrix = list(map(lambda x: list(x.strip()), input_str.splitlines()))

second_starts = []
N = len(matrix)
M = len(matrix[0])
for i in range(N):
    for j in range(M):
        if matrix[i][j] == "S":
            start = (i, j)
        if matrix[i][j] == "E":
            end = (i, j)
        if matrix[i][j] == "a":
            second_starts.append((i, j))

matrix[start[0]][start[1]] = "a"
matrix[end[0]][end[1]] = "z"


def adj(i, j):
    def f(coord):
        x, y = coord
        return 0 <= x < N and 0 <= y < M and ord(matrix[x][y]) - ord(matrix[i][j]) <= 1

    return list(filter(f, [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]))


def bfs(start, end):
    q = [start]
    visited = set([start])
    ans = 1
    while q:
        next_level = []
        for e in q:
            for a in adj(*e):
                if a == end:
                    return ans
                if a in visited:
                    continue
                visited.add(a)
                next_level.append(a)
        q = next_level
        ans += 1
    return float("inf")


ans1 = bfs(start, end)
ans2 = min(map(partial(bfs, end=end), second_starts))
print(ans1, ans2)
