#include <bits/stdc++.h>

std::string turn(std::vector<std::string> animals, std::string prev) {
    std::vector<std::string> candidates;
    std::string next;
    char last = prev.back();

    for (auto a : animals) {
        if (a[0] == last) {
            candidates.push_back(a);
        }
    }

    if (candidates.size() == 0) {
        return "?";
    }

    for (auto a : candidates) {
        std::vector<std::string> filteredAnimals;

        std::copy_if(
            animals.begin(), animals.end(), std::back_inserter(filteredAnimals),
            [&a](const std::string& x) { return x != a && x[0] == a.back(); });

        if (filteredAnimals.size() == 0) {
            next = a;
            next.push_back('!');
            return next;
        }
    }

    return candidates[0];
}
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(0);
    std::string prev;
    int x;
    std::vector<std::string> animals;

    std::cin >> prev >> x;

    for (int i = 0; i < x; i++) {
        std::string a;
        std::cin >> a;
        animals.push_back(a);
    }

    std::string t = turn(animals, prev);
    std::cout << t << std::endl;

    return 0;
}
