#include <bits/stdc++.h>
#include <sstream>
using namespace std;
int main() {
    string stri = "= 1 2";
    stringstream ss(stri);
    string word;
    while (getline(ss, word, ' ')) {
        cout << word << endl;
    }
    return 0;
}
