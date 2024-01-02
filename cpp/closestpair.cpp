#include <bits/stdc++.h>
using namespace std;

struct Point {
    double x, y;

    Point(double x, double y)
        : x(x),
          y(y) {}

    Point() = default;
    void operator>>(istream &is) { is >> x >> y; }
};

double dist(Point a, Point b) { return sqrt(pow(a.x - b.x, 2) + pow(a.y - b.y, 2)); }

pair<Point, Point> brute(vector<Point> p) {
    double d = 1e9;
    pair<Point, Point> ps;

    for (int i = 0; i < p.size(); i++) {
        for (int j = 0; j < p.size(); j++) {
            if (i != j && dist(p[i], p[j]) < d) {
                d = dist(p[i], p[j]);
                ps = {p[i], p[j]};
            }
        }
    }
    return ps;
}
pair<Point, Point> compute_strip(vector<Point> strip, double &d) {
    int n = strip.size();
    pair<Point, Point> ps;
    sort(strip.begin(), strip.end(), [](Point a, Point b) { return a.y < b.y; });

    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (strip[j].y - strip[i].y >= d) {
                break;
            }
            if (dist(strip[i], strip[j]) < d) {
                d = dist(strip[i], strip[j]);
                ps = {strip[i], strip[j]};
            }
        }
    }
    return ps;
}
pair<Point, Point> closest(vector<Point> points) {
    int n = points.size();

    if (n <= 3) {
        return brute(points);
    }

    sort(points.begin(), points.end(), [](Point a, Point b) { return a.x < b.x; });
    double mid = points[n / 2].x;
    vector<Point> xl, xr;

    for (int i = 0; i < n; i++) {
        if (i < n / 2) {
            xl.push_back(points[i]);
        } else {
            xr.push_back(points[i]);
        }
    }

    auto minl = closest(xl);
    auto minr = closest(xr);
    auto min = minl;

    if (dist(minl.first, minl.second) > dist(minr.first, minr.second)) {
        min = minr;
    }
    auto d = dist(min.first, min.second);

    vector<Point> strip;

    for (auto &p : points) {
        if (abs(p.x - mid) < d) {
            strip.push_back(p);
        }
    }

    auto strip_min = compute_strip(strip, d);

    if (d < dist(min.first, min.second)) {
        min = strip_min;
    }

    return min;
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    while (n != 0) {
        vector<Point> points;
        for (int i = 0; i < n; i++) {
            Point p;
            p >> cin;
            points.push_back(p);
        }
        auto min = closest(points);
        // auto b = brute(points);
        cout << min.first.x << " " << min.first.y << " " << min.second.x << " " << min.second.y << endl;
        // cout << b.first.x << " " << b.first.y << " " << b.second.x << " " << b.second.y << endl;
        // cout << fixed << setprecision(4) << dist(min.first, min.second) << endl;
        // cout << fixed << setprecision(4) << dist(b.first, b.second) << endl;
        cin >> n;
    }
}
