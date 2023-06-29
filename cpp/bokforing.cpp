#include <bits/stdc++.h>
using namespace std;
int main() {
    int n, q;

    cin >> n >> q;
    unordered_map<int, int> people;
    int v = 0;

    for (int i = 0; i < q; i++) {
        string s;
        cin >> s;
        if (s == "RESTART") {
            int x;
            cin >> x;
            v = x;
            people.clear();
        } else if (s == "SET") {
            int j, x;
            cin >> j >> x;
            people[j] = x;
        } else if (s == "PRINT") {
            int j;
            cin >> j;
            if (people.find(j) == people.end()) {
                cout << v << endl;
            } else {
                cout << people[j] << endl;
            }
        }
    }

    return 0;
}
