#include <bits/stdc++.h>
using namespace std;
int main() {
    int guess;
    int lo = 0;
    int hi = 1000;
    int mid = hi - (hi - lo) / 2;
    cout << mid << endl;
    string response;
    cin >> response;

    while (response != "correct") {
        if (response == "lower") {
            hi = mid - 1;
        } else if (response == "higher") {
            lo = mid + 1;
        }
        mid = hi - (hi - lo) / 2;
        cout << mid << endl;
        cin >> response;
    }

    return 0;
}
