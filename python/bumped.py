import math
import heapq


class WeightedGraph:
    def __init__(self, vertices, edges):
        self.numVertices = vertices
        self.numEdges = edges
        self.vertices = []
        self.adj = {}
        self.edges = {}

    def addNode(self, node: int):
        if node not in self.adj:
            self.adj[node] = set()
            self.vertices.append(node)

    def addEdge(self, a: int, b: int, weight: int):
        self.adj[a].add(b)
        self.adj[b].add(a)
        if self.edges.get((a, b), -1) == -1 and self.edges.get((b, a), -1) == -1:
            self.edges[(a, b)] = weight
            self.edges[(b, a)] = weight

    def getWeight(self, a: int, b: int):
        return self.edges.get((a, b), 0)

    def getNeighbours(self, node: int):
        return self.adj[node]

    def getVertices(self):
        return self.vertices


def dijkstra(graph, root, goal):
    dist = {}
    dist[root] = 0
    prev = {}
    seen = set()
    queue = []

    for n in graph.getVertices():
        if n != root:
            dist[n] = math.inf
            prev[n] = None
        heapq.heappush(queue, (dist[n], n))

    while queue:
        _, curr = heapq.heappop(queue)

        if curr in seen:
            continue

        seen.add(curr)

        for n in graph.getNeighbours(curr):
            newDist = dist[curr] + graph.getWeight(curr, n)

            if newDist < dist[n]:
                dist[n] = newDist

            heapq.heappush(queue, (newDist, n))
            prev[n] = curr
            # if n == goal:
            #     return dist, prev
    return dist, prev


def main():
    n, m, f, s, t = map(int, input().split())
    graph = WeightedGraph(n, m)
    flights = []

    for _ in range(m):
        i, j, c = map(int, input().split())
        graph.addNode(i)
        graph.addNode(j)
        graph.addEdge(i, j, c)

    for _ in range(f):
        i, j = map(int, input().split())
        flights.append((i, j))

    dist, prev = dijkstra(graph, s, t)

    # do dijkstra for whole graph
    # do dijkstra on all pairs of flights
    # find most expensive flights
    #
    # maxFlight = 0
    # flightDest = 0
    # flightFrom = 0
    # for x, y in flights:
    #     dist1, prev1 = dijkstra(graph, x, y)
    #     if maxFlight < dist1[y]:
    #         maxFlight = dist1[y]
    #         flightDest = y
    #         flightFrom = x

    # dist2, prev2 = dijkstra(graph, flightDest, t)

    # print(dist[flightFrom])
    # print(maxFlight)
    # print(dist2[t])
    # print(dist[flightFrom] + dist2[t] - maxFlight)


if __name__ == "__main__":
    main()
