from utils.api import get_input
from functools import reduce

input_str = get_input(7)

outputs = input_str.split("\n$")

tree = {"/": {}}
curr_path = ["/"]


def add_subdir(dest):
    e = tree
    for p in curr_path:
        e = e[p]
    if dest not in e:
        e[dest] = {}


def add_file(k):
    e = tree
    for p in curr_path:
        e = e[p]
    e["files"] = e.get("files", 0) + int(k)


for o in outputs[1:]:

    e = o.splitlines()
    s = e[0].replace("$", "").strip()
    command = s.split()[0]

    if command == "ls":
        ls_dir = None
        lines = [r.split() for r in e[1:]]
        for k, v in lines:
            if k == "dir":
                add_subdir(v)
            else:
                add_file(k)

    if command == "cd":
        dest = s.split()[1]
        if dest == "..":
            curr_path.pop()
        else:
            add_subdir(dest)
            curr_path.append(dest)

sizes = []


def dfs(node):
    total = node.get("files", 0)
    for k, v in node.items():
        if k == "files":
            continue
        total += dfs(v)
    sizes.append(total)
    return total


dfs(tree)
# answer 1
print(reduce(lambda a, b: a + b, filter(lambda x: x < 100000, sizes)))
# answer 2
to_del = 30000000 - (70000000 - max(sizes))
sizes.sort()
for e in sizes:
    if e >= to_del:
        print(e)
        break
