DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def solve(grid, poi):
    covered = set()
    antennas = 0
    for r, c in poi:

        for dr, dc in DIRS:
            rr, cc = r + dr, c + dc

            if 0 <= rr < len(grid) and 0 <= cc < len(grid[0]) and grid[rr][cc] == "*":
                if ((rr, cc)) not in covered and ((r, c)) not in covered:
                    covered.add((rr, cc))
                    covered.add((r, c))
                    antennas += 1

    for p in poi:
        if p not in covered:
            antennas += 1
    print(antennas)


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    grid = []
    poi = set()

    for i in range(n):
        row = []
        r = input().strip()
        for j in range(m):
            if r[j] == "*":
                poi.add((i, j))
        grid.append([c for c in r])
    solve(grid, poi)
