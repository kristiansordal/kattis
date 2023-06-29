#include <bits/stdc++.h>
using namespace std;
struct Point {
    double x;
    double y;
    double z;
};

struct GunShot {
    Point p;
    Point v;
};

struct Sphere {
    double r;
    bool popped;
    Point p;
};

Point dist(GunShot g, Sphere s) {
    return Point{g.p.x - s.p.x, g.p.y - s.p.y, g.p.z - (s.p.z + s.r)};
}

double magnitude(Point p) {
    return sqrt(pow(p.x, 2) + pow(p.y, 2) + pow(p.z, 2));
}

bool isBehind(GunShot g, Sphere s) {
    double bx = s.p.x - g.p.x;
    double by = s.p.y - g.p.y;
    double bz = (s.p.z + s.r) - g.p.z;
    double angle = acos((bx * g.v.x + by * g.v.y + bz * g.v.z) /
                        magnitude(g.v) / magnitude(Point{bx, by, bz}));

    return angle >= M_PI / 2 || abs(g.v.x - bx) == abs(g.v.x) + abs(bx) &&
                                    abs(g.v.y - by) == abs(g.v.y) + abs(by) &&
                                    abs(g.v.z - bz) == abs(g.v.z) + abs(bz);
}

double dot(Point p1, Point p2) {
    double x = p1.x * p2.x;
    double y = p1.y * p2.y;
    double z = p1.z * p2.z;

    return x + y + z;
}

Point unitVector(Point p) {
    double norm = sqrt((p.x * p.x) + (p.y * p.y) + (p.z * p.z));

    return Point{p.x / norm, p.y / norm, p.z / norm};
}

bool check_intersection(GunShot g, Sphere s) {
    Point u = unitVector(g.v);
    if (isBehind(g, s)) return false;

    Point c = {s.p.x, s.p.y, s.p.z + s.r};
    Point p = g.p;
    Point q = dist(g, s);
    double a = dot(u, u);
    double b = 2 * dot(u, q);
    double c1 = dot(q, q) - s.r * s.r;
    double d = (b * b) - (4 * a * c1);

    return d >= 0 ? true : false;
}

int main() {
    int balloons;
    int shots;
    vector<Sphere> spheres;
    vector<GunShot> gunShots;

    cin >> balloons;
    while (balloons != 0) {
        for (int i = 0; i < balloons; i++) {
            Sphere s;
            cin >> s.r >> s.p.z >> s.p.x >> s.p.y;
            s.popped = false;
            spheres.push_back(s);
        }

        cin >> shots;

        for (int i = 0; i < shots; i++) {
            GunShot g;
            cin >> g.p.x >> g.p.y >> g.p.z;
            cin >> g.v.x >> g.v.y >> g.v.z;
            gunShots.push_back(g);
        }

        for (auto& shot : gunShots) {
            int hits = 0;
            for (auto& s : spheres) {
                if (!s.popped) {
                    if (check_intersection(shot, s)) {
                        s.popped = true;
                        hits++;
                    }
                }
            }
            cout << hits << endl;
        }
        cin >> balloons;
        spheres.clear();
        gunShots.clear();
    }

    return 0;
}
