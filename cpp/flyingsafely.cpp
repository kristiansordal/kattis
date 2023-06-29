#include <bits/stdc++.h>

int bfs(std::unordered_map<int, std::vector<int>> graph, int source) {
    std::queue<int> q;
    std::set<int> visited;
    std::vector<int> parent(graph.size(), -1);
    int l = 0;

    q.emplace(source);
    visited.emplace(source);
    parent[source] = -1;

    while (visited.size() != graph.size()) {
        int curr = q.front();
        q.pop();

        for (auto n : graph[curr]) {
            if (visited.find(n) == visited.end()) {
                visited.emplace(n);
                q.push(n);
                l++;
            }
        }
    }
    return l;
}
int main() {
    int cases;
    std::cin >> cases;

    for (int i = 0; i < cases; i++) {
        int n, m;
        std::cin >> n >> m;
        std::unordered_map<int, std::vector<int>> routes;

        int a, b;
        for (int j = 0; j < m; j++) {
            std::cin >> a >> b;
            if (routes[a].empty()) {
                routes[a] = std::vector<int>{b};
            } else {
                routes[a].push_back(b);
            }
            if (routes[b].empty()) {
                routes[b] = std::vector<int>{a};
            } else {
                routes[b].push_back(b);
            }
        }

        int l = bfs(routes, a);
        std::cout << l << std::endl;

        routes.clear();
    }
    return 0;
}
