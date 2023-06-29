#include <bits/stdc++.h>
using namespace std;
int main() {
    int e, f, c;

    int sodas = 0;
    cin >> e >> f >> c;
    int bottles = e + f;

    while (bottles >= c) {
        int s = bottles / c;
        sodas += s;
        bottles -= s * c;
        bottles += s;
    }

    cout << sodas << endl;
    return 0;
}
