#include <bits/stdc++.h>
using namespace std;
struct Node {
    int id;
    int fuelCost;
    Node(int id, int f) : id(id), fuelCost(f){};
    Node() : id(-1), fuelCost(-1){};
};
struct Edge {
    int length;
    Node from;
    Node to;
    Edge(int l, Node f, Node t) : length(l), from(f), to(t){};
    Edge() : length(-1), from(Node()), to(Node()){};
};

class WeightedGraph {
   private:
    int numNodes;
    int numVertices;
    vector<Edge> roads = {};
    vector<Node> cities;

   public:
    WeightedGraph(int n, int v) : numNodes(n), numVertices(v), cities(n){};

    void addEdge(Node a, Node b, int weight) {
        roads.emplace_back(weight, a, b);
    }

    Node getNode(int id) { return cities[id]; }
    void addEdge(Edge v) { roads.emplace_back(v); }
    void addNode(Node a, int id) { cities[id] = a; }
    vector<Edge> getRoads() { return roads; }
};

void printGraph(WeightedGraph graph) {
    for (const auto& e : graph.getRoads()) {
        cout << "From: " << e.from.id << " To: " << e.to.id
             << " Length: " << e.length << endl;
    }
}

void dijkstra(WeightedGraph graph, Node root, Node goal) {}
int main() {
    int cities, roads;
    vector<int> fuelPrices;
    cin >> cities >> roads;

    WeightedGraph graph(cities, roads);

    // Get the fuel prices
    for (int i = 0; i < cities; i++) {
        int x;
        cin >> x;
        fuelPrices.push_back(x);
    }

    for (int i = 0; i < roads; i++) {
        int from, to, length;
        cin >> from >> to >> length;
        Node a(from, fuelPrices[from]);
        Node b(to, fuelPrices[to]);

        graph.addNode(a, from);
        graph.addNode(b, to);
        graph.addEdge(a, b, length);
    }

    int cars;
    cin >> cars;

    for (int i = 0; i < cars; i++) {
        int s, e, tank;
        cin >> s >> e >> tank;
        // Node root = graph.getNode(s);
        // Node goal = graph.getNode(e);
    }

    printGraph(graph);
    return 0;
}
