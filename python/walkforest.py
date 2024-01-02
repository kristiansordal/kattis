# class Node:
#     def __init__(self):


class WeightedGraph:
    def __init__(self, vertices, edges):
        self.n = vertices
        self.m = edges
        self.adj = [[0 for _ in range(self.n)] for _ in range(self.n)]

    def add_edge(self, u, v, w):
        self.adj[u][v] = w

    def remove_edge(self, u, v):
        self.adj[u][v] = 0

    def get_weight(self, u, v):
        return self.adj[u][v]

    def get_neighbours(self, v):
        return [i for i in range(self.n) if self.adj[v][i] != 0]


def dijkstra(g,root,goal):



def main():
    n, m = map(int, input().split())
    g = WeightedGraph(n, m)

    for _ in range(m):
        u, v, w = map(int, input().split())
        g.add_edge(u, v, w)


if __name__ == "__main__":
    main()
