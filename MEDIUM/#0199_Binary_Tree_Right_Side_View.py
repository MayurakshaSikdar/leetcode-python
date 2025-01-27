# 199. Binary Tree Right Side View


# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Example 1:
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
# Explanation:
#         1             <--
#     /     \
#   2         3         <--
#   \           \
#     5           4     <--

# Example 2:
# Input: root = [1,2,3,4,null,null,null,5]
# Output: [1,3,4,5]
# Explanation:
#             1         <--
#           /   \
#         2      3      <--
#       /
#     4     <--------------
#   /
# 5     <------------------

# Example 3:
# Input: root = [1,null,3]
# Output: [1,3]

# Example 4:
# Input: root = []
# Output: []

# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100


from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result
        queue = deque([root])
        while queue:
            right = None
            queue_len = len(queue)
            for _ in range(queue_len):
                node = queue.popleft()
                if node:
                    right = node
                    queue.append(node.left)
                    queue.append(node.right)
            if right:
                result.append(right.val)
        return result
