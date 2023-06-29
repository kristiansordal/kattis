#include <bits/stdc++.h>

#include <ranges>

using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int x;
    cin >> x;
    vector<string> names;

    for (int i = 0; i < x; i++) {
        string n;
        cin >> n;
        names.push_back(n);
    }

    int y;
    cin >> y;
    vector<string> nicks;
    auto indecies = ranges::iota(0, x);

    // cout << indecies << endl;

    for (int i = 0; i < y; i++) {
        string n;
        cin >> n;
        nicks.push_back(n);
    }

    for (int i = 0; i < nicks.size(); i++) {
        for (int j = 0; j < names.size(); j++) {
            if (nicks[i] <= names[j]) {
                bool isNick = false;
            }
        }
    }
    return 0;
}
