#include <iostream>
#include <sstream>
#include <string>

int find_short(const std::string& str) {
    std::istringstream iss(str);
    std::string word;
    int shortestLength = std::numeric_limits<int>::max();

    while (iss >> word) {
        int currentLength = static_cast<int>(word.length());
        if (currentLength < shortestLength) {
            shortestLength = currentLength;
        }
    }

    return shortestLength;
}
