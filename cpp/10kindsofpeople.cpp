#include <bits/stdc++.h>
using namespace std;

struct Coordinate {
    int x;
    int y;

    bool operator==(const Coordinate& a) { return x == a.x && y == a.y; }
    bool operator>(const Coordinate& o) const {
        if (x != o.x) {
            return x < o.x;
        } else {
            return y < o.y;
        }
    }
    // bool operator>(const Coordinate& lhs, const Coordinate& rhs) const {
    //     if (rhs.x > lhs.x) {
    //         return true;
    //     } else {
    //         return lhs.y < rhs.y;
    //     }
    // }
    // bool operator>(const Coordinate& a) {return}

    Coordinate(int x, int y) : x(x), y(y){};
};

const vector<Coordinate> neighbours = {Coordinate(1, 0), Coordinate(0, 1),
                                       Coordinate(-1, 0), Coordinate(0, -1)};

vector<Coordinate> getNeighbours(const vector<string>& world,
                                 const Coordinate& node, bool mode) {
    vector<Coordinate> ns;
    if (mode) {
        for (const auto& n : neighbours) {
            int y = node.x + n.x;
            int x = node.y + n.y;
            if (x >= 0 && x < world[0].size() && y >= 0 && y < world.size() &&
                world[y][x] == '0') {
                ns.push_back(Coordinate(x, y));
            }
        }
    } else {
        for (const auto& n : neighbours) {
            int y = node.x + n.x;
            int x = node.y + n.y;
            if (x >= 0 && x < world[0].size() && y >= 0 && y < world.size() &&
                world[y][x] == '1') {
                ns.emplace_back(Coordinate(x, y));
            }
        }
    }
    return ns;
}

int manhattan(const Coordinate& a, const Coordinate& b) {
    return abs(a.x - b.x) + abs(a.y - b.y);
}

string dijkstra(const vector<string>& world, const Coordinate& root,
                const Coordinate& goal, bool mode) {
    // if binary and start is 1
    if (mode && world[root.x][root.y] == '1') {
        return "";
        // if binary and goal is 1
    } else if (mode && world[goal.x][goal.y] == '1') {
        return "";
        // if decimal and start is 0
    } else if ((!mode) && world[root.x][root.y] == '0') {
        return "";
        // if decimal and goal is 0
    } else if (!mode && world[goal.x][goal.y] == '0') {
        return "";
    }

    auto comp = [goal](const Coordinate& a, const Coordinate& b) {
        return (manhattan(a, goal) >= manhattan(b, goal));
    };
    priority_queue<Coordinate, vector<Coordinate>, decltype(comp)> q(comp);
    set<Coordinate> found;
    found.emplace(root);
    q.push(root);

    while (!q.empty()) {
        Coordinate curr = q.top();
        q.pop();

        if (curr == goal) {
            if (mode) {
                return "binary";
            } else {
                return "decimal";
            }
        }

        for (const auto& n : getNeighbours(world, curr, mode)) {
            if (found.find(n) == found.end()) {
                found.emplace(n);
                q.push(n);
            }
        }
    }
    return "";
}
int main() {
    // use dijkstrsa
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int r, c;

    cin >> r >> c;

    vector<string> world;
    world.reserve(r);
    for (int i = 0; i < r; i++) {
        string s;
        cin >> s;

        world.push_back(s);
    }

    int q;
    cin >> q;

    for (int i = 0; i < q; i++) {
        int x1, y1, x2, y2;

        cin >> y1 >> x1 >> y2 >> x2;

        Coordinate start(x1, y1);
        Coordinate goal(x2, y2);

        // binary people can move on 0s
        // decimal people can move on 1s
        string bin = dijkstra(world, start, goal, true);
        string dec = dijkstra(world, start, goal, false);

        if (bin == "" && dec == "") {
            cout << "neither"
                 << "\n";
        } else if (bin == "") {
            cout << dec << "\n";
        } else if (dec == "") {
            cout << bin << "\n";
        }
    }
    return 0;
}
