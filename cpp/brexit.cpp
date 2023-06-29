// #include <bits/stdc++.h>

// struct CompareCountries {
//     bool operator()(std::pair<int, std::set<int>> &x,
//                     std::pair<int, std::set<int>> &y) const {
//         return x.second.size() < y.second.size();
//     }
// };

// void updateTrades(std::unordered_map<int, std::set<int>> &p,
//                   std::vector<std::pair<int, int>> sizes, std::set<int>
//                   &left, int root) {
//     std::set<int> neigbours = p[root];
//     int size = neigbours.size();
//     for (auto par : p) {
//         if (par.second.contains(root)) {
//         }
//     }
// }

// // put countries in priority queue from least no. of trading partners to most
// // keep a set of countries that have left
// // get the top of the priority queue, check if half of its countries have
// left
// // if yes: remove from priority queue and add to set
// // if no: some recursive stuff? pop the top and pass check the next, storing
// the
// // popped in a list

// void t(std::priority_queue<std::pair<int, std::set<int>>, CompareCountries>
//            &partnerships,
//        std::vector<int, std::set<int>> &notValid, std::set<int> &left,
//        std::unordered_map<int, int> sizes, int country) {
//     // std::set<int> &curr = partnerships.();
//     int curr = partnerships.top();

//     // for (auto l : curr.second) {
//     // }
//     //
//     std::set<int> x = {};
// }

// int main() {
//     int countries, trade, homeID, leave;

//     std::priority_queue<std::pair<int, std::set<int>>, CompareCountries>
//         partnerships;
//     std::unordered_map<int, std::set<int>> p;
//     std::unordered_map<int, int> sizes;
//     std::vector<int, std::set<int>> notValid;
//     std::set<int> left;

//     std::cin >> countries >> trade >> homeID >> leave;

//     for (int i = 0; i < trade; i++) {
//         int x, y;
//         std::cin >> x >> y;

//         if (p[x].empty()) {
//             std::set<int> v = {y};
//             p[x] = v;
//         } else {
//             p[x].emplace(y);
//         }

//         if (p[y].empty()) {
//             std::set<int> v = {x};
//             p[y] = v;
//         } else {
//             p[y].emplace(x);
//         }
//     }

//     for (auto par : p) {
//         sizes[par.first] = par.second.size();
//         partnerships.emplace(par);
//     }

//     left.emplace(leave);

//     return 0;
// }

#include <bits/stdc++.h>

struct CompareCountries {
    bool operator()(const std::pair<int, std::set<int>>& x,
                    const std::pair<int, std::set<int>>& y) const {
        return x.second.size() < y.second.size();
    }
};

void t(std::priority_queue<std::pair<int, std::set<int>>,
                           std::vector<std::pair<int, std::set<int>>>,
                           CompareCountries>& partnerships,
       std::vector<std::pair<int, std::set<int>>>& notValid,
       std::set<int>& left, std::unordered_map<int, int>& sizes, int country) {
    std::pair<int, std::set<int>> curr = partnerships.top();

    int leftPartners;
    for (int l : curr.second) {
        if (left.contains(l)) {
            leftPartners++;
        }
    }

    if (leftPartners >= sizes[country]) {
        left.emplace(curr.first);
        partnerships.pop();
    } else {
        partnerships.pop();
        notValid.push_back(curr);
    }
    t(partnerships, notValid, left, sizes, partnerships.top().first);
}

int main() {
    int countries, trade, homeID, leave;

    std::priority_queue<std::pair<int, std::set<int>>,
                        std::vector<std::pair<int, std::set<int>>>,
                        CompareCountries>
        partnerships;

    std::unordered_map<int, std::set<int>> p;
    std::unordered_map<int, int> sizes;
    std::vector<int, std::set<int>> notValid;
    std::set<int> left;

    std::cin >> countries >> trade >> homeID >> leave;

    for (int i = 0; i < trade; i++) {
        int x, y;
        std::cin >> x >> y;

        if (p[x].empty()) {
            std::set<int> v = {y};
            p[x] = v;
        } else {
            p[x].emplace(y);
        }

        if (p[y].empty()) {
            std::set<int> v = {x};
            p[y] = v;
        } else {
            p[y].emplace(x);
        }
    }

    for (auto par : p) {
        sizes[par.first] = par.second.size();
        partnerships.emplace(par);
    }

    left.emplace(leave);

    return 0;
}
