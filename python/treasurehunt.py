n, m = map(int, input().split())
grid = []
dirs = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "W": (0, -1)}
for _ in range(n):
    grid.append(input())

s = 0
q = [(0, 0)]
while q:
    r, c = q.pop(0)

    if r < 0 or r >= n or c < 0 or c >= m:
        print("Out")
        break

    if grid[r][c] == "T":
        print(s)
        break
    dr, dc = dirs[grid[r][c]]
    s += 1
    q.append((r + dr, c + dc))
