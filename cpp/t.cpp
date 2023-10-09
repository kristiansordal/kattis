#include <bits/stdc++.h>
#include <tuple>

using namespace std;

struct Node;
struct Edge {
    Node *n;
};

struct Node {
    Edge e;
};

void b();

void a() { b(); }

void b() {}

int main() {
    vector<basic_string<array<int, 2>>> a = {{{1, 2}, {2, 6}}};
    return 0;
}
