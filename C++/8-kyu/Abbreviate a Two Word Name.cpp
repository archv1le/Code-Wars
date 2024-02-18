#include <iostream>
#include <string>
#include <cctype>

std::string abbrevName(const std::string& name) {
    std::string initials;
    bool capitalizeNext = true;

    for (char c : name) {
        if (std::isspace(c)) {
            capitalizeNext = true; 
        } else if (capitalizeNext) {
            initials += std::toupper(c);  
            capitalizeNext = false;
        }
    }

    if (initials.length() == 2) {
        initials.insert(1, 1, '.');
    }

    return initials;
}
