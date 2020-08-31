# Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.
#
# Example:
#
#
# Input: 3
# Output:
# [
#   [1,null,3,2],
#   [3,2,null,1],
#   [3,1,null,null,2],
#   [2,1,3],
#   [1,null,2,null,3]
# ]
# Explanation:
# The above output corresponds to the 5 unique BST's shown below:
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
#
#
#  
# Constraints:
#
#
# 	0 <= n <= 8
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def construct(self, m, n):
        #return a list of treenodes
        res = []
        if m > n:
            return [None]
        else:
            for i in range(m, n + 1):
                left = self.construct(m, i - 1)
                right = self.construct(i + 1, n)
                for l in left:
                    for r in right:
                        cur_node = TreeNode(i)
                        cur_node.left = l
                        cur_node.right = r
                        res.append(cur_node)
        
        return res
            
            
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        else:
            return self.construct(1, n)
            
            
