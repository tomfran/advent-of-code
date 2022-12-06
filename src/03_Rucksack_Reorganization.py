from utils.api import get_input
from functools import reduce

input_str = get_input(3)

e = list(map(lambda x: x.strip(), input_str.splitlines()))


def priority(s):
    ref = "a" if s.islower() else "A"
    ret = ord(s) - ord(ref) + 1
    if not s.islower():
        ret += 26
    return ret


ans1 = 0
for s in e:
    n = len(s) // 2
    el = list(set(s[:n]) & set(s[n:]))[0]
    ans1 += priority(el)

ans2 = 0
for i in range(0, len(e), 3):
    el = reduce(lambda a, b: a & b, [set(r) for r in e[i : i + 3]])
    el = list(el)[0]
    ans2 += priority(el)

print(ans1, ans2)
