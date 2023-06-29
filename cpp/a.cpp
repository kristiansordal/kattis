#include <bits/stdc++.h>

#include <iostream>
#include <queue>
#include <sstream>
#include <unordered_map>

std::vector<std::string> tokenize(const std::string &s, char delim) {
    std::vector<std::string> result;
    std::stringstream ss(s);
    std::string item;
    while (std::getline(ss, item, delim)) {
        result.push_back(item);
    }
    return result;
}

class Cat {
   public:
    Cat(const std::string &name, int arrival, int infection)
        : name(name), arrival(arrival), infection(infection) {}

    std::string name;
    int arrival;
    int infection;
};

struct CompareCats {
    bool operator()(const Cat &a, const Cat &b) const {
        if (a.infection == b.infection) {
            return a.arrival > b.arrival;
        }
        return a.infection > b.infection;
    }
};
int main() {
    int n;
    std::cin >> n;
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

    // std::unordered_map<std::string, std::pair<int, int>> cats;
    std::priority_queue<Cat, std::vector<Cat>, CompareCats> cats;

    int arrival = 0;

    for (int i = 0; i < n; i++) {
        std::string cat;
        getline(std::cin, cat);
        std::vector<std::string> line = tokenize(cat, ' ');
        Cat curr = {line[1], std::stoi(line[2]), arrival++};
        int f = stoi(line[0]);

        if (f == 0) {
            cats.emplace(curr);
        } else if (f == 1) {
        } else if (f == 2) {
        } else if (f == 3) {
        }
    }
    // for (int i = 0; i < n; i++) {
    //     std::string cat;
    //     getline(std::cin, cat);
    //     std::vector<std::string> line = tokenize(cat, ' ');
    //     int f = std::stoi(line[0]);

    //     if (f == 0) {
    //         int infection = std::stoi(line[2]);
    //         cats[line[1]] = std::make_pair(infection, arrival++);
    //         if (infection > max) {
    //             max = infection;
    //             maxCat = line[1];
    //         }
    //     } else if (f == 1) {
    //         std::pair<int, int> val = cats[line[1]];
    //         cats[line[1]] =
    //             std::make_pair(val.first + std::stoi(line[2]), val.second);
    //         if (cats[line[1]].first > max) {
    //             max = cats[line[1]].first;
    //             maxCat = line[1];
    //         } else if (cats[line[1]].first == max) {
    //             if (cats[line[1]].second < cats[maxCat].second) {
    //                 maxCat = line[1];
    //             }
    //         }
    //     } else if (f == 2) {
    //         cats.erase(line[1]);
    //         if (line[1] == maxCat && !cats.empty()) {
    //             max = 0;
    //             maxCat = "";
    //             for (const auto &kv : cats) {
    //                 if (kv.second.first > max) {
    //                     max = kv.second.first;
    //                     maxCat = kv.first;
    //                 } else if (kv.second.first == max) {
    //                     if (kv.second.second < cats[maxCat].second) {
    //                         maxCat = kv.first;
    //                     }
    //                 }
    //             }
    //         }
    //     } else if (f == 3) {
    //         if (cats.empty()) {
    //             std::cout << "The clinic is empty" << std::endl;
    //         } else {
    //             std::cout << maxCat << std::endl;
    //         }
    //     }
    // }
    return 0;
}
