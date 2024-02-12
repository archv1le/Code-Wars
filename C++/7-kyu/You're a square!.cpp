#include <cmath>

bool is_square(int n) {
  if (n < 0) {
    return false;
  }

  int sqrt_n = static_cast<int>(sqrt(n));

  return sqrt_n * sqrt_n == n;
}
