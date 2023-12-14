def bfs(grid, root):
    visited = set()
    q = []
    q.append(root)
    visited.add(root)
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    path = {}

    while q:
        curr = q.pop(0)
        for d in dirs:
            if grid[curr[0] + d[0]][curr[1] + d[1]] != -1:
                q.append((curr[0] + d[0], curr[1] + d[1]))
                visited.add((curr[0] + d[0], curr[1] + d[1]))
                path[(curr[0] + d[0], curr[1] + d[1])] = curr

    return path


def get_path_length(path, root, end):
    curr = end
    count = 0
    while curr != root:
        curr = path[curr]
        count += 1
    return count


def main():
    r, c = map(int, input().split())
    grid = []

    for _ in range(r):
        r = [int(x) for x in input()]
        r.insert(0, -1)
        r.append(-1)
        grid.append(r)
    grid.insert(0, [-1] * (c + 2))
    grid.append([-1] * (c + 2))
    print(bfs(grid, (1, 1)))


if __name__ == "__main__":
    main()
