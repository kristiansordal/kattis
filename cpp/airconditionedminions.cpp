#include <bits/stdc++.h>

#include <algorithm>
#include <queue>

bool comparetemps(std::pair<int, int> a, std::pair<int, int> b) {
    return a.first == b.second ? a.first < b.first : a.second < b.second;
}

int main() {
    int n;
    std::cin >> n;

    std::vector<std::pair<int, int>> temps;

    for (int i = 0; i < n; i++) {
        int x, y;
        std::cin >> x >> y;
        temps.push_back(std::make_pair(x, y));
    }

    std::sort(temps.begin(), temps.end(), comparetemps);
    int rooms = 1;
    int prev = temps[0].second;

    for (int i = 1; i < temps.size(); i++) {
        if (temps[i].first > prev) {
            prev = temps[i].second;
            rooms++;
        }
    }
    std::cout << rooms << std::endl;
    return 0;
}
