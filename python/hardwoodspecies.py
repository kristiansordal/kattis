from collections import defaultdict
import sys


def main():
    trees = [x.strip() for x in sys.stdin.readlines()]
    le = len(trees)
    l = defaultdict(float)

    for t in trees:
        l[t] += 1

    ts = []
    for k in l:
        l[k] /= le
        ts.append((k, l[k] * 100))

    ts = sorted(ts)

    for t in ts:
        print(f"{t[0]} {t[1]}")


if __name__ == "__main__":
    main()
