#include <vector>

int findOdd(const std::vector<int>& numbers) {
    int result = 0;

    for (int num : numbers) {
        result ^= num;
    }

    return result;
}
