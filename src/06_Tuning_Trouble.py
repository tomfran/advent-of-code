from utils.api import get_input
from functools import partial

input_str = get_input(6).strip()

n = len(input_str)


def f(i, l):
    return i + l if len(set(input_str[i : i + l])) == l else n


ans1 = min(map(partial(f, l=4), range(n)))
ans2 = min(map(partial(f, l=14), range(n)))
print(ans1, ans2)
