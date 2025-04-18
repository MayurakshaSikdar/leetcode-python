# 169. Majority Element


# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.

# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

# Constraints:
# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109

# Follow-up: Could you solve the problem in linear time and in O(1) space?


from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elements = {}.fromkeys(list(set(nums)), 0)
        __max = float('-inf')
        for n in nums:
            elements[n] += 1
            if elements.get(__max, 0) < elements[n]:
                __max = n
        return __max
