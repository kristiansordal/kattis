from collections import defaultdict
from math import floor


def main():
    atoms, count = input().split()
    count = int(count)
    goal = input().strip()
    m = defaultdict(int)
    n = defaultdict(int)
    atoms = list(atoms)
    goal = list(goal)

    c = []
    while atoms:
        curr = atoms.pop()
        if curr.isdigit():
            c.append(int(curr) * (10 ** len(c)))
        else:
            if not c:
                m[curr] += count
            else:
                m[curr] += sum(c) * count
                c = []
    c = []
    while goal:
        curr = goal.pop()
        if curr.isdigit():
            c.append(int(curr) * (10 ** len(c)))
        else:
            if not c:
                n[curr] += 1
            else:
                n[curr] += sum(c)
                c = []

    ans = min(floor(m[k] / n[k]) if k in m else 0 for k in n)
    print(ans)


if __name__ == "__main__":
    main()
