#include <bits/stdc++.h>

using namespace std;
void knapsack(vector<int> v, vector<int> w, int W, vector<int> &seq, int &len) {
    int n = v.size();
    vector<int> dp(W + 1, 0);
    vector<vector<bool>> ids(n, vector<bool>(W + 1, false));

    for (int i = 0; i < n; i++) {
        for (int j = W; j >= w[i]; j--) {
            if (dp[j - w[i]] + v[i] > dp[j]) {
                dp[j] = dp[j - w[i]] + v[i];
                ids[i][j] = true;
            }
        }
    }

    int i = n - 1, j = W;
    seq.clear();

    while (i >= 0 && j >= 0) {
        if (ids[i][j]) {
            seq.push_back(i);
            j -= w[i];
        }

        i--;
    }

    len = seq.size();
    reverse(seq.begin(), seq.end());
}

int main() {
    int n, W;
    vector<int> w;
    vector<int> v;

    while (cin >> W && cin >> n) {
        w.assign(n, 0);
        v.assign(n, 0);

        for (int i = 0; i < n; i++) {
            int x, y;
            cin >> x >> y;
            v[i] = x;
            w[i] = y;
        }

        vector<int> seq;
        int len;
        knapsack(v, w, W, seq, len);

        cout << len << endl;
        for (auto &i : seq) {
            cout << i << " ";
        }
        cout << endl;
    }
    return 0;
}
