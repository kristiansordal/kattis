from heapq import heappop, heappush
import sys
from math import inf


class Node:
    def __init__(self, id, weight, fuel):
        self.id = id
        self.weight = weight
        self.fuel = fuel

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


def dijkstra(g, root, goal, prices, capacity):
    q = []
    prev = {}
    dist = {}
    seen = set()
    prev[root] = root
    dist[root] = 0

    for v in g.getNodes():
        if v != root:
            heappush(q, Node(v, inf, -1))
            prev[v] = None
            dist[v] = inf

    heappush(q, Node(root, 0, 20))
    fuel = capacity

    while q:
        curr = heappop(q)
        seen.add(curr.id)

        # if goal in seen:
        #     return dist

        for n in g.getNeighbours(curr.id):
            weight = g.getWeight(curr.id, n)

            # check if we can go along this road
            if weight <= capacity:
                # check if we can go with the fuel we have
                if weight <= fuel:
                    d = curr.weight + weight * prices[n]

                    if d < dist[n]:
                        dist[n] = d
                        prev[n] = curr.id
                        heappush(q, Node(n, d))
                else:
                    fuel = capacity

                    dist[curr.id] = dist[curr.id] + (capacity - fuel) * prices[curr.id]

    return dist


def getPath(path, root, goal):
    p = []
    p.append(root)

    while root != goal:
        p.append(path[root])
        root = path[root]

    return " -> ".join(map(str, reversed(p)))


def main():
    g = WeightedGraph()

    _, m = map(int, input().split())

    prices = list(map(int, sys.stdin.readline().split()))
    print(prices)

    for _ in range(m):
        x, y, z = map(int, input().split())
        g.addNode(x)
        g.addNode(y)
        g.addEdge(x, y, z)

    queries = int(input())

    for _ in range(queries):
        capacity, y, z = map(int, input().split())
        p = dijkstra(g, y, z, prices, capacity)
        print(p[z])


if __name__ == "__main__":
    main()
