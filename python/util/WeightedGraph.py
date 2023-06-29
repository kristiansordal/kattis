class WeightedGraph:
    def __init__(self, vertices, nodes):
        self.numVertices = vertices
        self.numNodes = nodes
        self.adj = {}
        self.weights = {}

    def addNode(self, node):
        if node not in self.adj:
            self.adj[node] = set()

    def addEdge(self, a, b, weight):
        self.adj[a].add(b)
        self.adj[b].add(a)
        self.weights[(a, b)] = weight

    def getWeight(self, a, b):
        return self.weights[(a, b)]

    def getNeighbours(self, node):
        return self.adj[node]
