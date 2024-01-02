#include <bits/stdc++.h>
using namespace std;

void subsequence(vector<int> s, vector<int> &dp, vector<vector<int>> &seq, int n) {
    for (int i = 0; i < n; i++) {
        if (i > 0) {
            int opt = 0;
            vector<int> ids;

            for (int j = 0; j < i; j++) {
                if (s[j] < s[i] && dp[i] > opt) {
                    opt = dp[j];
                    ids = seq[j];
                }
            }

            if (opt == 0) {
                dp[i] = 1;
                seq[i] = {i};
            } else {
                dp[i] = opt + 1;
                seq[i] = ids;
                seq[i].push_back(i);
            }
        } else {
            dp[i] = 1;
            seq[i] = {i};
        }
    }
}
int main() {

    int n;

    while (cin >> n) {
        vector<int> s(n);
        for (int i = 0; i < n; i++) {
            int x;
            cin >> x;
            s[i] = x;
        }
        vector<int> dp(n, 0);
        vector<vector<int>> seq(n, vector<int>());
        subsequence(dp, s, seq, n);

        auto m = max_element(dp.begin(), dp.end());
        auto id = distance(dp.begin(), m);

        cout << *m << endl;
        for (auto i : seq[id]) {
            cout << i << " ";
        }
        cout << endl;
    }
    return 0;
}
