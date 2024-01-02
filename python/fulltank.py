# fmt: off
from collections import defaultdict
from heapq import heappush, heappop


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


def dijkstra(g, s, e, cap, fuel):
    seen = set()
    dist = defaultdict(lambda: 2**32)
    q = [(fuel[s], s)]
    dist[s] = 0

    while q:
        f, u = heappop(q)

        if u in seen: continue
        if u == e: return dist[u]

        seen.add(u)

        for v in g.get_neighbours(u):
            consumed_fuel = g.get_weight(u, v)
            if min(cap, f + fuel[v]) - consumed_fuel < 0: continue
            if dist[v] > dist[u] + consumed_fuel:
                f -= consumed_fuel
                dist[v] = dist[u] + consumed_fuel
                heappush(q, (min(cap, f + fuel[v]), v))
                # q.cappend((f - consumed_fuel, v))
    return None



def main():
    n, m = map(int, input().split())
    g = WeightedGraph(n, m)
    fuel_prices = [*map(int, input().split())]

    for _ in range(m):
        u, v, w = map(int, input().split())
        g.add_edge(u, v, w)

    q = int(input())
    dests = []
    for _ in range(q):
        dests.append([*map(int, input().split())])

    for f,s,e in dests:
        # print(s,e,f)
        ans = dijkstra(g,s,e,f,fuel_prices)
        print(ans)



if __name__ == "__main__":
    main()
