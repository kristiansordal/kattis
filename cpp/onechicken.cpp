#include <bits/stdc++.h>
int main() {
    int n, m;
    std::cin >> n >> m;

    if (n < m) {
        if (m - n == 1) {
            std::cout << "Dr. Chaz will have " << m - n
                      << " piece of chicken left over!" << std::endl;

        } else {
            std::cout << "Dr. Chaz will have " << m - n
                      << " pieces of chicken left over!" << std::endl;
        }
    } else {
        if (n - m == 1) {
            std::cout << "Dr. Chaz needs " << n - m << " more piece of chicken!"
                      << std::endl;

        } else {
            std::cout << "Dr. Chaz needs " << n - m
                      << " more pieces of chicken!" << std::endl;
        }
    }

    return 0;
}
