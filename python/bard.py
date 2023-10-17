import sys


def main():
    present = [[int(x) for x in l.strip().split()] for l in sys.stdin]
    n = present.pop(0)
    e = present.pop(0)
    present = list(map(lambda x: x[1:], present))
    maxSongs = len(list(filter(lambda x: 1 in x, present)))
    v = list(range(1, max(map(max, present)) + 1))
    v = {k: 0 for k in v}

    for n in present:
        if 1 in n:
            for k in n:
                v[k] += 1
        else:
            m = max(v.values())
            for k in n:
                v[k] = m

    knowAll = sorted(list(filter(lambda x: v[x] == maxSongs, v.keys())))
    for x in knowAll:
        print(x)


main()
