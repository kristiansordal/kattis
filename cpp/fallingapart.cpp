#include <bits/stdc++.h>
int main() {
    int x;
    std::cin >> x;
    std::priority_queue<int> pq;
    int a = 0;
    int b = 0;
    bool turn = true;

    for (int i = 0; i < x; i++) {
        int x;
        std::cin >> x;
        pq.push(x);
    }

    while (!pq.empty()) {
        if (turn) {
            a += pq.top();
            pq.pop();
            turn = !turn;
        } else {
            b += pq.top();
            pq.pop();
            turn = !turn;
        }
    }

    std::cout << a << " " << b << std::endl;

    return 0;
}
