#include <bits/stdc++.h>

#include <iostream>

int main() {
    std::unordered_map<int, std::string> vars;

    std::string line;
    while (getline(std::cin, line)) {
        std::stringstream iss(line);
        std::string c;
        iss >> c;

        if (c == "def") {
            std::string var int x;
            iss >> var >> x;
            vars[x] = var;
        } else if (c == "calc") {
        }
        // switch (c) {
        //     case "def": {
        //         std::string var;
        //         int x;
        //         iss >> var >> x;
        //     }
        // }
    }

    return 0;
}
