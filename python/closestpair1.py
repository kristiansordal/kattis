from math import sqrt, inf


class Point:
    def __init__(self, x=0.0, y=0.0, id=-1):
        self.x = x
        self.y = y
        self.id = id

    def __lt__(self, other):
        return self.x < other.x


class Pair:
    def __init__(self, p1=Point(), p2=Point()):
        self.p1 = p1
        self.p2 = p2

    def dist(self):
        return sqrt((self.p2.x - self.p1.x) ** 2 + (self.p2.y - self.p1.y) ** 2)

    def __lt__(self, other):
        return self.dist() < other.dist()

    def __gt__(self, other):
        return self.dist() > other.dist()

    def __eq__(self, other):
        return self.dist() == other.dist()

    def __str__(self):
        return f"{self.p1.x} {self.p1.y} {self.p2.x} {self.p2.y}"


def byy(obj):
    return obj.y


def bruteforce(points):
    pair = Pair()
    opt = inf

    for p1 in points:
        for p2 in points:
            if p1.id != p2.id:
                opt_pair = Pair(p1, p2)
                delta = opt_pair.dist()
                if delta < opt:
                    pair = opt_pair
                    opt = delta
    return pair


def compute_strip(strip):
    delta = inf
    pair = Pair()

    for i in range(len(strip) - 1):
        s = strip[i : i + 4]
        bf_pair = bruteforce(s)
        if bf_pair.dist() < delta:
            delta = bf_pair.dist()
            pair = bf_pair

    return pair


def closest_pair(sorted_x, sorted_y):
    n = len(sorted_x)

    if n <= 3:
        return bruteforce(sorted_x)

    mid = n // 2

    xl = []
    yl = []
    xr = []
    yr = []

    l = set()

    for i, p in enumerate(sorted_x):
        if i < mid:
            xl.append(p)
            l.add(p)
        else:
            xr.append(p)

    for i in sorted_y:
        if i in l:
            yl.append(i)
        else:
            yr.append(i)

    opt_left_pair = closest_pair(xl, yl)
    opt_right_pair = closest_pair(xr, yr)

    opt_pair = min(opt_left_pair, opt_right_pair)

    line = sorted_x[mid].x

    strip = []
    for p in sorted_y:
        if abs(p.x - line) < opt_pair.dist():
            strip.append(p)

    strip_pair = compute_strip(strip)
    if strip_pair.dist() < opt_pair.dist():
        return strip_pair

    return opt_pair


def main():
    x = [1, 2, 3, 4, 5]
    n = int(input())

    while n != 0:
        points = []
        for i in range(n):
            x, y = map(float, input().split())
            points.append(Point(x, y, i))

        sorted_x = sorted(points)
        sorted_y = sorted(points, key=byy)

        pair = closest_pair(sorted_x, sorted_y)
        print(pair)

        n = int(input())


if __name__ == "__main__":
    main()
