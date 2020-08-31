# Find the sum of all left leaves in a given binary tree.
#
# Example:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root == None:
            return 0
        res = 0
        if root.left != None and root.left.left == None and root.left.right == None:
            res += root.left.val
        res += self.sumOfLeftLeaves(root.right) + self.sumOfLeftLeaves(root.left)
        return res
