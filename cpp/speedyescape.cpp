#pragma once
#include <iostream>
#include <set>
#include <unordered_map>
#include <vector>

using namespace std;
template <typename T> class WeightedGraph {
  private:
    vector<vector<T>> adj;
    set<T> vertices;
    vector<T> exits;
    int size;

  public:
    bool contains(T v) { return vertices.find(v) != vertices.end(); }
    void add_node(T v) {
        if (!contains(v)) {
            vertices.emplace(v);
        }
    }

    void add_exit(T v) { exits.push_back(v); }

    void add_edge(T v, T u, int w) {
        adj[v][u] = w;
        adj[u][v] = w;
    }

    vector<T> get_neighbours(T v) {
        vector<T> neighbours;
        for (int i = 0; i < size; i++) {
            if (adj[v][i] != 0) {
                neighbours.push_back(i);
            }
        }
        return neighbours;
    }

    int get_weight(T v, T u) { return adj[v][u]; }

    WeightedGraph(int n)
        : size(n) {
        adj.assign(n, vector<T>(n, 0));
    }
};

int main() {
    int n, m, e;

    cin >> n >> m >> e;
    WeightedGraph<int> g(n);

    for (int i = 0; i < m; i++) {
        int v, u, w;
        cin >> v >> u >> w;
        g.add_node(v);
        g.add_node(u);
        g.add_edge(v, u, w);
    }

    for (int i = 0; i < e; i++) {
        int v;
        cin >> v;
        g.add_exit(v);
    }

    int x, y;
    cin >> x >> y;
}
