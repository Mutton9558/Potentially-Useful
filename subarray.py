# A system that can determine sum of a given subarray with the condition that it is the maximum possible sum from all possible subarrays
# Python Version
import sys

def maxSubArray(nums):
    sum = 0
    maxSum = -sys.maxsize - 1
    for num in nums:
        sum = max(sum, 0) + num
        maxSum = max(maxSum, sum)

    return maxSum

nums = [-2,1,-3,8,-3]
print(maxSubArray(nums))