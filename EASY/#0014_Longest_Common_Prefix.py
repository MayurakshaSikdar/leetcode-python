# 14. Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.


from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        n = len(strs[0])
        if n == 0: return ""
        for i in range(n, 0, -1):
            if all(map(lambda x: x.startswith(strs[0][:i]), strs)):
                return strs[0][:i]
        return ""

print(Solution().longestCommonPrefix(["dog","racecar","car"]))