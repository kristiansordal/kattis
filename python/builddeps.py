from collections import deque, defaultdict
import sys


class DAG:
    def __init__(self):
        self.adj = defaultdict(list)
        self.in_deg = defaultdict(int)

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.in_deg[v] += 1

    def neighbors(self, u):
        return self.adj[u]

    def in_degree(self, u):
        return self.in_deg[u]


def topsort(g, root):
    source = deque([n for n in g.adj if g.in_degree(n) == 0 and n != root])
    while source:
        curr = source.popleft()
        for n in g.neighbors(curr):
            g.in_deg[n] -= 1
            if g.in_degree(n) == 0 and n != root:
                source.append(n)

    source.append(root)

    while source:
        curr = source.popleft()
        print(curr)
        for n in g.neighbors(curr):
            g.in_deg[n] -= 1
            if g.in_degree(n) == 0:
                source.append(n)


def main():
    n = int(input())
    g = DAG()

    for _ in range(n):
        nodes = sys.stdin.readline().split()
        to = nodes[0][:-1]
        ins = nodes[1:]

        for i in ins:
            g.add_edge(i, to)

    changed = input().strip()
    topsort(g, changed)


if __name__ == "__main__":
    main()
