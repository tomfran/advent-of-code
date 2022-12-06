from utils.api import get_input

input_str = get_input(1)
l = input_str.split("\n\n")
l = [sum(map(int, b.split("\n"))) for b in l]
l.sort()

print(l[-1], sum(l[-3:]))
