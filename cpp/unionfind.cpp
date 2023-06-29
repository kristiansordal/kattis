#include <bits/stdc++.h>
#include <sstream>
using namespace std;

template <typename T> struct Node {
    T parent;
    T node;

    Node() : parent(T()), node(T()){};
    Node(T _parent, T _node) {
        parent = _parent;
        node = _node;
    }
};

template <typename T> class UnionFind {
  public:
    unordered_map<T, Node<T>> components;
    unordered_map<T, int> rank;

    void makeSet(T &t) {
        if (components.find(t) == components.end()) {
            components[t] = Node<T>(t, t);
            rank[t] = 0;
        }
    }

    T find(T &t) {
        Node<T> curr = components[t];
        if (curr.parent != curr.node) {
            curr.parent = find(curr.parent);
            return curr.parent;
        }
        return t;
    }

    bool connected(T &v, T &u) { return find(v) == find(u); }

    void merge(T &v, T &u) {
        T x = find(v);
        T y = find(u);

        if (x == y) {
            return;
        }

        if (rank[x] < rank[y]) {
            components[x].parent = y;
        } else if (rank[y] < rank[x]) {
            components[y].parent = x;
        } else {
            components[y].parent = x;
            rank[x]++;
        }
        // components[y] = Node<T>(x, y);
    }
};

int main() {
    UnionFind<int> UF;
    int n, q;
    cin >> n >> q;
    for (int i = 0; i < q; i++) {
        string query;
        int x, y;
        cin >> query >> x >> y;
        UF.makeSet(x);
        UF.makeSet(y);

        if (query == "?") {
            if (UF.connected(x, y)) {
                cout << "yes" << endl;
            } else {
                cout << "no" << endl;
            }
        } else {
            UF.merge(x, y);
        }
    }

    return 0;
}
