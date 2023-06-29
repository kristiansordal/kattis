#include <bits/stdc++.h>
int main() {
    std::vector<std::string> days = {"MON", "TUE", "WED", "THU",
                                     "FRI", "SAT", "SUN"};
    std::unordered_map<std::string, int> months;
    months["JAN"] = 0;
    months["FEB"] = months["JAN"] + 31;
    months["MAR"] = months["FEB"] + 28;
    months["APR"] = months["MAR"] + 31;
    months["MAY"] = months["APR"] + 30;
    months["JUN"] = months["MAY"] + 31;
    months["JUL"] = months["JUN"] + 30;
    months["AUG"] = months["JUL"] + 31;
    months["SEP"] = months["AUG"] + 31;
    months["OCT"] = months["SEP"] + 30;
    months["NOV"] = months["OCT"] + 31;
    months["DEC"] = months["NOV"] + 30;

    int day;
    std::string month;
    std::string jan;
    std::cin >> day >> month >> jan;

    auto index = std::find(days.begin(), days.end(), jan) - days.begin();

    for (int i = 0; i < months[month] + (day - 1); i++) {
        index++;
        if (index > 6) {
            index = 0;
        }
    }

    if ((days[index] == "FRI" || days[index] == "THU") &&
        (month != "JAN" && month != "FEB")) {
        std::cout << "Not sure" << std::endl;
    } else if (days[index] == "FRI") {
        std::cout << "TGIF" << std::endl;
    } else {
        std::cout << ":(" << std::endl;
    }

    return 0;
}
