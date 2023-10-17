from math import pi, inf
from heapq import heappush, heappop


def neighbours(grid, i, j):
    ns = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    neigh = []

    for n in ns:
        if i + n[0] >= 0 and i + n[0] < len(grid):
            if j + n[1] >= 0 and j + n[1] < len(grid[0]):
                neigh.append((i + n[0], j + n[1]))

    return neigh


def dijkstra(g, s):
    found = set()
    q = []
    dist = {}
    dist[s] = 0
    if g[s[0]][s[1]] == "X":
        heappush(q, (10, s))
    else:
        heappush(q, ((2 * pi * 5) / 4, s))

    for v in g.V:
        if v != s:
            dist[v] = inf
            heappush(q, (inf, v))

    while len(found) < h * w:
        _, v = heappop(q)
        found.add(v)

        for n, w in g.N[v]:
            alt = dist[v] + w

            if alt < dist[n]:
                dist[n] = alt
                heappush(q, (alt, n))

    return dist


def main():
    h, w = map(int, input().split())
    g = []

    for _ in range(h):
        r = input().strip()
        g.append(r)

    s = (0, 0)
    found = set()
    q = []
    dist = {}
    if g[s[0]][s[1]] == "X":
        heappush(q, (10, s))
        dist[s] = 10
    else:
        heappush(q, ((2 * pi * 5) / 4, s))
        dist[s] = (2 * pi * 5) / 4

    for i in range(h):
        for j in range(w):
            if (i, j) != s:
                dist[(i, j)] = inf
                heappush(q, (inf, (i, j)))
        _, v = heappop(q)
        found.add(v)

        for n in neighbours(g, v[0], v[1]):
            alt = 0

            if g[v[0]][v[1]] == "X":
                if g[n[0]][n[1]] == "X":
                    alt = dist[v] + 10
                else:
                    alt = dist[v] + 5 + ((2 * pi * 5) / 4)

            if g[v[0]][v[1]] == "O":
                if g[n[0]][n[1]] == "X":
                    alt = dist[v] + 15
                else:
                    alt = dist[v] + (2 * pi * 5) / 4

            if alt < dist[n]:
                dist[n] = alt
                heappush(q, (alt, n))

    print(dist[(h - 1, w - 1)])


if __name__ == "__main__":
    main()
