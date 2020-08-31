# Given a binary tree root. Split the binary tree into two subtrees by removing 1 edge such that the product of the sums of the subtrees are maximized.
#
# Since the answer may be too large, return it modulo 10^9 + 7.
#
#  
# Example 1:
#
#
#
#
# Input: root = [1,2,3,4,5,6]
# Output: 110
# Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)
#
#
# Example 2:
#
#
#
#
# Input: root = [1,null,2,3,4,null,null,5,6]
# Output: 90
# Explanation:  Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)
#
#
# Example 3:
#
#
# Input: root = [2,3,9,10,7,8,6,5,4,11,1]
# Output: 1025
#
#
# Example 4:
#
#
# Input: root = [1,1]
# Output: 1
#
#
#  
# Constraints:
#
#
# 	Each tree has at most 50000 nodes and at least 2 nodes.
# 	Each node's value is between [1, 10000].
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        self.res = 0  
        total = 0
        def sum_(Node):
            if Node == None:
                return 0
            sum_l, sum_r = sum_(Node.left), sum_(Node.right)
            self.res = max(self.res, sum_l * (total - sum_l), sum_r * (total - sum_r))
            return sum_l + sum_r + Node.val
        total = sum_(root)
        sum_(root)
        return self.res % (10**9 + 7)
