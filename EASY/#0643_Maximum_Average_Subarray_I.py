# 643. Maximum Average Subarray I

# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
# Any answer with a calculation error less than 10^-5 will be accepted.

# Example 1:
# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

# Example 2:
# Input: nums = [5], k = 1
# Output: 5.00000

# Constraints:
# n == nums.length
# 1 <= k <= n <= 10^5
# -10^4 <= nums[i] <= 10^4

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        if n < k:
            return 0.0
        if n == k:
            return sum(nums) / k
        max_sum = current_sum = sum(nums[:k])
        for i in range(k, n):
            current_sum = current_sum - nums[i - k] + nums[i]
            max_sum = max(max_sum, current_sum)
        return max_sum / k
