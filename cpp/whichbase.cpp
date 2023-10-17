#include <bits/stdc++.h>
using namespace std;
string octal(double n) {
    stringstream s;
    s << oct << n;
    return s.str();
}

string hexal(double n) {
    stringstream s;
    s << hex << n;
    return s.str();
}

int main() {
    int n;
    cin >> n;
    std::vector<std::pair<int, double>> tests;

    for (int i = 0; i < n; i++) {
        std::vector<int> r;
        int s;
        double n;
        cin >> s >> n;
        tests.push_back(make_pair(s, n));
    }

    for (auto &t : tests) {
        std::cout << t.first << " ";
        std::cout << octal(t.second) << " ";
        std::cout << t.second << " ";
        std::cout << hexal(t.second) << std::endl;
    }
    return 0;
}
