from utils.api import get_input
from collections import deque


def parse(line):
    for e in ["Sensor at x=", ", y=", ": closest beacon is at x="]:
        line = line.replace(e, " ")
    return tuple(map(int, line.split()))


def distance(a, b, c, d):
    return abs(a - c) + abs(b - d)


input_str = get_input(15)
sensors_beacons = list(map(parse, input_str.splitlines()))
distances = [distance(*e) for e in sensors_beacons]
zipped = list(zip(sensors_beacons, distances))


def check_row(row):
    covered = []
    beacons = set()
    for (xs, ys, xb, yb), d in zipped:
        if yb == row:
            beacons.add(xb)
        window = d - abs(row - ys)
        if window >= 0:
            covered += [(max(xs - window, 0), 0), (min(xs + window + 1, 4000000), 1)]
    beacons = list(sorted(beacons))

    def find_overlaps(x1, x2):
        found = 0
        for b in beacons:
            if x1 <= b <= x2:
                found += 1
            if b > x2:
                return found
        return found

    intervals = []
    ans = 0
    covered.sort()
    open_x = close_x = curr_open = 0
    for x, t in covered:
        if t == 0:
            curr_open += 1
            if curr_open == 1:
                open_x = x
        if t == 1:
            curr_open -= 1
            if curr_open == 0:
                close_x = x
                ans += close_x - open_x
                ans -= find_overlaps(open_x, close_x)
                intervals.append((open_x, close_x))
    return ans, intervals


limit = 4000000


def find_free_x(intervals):
    cover = set()
    for a, b in intervals:
        cover.update(range(a, b))
    for x in range(0, limit + 1):
        if x not in cover:
            return x * 4000000


print(check_row(2000000)[0])

for i in range(1700000, limit):
    if i % 100000 == 0:
        print(i)
    cover, intervals = check_row(i)
    if cover < limit:
        print(f"found: {i}")
        print(i + find_free_x(intervals))
        exit(0)
