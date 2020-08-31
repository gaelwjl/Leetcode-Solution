# A full binary tree is a binary tree where each node has exactly 0 or 2 children.
#
# Return a list of all possible full binary trees with N nodes.  Each element of the answer is the root node of one possible tree.
#
# Each node of each tree in the answer must have node.val = 0.
#
# You may return the final list of trees in any order.
#
#  
#
# Example 1:
#
#
# Input: 7
# Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
# Explanation:
#
#
#
#  
#
# Note:
#
#
# 	1 <= N <= 20
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        memo = {0:[], 1:[TreeNode(0)]}
        def dp(n):
            if n in memo:
                return memo[n]
            elif n % 2 == 1:
                res = []
                for x in range(n):
                    for leftnode in dp(x):
                        for rightnode in dp(n - 1 - x):
                            root = TreeNode(0)
                            root.left = leftnode
                            root.right = rightnode
                            res.append(root)
                memo[n] = res
                return res
            else:
                memo[n] = []
                return []
        return dp(N)
