from collections import deque


def bfs(grid, color):
    best = set()
    q = deque([(0, 0)])

    while q:
        r, c = q.popleft()

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            rr, cc = r + dr, c + dc
            if 0 <= rr < len(grid) and 0 <= cc < len(grid[0]):
                if grid[rr][cc] == color:
                    q.append((rr, cc))
                    best.add((r, c))

    return best


def bfs1(grid, color, best):
    q = deque(best)

    new_best = set()

    while q:
        r, c = q.popleft()

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            rr, cc = r + dr, c + dc
            if 0 <= rr < len(grid) and 0 <= cc < len(grid[0]):
                if grid[rr][cc] == color:
                    q.append((rr, cc))
                    new_best.add((rr, cc))
    return new_best


def flood(grid, n):
    moves = {i: 0 for i in range(1, 7)}
    seen_tiles = 0
    BEST, COLOR = set(), 0

    while seen_tiles < n * n:

        # how many tiles are reachable from our origin color?
        BEST = bfs(grid, grid[0][0])

        new_best = []
        for color in range(1, 7):
            if color != grid[0][0]:
                new_best.append((bfs1(grid, color, BEST), color))

        # # seen_sets = [(bfs(grid, i, BEST.copy()), i) for i in range(1, 7) if i != grid[0][0]]
        BEST, COLOR = min(new_best, key=lambda x: (-len(x[0]), x[1]))
        seen_tiles = len(BEST)
        moves[COLOR] += 1

        for r, c in BEST:
            grid[r][c] = COLOR

        for l in grid:
            print("".join(str(x) for x in l))
        print()

    print(sum(moves.values()))
    print(" ".join(str(x) for x in moves.values()))


def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        grid = []
        for _ in range(n):
            grid.append([int(x) for x in input().strip()])
        flood(grid, n)


if __name__ == "__main__":
    main()
