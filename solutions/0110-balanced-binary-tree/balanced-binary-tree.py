# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as:
#
#
# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
#
#
#  
#
# Example 1:
#
# Given the following tree [3,9,20,null,null,15,7]:
#
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# Return true.
#
# Example 2:
#
# Given the following tree [1,2,2,3,3,null,null,4,4]:
#
#
#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
#
#
# Return false.
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def _isBalanced(self, Node):
        if Node == None:
            return 0
        left = self._isBalanced(Node.left)
        right = self._isBalanced(Node.right)
        print(left, right)
        if left == -1 or right == -1:
            return -1
        elif abs(right - left) > 1:
            return -1
        else:
            return max(left, right) + 1
    
    
    def isBalanced(self, root: TreeNode) -> bool:
        return self._isBalanced(root) != -1
