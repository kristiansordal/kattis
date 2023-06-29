#include <bits/stdc++.h>

#include <cstdlib>
#include <ctime>

std::string gen(int n) {
    std::string rand;
    srand(time(0));

    for (int i = 0; i < n; i++) {
        char randomChar = 'a' + std::rand() % 26;
        rand.push_back(randomChar);
    }
    return rand;
}
int main() {
    int min, max;
    std::set<std::string> vocab = {};
    std::vector<std::string> essay = {};
    std::cin >> min >> max;

    std::cout << min << std::endl;
    std::cout << max << std::endl;

    for (int i = 0; i < min; i++) {
        int n = 1 + (std::rand() % 15);
        std::string word = gen(n);
        essay.push_back(word);
        vocab.emplace(word);
    }

    while (essay.size() < max) {
        int n = 1 + (std::rand() % 15);
        std::string word = gen(n);
        essay.push_back(word);
        vocab.emplace(word);
    }

    for (int i = 0; i < essay.size(); i++) {
        if (i < essay.size() - 1) {
            std::cout << essay[i] << " ";
        } else {
            std::cout << essay[i] << std::endl;
        }
    }
    std::cout << essay.size() << std::endl;
    std::cout << vocab.size() << std::endl;
    return 0;
}
