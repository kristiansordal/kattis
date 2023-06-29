import sys
import copy
import math


def dist(x):
    return math.sqrt(x[0] ** 2 + x[1] ** 2)


def origin_max_dist(coords):
    maxDist = 0
    maxCoords = []

    for c in coords:
        d = dist(c)
        if d > maxDist:
            maxDist = d
            maxCoords = c
    return maxCoords


def max_dist_point(coords, point):
    maxDist = 0
    maxCoords = []

    for c in coords:
        d = dist([point[0] - c[0], point[1] - c[1]])
        if d > maxDist:
            maxDist = d
            maxCoords = c

    return maxCoords


def main():
    inp = [list(map(int, x.split())) for x in sys.stdin.readlines()]
    configs = []
    beacons = []
    for x in inp:
        if len(x) != 1:
            beacons.append(x)
        else:
            configs.append(copy.deepcopy(beacons))
            beacons.clear()

    configs = configs[1:]

    for b in configs:
        p1 = origin_max_dist(b)
        p2 = max_dist_point(b, p1)
        print(p1, " ", p2)
        print((p2[0] - p1[0]) * (p2[1] - p1[1]))


if __name__ == "__main__":
    main()
