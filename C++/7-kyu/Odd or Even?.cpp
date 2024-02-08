#include <string>
#include <vector>
#include <bits/stdc++.h>

std::string odd_or_even(const std::vector<int> &arr) {
  int vectorSum = accumulate(arr.begin(), arr.end(), 0);
  
  return vectorSum % 2 ? "odd" : "even";
}
