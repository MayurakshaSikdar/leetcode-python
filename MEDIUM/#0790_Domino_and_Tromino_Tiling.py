# 790. Domino and Tromino Tiling

# You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.
# Given an integer n, return the number of ways to tile an 2 x n board.
# Since the answer may be very large, return it modulo 109 + 7.
# In a tiling, every square must be covered by a tile. Two tilings are different if and only if 
# there are two 4-directionally adjacent cells on the board such that exactly one of the tilings 
# has both squares occupied by a tile.

# Example 1:
# Input: n = 3
# Output: 5
# Explanation: The five different ways are show above.

# Example 2:
# Input: n = 1
# Output: 1

# Constraints:
# 1 <= n <= 1000


class Solution:
    def numTilings(self, N: int) -> int:
        modulus = 10**9 + 7
        memory = [0] * 1001
        memory[1], memory[2], memory[3] = 1, 2, 5
        if N <= 3:
            return memory[N]
        for i in range(4, N + 1):
            memory[i] = 2 * memory[i - 1] + memory[i - 3]
            memory[i] %= modulus
        return memory[N]
