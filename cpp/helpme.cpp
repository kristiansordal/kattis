#include <bits/stdc++.h>

#include <cctype>
int main() {
    std::vector<std::string> board;

    for (int i = 0; i < 17; i++) {
        std::string in;
        std::cin >> in;

        if (!(in[0] == '+')) {
            board.push_back(in);
        }
    }

    std::vector<std::vector<std::string>> board2;
    std::vector<std::string> row;

    for (auto s : board) {
        std::string f;
        for (int i = 0; i < size(s); i++) {
            if (i % 4 == 0) {
                row.push_back(f);
                f.clear();
            } else {
                f.push_back(s[i]);
            }
        }
        board2.push_back(row);
        row.clear();
    }

    std::string w = "White: ";
    std::string b = "Black: ";

    std::vector<char> r = {'1', '2', '3', '4', '5', '6', '7', '8'};
    std::vector<char> file = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'};
    std::vector<char> white = {'R', 'B', 'K', 'Q', 'P', 'N'};
    std::vector<char> black = {'r', 'b', 'k', 'q', 'p', 'n'};

    for (int i = 7; i > 0; i--) {
        for (int j = 0; j < 7; j++) {
            char p = board2[i][j][1];
            if (std::find(white.begin(), white.end(), p) != white.end()) {
                w.push_back(std::toupper(p));
                w.push_back(file[j]);
                w.push_back(r[i]);
                w.push_back(',');
                w.push_back(' ');
            } else if (std::find(black.begin(), black.end(), p) !=
                       black.end()) {
                b.push_back(std::toupper(p));
                b.push_back(file[j]);
                b.push_back(r[i]);
                b.push_back(',');
                b.push_back(' ');
            }
        }
    }
    std::cout << w << std::endl;
    std::cout << b << std::endl;
    return 0;
}
