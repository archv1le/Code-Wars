#include <iostream>
#include <vector>
#include <algorithm>

bool check(const std::vector<std::string>& seq, const std::string& elem) {
    return std::find(seq.begin(), seq.end(), elem) != seq.end();
}
