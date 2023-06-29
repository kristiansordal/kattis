#include <bits/stdc++.h>
#include <sstream>
using namespace std;

bool sortFunc(pair<string, unsigned long> &a, pair<string, unsigned long> &b) {
    if (a.second != b.second) {
        return a.second > b.second;
    }
    return a.first < b.first;
}

int main() {
    int c;
    cin >> c;

    for (int i = 0; i < c; i++) {
        int n;
        cin >> n;
        vector<pair<string, unsigned long>> people;
        for (int i = 0; i < n; i++) {
            string name, s, throwaway;
            cin >> name >> s >> throwaway;
            name.pop_back();

            stringstream ss(s);
            string c;
            string cs;

            while (getline(ss, c, '-')) {
                if (c == "lower") {
                    cs.push_back('1');
                } else if (c == "middle") {
                    cs.push_back('2');
                } else if (c == "upper") {
                    cs.push_back('3');
                }
            }

            reverse(cs.begin(), cs.end());

            while (cs.size() < 10) {
                cs.push_back('2');
            }

            unsigned long val = 0;
            for (int i = 0; i < cs.size(); i++) {
                val *= 10;
                val += cs[i] - '0';
            }

            people.push_back(make_pair(name, val));
        }

        sort(people.begin(), people.end(), sortFunc);

        for (const auto &p : people) {
            cout << p.first << endl;
        }

        cout << "==============================" << endl;
    }

    return 0;
}
