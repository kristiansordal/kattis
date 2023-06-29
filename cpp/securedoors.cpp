#include <bits/stdc++.h>
using namespace std;
int main() {
    int x;

    cin >> x;
    set<string> inside = {};

    for (int i = 0; i < x; i++) {
        string action;
        string person;
        cin >> action >> person;

        if (action == "entry") {
            if (inside.find(person) == inside.end()) {
                cout << person << " entered" << endl;
                inside.emplace(person);
            } else {
                cout << person << " entered"
                     << " (ANOMALY)" << endl;
            }
        } else {
            if (inside.find(person) != inside.end()) {
                cout << person << " exited" << endl;
                inside.erase(person);
            } else {
                cout << person << " exited"
                     << " (ANOMALY)" << endl;
            }
        }
    }

    return 0;
}
