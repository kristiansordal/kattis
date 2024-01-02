n = int(input())
det = lambda x, y: x[0] * y[1] - x[1] * y[0]

while n != 0:
    verts = []
    for _ in range(n):
        x, y = map(int, input().split())
        verts.append((x, y))

    area = 0.0
    for i in range(len(verts) - 1):
        area += det((verts[i]), verts[i + 1])
    area += det(verts[-1], verts[0])

    if area < 0:
        print("CW " + "{:.1f}".format((abs(area) / 2)))
    else:
        print("CCW " + "{:.1f}".format((abs(area) / 2)))

    n = int(input())
