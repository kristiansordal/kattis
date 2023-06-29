#include <bits/stdc++.h>
using namespace std;
int main() {
    int x;
    cin >> x;
    double y = 400;

    for (int i = 0; i < x; i++) {
        double cals;
        cin >> cals;
        cout << ceil(cals / y) << endl;
    }

    return 0;
}
