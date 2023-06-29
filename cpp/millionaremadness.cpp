#include <bits/stdc++.h>
using namespace std;
int bfs(vector<vector<int>> grid, int x, int y, int ladder) {
    int offsets[][2] = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1},
                        {0, 1},   {1, -1}, {1, 0},  {1, 1}};
}
int main() {
    int n, m;
    vector<vector<int>> grid;
    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        vector<int> row;
        for (int i = 0; i < m; i++) {
            int x;
            cin >> x;
            row.push_back(x);
        }
        grid.push_back(row);
    }

    return 0;
}
