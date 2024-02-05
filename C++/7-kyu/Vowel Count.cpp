#include <string>

int getCount(const std::string& inputStr) {
  int vowelCount = 0;
  
  for (char c : inputStr) {
    if (std::tolower(c) == 'a' ||
        std::tolower(c) == 'e' ||
        std::tolower(c) == 'i' ||
        std::tolower(c) == 'o' ||
        std::tolower(c) == 'u') {
      vowelCount++;
    }
  }
  
  return vowelCount;
}
