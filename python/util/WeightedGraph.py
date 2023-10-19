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
        self.__size = 0

    def addNode(self, v):
        if v not in self.adj:
            self.adj[v] = set()
            self.vertices.add(v)
            self.__size += 1

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

    def size(self):
        return self.__size


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


def prim(g, root):
    q = []
    dist = {}
    mst = set()
    found = set()
    prev = {}

    for v in g.getNodes():
        heappush(q, Node(v, inf))
        dist[v] = inf
        prev[v] = None

    dist[root] = 0
    heappush(q, Node(root, 0))

    while len(mst) != g.size() - 1:
        curr = heappop(q)
        if curr.id in found:
            continue

        found.add(curr.id)

        if prev[curr.id] is not None:
            mst.add((prev[curr.id], curr.id))

        for n in g.getNeighbours(curr.id):
            if n not in found:
                weight = g.getWeight(curr.id, n)

                if weight < dist[n]:
                    dist[n] = weight
                    prev[n] = curr.id
                    heappush(q, Node(n, weight))

    return mst


def getPath(path, root, goal):
    p = []
    p.append(root)

    while root != goal:
        p.append(path[root])
        root = path[root]

    return " -> ".join(map(str, reversed(p)))


def main():
    g = WeightedGraph()

    g.addNode(1)
    g.addNode(2)
    g.addNode(3)
    g.addNode(4)
    g.addNode(5)
    g.addNode(6)
    g.addNode(7)

    g.addEdge(1, 2, 20)
    g.addEdge(1, 3, 32)
    g.addEdge(1, 4, 45)
    g.addEdge(1, 5, 58)
    g.addEdge(1, 6, 64)
    g.addEdge(1, 7, 45)
    g.addEdge(2, 3, 32)
    g.addEdge(2, 4, 63)
    g.addEdge(2, 5, 42)
    g.addEdge(2, 6, 54)
    g.addEdge(2, 7, 28)
    g.addEdge(3, 4, 51)
    g.addEdge(3, 5, 40)
    g.addEdge(3, 6, 36)
    g.addEdge(3, 7, 59)
    g.addEdge(4, 5, 91)
    g.addEdge(4, 6, 85)
    g.addEdge(4, 7, 89)
    g.addEdge(5, 6, 22)
    g.addEdge(5, 7, 51)
    g.addEdge(6, 7, 70)

    mst = prim(g, 1)

    s = 0
    for e in mst:
        s += g.weights[e]
    print(s)

    print(sorted(mst))


if __name__ == "__main__":
    main()
