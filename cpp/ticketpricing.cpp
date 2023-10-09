#include <bits/stdc++.h>
using namespace std;
struct Estimate {
    int tickets;
    int price;
    Estimate(int t, int p) : tickets(t), price(p){};
    Estimate(int t) : tickets(t), price(0){};
    Estimate() : tickets(0), price(0){};
};

void pricing(std::vector<Estimate> estimates) {}
int main() {
    int n, w;
    cin >> n >> w;
    vector<Estimate> estimates(w + 1);

    for (int i = 0; i <= w; i++) {
        int k;
        cin >> k;
        for (int i = 0; i < k; i++) {
            int x;
            cin >> x;
            estimates.push_back(Estimate(x));
        }

        for (int i = 0; i < k; i++) {
            int x;
            cin >> x;
            estimates[w].tickets = x;
        }
    }

    for (int i = 0; i < w; i++) {
        cout << estimates[w].price << endl;
        cout << estimates[w].tickets << endl;
    }

    return 0;
}
