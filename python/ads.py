allowed = "?,.! "
n, m = map(int, input().split())
grid = []
for _ in range(n):
    r = []
    s = input()
    for c in s:
        r.append(c)
    grid.append(r)
corners = []
print(grid)

for i, r in enumerate(grid):
    for j, c in enumerate(r):
        if 0 <= i < n - 1 and 0 <= j < m - 1:
            if c == "+" and grid[i + 1][j] == "+" and grid[i][j + 1] == "+":
                corners.append((i, j))
print(corners)
