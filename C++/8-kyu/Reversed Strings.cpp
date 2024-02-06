#include <string> 
#include <algorithm>

std::string reverseString(std::string str) {
  std::string result = str;
  
  std::reverse(result.begin(), result.end());

  return result;
}
