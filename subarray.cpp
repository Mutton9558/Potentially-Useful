// A system that can determine sum of a given subarray with the condition that it is the maximum possible sum from all possible subarrays
// C++ Version
#include <iostream>
#include <climits>

int maxSubArray(int nums[], int size) {
    int sum = 0;
    int maxSum = INT_MIN;

    for (int i = 0; i < size; ++i) {
        sum = std::max(sum, 0) + nums[i];
        maxSum = std::max(maxSum, sum);
    }
    return maxSum;
}

int main() {
    int nums[5] = {-2, 1, -3, 8, -3};
    std::cout << maxSubArray(nums, 5);
    return 0;
}