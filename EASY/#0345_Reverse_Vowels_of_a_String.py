# 345. Reverse Vowels of a String

# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# Example 1:
# Input: s = "IceCreAm"
# Output: "AceCreIm"
# Explanation:
# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"

# Constraints:
# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.


class Solution:
    def reverseVowels(self, s: str) -> str:
        _VOWEL = {
            'a': True,
            'e': True,
            'i': True,
            'o': True,
            'u': True,
            'A': True,
            'E': True,
            'I': True,
            'O': True,
            'U': True,
        }
        if not s:
            return ''

        n = len(s) - 1
        data = list(s)
        i = 0
        while i < n:
            char_first, char_last = data[i], data[n]
            if char_first in _VOWEL and char_last in _VOWEL:
                data[i], data[n] = char_last, char_first
                i += 1
                n -= 1
            if char_first not in _VOWEL:
                i += 1
            if char_last not in _VOWEL:
                n -= 1
        return ''.join(data)
