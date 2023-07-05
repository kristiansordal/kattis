#include <bits/stdc++.h>
using namespace std;
int main() {

    // int x;
    // cin >> x;
    vector<int> nums;

    int x = 22 ^ (22 << 1);
    int y = 55 ^ (55 << 1);
    int a = 58 | (58 >> 1);
    int b = 89 ^ (89 << 1);
    int c = 22 | 22;
    cout << x << endl;
    cout << a << endl;
    cout << y << endl;
    cout << b << endl;
    cout << c << endl;

    return 0;
}
