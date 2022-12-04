from utils.api import get_input
from functools import reduce

input_str = get_input(4)


def parse(e):
    f = lambda x: list(map(int, x.split("-")))
    parts = map(f, e.strip().split(","))
    return next(parts) + next(parts)


def check1(e):
    a, b, c, d = e
    return (a <= c and d <= b) or (c <= a and b <= d)


def check2(e):
    t1 = tuple(e[:2])
    t2 = tuple(e[2:])
    a = min([t1, t2], key=lambda x: x[0])
    b = t1 if a == t2 else t2
    return b[0] <= a[1]


e = input_str.splitlines()

print(len(list(filter(check1, map(parse, e)))))
print(len(list(filter(check2, map(parse, e)))))
