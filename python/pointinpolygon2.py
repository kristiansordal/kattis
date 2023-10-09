def slope(p1, p2):
    # straight line
    if p2[0] - p1[0] == 0:
        return 0

    return (p2[1] - p1[1]) / (p2[0] - p1[0])


def intersects(p, polygon):
    lines = 0
    for i in range(len(polygon)):
        p1 = min(polygon[i], polygon[(i + 1) % len(polygon)])
        p2 = max(polygon[i], polygon[(i + 1) % len(polygon)])

        if (p1[1] > p[1]) != (p2[1] > p[1]):
            if p[0] < (p2[0] - p1[0]) * (p[1] - p1[1]) / (p2[1] - p1[1]) + p1[0]:
                lines += 1
            else:
                s = slope(p1, p2)

                if s == 0:
                    if p1[0] <= p[0] and p2[0] >= p[0]:
                        return 2
                else:
                    y = p[1]
                    b = p1[1]
                    x = (y - b) / s

                    if p[0] == x:
                        return 2

    return lines % 2


def checkPoints(points, polygon):
    for p in points:
        v = intersects(p, polygon)
        if v == 2:
            print("on")
        elif v == 1:
            print("in")
        else:
            print("out")


def main():
    n = int(input())
    polygons = []
    points = []

    while n != 0:
        polygon = []
        point = []
        for _ in range(n):
            x, y = map(int, input().split())
            polygon.append((x, y))
        polygons.append(polygon)

        m = int(input())

        for _ in range(m):
            x, y = map(int, input().split())
            point.append((x, y))
        points.append(point)

        n = int(input())

    for i in range(len(polygons)):
        checkPoints(points[i], polygons[i])


if __name__ == "__main__":
    main()
