#include <bits/stdc++.h>
using namespace std;
int main() {
    int k, n;
    int time = 210;
    cin >> k >> n;

    set<int> people;

    for (int i = 0; i < n; i++) {
        int t;
        char a;

        cin >> t >> a;

        time -= t;
        if (a == 'T') {
            k = (k + 1) % 8;
        }
    }

    cout << k << endl;

    return 0;
}
