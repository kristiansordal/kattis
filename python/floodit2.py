def bfs(grid, color, seen, n):
    q = list(seen) if seen else [(0, 0)]
    while q:
        r, c = q.pop(0)

        for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            rr, cc = r + dr, c + dc

            if 0 <= rr < n and 0 <= cc < n and (rr, cc) not in seen:
                if grid[rr][cc] == color:
                    q.append((rr, cc))  # type: ignore
                    seen.add((rr, cc))

    return seen


def solve(grid, n):
    SEEN = {(0, 0)}
    COUNTS = {i: 0 for i in range(1, 7)}
    moves = 0

    while len(SEEN) < n * n:
        ns = []

        sc = bfs(grid, grid[0][0], SEEN, n)

        for color in range(1, 7):
            if color != grid[0][0]:
                ns.append((color, bfs(grid, color, sc.copy(), n)))

        color, SEEN = sorted(ns, key=lambda x: (-len(x[1]), x[0]))[0]
        COUNTS[color] += 1
        moves += 1

        for r, c in SEEN:
            grid[r][c] = color

    return moves, COUNTS


t = int(input())

for _ in range(t):
    n = int(input())
    grid = [[0 for _ in range(n)] for _ in range(n)]
    for r in range(n):
        l = input().strip()
        for i, c in enumerate(l):
            c = int(c)
            grid[r][i] = c
    moves, counts = solve(grid, n)

    print(moves)
    print(" ".join(map(str, counts.values())))
