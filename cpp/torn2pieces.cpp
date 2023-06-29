#include <bits/stdc++.h>

#include <set>
using namespace std;

vector<string> backtrace(unordered_map<string, string> parents, string root,
                         string end) {
    vector<string> path = {end};
    string curr = end;

    while (curr != root) {
        path.push_back(parents[curr]);
        curr = parents[curr];
    }
    return path;
}

void bfs(unordered_map<string, set<string>> graph, string root, string end) {
    set<string> found = {root};
    queue<string> toSearch;
    unordered_map<string, string> parents;

    toSearch.push(root);

    while (!toSearch.empty()) {
        string curr = toSearch.front();
        toSearch.pop();

        if (curr == end) {
            auto path = backtrace(parents, root, end);
            for (int i = path.size() - 1; i >= 0; i--) {
                cout << path[i] << " ";
            }
            return;
        }

        for (const auto n : graph[curr]) {
            if (found.find(n) == found.end()) {
                found.emplace(n);
                toSearch.push(n);
                if (n != curr) {
                    parents[n] = curr;
                }
            }
        }
    }
    cout << "no route found" << endl;
}
int main() {
    int n;
    cin >> n;

    unordered_map<string, set<string>> graph;

    for (int i = 0; i <= n; i++) {
        string input;
        getline(cin, input);

        stringstream ss(input);
        string word;
        vector<string> words = {};

        while (ss >> word) {
            words.push_back(word);
        }

        for (int i = 1; i < words.size(); i++) {
            graph[words[0]].emplace(words[i]);
            graph[words[i]].emplace(words[0]);
        }
    }

    string root, end;
    cin >> root >> end;

    bfs(graph, root, end);
    return 0;
}
