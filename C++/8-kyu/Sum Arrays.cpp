#include <iostream>
#include <vector>

int sum(const std::vector<int>& nums) {
    int result = 0;

    for (int num : nums) {
        result += num;
    }

    return result;
}
