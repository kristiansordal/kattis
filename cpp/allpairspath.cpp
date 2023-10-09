#include <bits/stdc++.h>

template <typename T> class Graph {
  private:
    std::unordered_map<T, std::vector<T>> adj_;
    std::set<T> vertices_;
    int size_ = 0;

  public:
    bool contains(T v) { return vertices_.find(v) != vertices_.end(); }
    void addVertex(T v) {
        if (!contains(v)) {
            vertices_.emplace(v);
            size_++;
        }
    }

    void addEdge(T v, T u) {
        if (!contains(v)) {
            throw std::invalid_argument("Error: Node " + std::to_string(v) + " not in graph");
        }
        if (!contains(u)) {
            throw std::invalid_argument("Error: Node " + std::to_string(u) + " not in graph");
        }

        if (adj_[v].size() == 0) {
            adj_[v] = {u};
        } else {
            adj_[v].push_back(u);
        }

        if (adj_[u].size() == 0) {
            adj_[u] = {v};
        } else {
            adj_[u].push_back(v);
        }
    }

    std::vector<T> neighbours(T v) { return adj_[v]; }
    std::set<T> vertices() { return vertices_; }

    int size() { return size_; }
};

template <typename T> struct EdgeKey {
    T v;
    T u;

    EdgeKey(T v_, T u_) : v(v_), u(u_){};

    bool operator==(const EdgeKey &other) const { return v == other.v && u == other.u; }
};

template <typename T> struct std::hash<EdgeKey<T>> {
    size_t operator()(const EdgeKey<T> &key) const {
        size_t h1 = std::hash<T>{}(key.v);
        size_t h2 = std::hash<T>{}(key.u);
        return h1 ^ (h2 << 1);
    }
};

template <typename T> class WeightedGraph : public Graph<T> {

  private:
    std::unordered_map<EdgeKey<T>, int> weight_;

  public:
    int weight(T v, T u) { return weight_[EdgeKey<T>(v, u)]; }

    void addEdge(T v, T u, int w) {
        if (!Graph<T>::contains(v)) {
            throw std::invalid_argument("Error: Node " + std::to_string(v) + " not in graph");
        }
        if (!Graph<T>::contains(u)) {
            throw std::invalid_argument("Error: Node " + std::to_string(u) + " not in graph");
        }

        Graph<T>::addEdge(v, u);

        weight_[EdgeKey(v, u)] = w;
        weight_[EdgeKey(u, v)] = w;
    }
};
int main() {

    int n, m, q;
    WeightedGraph<int> graph{};

    std::cin >> n >> m >> q;
    for (int i = 0; i < m; i++) {
        int u, v, w;
    }
    // while (n != 0 && m != 0 && q != 0) {
    // }

    return 0;
}
