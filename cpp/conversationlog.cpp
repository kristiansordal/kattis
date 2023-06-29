#include <bits/stdc++.h>
using namespace std;
int main() {
    unordered_map<string, int> words;
    int x;
    cin >> x;
    for (int i = 0; i < x + 1; i++) {
        string s;
        getline(cin, s);
        stringstream ss(s);
        string token;

        if (i == 1) {
            while (getline(ss, token, ' ')) {
                if (!isupper(token[0])) {
                    if (words.find(token) == words.end()) {
                        words[token] = 1;
                    } else {
                        words[token]++;
                    }
                }
            }
        } else {
            unordered_map<string, bool> found;
            for (auto pair : words) {
                found[pair.first] = false;
            }

            while (getline(ss, token, ' ')) {
                if (!(words.find(token) == words.end())) {
                    words[token]++;
                    found[token] = true;
                }
            }

            for (auto pair : found) {
                if (!pair.second) {
                    words.erase(pair.first);
                }
            }
        }
    }

    for (const auto& pair : words) {
        cout << pair.first << endl;
    }

    return 0;
}
