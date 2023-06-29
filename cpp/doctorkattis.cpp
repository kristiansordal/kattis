#include <bits/stdc++.h>

#include <iostream>
#include <sstream>
#include <unordered_map>
#define ll long long

using namespace std;
struct compareCats {
    bool operator()(const int &a, const int &b) const { return a > b; }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    ll n;
    cin >> n;

    unordered_map<string, pair<ll, ll>> cats;
    map<int, map<string, ll>, compareCats> queue;

    int f, infection, updateInfection;
    ll arrival = 0;
    string name;

    for (int i = 0; i < n; i++) {
        string cat;
        cin >> f;

        switch (f) {
            case 0: {
                cin >> name >> infection;
                cats[name] = make_pair(infection, arrival);
                queue[infection].insert(make_pair(name, arrival++));
            }
            case 1: {
                cin >> name >> updateInfection;
                ll tempID =
                // cats[name].first += updateInfection;
            }
            case 2: {
            }
            case 3: {
            }
        }
        // if (f == 0) {
        //     cats.emplace(line[1],
        //                  make_pair(stoi(line[2]), arrival++));
        // } else if (f == 1) {
        //     auto it = cats.find(line[1]);
        //     pair<int, int> val = cats.at(line[1]);
        //     if (it != cats.end()) {
        //         it->second =
        //             make_pair(val.first + stoi(line[2]),
        //             val.second);
        //     }
        // } else if (f == 2) {
        //     cats.erase(line[1]);
        // } else if (f == 3) {
        //     if (cats.empty()) {
        //         cout << "The clinic is empty" << endl;
        //     } else {
        //         // auto max = max_element(
        //         //     cats.begin(), cats.end(), [](const auto &a, const auto
        //         //     &b) {
        //         //         return a.second.first <= b.second.first;
        //         //     });
        //         // cout << max->first << endl;
        //         cout << cats.rbegin()->first << endl;
        //     }
        // }
    }
    return 0;
}
