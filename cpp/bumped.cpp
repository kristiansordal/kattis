// #include <bits/stdc++.h>
// using namespace std;

#include <bits/stdc++.h>
using namespace std;

class WeightedGraph {
   private:
    int edges;
    unordered_map<int, set<int>> adjacencyList;
    set<int> vertices;

   public:
    void addVertex(int v) {
        bool changed = vertices.find(v) == vertices.end();
        vertices.emplace(v);
        if (changed) {
            adjacencyList[v] = {};
        }
    }
};
int main() {}
// // Structure to represent an edge with weight
// struct Edge {
//     int destination;
//     int weight;
//     Edge(int dest, int w) : destination(dest), weight(w) {}
//     bool operator>(Edge& e) { return weight > e.weight; }
// };
// struct Flight {
//     int to;
//     int from;
//     Flight(int from, int to) : from(from), to(to){};
// };

// class WeightedGraph {
//    private:
//     int numVertices;
//     int numNodes;
//     vector<vector<Edge>> graph;
//     unordered_map<int, int> dist;

//    public:
//     WeightedGraph(int numV, int numNodes) : numVertices(numV), graph(numV), dist(numNodes) {}

//     void addEdge(int source, int destination, int weight) {
//         graph[source].push_back(Edge(destination, weight));
//         graph[destination].push_back(Edge(source, weight));  // Add the reverse edge
//         dist[source] = INT_MAX;
//         dist[destination] = INT_MAX;
//     }

//     void updDist(int node, int w) { dist[node] = w; }

//     vector<Edge> getNeighbours(int node) { return graph[node]; }
// };

// vector<Edge> dijkstra(WeightedGraph& g, Edge source, Edge goal) {
//     set<Edge> visited = {source};
//     priority_queue<Edge, vector<Edge>> q;
//     unordered_map<Edge, Edge> prev;
//     q.push(source);
//     g.updDist(source.destination, 0);
// }

// int main() {
//     int n, m, f, s, t;
//     cin >> n >> m >> f >> s >> t;
//     WeightedGraph graph(m, n);
//     vector<Flight> flights;

//     for (int i = 0; i < m; i++) {
//         int x, y, c;
//         cin >> x >> y >> c;

//         graph.addEdge(x, y, c);
//     }

//     for (int i = 0; i < f; i++) {
//         int x, y;
//         cin >> x >> y;
//         flights.push_back(Flight(x, y));
//     }

//     return 0;
// }
