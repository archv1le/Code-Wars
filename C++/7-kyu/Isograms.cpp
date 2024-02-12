#include <string>
#include <unordered_set>
#include <cctype>

bool is_isogram(const std::string& str) {
  std::unordered_set<char> seenChars;

  for (char ch : str) {
    char lowerCh = std::tolower(ch);

    if (seenChars.count(lowerCh) > 0) {
      return false;
    }

    seenChars.insert(lowerCh);
  }

  return true;
}
