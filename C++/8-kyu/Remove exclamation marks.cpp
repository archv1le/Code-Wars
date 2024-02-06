#include <string>
#include <algorithm>

std::string removeExclamationMarks(std::string str) {
    auto iterator = std::remove_if(str.begin(), str.end(), [](char c) { return c == '!'; });
    
    str.erase(iterator, str.end());

    return str;
}
