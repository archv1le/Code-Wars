#include <string>

class Accumul {
public:
    static std::string accum(const std::string &s);
};

std::string Accumul::accum(const std::string &s) {
    std::string result;

    for (std::size_t i = 0; i < s.length(); ++i) {
        result += std::toupper(s[i]);
        for (std::size_t j = 0; j < i; ++j) {
            result += std::tolower(s[i]);
        }

        if (i < s.length() - 1) {
            result += '-';
        }
    }

    return result;
}
