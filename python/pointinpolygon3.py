from math import inf

# IN, OUT, ON = 0, 1, 2
NO, YES, COLLINEAR = 0, 1, 2


def intersects(v1x1, v1y1, v1x2, v1y2, v2x1, v2y1, v2x2, v2y2):
    a1 = v1y2 - v1y1
    b1 = v1x1 - v1x2
    c1 = (v1x2 * v1y1) - (v1x1 * v1y2)

    d1 = (a1 * v2x1) + (b1 * v2y1) + c1
    d2 = (a1 * v2x2) + (b1 * v2y2) + c1

    if d1 > 0 and d2 > 0:
        return NO
    if d1 < 0 and d2 < 0:
        return NO

    a2 = v2y2 - v2y1
    b2 = v2x1 - v2x2
    c2 = (v2x2 * v2y1) - (v2x1 * v2y2)

    d1 = (a2 * v1x1) + (b2 * v1y1) + c2
    d2 = (a2 * v1x2) + (b2 * v1y2) + c2

    if d1 > 0 and d2 > 0:
        return NO
    if d1 < 0 and d2 < 0:
        return NO

    if (a1 * b2) - (a2 * b1) == 0:
        return COLLINEAR

    return YES


def raycast(points, polygon):
    mnx = min(polygon, key=lambda p: p[0])
    ray = (mnx[0] - 1, points[1])
    sides = []

    for i in range(len(polygon)):
        sides.append((polygon[i - 1], polygon[i]))

    intersections = 0

    for side in sides:
        if (
            a := intersects(
                ray[0], ray[1], points[0], points[1], side[0][0], side[0][1], side[1][0], side[1][1]
            )
            == YES
        ):
            intersections += 1
        elif a == COLLINEAR:
            return 2
    return intersections % 2 == 1


while (n := int(input())) != 0:
    polygon, points = [], []
    for _ in range(n):
        x, y = map(float, input().split())
        polygon.append((x, y))

    m = int(input())

    for _ in range(m):
        x, y = map(float, input().split())
        points.append((x, y))

    for point in points:
        if r := raycast(point, polygon):
            print("in")
        elif r == 2:
            print("on")
        else:
            print("out")
