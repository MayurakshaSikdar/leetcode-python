# 383. Ransom Note

# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true

# Constraints:
# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if not ransomNote:
            return True
        if len(ransomNote) > len(magazine):
            return False
        letters = {}.fromkeys(set(magazine), 0)
        for l in magazine:
            letters[l] = letters.get(l, 0) + 1
        for i in ransomNote:
            if letters.get(i, 0) < 1:
                return False
            letters[i] -= 1
        return True


print(Solution().canConstruct(ransomNote = "a", magazine = "b"))
print(Solution().canConstruct(ransomNote = "aa", magazine = "ab"))
print(Solution().canConstruct(ransomNote = "aa", magazine = "aab"))