#include <bits/stdc++.h>
int main() {
    int people, trees;

    std::cin >> people >> trees;

    std::vector<int> posP;
    std::unordered_map<int, bool> posT;
    for (int i = 0; i < people; i++) {
        int pos;
        std::cin >> pos;
        posP.push_back(pos);
    }

    for (int i = 0; i < trees; i++) {
        int pos;
        std::cin >> pos;
        posT[pos] = false;
    }

    for (auto t : posT) {
    }
    return 0;
}
