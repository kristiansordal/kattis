#include <bits/stdc++.h>

void updateMap(std::map<std::string, int> &m, std::string k) {
    std::string s;

    for (int i = 0; i < k.size(); i++) {
        s += k[i];
        if (m.count(s)) {
            m[s] += 1;
        } else {
            m[s] = 0;
        }
    }
}

int main() {
    int n;
    std::cin >> n;
    std::map<std::string, int> chars;

    for (int i = 0; i < n; i++) {
        std::string l;
        std::cin >> l;

        updateMap(chars, l);
        std::cout << chars[l] << std::endl;
    }
    return 0;
}
