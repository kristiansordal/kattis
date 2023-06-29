#include <bits/stdc++.h>
using namespace std;
struct Person {
    int money;
    int time;

    Person(int m, int t) {
        money = m;
        time = t;
    }
};

bool sortMoney(const Person& p1, const Person& p2) {
    return p1.money >= p2.money;
}

int main() {
    int n, t;
    cin >> n >> t;
    vector<Person> people;

    for (int i = 0; i < n; i++) {
        int x, y;
        cin >> x >> y;
        Person p(x, y);
        people.push_back(p);
    }

    sort(people.begin(), people.end(), sortMoney);

    return 0;
}
