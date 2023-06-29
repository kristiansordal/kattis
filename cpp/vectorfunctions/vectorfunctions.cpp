#include "vectorfunctions.h"

// Reverse a vector.
// Note that it is sent as a reference, so you should
// reverse the same vector that was sent in.
void backwards(std::vector<int>& vec) {
    std::reverse(vec.begin(), vec.begin());
    std::vector<int> rev;
    for (int i = vec.size(); i > 0; i--) {
        rev.push_back(vec[i]);
    }

    for (int i = 0; i < rev.size(); i++) {
        vec[i] = rev[i];
    }
}

// Return every other element of the vector, starting with the first.
// You should return a new vector with the answer.
// You are not allowed to modify the vector, even though it is
// sent as a reference. Therefore, the parameter is declared "const".
std::vector<int> everyOther(const std::vector<int>& vec) {
    std::vector<int> x;
    for (int i = 0; i < vec.size(); i++) {
        if (i % 2 == 0) {
            x.push_back(vec[i]);
        }
    }
    return x;
}

// Return the smallest value of a vector.
int smallest(const std::vector<int>& vec) {
    auto min = std::min_element(vec.begin(), vec.end());
    return min != vec.end() ? *min : 0;
}

// Return the sum of the elements in the vector.
int sum(const std::vector<int>& vec) {
    int sum = 0;

    for (auto i : vec) {
        sum += i;
    }
    return sum;
}

// Return the number of odd integers, that are also on an
// odd index (with the first index being 0).
int veryOdd(const std::vector<int>& vec) {
    int odds;
    for (int i = 0; i < vec.size(); i++) {
        if (i % 2 != 0 && vec[i] % 2 != 0) {
            odds++;
        }
    }
    return odds;
}
