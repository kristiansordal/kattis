#include <bits/stdc++.h>
using namespace std;

template <typename T> class WeightedGraph {
  private:
    vector<vector<T>> adj;
    vector<vector<T>> capacity;

  public:
    WeightedGraph(int n) {
        adj.assign(n, std::vector<T>(n, 0));
        capacity.assign(n, std::vector<T>(n, 0));
    }

    void add_edge(int u, int v, T w) {
        adj[u][v] = w;
        capacity[u][v] = w;
    }

    void set_capacity(int u, int v, T w) { capacity[u][v] = w; }
    int get_weight(int u, int v) { return adj[u][v]; }
    int get_capacity(int u, int v) { return capacity[u][v]; }
    vector<vector<T>> capacity_matrix() { return capacity; }
    int size() { return adj.size(); }

    std::vector<T> get_neighbors(int u) {
        std::vector<int> neighbors;
        for (int i = 0; i < adj[u].size(); i++) {
            if (adj[u][i] != 0) {
                neighbors.push_back(i);
            }
        }
        return neighbors;
    }
};

template <typename T> bool dfs(WeightedGraph<T> g, vector<T> &path, T s, T t) {
    vector<bool> visited(g.size(), false);
    visited[s] = true;
    queue<int> st;
    st.push(s);

    while (!st.empty()) {
        int u = st.front();
        st.pop();

        for (int v : g.get_neighbors(u)) {
            if (!visited[v] && g.get_capacity(u, v) > 0) {
                st.push(v);
                visited[v] = true;
                path[v] = u;
                if (v == t) {
                    return true;
                }
            }
        }
    }
    return false;
}

template <typename T> int maximum_flow(WeightedGraph<T> &g, T s, T t) {
    vector<T> path(g.size());
    vector<vector<int>> flow;
    int maxflow = 0;

    while (dfs(g, path, s, t)) {
        int flow = 1 << 30;

        for (int n = t; n != s; n = path[n]) {
            int parent = path[n];
            flow = min(flow, g.get_capacity(parent, n));
        }

        for (int n = t; n != s; n = path[n]) {
            int parent = path[n];
            g.set_capacity(parent, n, g.get_capacity(parent, n) - flow);
            g.set_capacity(n, parent, g.get_capacity(n, parent) + flow);
        }
        maxflow += flow;
    }
    return maxflow;
}

int main() {
    int n, m, s, t, u, v, w;

    cin >> n >> m >> s >> t;

    WeightedGraph<int> g(n);

    for (int i = 0; i < m; i++) {
        cin >> u >> v >> w;
        g.add_edge(u, v, w);
    }

    int maxflow = maximum_flow(g, s, t);
    auto cap = g.capacity_matrix();
    int flow_edges = 0;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (g.get_weight(i, j) - cap[i][j] > 0) {
                flow_edges++;
            }
        }
    }

    std::cout << n << " " << maxflow << " " << flow_edges << std::endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (g.get_weight(i, j) - cap[i][j] > 0) {
                std::cout << i << " " << j << " " << g.get_weight(i, j) - cap[i][j] << std::endl;
            }
        }
    }

    return 0;
}
