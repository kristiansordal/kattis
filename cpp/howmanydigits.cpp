#include <bits/stdc++.h>

#include <iostream>
#include <string>

int digs(int n) {
    if (n < 0) {
        return 0;
    }

    if (n <= 1) {
        return 1;
    }

    double d = 0;
    for (int i = 2; i <= n; i++) {
        d += log10(i);
    }

    return floor(d) + 1;
}
int main() {
    std::string line;

    while (getline(std::cin, line)) {
        std::istringstream iss(line);
        int x;
        iss >> x;

        std::cout << digs(x) << std::endl;
    }

    return 0;
}
