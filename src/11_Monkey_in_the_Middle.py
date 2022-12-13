from utils.api import get_input
from collections import deque

input_str = get_input(11)

e = input_str.split("\n\n")

M = 1


def parse(s):
    lines = s.splitlines()[1:]
    items = deque([int(e) for e in lines[0].split(":")[1].split(",")])
    op = lines[1].split("=")[1]
    div = int(lines[2].split("by")[1])
    global M
    M *= div
    choices = []
    choices.append(int(lines[3].split("monkey")[1]))
    choices.append(int(lines[4].split("monkey")[1]))
    return [items, op, div, choices, 0]


def compute_stress(items, op):
    old = items[0]
    new = eval(op) // 3
    return new


def compute_stress2(items, op):
    old = items[0]
    new = eval(op)
    return new % M


monkeys = list(map(parse, e))
n = len(monkeys)
counters = [0 for _ in range(n)]


rounds = 10000
for r in range(rounds):
    for monkey in monkeys:
        for _ in range(len(monkey[0])):
            monkey[4] += 1
            # stress = compute_stress1(monkey[0], monkey[1]) # ans1
            stress = compute_stress2(monkey[0], monkey[1])  # ans2
            ind = monkey[3][0] if stress % monkey[2] == 0 else monkey[3][1]
            monkeys[ind][0].append(stress)
            monkey[0].popleft()

e = [m[4] for m in monkeys]
e.sort()
print(e[-1] * e[-2])
