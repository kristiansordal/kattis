#include <bits/stdc++.h>
using namespace std;
struct Rect {
    double x;
    double y;
    double w;
    double h;
    double r;
    Rect(double x, double y, double w, double h, double r) : x(x), y(y), w(w), h(h), r(r){};
};

struct Coordinate {
    double x;
    double y;
    Coordinate(double x, double y) : x(x), y(y){};
    Coordinate() : x(0), y(0){};
};

bool inside(int x1, int x2, int y1, int y2, Coordinate c) { return c.x >= x1 && c.x <= x2 && c.y >= y1 && c.y <= y2; }

int main() {
    double n;
    cin >> n;
    Coordinate *centerLU, *centerRU, *centerRD, *centerLD;
    for (double i = 0; i < n; i++) {
        double x, y, w, h, r, m;

        cin >> x >> y >> w >> h >> r;

        Rect rect(x, y, w, h, r);

        cin >> m;

        for (double i = 0; i < m; i++) {
            double x1, y1;
            cin >> x1 >> y1;
            Coordinate coord(x1, y1);

            double farX = rect.x + rect.w;
            double farY = rect.y + rect.h;
            centerLU->x = rect.x + rect.r;
            centerLU->y = rect.y + rect.r;
            centerLD->x = rect.x + rect.r;
            centerLD->y = rect.y + rect.h + rect.r;
            centerRU->x = rect.x + rect.w + rect.r;
            centerRU->y = rect.y + rect.r;
            centerRD->x = rect.x + rect.w + rect.r;
            centerRD->y = rect.y + rect.h + rect.r;

            if (coord.x >= rect.x && coord.y >= rect.y && coord.x <= farX && coord.y <= farY) {
                if (inside(rect.x, rect.x + rect.r, rect.y, rect.y + rect.r, coord)) {
                    double distLU = sqrt(pow(coord.x - centerLU->x, 2) + pow(coord.y - centerLU->y, 2));
                    if (distLU > rect.r) {
                        cout << "outside" << endl;
                    } else {
                        cout << "inside" << endl;
                    }
                } else if (inside(rect.x, rect.x + rect.r, rect.y + rect.h - rect.r, rect.y + rect.h, coord)) {
                    double distLD = sqrt(pow(coord.x - centerLD->x, 2) + pow(coord.y - centerLD->y, 2));
                    if (distLD > rect.r) {
                        cout << "outside" << endl;
                    } else {
                        cout << "inside" << endl;
                    }
                } else if (inside(rect.x + rect.w - rect.r, rect.x + rect.w, rect.y, rect.y + rect.r, coord)) {
                    double distRU = sqrt(pow(coord.x - centerLD->x, 2) + pow(coord.y - centerLD->y, 2));
                    if (distRU > rect.r) {
                        cout << "outside" << endl;
                    } else {
                        cout << "inside" << endl;
                    }
                } else if (inside(rect.x + rect.w - rect.r, rect.x + rect.w, rect.y + rect.h - rect.r, rect.y + rect.h,
                                  coord)) {
                    double distRD = sqrt(pow(coord.x - centerLD->x, 2) + pow(coord.y - centerLD->y, 2));
                    if (distRD > rect.r) {
                        cout << "outside" << endl;
                    } else {
                        cout << "inside" << endl;
                    }
                }

            } else {
                cout << "outside" << endl;
            }
        }
        cout << endl;
    }
    return 0;
}
