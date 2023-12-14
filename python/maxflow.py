from collections import defaultdict
from math import inf


class WeightedGraph:
    def __init__(self, vertices, edges):
        self.numVertices = vertices
        self.numEdges = edges
        self.vertices = []
        self.adj = [[0 for _ in range(vertices)] for _ in range(vertices)]
        self.capacity = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, a: int, b: int, weight: int):
        self.adj[a][b] = weight
        self.capacity[a][b] = weight
        self.capacity[b][a] = 0

    def remove_edge(self, a: int, b: int):
        self.adj[a][b] = 0

    def set_capacity(self, a: int, b: int, c: int):
        self.capacity[a][b] = c

    def get_weight(self, a: int, b: int):
        return self.adj[a][b]

    def get_capacity(self, a: int, b: int):
        return self.capacity[a][b]

    def get_neighbours(self, node: int):
        return [i for i in range(self.numVertices) if self.adj[node][i] > 0]

    def get_vertices(self):
        return self.vertices


def dfs(graph, s, t):
    found = set()
    q = []
    q.append(s)
    path = defaultdict(list)
    while q:
        c = q.pop()
        if c not in found:
            found.add(c)

            for n in graph.get_neighbours(c):
                if graph.get_capacity(c, n) > 0:
                    q.append(n)
                    path[n].append(c)
                    if n == t:
                        return path
    return path


def get_path(graph, path, s, t):
    p = []
    c = t
    min_flow = inf
    if t not in path.keys():
        return [], 0

    while c != s:
        p.append((path[c][0], c))
        w = graph.get_weight(path[c][0], c)
        if w < min_flow:
            min_flow = w
        c = path[c][0]
    return list(reversed(p)), min_flow


def maximum_flow(graph, source, sink):
    flow = defaultdict(lambda: 0)
    path = dfs(graph, source, sink)
    augmenting_path, min_flow = get_path(graph, path, source, sink)

    while len(augmenting_path) > 0:
        for k, v in augmenting_path:
            flow[(k, v)] += int(min_flow)
            flow[(v, k)] -= int(min_flow)
            graph.set_capacity(k, v, graph.get_weight(k, v) - flow[(k, v)])
            graph.set_capacity(v, k, flow[(v, k)])

        path = dfs(graph, source, sink)
        augmenting_path, min_flow = get_path(graph, path, source, sink)

    return flow


def main():
    n, m, s, t = map(int, input().split())
    g = WeightedGraph(n, m)

    for _ in range(m):
        u, v, w = map(int, input().split())
        g.add_edge(u, v, w)

    flow = maximum_flow(g, s, t)

    fl = m = 0
    for f in flow:
        if flow[f] > 0:
            m += 1
            if f[1] == t:
                fl += flow[f]

    print(f"{n} {fl} {m}")

    for f in flow:
        if flow[f] > 0:
            print(f"{f[0]} {f[1]} {flow[f]}")


if __name__ == "__main__":
    main()
