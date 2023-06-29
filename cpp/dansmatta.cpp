#include <bits/stdc++.h>
using namespace std;
int main() {
    int x;
    cin >> x;

    string l = "V";
    string r = "H";
    int moves = 0;

    for (int i = 0; i < x; i++) {
        string m;
        cin >> m;
        if (m.length() == 1) {
            if (l == m || r == m) {
                continue;
            } else if (m == "U") {
                l = m;
            } else if (m == "V") {
                l = m;
            } else if (m == "D") {
                r = m;
            } else if (m == "H") {
                r = m;
            }
            moves++;
        } else {
            string s1(&m[0]);
            if (l == m[0] || l == m[1]) {
            }
        }
    }

    return 0;
}
