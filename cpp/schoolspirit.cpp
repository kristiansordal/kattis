#include <bits/stdc++.h>
using namespace std;
int main() {
    int x;
    double sum = 0;
    double avg = 0;
    cin >> x;

    for (int i = 0; i < x; i++) {
        int s;
        cin >> s;
        sum += s * pow((4.0 / 5.0), i);
        avg += s;
    }
    cout << sum / 5 << endl;
    cout << sum - (sum / x) << endl;
    cout << avg / x << endl;

    return 0;
}
