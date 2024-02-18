#include <iostream>
#include <string>
#include <unordered_map>
#include <cctype>

std::string duplicate_encoder(const std::string& word) {
    std::string result;
    std::unordered_map<char, int> charCount;

    for (char c : word) {
        charCount[std::tolower(c)]++;
    }

    for (char c : word) {
        if (charCount[std::tolower(c)] > 1) {
            result += ')';
        } else {
            result += '(';
        }
    }

    return result;
}
