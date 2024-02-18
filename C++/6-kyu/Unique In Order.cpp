#include <iostream>
#include <vector>

template <typename T>
std::vector<T> uniqueInOrder(const std::vector<T>& iterable) {
    std::vector<T> result;

    for (const T& item : iterable) {
        if (result.empty() || item != result.back()) {
            result.push_back(item);
        }
    }

    return result;
}

std::vector<char> uniqueInOrder(const std::string& iterable) {
    std::vector<char> result;

    for (char c : iterable) {
        if (result.empty() || c != result.back()) {
            result.push_back(c);
        }
    }

    return result;
}
