def checkPoints(points, polygon):
    for p in points:
        lines = set()
        for i in range(0, len(polygon)):
            if i == len(polygon) - 1:
                p1 = min(polygon[i], polygon[0])
                p2 = max(polygon[i], polygon[0])
            else:
                p1 = min(polygon[i], polygon[i + 1])
                p2 = max(polygon[i], polygon[i + 1])
            # print(f"{p1}, {p2}")
            # print(f"P: {p}")
            # print(f"P1: {p1}")
            # print(f"P2: {p2}")
            a = 0

            if p2[0] - p1[0] > 0:
                a = (p2[1] - p1[1]) / (p2[0] - p1[0])

            b = p1[0]
            # print(f"y = {a}x + {b}")

            # y = ax + b
            # ax = y - b
            # x = (y-b)/a
            # if a != 0:
            #     print((p[1] - b) / a)
            # else:
            #     print((p[1] - b))
            # print(p[0])
            if a == 0 or p[0] <= (p[1] - b) / a:
                if p1[1] > p[1] and p2[1] < p[1]:
                    lines.add(p1)
                elif p1[1] < p[1] and p2[1] > p[1]:
                    lines.add(p2)

        if len(lines) % 2 == 0:
            print("out")
        else:
            print("in")


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
