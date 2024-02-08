#include <string>

std::string fakeBin(std::string str) {
  std::string result = str;
  
  for (char& digit : result) {
    if (digit < '5') {
      digit = '0';
    } else {
      digit = '1';
    }
  }
  
  return result;
}
