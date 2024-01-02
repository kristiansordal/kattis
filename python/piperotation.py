# fmt: off
from collections import deque


def main():
    r, c = map(int, input().split())

    grid = []
    for _ in range(r):
        grid.append(input().strip())

    # A Nothing
    # B Straight
    # C Elbow
    # D Four way

    start = []

    for i, r in enumerate(grid):
        for j, c in enumerate(r):
            if c in "BCD":
                start.append((i, j))
                break

    q = deque(start)
    SEEN = set()

    while q:
        r,c = q.popleft()

        if (r,c) in SEEN: continue
        SEEN.add((r,c))

        if grid[r][c] == "B":






if __name__ == "__main__":
    main()
