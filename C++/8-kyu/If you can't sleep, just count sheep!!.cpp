#include <string>

std::string countSheep(int number) {
  if (number == 0) {
    return "";
  }
  
  std::string result = "";
  
  for (int i = 1; i <= number; i++) {
    result += std::to_string(i) + " sheep...";
  }
  
  return result;
}
