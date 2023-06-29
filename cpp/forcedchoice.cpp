#include <bits/stdc++.h>
using namespace std;
int main() {
    int n, p, s;
    cin >> n >> p >> s;

    vector<set<int>> sets;
    for (int i = 0; i < s; i++) {
        int x;
        cin >> x;
        set<int> s;
        for (int i = 0; i < x; i++) {
            int y;
            cin >> y;
            s.emplace(y);
        }

        if (s.find(p) == s.end()) {
            cout << "REMOVE" << endl;
        } else {
            cout << "KEEP" << endl;
        }
    }

    return 0;
}
