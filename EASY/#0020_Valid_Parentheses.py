# 20. Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([])"
# Output: true

# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.


from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        if s == None or len(s)%2 == 1:
            return False
        stack = []
        top = -1
        openBraces = ('(', '{', '[')
        closeBraces = (')', '}', ']')
        for i in s:
            if i in openBraces:
                stack.append(i)
                top += 1
            elif i in closeBraces and top != -1:
                if i == ')' and stack[top] != '(':
                    return False
                elif i == '}' and stack[top] != '{':
                    return False
                elif i == ']' and stack[top] != '[':
                    return False
                else:
                    stack.pop()
                    top -= 1
            else:
                return False
        if top != -1:
            return False
        return True