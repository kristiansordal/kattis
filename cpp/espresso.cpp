#include <bits/stdc++.h>

int main() {
    int n, s;
    int refills = 0;
    std::cin >> n >> s;
    int tank = s;

    for (int i = 0; i < n; i++) {
        std::string o;
        std::cin >> o;
        if (o.size() > 1) {
            int x = std::stoi(std::string(1, o[0]));
            if (tank < x + 1) {
                refills++;
                tank = s;
            }
            tank -= x + 1;
        } else {
            int x = std::stoi(std::string(1, o[0]));
            if (tank < x) {
                refills++;
                tank = s;
            }
            tank -= x;
        }
    }
    std::cout << refills << std::endl;

    return 0;
}
