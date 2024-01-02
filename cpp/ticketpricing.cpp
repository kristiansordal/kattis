#include <bits/stdc++.h>
using namespace std;
struct Estimate {
    int ticket_price;
    int tickets_sold;

    Estimate(int ticket_price, int tickets_sold)
        : ticket_price(ticket_price),
          tickets_sold(tickets_sold) {}

    Estimate() = default;
};
int main() {
    // n is number of seats left, w is weeks left
    int n, w;
    cin >> n >> w;

    vector<Estimate> estimates;
    vector<int> tickets;
    vector<int> prices;

    int k;
    cin >> k;

    for (int i = 0; i < k; i++) {
        int p;
        cin >> p;
    }
    for (int i = 0; i < k; i++) {
        int s;
        cin >> s;
    }

    for (int i = 0; i < k; i++) {
        estimates.push_back()
    }

    return 0;
}
