# 135. Candy


# There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
# You are giving candies to these children subjected to the following requirements:
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# Return the minimum number of candies you need to have to distribute the candies to the children.

# Example 1:
# Input: ratings = [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

# Example 2:
# Input: ratings = [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
# The third child gets 1 candy because it satisfies the above two conditions.

# Constraints:
# n == ratings.length
# 1 <= n <= 2 * 104
# 0 <= ratings[i] <= 2 * 104


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
