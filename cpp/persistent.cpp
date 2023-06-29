#include <bits/stdc++.h>

using namespace std;

vector<int> strToInt(string &s) {
    vector<int> res;
    stringstream ss(s);
    int c;
    while (ss >> c) {
        res.push_back(c);
    }

    return res;
}

string persistent(vector<int> nums) {
    int newNum = 0;
    for (auto n : nums) {
        newNum *= n;
    }

    return to_string(newNum);
}

int main() {
    int x;
    cin >> x;

    while (x != -1) {
        int persistence = 0;
        string s = to_string(x);
        vector<int> num = strToInt(s);
        while (num.size() != 1) {
        }
    }
    return 0;
}
