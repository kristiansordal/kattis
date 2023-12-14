import networkx as nx
from heapq import heappush, heappop, heapify
import sys


class Node:
    def __init__(self, node, weight, shamans, titans):
        self.node = node
        self.weight = weight
        self.shamans = shamans
        self.titans = titans

    def __eq__(self, o):
        return self.weight == o.weight and self.shamans == o.shamans and self.titans == o.titans

    def __lt__(self, o):
        if self.titans != o.titans:
            return self.titans < o.titans
        elif self.shamans != o.shamans:
            return self.shamans < o.shamans
        else:
            return self.weight < o.weight

    def __str__(self):
        return f"{self.weight} {self.shamans} {self.titans}"


def dijkstra(g: nx.Graph, s, e):
    v = set()
    dist = {}
    q = [Node(s, 0, 0, 0)]
    for n in g.nodes:
        if n != s:
            dist[n] = Node(n, 2**32, 2**32, 2**32)

    dist[s] = Node(s, 0, 0, 0)
    heapify(q)

    while e not in v or q:
        if len(q) == 0:
            break

        c = heappop(q)
        v.add(c.node)

        for n in g.neighbors(c.node):
            w = g.edges[c.node, n]["weight"]
            col = g.edges[c.node, n]["color"]

            new_node = Node(
                n,
                c.weight + w,
                c.shamans + 1 if col == "1" else c.shamans,
                c.titans + 1 if col == "2" else c.titans,
            )

            v.add(n)

            if (
                (new_node.titans < dist[n].titans)
                or (new_node.titans == dist[n].titans and new_node.shamans < dist[n].shamans)
                or (
                    new_node.titans == dist[n].titans
                    and new_node.shamans == dist[n].shamans
                    and new_node.weight < dist[n].weight
                )
            ):
                dist[n] = new_node
                heappush(q, new_node)
    return dist


def main():
    D = open("fot.txt", "r").read().splitlines()
    g = nx.Graph()
    x = D[0].split()[2]
    y = D[0].split()[3]

    for l in D[1:]:
        l = l.split()
        g.add_node(l[0])
        g.add_node(l[1])
        g.add_edge(l[0], l[1], weight=int(l[2]), color=l[3])

    dist = dijkstra(g, x, y)
    if y not in dist.keys() or dist[y].weight == 2**32:
        print("IMPOSSIBLE")
    else:
        print(dist[y])


if __name__ == "__main__":
    main()
