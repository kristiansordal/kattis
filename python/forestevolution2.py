from math import sqrt, atan2


def side(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0]) > 0


def segment(points, hull, x, y):
    above = set()
    below = set()

    print(f"X: {x}, Y: {y}")
    for p in points:
        print(p)
        if p not in hull:
            if side(p, x, y):
                above.add(p)
            else:
                below.add(p)

    return above, below


def dist(a, b, c):
    x = abs((b[0] - a[0]) * (a[1] - c[1]) - (a[0] - c[0]) * (b[1] - a[1])) / (
        sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)
    )
    return x


def getMax(points, x, y, sideFlag):
    maxDist = 0
    maxPoint = (0, 0)
    for p in points:
        d = dist(x, y, p)
        if d > maxDist:
            maxPoint = p
            maxDist = d
        elif d == maxDist:
            if sideFlag:
                if p[0] < maxPoint[0]:
                    maxPoint = p
            else:
                if p[0] > maxPoint[0]:
                    maxPoint = p

    return maxPoint


def toPolar(points):
    pointsAngle = []
    for p in points:
        phi = atan2(p[1], p[0])
        r = sqrt(p[0] ** 2 + p[1] ** 2)
        pointsAngle.append((p, (phi, r)))

    return pointsAngle


def det(x, y):
    return (x[0] * y[1]) - (y[0] * x[1])


def shoelace(points):
    twoA = 0
    for i in range(len(points)):
        if i == len(points) - 1:
            twoA += det(points[i], points[0])
        else:
            twoA += det(points[i], points[i + 1])

    return twoA / 2


def convexHull(points):
    hull = set()

    x = min(points)
    y = max(points)

    hull.add(x)
    hull.add(y)

    above, below = segment(points, hull, x, y)

    findHull(above, x, y, hull, True)
    findHull(below, x, y, hull, False)

    return hull


def findHull(points, x, y, hull, sideFlag):
    if not points:
        return

    maxPoint = getMax(points, x, y, sideFlag)
    hull.add(maxPoint)
    points.remove(maxPoint)

    above1, below1 = segment(points, hull, x, maxPoint)
    above2, below2 = segment(points, hull, maxPoint, y)

    if sideFlag:
        findHull(above1, x, maxPoint, hull, True)
        findHull(above2, maxPoint, y, hull, True)
    else:
        findHull(below1, x, maxPoint, hull, False)
        findHull(below2, maxPoint, y, hull, False)


def main():
    p, a = map(int, input().split())
    points1 = set()
    points2 = set()
    for _ in range(p):
        x, y = map(float, input().split())
        points1.add((x, y))

    for _ in range(a):
        x, y = map(float, input().split())
        points2.add((x, y))

    hull1 = convexHull(points1)
    hull2 = convexHull(points2)

    print(hull1)
    print(hull2)

    polar1 = list(map(lambda x: x[0], (sorted(toPolar(hull1), key=lambda p: p[1][0]))))
    polar2 = list(map(lambda x: x[0], (sorted(toPolar(hull2), key=lambda p: p[1][0]))))

    area1 = shoelace(polar1)
    area2 = shoelace(polar2)
    print(area1 + area2)


if __name__ == "__main__":
    main()
