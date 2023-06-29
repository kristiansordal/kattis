#include <bits/stdc++.h>

#include <sstream>
class Player {
   public:
    Player(const std::string &name, int skill1, int skill2, int skill3)
        : name(name), skill1(skill1), skill2(skill2), skill3(skill3) {}

    std::string name;
    int skill1;
    int skill2;
    int skill3;
};

struct cmpskill1 {
    bool operator()(const Player &a, const Player &b) const {
        if (a.skill1 == b.skill1) {
            std::string as = a.name;
            as.erase(0, 6);
            std::string bs = b.name;
            bs.erase(0, 6);
            return std::stoi(as) > std::stoi(bs);
        }
        return a.skill1 < b.skill1;
    }
};

struct cmpskill2 {
    bool operator()(const Player &a, const Player &b) const {
        if (a.skill2 == b.skill2) {
            std::string as = a.name;
            as.erase(0, 6);
            std::string bs = b.name;
            bs.erase(0, 6);
            return std::stoi(as) > std::stoi(bs);
        }
        return a.skill2 < b.skill2;
    }
};
struct cmpskill3 {
    bool operator()(const Player &a, const Player &b) const {
        if (a.skill3 == b.skill3) {
            std::string as = a.name;
            as.erase(0, 6);
            std::string bs = b.name;
            bs.erase(0, 6);
            return std::stoi(as) > std::stoi(bs);
        }
        return a.skill3 < b.skill3;
    }
};
int main() {
    int n;
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cin >> n;

    // three pqs with comparators for each skill and name
    // hashmap to see if they have already been selected
    std::priority_queue<Player, std::vector<Player>, cmpskill1> pqskill1;
    std::priority_queue<Player, std::vector<Player>, cmpskill2> pqskill2;
    std::priority_queue<Player, std::vector<Player>, cmpskill3> pqskill3;
    std::unordered_map<std::string, bool> chosen;

    for (int i = 0; i < n; i++) {
        std::vector<std::string> l;
        for (int i = 0; i < 4; i++) {
            std::string s;
            std::cin >> s;
            l.push_back(s);
        }

        Player p =
            Player(l[0], std::stoi(l[1]), std::stoi(l[2]), std::stoi(l[3]));
        pqskill1.emplace(p);
        pqskill2.emplace(p);
        pqskill3.emplace(p);
    }

    int size = n;

    while (size % 3 != 0) {
        size -= 1;
    }

    while (chosen.size() < size) {
        std::vector<std::string> team;
        for (int i = 0; i < 3; i++) {
            if (i == 0) {
                Player curr = pqskill1.top();
                while (chosen.count(curr.name)) {
                    pqskill1.pop();
                    curr = pqskill1.top();
                }
                chosen[curr.name] = true;
                team.push_back(curr.name);
            } else if (i == 1) {
                Player curr = pqskill2.top();
                while (chosen.count(curr.name)) {
                    pqskill2.pop();
                    curr = pqskill2.top();
                }
                chosen[curr.name] = true;
                team.push_back(curr.name);

            } else {
                Player curr = pqskill3.top();
                while (chosen.count(curr.name)) {
                    pqskill3.pop();
                    curr = pqskill3.top();
                }
                chosen[curr.name] = true;
                team.push_back(curr.name);
            }
        }
        sort(team.begin(), team.end());
        std::cout << team[0] << " " << team[1] << " " << team[2] << std::endl;
        team.clear();
    }
    return 0;
}
