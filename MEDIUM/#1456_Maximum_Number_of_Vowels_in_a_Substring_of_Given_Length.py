# 1456. Maximum Number of Vowels in a Substring of Given Length

# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

# Example 1:
# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.

# Example 2:
# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.

# Example 3:
# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.

# Constraints:
# 1 <= s.length <= 105
# s consists of lowercase English letters.
# 1 <= k <= s.length


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        __VOWEL = {
            'a': True,
            'e': True,
            'i': True,
            'o': True,
            'u': True
        }
        _max_vowel = _vowel = sum(_ in __VOWEL for _ in s[:k])
        j = 0
        for i in range(k, n):
            _vowel += 1 if s[i] in __VOWEL else 0
            _vowel -= 1 if s[j] in __VOWEL else 0
            _max_vowel = max(_max_vowel, _vowel)
            j += 1
        return _max_vowel
