from math import sqrt
import heapq


def main():
    _, _, _ = map(int, input().split())
    p = list(map(int, input().split()))
    r = list(map(int, input().split()))
    si = list(map(int, input().split()))

    rads = r + [sqrt(s**2 + s**2) / 2 for s in si]

    heapq.heapify(rads)
    heapq.heapify(p)

    fits = 0
    while p and rads:
        if p[0] > rads[0]:
            fits += 1
            heapq.heappop(p)
            heapq.heappop(rads)
        else:
            heapq.heappop(p)
    print(fits)


main()
