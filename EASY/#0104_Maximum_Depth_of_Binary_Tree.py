# 104. Maximum Depth of Binary Tree


# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Example 2:
# Input: root = [1,null,2]
# Output: 2

# Constraints:
# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        else:
            leftD = self.maxDepth(root.left)
            rightD = self.maxDepth(root.right)
            if leftD < rightD:
                return rightD + 1
            return leftD + 1




def insert(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def create_bst(values):
    if not values:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1

    while i < len(values):
        node = queue.pop(0)

        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root

# Create the BST
root = create_bst([3, 9, 20, None, None, 15, 7])

# Print the BST (in-order traversal)
def inorder(root):
    if root:
        print(root.val, end=" ")
        inorder(root.left)
        inorder(root.right)

inorder(root)