# Given a non-empty binary tree, find the maximum path sum.
#
# For this problem, a path is defined as any node sequence from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.
#
#  
# Example 1:
#
#
# Input: root = [1,2,3]
# Output: 6
#
#
# Example 2:
#
#
# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
#
#
#  
# Constraints:
#
#
# 	The number of nodes in the tree is in the range [0, 3 * 104].
# 	-1000 <= Node.val <= 1000
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = -float('inf')
        def dfs(node):
            lp, rp = 0, 0
            if node.left:
                lp = dfs(node.left)
            if node.right: 
                rp = dfs(node.right)
            self.ans = max(self.ans, max(lp, 0) + max(rp, 0) + node.val)
            return max(max(lp, 0), max(rp, 0)) + node.val
        dfs(root)
        return self.ans

