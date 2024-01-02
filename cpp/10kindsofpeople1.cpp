#include <bits/stdc++.h>
#include <sstream>

using namespace std;

bool bfs(vector<vector<int>> &grid, int r1, int c1, int r2, int c2, int type) {
    if (type != grid[r1][c1]) {
        return false;
    }
    queue<pair<int, int>> q;
    vector<vector<bool>> visited(grid.size(), vector<bool>(grid[0].size(), false));
    vector<pair<int, int>> dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    q.push({r1, c1});
    visited[r1][c1] = true;

    while (q.size() > 0) {
        auto c = q.front();
        q.pop();

        if (c.first == r2 && c.second == c2) {
            return true;
        }

        for (auto d : dirs) {
            int x = c.first + d.first;
            int y = c.second + d.second;

            if (x >= 0 && x < grid.size() && y >= 0 && y < grid[0].size() && !visited[x][y] &&
                !(grid[x][y] ^ grid[r1][c1])) {
                q.push({x, y});
                visited[x][y] = true;
            }
        }
    }
    return false;
}
int Main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int r, c, n, r1, c1, r2, c2;
    vector<vector<int>> grid;
    cin >> r >> c;
    grid.assign(r, vector<int>());

    for (int i = 0; i < r; i++) {
        string s;
        cin >> s;

        for (auto &j : s) {
            grid[i].push_back(j - '0');
        }
    }

    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> r1 >> c1 >> r2 >> c2;

        r1--;
        c1--;
        r2--;
        c2--;

        if (grid[r1][c1] != grid[r2][c2]) {
            cout << "neither" << endl;
            continue;
        }

        bool bin = bfs(grid, r1, c1, r2, c2, 0);
        bool dec = bfs(grid, r1, c1, r2, c2, 1);

        if (bin) {
            cout << "binary" << endl;
        } else if (dec) {
            cout << "decimal" << endl;
        } else {
            cout << "neither" << endl;
        }
    }

    return 0;
}
