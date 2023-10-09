#include <bits/stdc++.h>

bool cmp(const std::pair<int, int> &a, const std::pair<int, int> &b) { return a.second < b.second; }

int interval_schedule(std::vector<std::pair<int, int>> intervals) {
    std::vector<std::pair<int, int>> s = {intervals[0]};

    for (int i = 1; i < intervals.size(); i++) {
        if (intervals[i].first >= s[s.size() - 1].second) {
            s.push_back(intervals[i]);
        }
    }
    return s.size();
}
int main() {
    int n;
    std::cin >> n;

    std::vector<std::pair<int, int>> intervals;

    for (int i = 0; i < n; i++) {
        int x, y;
        std::cin >> x >> y;

        intervals.push_back(std::make_pair(x, y));
    }

    std::sort(intervals.begin(), intervals.end(), cmp);

    std::cout << interval_schedule(intervals) << std::endl;

    return 0;
}
