from math import sqrt, atan2


def det2x2(a, b, c, d):
    return (a * c) - (b * d)


# return 1 if inside
# return 0 if on edge or vertex
# return -1 if outside
def insideTriangle(a, b, c, p):
    # extract the coords
    x, y = p
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c

    # elements of the determinant
    t_a = x1 - x3
    t_b = x2 - x3
    t_c = y1 - y3
    t_d = y2 - y3

    det = det2x2(t_a, t_b, t_c, t_d)

    if det == 0:
        return 0
    alpha = ((y2 - y3) * (x - x3) + (x3 - x2) * (y - y3)) / det
    beta = ((y3 - y1) * (x - x3) + (x1 - x3) * (y - y3)) / det
    gamma = 1 - alpha - beta

    lambdas = [alpha, beta, gamma]

    if all(x > 0 and x < 1 for x in lambdas):
        return 1
    elif any(x == 0 for x in lambdas):
        return 0
    else:
        return -1


def side(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) > (b[1] - a[1]) * (c[0] - a[0])


def segment(points, x, y):
    above = set()
    below = set()

    for p in points:
        if side(x, y, p):
            above.add(p)
        else:
            below.add(p)
    return above, below


def dist(a, b, c):
    return abs((b[0] - a[0]) * (a[1] - c[1]) - (a[0] - c[0]) * (b[1] - a[1])) / sqrt(
        (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2
    )


def getMax(points, x, y, sideFlag):
    maxPoint = (0, 0)
    maxDist = 0
    for p in points:
        s = abs(dist(x, y, p))
        if s == 0.0:
            print(s)
        if s > maxDist:
            maxPoint = p
            maxDist = s
        elif s == maxDist:
            if sideFlag:
                if p[0] < maxPoint[0]:
                    maxPoint = p
            else:
                if p[0] > maxPoint[0]:
                    maxPoint = p

    return maxPoint


def quickHull(points):
    hull = set()

    x = min(points)
    y = max(points)

    hull.add(x)
    hull.add(y)

    points.remove(x)
    points.remove(y)

    above, below = segment(points, x, y)

    findHull(above, hull, x, y, True)
    findHull(below, hull, x, y, False)
    return hull


def findHull(points, hull, x, y, side):
    if not points:
        return

    z = getMax(points, x, y, side)
    # if z != (0, 0):
    points.remove(z)
    hull.add(z)

    newPoints = set()

    for p in points:
        if insideTriangle(x, y, z, p) == -1:
            newPoints.add(p)

    above1, below1 = segment(points, x, z)
    above2, below2 = segment(points, z, y)

    if side:
        findHull(above1, hull, x, z, side)
        findHull(above2, hull, z, y, side)
    else:
        findHull(below1, hull, x, z, side)
        findHull(below2, hull, z, y, side)


def angle(x):
    return (atan2(x[1], x[0]), x)


def main():
    n = int(input())
    while n != 0:
        points = set()
        for _ in range(n):
            x, y = map(float, input().split())
            points.add((x, y))

        if n > 2:
            points = quickHull(points)
        angles = list(map(lambda x: x[1], sorted([angle(x) for x in points])))

        print(len(angles))

        for a in angles:
            print(int(a[0]), " ", int(a[1]))

        n = int(input())


if __name__ == "__main__":
    main()
