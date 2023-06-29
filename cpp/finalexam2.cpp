#include <bits/stdc++.h>
int main() {
    int x;
    std::cin >> x;
    std::string prev;
    std::string curr;
    int corr = 0;
    std::cin >> prev;

    for (int i = 0; i < x - 1; i++) {
        std::cin >> curr;
        if (curr == prev) {
            corr++;
        }
        prev = curr;
    }

    std::cout << corr << std::endl;
    return 0;
}
