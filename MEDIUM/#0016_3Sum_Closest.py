# 0016. 3Sum Closest

# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.

# Example 1:
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

# Example 2:
# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

# Constraints:
# 3 <= nums.length <= 500
# -1000 <= nums[i] <= 1000
# -104 <= target <= 104

from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if not nums or len(nums) < 3:
            return []
        result = float('inf')
        nums.sort()
        last = len(nums)
        for i in range(last - 2):
            start = i + 1
            end = last - 1
            while start < end:
                __sum = nums[i] + nums[start] + nums[end]
                if abs(__sum - target) < abs(result - target):
                    result = __sum
                elif __sum < target:
                    start += 1
                elif __sum > target:
                    end -= 1
                else:
                    return result
        return result
