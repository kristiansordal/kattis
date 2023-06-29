#include <bits/stdc++.h>

#include <iostream>

// long long factorial(int x, std::map<int, long long> &facs) {
//     if (facs.count(x)) {
//         return facs[x];
//     }
//     if (x == 0) {
//         return 0;
//     }

//     long long res = 1;

//     for (int i = 2; i <= x; i++) {
//         res *= i;
//     }

//     facs[x] = res;
//     return res;
// }
// std::map<char, int> charCount(const std::string &s) {
//     std::map<char, int> count;
//     for (auto c : s) {
//         count[c]++;
//     }
//     return count;
// }

// long long anagrams(const std::string &s, std::map<int, long long> &facs) {
//     int n = s.length();
//     long long perms = factorial(n, facs);

//     std::map<char, int> count = charCount(s);

//     for (std::map<char, int>::iterator it = count.begin(); it != count.end();
//          it++) {
//         perms /= factorial(it->second, facs);
//     }
//     return perms;
// }

// int main() {
//     std::string line;
//     std::map<int, long long> facs;

//     while (getline(std::cin, line)) {
//         std::istringstream iss(line);
//         std::string l;
//         iss >> l;
//         std::cout << anagrams(l, facs) << std::endl;
//     }
//     return 0;
// }

std::string multiply(std::string a, std::string b) {
    int n = a.length(), m = b.length();
    std::vector<int> result(n + m, 0);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            result[i + j] += (a[n - i - 1] - '0') * (b[m - j - 1] - '0');
            result[i + j + 1] += result[i + j] / 10;
            result[i + j] %= 10;
        }
    }
    while (result.size() > 1 && result.back() == 0) {
        result.pop_back();
    }
    std::string c;
    for (int i = result.size() - 1; i >= 0; --i) {
        c += (char)(result[i] + '0');
    }
    return c;
}

std::string factorial(int x, std::map<int, std::string> &facs) {
    if (facs.count(x)) {
        return facs[x];
    }
    if (x == 0) {
        return 0;
    }

    std::string res = "1";

    for (int i = 2; i <= x; i++) {
        res = multiply(res, std::to_string(i));
    }

    facs[x] = res;
    return res;
}
std::map<char, int> charCount(const std::string &s) {
    std::map<char, int> count;
    for (auto c : s) {
        count[c]++;
    }
    return count;
}

std::string anagrams(const std::string &s, std::map<int, std::string> &facs) {
    int n = s.length();
    std::string perms = factorial(n, facs);

    std::map<char, int> count = charCount(s);

    for (std::map<char, int>::iterator it = count.begin(); it != count.end();
         it++) {
        perms /= factorial(it->second, facs);
    }
    return perms;
}

int main() {
    std::string line;
    std::map<int, long long> facs;

    while (getline(std::cin, line)) {
        std::istringstream iss(line);
        std::string l;
        iss >> l;
        std::cout << anagrams(l, facs) << std::endl;
    }
    return 0;
}
