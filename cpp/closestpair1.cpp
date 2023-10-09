#include <bits/stdc++.h>

using namespace std;

struct Point {
    double x;
    double y;
    int id;

    Point(double x, double y, int id) : x(x), y(y), id(id) {}
    Point() : x(-1), y(-1), id(-1) {}

    struct ByX {
        bool operator()(const Point &p1, const Point &p2) const { return std::tie(p1.x, p1.y) < std::tie(p2.x, p2.y); };
    };
    struct ByY {
        bool operator()(const Point &p1, const Point &p2) const { return std::tie(p1.y, p1.x) < std::tie(p2.y, p2.x); };
    };
};

double dist(Point p1, Point p2) {
    auto dx = p2.x - p1.x;
    auto dy = p2.y - p1.y;

    return sqrt(abs((dx * dx) + (dy * dy)));
}

struct Pair {
    Point p1;
    Point p2;
    double delta;

    Pair(Point p1, Point p2) : p1(p1), p2(p2), delta(dist(p1, p2)) {}

    bool operator<(const Pair &obj) const { return delta < obj.delta; }
    friend std::ostream &operator<<(std::ostream &os, const Pair &p) {
        os << "(" << p.p1.x << ", " << p.p1.y << "), (" << p.p2.x << ", " << p.p2.y << ")";
        return os;
    }
};

Pair bruteforce(std::vector<Point> &x) {
    double opt = INT_MAX;
    Point p1;
    Point p2;

    for (auto &i : x) {
        for (auto &j : x) {
            if (i.id != j.id) {
                auto opt_pair = Pair(i, j);
                auto delta = dist(i, j);
                if (delta < opt) {
                    opt = delta;
                    p1 = i;
                    p2 = j;
                }
            }
        }
    }

    return Pair(p1, p2);
}

Pair compute_strip(std::vector<Point> strip) {
    double delta = 1e300;

    auto pair = Pair(Point(), Point());

    for (size_t i = 0; i < strip.size() - 1; ++i) {
        for (size_t j = i + 1; j < std::min(i + 4, strip.size()); ++j) {
            std::vector<Point> s(strip.begin() + i, strip.begin() + j + 1);
            Pair bf_pair = bruteforce(s);
            double bf_dist = dist(bf_pair.p1, bf_pair.p2);
            if (bf_dist < delta) {
                delta = bf_dist;
                pair = bf_pair;
            }
        }
    }
    return pair;
}

Pair closestPair(std::vector<Point> sorted_x, std::vector<Point> sorted_y) {
    int n = sorted_x.size();

    if (n <= 3) {
        auto x = bruteforce(sorted_x);
        return x;
    }

    int mid = std::floor(n / 2);

    std::vector<Point> xl, xr;
    std::vector<Point> yl, yr;
    std::set<Point, Point::ByX> l;

    for (int i = 0; i < n; i++) {
        if (i < mid) {
            xl.push_back(sorted_x[i]);
            l.emplace(sorted_x[i]);
        } else {
            xr.push_back(sorted_x[i]);
        }
    }

    for (int i = 0; i < n; i++) {
        if (l.find(sorted_y[i]) != l.end()) {
            yl.push_back(sorted_y[i]);
        } else {
            yr.push_back(sorted_y[i]);
        }
    }

    Pair opt_left_pair = closestPair(xl, yl);
    Pair opt_right_pair = closestPair(xr, yr);
    Pair opt_pair = *min(&opt_left_pair, &opt_right_pair);

    double line = sorted_x[mid].x;

    std::vector<Point> strip;

    for (auto &p : sorted_y) {
        if (abs(p.x - line) < opt_pair.delta) {
            strip.push_back(p);
        }
    }

    if (strip.size() < 4) {
        std::cout << "Returning min point 1: " << opt_pair << std::endl;
        return opt_pair;
    }

    auto strip_pair = compute_strip(strip);

    if (opt_pair.delta < strip_pair.delta) {
        return opt_pair;
    }

    return strip_pair;
}

int main() {
    int n;
    cin >> n;

    while (n != 0) {
        std::vector<Point> sorted_x;
        std::vector<Point> sorted_y;

        for (int i = 0; i < n; i++) {
            double x, y;
            cin >> x >> y;
            sorted_x.push_back(Point(x, y, i));
            sorted_y.push_back(Point(x, y, i));
        }

        sort(sorted_x.begin(), sorted_x.end(), Point::ByX());
        sort(sorted_y.begin(), sorted_y.end(), Point::ByY());

        auto close = closestPair(sorted_x, sorted_y);

        std::cout << std::fixed << std::setprecision(2) << close.p1.x << " " << close.p1.y << " " << close.p2.x << " "
                  << close.p2.y << std::endl;

        std::cin >> n;
    }
    return 0;
}
