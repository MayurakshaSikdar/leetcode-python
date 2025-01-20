# 450. Delete Node in a BST

# Given a root node reference of a BST and a key, delete the node with the given key in the BST.
# Return the root node reference (possibly updated) of the BST.
# Basically, the deletion can be divided into two stages:
# Search for a node to remove.
# If the node is found, delete the node.

# Example 1:
# Input: root = [5,3,6,2,4,null,7], key = 3
# Output: [5,4,6,2,null,null,7]
# Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
# One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
# Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

# Example 2:
# Input: root = [5,3,6,2,4,null,7], key = 0
# Output: [5,3,6,2,4,null,7]
# Explanation: The tree does not contain a node with value = 0.

# Example 3:
# Input: root = [], key = 0
# Output: []

# Constraints:
# The number of nodes in the tree is in the range [0, 10^4].
# -10^5 <= Node.val <= 10^5
# Each node has a unique value.
# root is a valid binary search tree.
# -10^5 <= key <= 10^5

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if root.val == key:
            return self.traverser(root)
        answer = root
        while root:
            if root.val > key:
                if root.left and root.left.val == key:
                    root.left = self.traverser(root.left)
                    break
                else:
                    root = root.left
            else:
                if root.right and root.right.val == key:
                    root.right = self.traverser(root.right)
                    break
                else:
                    root = root.right
        return answer


    def traverser(self, node):
        if not node.left:
            return node.right
        if not node.right:
            return node.left
        rc = node.right
        left_biggest = self.find_biggest(node.left)
        left_biggest.right = rc
        return node.left


    def find_biggest(self, node):
        while node.right:
            node = node.right
        return node
