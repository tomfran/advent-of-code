from utils.api import get_input


class Packet:
    def __init__(self, p):
        self.p = p

    def __lt__(self, other):
        return Packet.compare(self.p, other.p) == -1

    def __eq__(self, other):
        return self.p == other.p

    def __repr__(self):
        return str(self.p)

    def compare(a, b):
        # both lists
        if type(a) == list and type(b) == list:
            res = 0
            while res == 0:
                if not b and not a:
                    return 0
                if not b and a:
                    return 1
                if not a and b:
                    return -1
                res = Packet.compare(a[0], b[0])
                a = a[1:]
                b = b[1:]
            return res
        # both integers
        if type(a) == type(b) == int:
            if a == b:
                return 0
            return -1 if a < b else 1

        if type(a) == int:
            return Packet.compare([a], b)
        return Packet.compare(a, [b])


def parse(lines):
    e = lines.strip().split("\n")
    return Packet(eval(e[0])), Packet(eval(e[1]))


input_str = get_input(13)

couples = list(map(parse, input_str.split("\n\n")))


div1 = Packet([[2]])
div2 = Packet([[6]])
packet_list = [div1, div2]

ans1 = 0
for i, (p1, p2) in enumerate(couples):
    packet_list += [p1, p2]
    if p1 < p2:
        ans1 += i + 1

packet_list.sort()
ans2 = (packet_list.index(div1) + 1) * (packet_list.index(div2) + 1)

print(ans1, ans2)
