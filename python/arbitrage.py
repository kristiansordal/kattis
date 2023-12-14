from math import inf, log


class DirectedWeightedGraph:
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
        self.weights[(a, b)] = weight

    def getWeight(self, u, v):
        return self.weights[(u, v)]

    def getNeighbours(self, v):
        return self.adj[v]

    def getNodes(self):
        return self.vertices

    def size(self):
        return self.__size


def bellmann_ford(g, s):
    dist = {}

    for v in g.getNodes():
        dist[v] = inf

    dist[s] = 0

    for _ in range(g.size()):
        for k, w in g.weights.items():
            u, v = k
            if dist[u] + log(w) < dist[v]:
                dist[v] = dist[u] + log(w)

    if dist[s] < 0:
        return False
    return True


def main():
    n = int(input())

    while n != 0:
        g = DirectedWeightedGraph()
        currencies = input().split()
        for c in currencies:
            g.addNode(c)

        x = int(input())

        for _ in range(x):
            f, t, e = input().split()
            e = int(e.split(":")[0]) / int(e.split(":")[-1])
            g.addEdge(f, t, e)

        if all(bellmann_ford(g, x) for x in currencies):
            print("Ok")
        else:
            print("Arbitrage")

        n = int(input())


if __name__ == "__main__":
    main()
