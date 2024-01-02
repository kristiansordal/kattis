#include <bits/stdc++.h>
using namespace std;
int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<char>> grid;
    grid.assign(n, vector<char>(m, ' '));
    unordered_map<char, pair<int, int>> dirs = {{'N', {-1, 0}}, {'S', {1, 0}}, {'E', {0, 1}}, {'W', {0, -1}}};

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            char c;
            cin >> c;
            grid[i][j] = c;
        }
    }

    queue<pair<int, int>> q;
    q.push(make_pair(0, 0));
    int s = 0;

    while (q.size() > 0) {
        auto [r, c] = q.front();
        q.pop();

        if (r <= -1 || r >= n || c <= -1 || c >= m) {
            cout << "Out" << endl;
            return 0;
        }
        if (grid[r][c] == 'T') {
            cout << s << endl;
            return 0;
        }
        s++;
        auto d = dirs[grid[r][c]];
        q.push(make_pair(r + d.first, c + d.second));
    }

    return 0;
}
