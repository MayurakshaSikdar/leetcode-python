# 1493. Longest Subarray of 1's After Deleting One Element

# Given a binary array nums, you should delete one element from it.
# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

# Example 1:
# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

# Example 2:
# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

# Example 3:
# Input: nums = [1,1,1]
# Output: 2
# Explanation: You must delete one element.

# Constraints:
# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.


from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 and nums[0] == 1:
            return 0
        if all(map(lambda x: x == 1, nums)):
            return len(nums)-1
        i, j = 0, 0
        _max = 0
        _zero_count = 0
        while i < n:
            if nums[i] == 0:
                _zero_count += 1
            while _zero_count > 1:
                if nums[j] == 0:
                    _zero_count -= 1
                j += 1
            i += 1
            _max = max(_max, i-j-_zero_count)
        return _max
