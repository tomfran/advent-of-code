from utils.api import get_input

input_str = get_input(5)

stacks = [
    ["T", "D", "W", "Z", "V", "P"],
    ["L", "S", "W", "V", "F", "J", "D"],
    ["Z", "M", "L", "S", "V", "T", "B", "H"],
    ["R", "S", "J"],
    ["C", "Z", "B", "G", "F", "M", "L", "W"],
    ["Q", "W", "V", "H", "Z", "R", "G", "B"],
    ["V", "J", "P", "C", "B", "D", "N"],
    ["P", "T", "B", "Q"],
    ["H", "G", "Z", "R", "C"],
]

for e in input_str.splitlines():
    a, b, c = map(int, e.split())
    tmp = []
    for _ in range(a):
        tmp.append(stacks[b - 1].pop())
    stacks[c - 1] += tmp  # answer 1
    # stacks[c - 1] += tmp[::-1]  # answer 2

print("".join([e[-1] for e in stacks]))
