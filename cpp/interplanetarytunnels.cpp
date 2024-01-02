#include <bits/stdc++.h>

using namespace std;
template <typename T> class Graph {
  private:
    vector<vector<int>> adj;

  public:
    void add_edge(int v, int u) {
        adj[v][u] = 1;
        adj[u][v] = 1;
    }

    vector<int> neighbors(int v) {
        vector<int> result;
        for (int i = 0; i < adj.size(); i++) {
            if (adj[v][i] == 1) {
                result.push_back(i);
            }
        }
        return result;
    }

    int size() { return adj.size(); }

    Graph(int n) { adj.assign(n, vector<int>(n, 0)); }
};

int bfs(Graph<int> &g, int s, int e) {
    queue<int> q;
    q.push(s);
    unordered_map<int, int> dist;
    set<int> seen;
    while (!q.empty()) {
        int v = q.front();
        q.pop();

        if (v == e)
            return dist[v];

        if (seen.find(v) != seen.end())
            continue;

        seen.insert(v);

        for (auto u : g.neighbors(v)) {
            dist[u] = dist[v] + 1;
            q.push(u);
        }
    }
    return -1;
}
int main() {
    int n, m, s, e;
    cin >> n >> m >> s >> e;

    Graph<int> g(n);

    for (int i = 0; i < m; i++) {
        int v, u;
        cin >> v >> u;
        g.add_edge(v, u);
    }

    int p = bfs(g, s, e);

    if (p % 2 == 0) {
        cout << (int)floor(p / 2) << endl;
    } else {
        cout << ((int)floor(p / 2)) + 1 << endl;
    }

    return 0;
}
