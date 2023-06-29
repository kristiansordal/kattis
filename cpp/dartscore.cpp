#include <bits/stdc++.h>

std::string multToScore(int m) {
    if (m == 1) {
        return "single";
    } else if (m == 2) {
        return "double";
    } else {
        return "triple";
    }
}
std::vector<std::string> computeScore(int score, int multiplier, int throws,
                                      std::vector<std::string> strs) {
    if (throws == 0 && score == 0) {
        return strs;
    }
    if (throws == 1 && score != 0) {
        bool impossible = true;
        for (int i = 1; i <= 3; i++) {
            for (int j = 1; j <= 20; j++) {
                if (score - i * j == 0) {
                    impossible = false;
                    break;
                }
            }
        }

        if (impossible) {
            return std::vector<std::string>{"impossible"};
        }
    }

    for (int i = 20; i >= 1; i--) {
        if (score - i * multiplier >= 0) {
            score -= i * multiplier;
            strs.push_back(multToScore(multiplier));
            strs.push_back(" ");
            strs.push_back(std::to_string(i));
            strs.push_back("\n");
            break;
        }
    }

    if (score >= 20 * multiplier) {
        strs = computeScore(score, multiplier, throws - 1, strs);
    } else {
        strs = computeScore(score, multiplier - 1, throws - 1, strs);
    }
    return strs;
}

int main() {
    int score;
    std::vector<std::string> strs;
    std::cin >> score;
    strs = computeScore(score, 3, 3, strs);

    for (auto i : strs) {
        std::cout << i;
    }

    return 0;
}
