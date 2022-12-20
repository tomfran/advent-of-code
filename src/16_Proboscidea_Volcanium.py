from utils.api import get_input

input_str = get_input(16)

graph = {}
flow = {}

for line in input_str.splitlines():
    els = line.replace(",", " ").split()
    valve = els[1]
    flow_rate = int(els[4].replace(";", "").split("=")[1])
    successors = els[9:]
    graph[valve] = successors
    if flow_rate:
        flow[valve] = flow_rate


def bfs(node):
    visited = set([node])
    distance = {}
    q = [node]
    curr_level = 0
    while q:
        next_level = []
        for e in q:
            distance[e] = curr_level
            for adj in graph[e]:
                if adj in visited:
                    continue
                visited.add(adj)
                next_level.append(adj)
        curr_level += 1
        q = next_level
    distance.pop(node)
    return distance


# compute pairwise minpaths
min_paths = {}
for node in graph.keys():
    min_paths[node] = bfs(node)

opened = {}
ans = 0


answer_space = {}


def normalize(d):
    return tuple(sorted([k for k, v in d.items() if v]))


def update_answer_space(d, v):
    t = answer_space.get(normalize(d), 0)
    answer_space[normalize(d)] = max(t, v)


def solve(node, time, curr):
    update_answer_space(opened, curr)
    if time <= 0:
        return

    opened[node] = True
    acc = max(0, flow[node] * (time - 1))
    curr += acc

    global ans
    ans = max(ans, curr)

    valves_left = [k for k, v in opened.items() if not v]
    if not valves_left:
        update_answer_space(opened, curr)
    for left in valves_left:
        time_lost = min_paths[node][left] + 1
        solve(left, time - time_lost, curr)

    opened[node] = False


# first answer
for start in flow.keys():
    opened = {k: False for k in flow.keys()}
    solve(start, 30 - min_paths["AA"][start], 0)
print(ans)

# launch on 26 minutes
answer_space = {}
for start in flow.keys():
    opened = {k: False for k in flow.keys()}
    solve(start, 26 - min_paths["AA"][start], 0)

ans = 0


def disjoint(t1, t2):
    return not (set(t1) & set(t2))


# find maximum sum of disjointed paths
n = len(answer_space)
answer_space = list(answer_space.items())
for i in range(n):
    for j in range(i + 1, n):
        el1, v1 = answer_space[i]
        el2, v2 = answer_space[j]
        if disjoint(el1, el2):
            ans = max(ans, v1 + v2)
print(ans)
