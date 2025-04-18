# 125. Valid Palindrome

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 
# Constraints:
# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.


class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1
        if len(s.strip()) <= 1:
            return True
        s = s.lower()
        while start <= end:
            chr_start, chr_end = s[start], s[end]
            if not chr_start.isalnum():
                start += 1
                continue
            if not chr_end.isalnum():
                end -= 1
                continue
            if chr_start != chr_end:
                break
            start, end = start + 1, end - 1
        return start >= end
