#include <bits/stdc++.h>

#include <iostream>

std::array<int, 8> increment(std::array<int, 8> regs, std::array<int, 8> primes,
                             int i, int& ops) {
    if (regs[i] % primes[i] == 0 && regs[i] != 0) {
        increment(regs, primes, i + 1, ops);
    } else {
        ops++;
        regs[i]++;
    }
    return regs;
}

int main() {
    std::array<int, 8> regs;
    std::array<int, 8> primes = {2, 3, 5, 7, 11, 13, 17, 19};
    int ops = 0;

    for (int i = 0; i < 8; i++) {
        int x;
        std::cin >> x;
        regs[i] = x;
    }

    while (regs[7] > 19) {
        regs = increment(regs, primes, 0, ops);
    }

    std::cout << ops << std::endl;

    return 0;
}
