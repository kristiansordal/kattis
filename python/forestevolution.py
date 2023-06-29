from math import sqrt


# cross product
def cross(a, b, p):
    ab = [b[0] - a[0], b[1] - a[1]]
    ap = [p[0] - a[0], p[1] - a[1]]

    cp = ab[0] * ap[1] - ab[1] * ap[0]

    return cp


# sign of a number
def sign(a, b, c):
    side = (a[0] - c[0]) * (b[1] - c[1]) - (b[0] - c[0]) * (a[1] - c[1])
    if side > 0:
        return 1
    if side < 0:
        return -1
    return 0


# distance from point to line
def dist(a, c, p):
    return abs(a * p[0] - p[1] + c) / sqrt(a**2 + 1)


# area of triangle
def triArea(a, b, c):
    return abs((a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1])) / 2)


# check if inside triangle
def inTriangle(p, a, b, c):
    a0 = triArea(a, b, c)
    a1 = triArea(p, a, c)
    a2 = triArea(p, a, b)
    a3 = triArea(p, b, c)
    return a0 == a1 + a2 + a3


def convexHull(points):
    hull = set()
    minPoint = min(points)
    maxPoint = max(points)

    hull.add(minPoint)
    hull.add(maxPoint)

    below = set()
    above = set()

    for p in points:
        s = cross(maxPoint, minPoint, p)

        if p not in hull:
            if s > 0:
                above.add(p)
            elif s < 0:
                below.add(p)

    findHull(above, maxPoint, minPoint, hull)
    findHull(below, minPoint, maxPoint, hull)

    return hull


def findHull(points, x, y, hull):
    if not points:
        return

    maxPoint = max(zip(map(lambda p: cross(x, y, p), points), points))[1]
    hull.add(maxPoint)
    above = set()
    below = set()

    for p in points:
        if not inTriangle(p, x, y, maxPoint):
            s = cross(x, maxPoint, p)
            if s > 0:
                above.add(p)
            if s < 0:
                below.add(p)

    findHull(above, x, maxPoint, hull)
    findHull(below, maxPoint, y, hull)

    return hull


def main():
    p, a = map(int, input().split())
    points = []
    for _ in range(p + a):
        x, y = map(float, input().split())
        points.append((x, y))

    hull = convexHull(points)
    print(sorted(hull))


if __name__ == "__main__":
    main()
