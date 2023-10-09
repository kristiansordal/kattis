from math import sqrt
# def count_mosquitoes(p, r):

#     for p1 in p:
#         for p2 in p:


def isInside(ps, c,r):
    for p in ps:
        d = sqrt(p[0]**2 + c[0]**2 + p[1]**2 + c[1]**2)
        if d <= r:






def main():
    n = int(input())

    for _ in range(n):
        p, r = map(int, input().split())

        points = []

        for _ in range(p):
            points.append(map(int, input().split()))


if __name__ == "__main__":
    main()
