#include <vector>
#include <algorithm>

int findSmallest(std::vector <int> list) {
  auto smallestInteger = std::min_element(list.begin(), list.end());
  
  if (smallestInteger != list.end()) {
    return *smallestInteger;
  }
  
  return 0;
}
