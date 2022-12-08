from utils.api import get_input
from pprint import pprint
from functools import partial, reduce

input_str = get_input(8)

m = [*map(lambda x: [int(e) for e in x], input_str.splitlines())]


def solve():

    r, c = len(m), len(m[0])

    def bound(i, j):
        return 0 <= i < r and 0 <= j < c

    def dfs(i, j, delta):
        a, b = delta
        k, h = i + a, j + b
        if not bound(k, h):
            return []
        return [m[k][h]] + dfs(k, h, delta)

    def check1(values, ref):
        for e in values:
            if e >= ref:
                return False
        return True

    def check2(values, ref):
        acc = 0
        for e in values:
            acc += 1
            if e >= ref:
                break
        return acc

    deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    ans1 = 0
    ans2 = 0
    for i in range(r):
        for j in range(c):
            # build lists in each direction
            directions = [dfs(i, j, delta) for delta in deltas]
            # if this tree is visible, update first answer
            f1 = partial(check1, ref=m[i][j])
            if any(map(f1, directions)):
                ans1 += 1
            # compute scenic score, update second answer
            f2 = partial(check2, ref=m[i][j])
            tmp = reduce(lambda a, b: a * b, map(f2, directions), 1)
            ans2 = max(ans2, tmp)

    return ans1, ans2


print(*solve())
