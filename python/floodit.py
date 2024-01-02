from copy import deepcopy

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def solve(grid):
    moves = 0
    color_counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    # update the grid until its all the same color
    while True:

        # store how many cells we filled, and which color
        filled = []

        max_color = 0
        max_seen = set()
        max_len = 0

        # iterate through the colors, check which color yields the greatest change
        for color in range(1, 7):

            for r, c in max_seen:
                grid[r][c] = color

            # create a copy of the grid
            g = deepcopy(grid)
            q = [(0, 0)]
            SEEN = set()

            while q:
                r, c = q.pop(0)

                # check if we've already visited this cell
                if (r, c) in SEEN:
                    continue

                SEEN.add((r, c))

                for dr, dc in DIRS:
                    rr, cc = r + dr, c + dc

                    # bounds check
                    if 0 <= rr < len(grid) and 0 <= cc < len(grid[0]):

                        # check if we can go to this color
                        if color == g[rr][cc]:
                            q.append((rr, cc))

            filled.append((color, SEEN, len(SEEN)))

        # determine the max color, and its coordinates
        for color, seen, count in filled:
            if count == max_len:
                if color < max_color:
                    max_color = color
                    max_seen = seen
                    max_len = count

            elif count > max_len:
                max_color = color
                max_seen = seen
                max_len = count

        # upate the grid

        for r, c in max_seen:
            grid[r][c] = max_color

        moves += 1
        color_counts[max_color] += 1

        for l in grid:
            print("".join(map(str, l)))


t = int(input())

for _ in range(t):
    n = int(input())
    grid = [[0 for _ in range(n)] for _ in range(n)]
    for r in range(n):
        l = input().strip()
        for i, c in enumerate(l):
            c = int(c)
            grid[r][i] = c

    solve(grid)
