from heapq import heappop, heappush
from math import inf


class Node:
    def __init__(self, id, weight):
        self.id = id
        self.weight = weight

    def __lt__(self, obj):
        return self.weight < obj.weight


class WeightedGraph:
    def __init__(self):
        self.vertices = set()
        self.adj = {}
        self.weights = {}
        self.size = 0

    def addNode(self, v):
        if v not in self.adj:
            self.adj[v] = set()
            self.vertices.add(v)
            self.size += 1

    def addEdge(self, a, b, weight):
        self.adj[a].add(b)
        self.adj[b].add(a)
        self.weights[(a, b)] = weight
        self.weights[(b, a)] = weight

    def getWeight(self, u, v):
        return self.weights[(u, v)]

    def getNeighbours(self, v):
        return self.adj[v]

    def getNodes(self):
        return self.vertices


def dijkstra(g, root, goal):
    q = []
    prev = {}
    dist = {}
    seen = set()
    prev[root] = root
    dist[root] = 0

    for v in g.getNodes():
        if v != root:
            heappush(q, Node(v, inf))
            prev[v] = None
            dist[v] = inf

    heappush(q, Node(root, 0))

    while q:
        curr = heappop(q)
        seen.add(curr.id)

        if goal in seen:
            return prev

        for n in g.getNeighbours(curr.id):
            d = curr.weight + g.getWeight(curr.id, n)

            if d < dist[n]:
                dist[n] = d
                prev[n] = curr.id
                heappush(q, Node(n, d))

    return prev


def getPath(path, root, goal):
    p = []
    p.append(root)

    while root != goal:
        p.append(path[root])
        root = path[root]

    return " -> ".join(map(str, reversed(p)))


def main():
    g = WeightedGraph()

    for i in range(10):
        g.addNode(i)

    g.addEdge(0, 1, 10)
    g.addEdge(0, 2, 5)
    g.addEdge(0, 3, 5)
    g.addEdge(2, 4, 1)
    g.addEdge(3, 4, 2)

    path = dijkstra(g, 0, 4)
    p = getPath(path, 4, 0)

    print(p)


if __name__ == "__main__":
    main()
