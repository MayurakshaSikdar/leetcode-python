# 62. Unique Paths


# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
# The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
# The robot can only move either down or right at any point in time.
# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 10^9.
# Example 1:
# Input: m = 3, n = 7
# Output: 28

# Example 2:
# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down

# Constraints:
# 1 <= m, n <= 100


from typing import List

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1 for _ in range(n)] for _ in range(m)]
        return self.find_path(0, 0, m, n, memo)

    def find_path(self, x: int, y: int, m: int, n: int, memo: List[List[int]]) -> int:
        if x == m - 1 and y == n - 1:
            return 1
        if memo[x][y] != -1:
            return memo[x][y]
        right = 0
        down = 0
        if x < m - 1:
            right = self.find_path(x + 1, y, m, n, memo)
        if y < n - 1:
            down = self.find_path(x, y + 1, m, n, memo)
        memo[x][y] = right + down
        return memo[x][y]
