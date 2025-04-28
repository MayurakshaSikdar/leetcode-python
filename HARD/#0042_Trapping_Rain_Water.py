# 42. Trapping Rain Water


# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it can trap after raining.

# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

# Example 2:
# Input: height = [4,2,0,3,2,5]
# Output: 9

# Constraints:
# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105


from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        if len(ratings) < 2:
            return n
        i, j = 0, 1
        while j < n:
            if ratings[j] > ratings[i]:
                candies[j] = (candies[i] + 1)
            i, j = i+1, j+1
        i, j = n-1, n-2
        while j >= 0:
            if ratings[j] > ratings[i]:
                candies[j] = max(candies[j], candies[i] + 1)
            i, j = i-1, j-1
        return sum(candies)
