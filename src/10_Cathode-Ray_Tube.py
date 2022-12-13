from utils.api import get_input


def parse(s):
    return s.strip().split()


lines = map(parse, get_input(10).splitlines())

x = 1
clk = ans = 0


def increment():
    global x, clk, ans
    increment2()
    clk += 1
    if clk == 20 or (clk - 20) % 40 == 0:
        ans += x * clk


def increment2():
    global clk
    if (clk + 1) % 40 == 0:
        print()
    elif clk % 40 in [x - 1, x, x + 1]:
        print("▓", end="")
    else:
        print("░", end="")
    # clk += 1


for line in lines:
    if line[0] == "noop":
        increment()
    else:
        increment()
        increment()
        x += int(line[1])

print(ans)
