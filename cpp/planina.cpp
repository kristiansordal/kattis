#include <bits/stdc++.h>
using namespace std;
int main() {

    long long x;
    cin >> x;
    for (int i = 0; i < 16; i++) {
        cout << pow((pow(2, i) + 1), 2) << endl;
    }

    return 0;
}
