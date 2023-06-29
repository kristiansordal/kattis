#include <bits/stdc++.h>

int runesToInt(std::string runes) {
    std::string x;
    for (auto c : runes) {
        if (c == 'B') {
            x.push_back('1');
        } else {
            x.push_back('0');
        }
    }
    return std::stoi(x, nullptr, 2);
}

std::string intToBinary(int num) {
    std::bitset<32> binary(num);
    return binary.to_string();
}

std::string intToRunes(int x, int size) {
    std::string bin = intToBinary(x);
    std::string runes;

    for (int i = bin.size() - size; i < bin.size(); i++) {
        if (bin[i] == '1') {
            runes.push_back('B');
        } else {
            runes.push_back('A');
        }
    }
    return runes;
}

int binaryToInt(int num) {
    std::bitset<32> binary(num);
    return std::stoi(binary.to_string(), nullptr, 2);
}

int main() {
    std::string runes;
    int days;

    std::cin >> runes >> days;

    int x = runesToInt(runes);
    std::cout << x << std::endl;
    std::cout << days << std::endl;
    std::cout << intToBinary(1) << std::endl;
    // int y = std::stoi(intToBinary(days), nullptr, 2);

    std::string z = intToRunes(x + days, runes.size());
    std::cout << z << std::endl;

    return 0;
}
