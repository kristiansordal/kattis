#include <bits/stdc++.h>

int getMins(std::string s) {
    std::string hrs{s[0], s[1]};
    std::string min{s[3], s[4]};
    return std::stoi(hrs) * 60 + std::stoi(min);
}
int main() {
    std::vector<int> in;
    std::vector<std::string> days{"Saturday",  "Sunday",   "Monday", "Tuesday",
                                  "Wednesday", "Thursday", "Friday"};
    std::string l;
    for (int i = 0; i < 4; i++) {
        std::cin >> l;
        in.push_back(getMins(l));
    }

    bool *b;
    b = new bool[1000000];
    for (int i = in[0]; i < 1000000; i += in[2]) {
        b[i] = true;
    }

    for (int i = in[1]; i < 1000000; i += in[3]) {
        if (b[i]) {
            int day = (i + 5) / 24 / 60 % 7;
            std::cout << days[day] << std::endl;
            std::cout << std::setfill('0') << std::setw(2) << i / 60 % 24 << ":"
                      << std::setfill('0') << std::setw(2) << i % 60
                      << std::endl;
            return 0;
        }
    }
    std::cout << "Never" << std::endl;
    return 0;
}
