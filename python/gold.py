m,n = map(int, input().split())
grid = [[x for x in input().strip()] for _ in range(n)]
# start =[[(i,j) for j,c in enumerate(r) if c == "P"] for i,r in enumerate(grid) ]
start = []

for i,r in enumerate(grid):
    for j,c in enumerate(r):
        if c == "P":
            start.append((i,j))

q  = [start[0]]
v = set()
dirs = [(0,1),(0,-1),(1,0),(-1,0)]
gold = 0

while q:
    r,c = q.pop(0)

    if grid[r][c] == "T":
        break

    for dr,dc in dirs:
        nr,nc = r+dr,c+dc


        if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] not in "#" and (nr,nc) not in v:
            v.add((nr,nc))
            q.append((nr,nc))

            if grid[nr][nc] == "G":
                gold += 1
print(gold)





