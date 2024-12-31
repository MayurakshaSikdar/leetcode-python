# 1071. Greatest Common Divisor of Strings

# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t
# (i.e., t is concatenated with itself one or more times).
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

# Example 1:
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"

# Example 2:
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"

# Example 3:
# Input: str1 = "LEET", str2 = "CODE"
# Output: ""

# Constraints:
# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of English uppercase letters.


class Solution(object):
    def gcdOfStrings(self, str1, str2):
        n1, n2 = len(str1), len(str2)
        smaller = min(n1, n2)
        def check_divisor(n):
            if n1%n == 1 or n2%n == 1:
                return False
            return (str1[:n] * (n1//n)) == str1 and (str1[:n] * (n2//n)) == str2

        for i in range(smaller, 0, -1):
            if check_divisor(i):
                return str1[:i]
        return ''
