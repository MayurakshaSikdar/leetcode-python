# 2352. Equal Row and Column Pairs

# Given a 0-indexed n x n integer matrix `grid`, return the number of pairs (ri, cj) 
# such that row `ri` and column `cj` are equal.

# A row and column pair is considered equal if they contain the same elements 
# in the same order (i.e., an equal array).

# Example 1:
# Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
# Output: 1
# Explanation: There is 1 equal row and column pair:
# - (Row 2, Column 1): [2,7,7]

# Example 2:
# Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
# Output: 3
# Explanation: There are 3 equal row and column pairs:
# - (Row 0, Column 0): [3,1,2,2]
# - (Row 2, Column 2): [2,4,2,2]
# - (Row 3, Column 2): [2,4,2,2]

# Constraints:
# - n == grid.length == grid[i].length
# - 1 <= n <= 200
# - 1 <= grid[i][j] <= 10^5


from typing import List
from hashlib import md5

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        _row_hash_dict = {}
        _column_hash_dict = {}
        for row in grid:
            key = md5(str(row).encode()).hexdigest()
            if _row_hash_dict.get(key):
                _row_hash_dict[key] += 1
            else:
                _row_hash_dict[key] = 1
        n = len(grid)
        for row in range(n):
            _temp = []
            for column in range(n):
                _temp.append(grid[column][row])
            key = md5(str(_temp).encode()).hexdigest()
            if _column_hash_dict.get(key):
                _column_hash_dict[key] += 1
            else:
                _column_hash_dict[key] = 1
        counter = 0
        for i in _row_hash_dict:
            if i in _column_hash_dict:
                counter += _column_hash_dict[i] * _row_hash_dict[i]

        return counter
