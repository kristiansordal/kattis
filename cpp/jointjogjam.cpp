#include <bits/stdc++.h>

#include <cmath>
#include <iostream>
int main() {
    std::vector<std::pair<double, double>> o;
    std::vector<std::pair<double, double>> k;

    for (int i = 0; i < 4; i++) {
        double x;
        double y;
        std::cin >> x >> y;
        if (i % 2 == 0) {
            k.push_back(std::pair<double, double>(x, y));
        } else {
            o.push_back(std::pair<double, double>(x, y));
        }
    }

    std::vector<double> dist;

    double ss = sqrt(pow((o[0].first - k[0].first), 2) +
                     pow((o[0].second - k[0].second), 2));
    double ee = sqrt(pow((o[1].first - k[1].first), 2) +
                     pow((o[1].second - k[1].second), 2));

    dist.push_back(ss);
    dist.push_back(ee);
    auto max = std::max_element(dist.begin(), dist.end());

    std::cout << std::fixed << std::setprecision(10) << *max << std::endl;

    return 0;
}
