# Given the root of a binary tree, each node in the tree has a distinct value.
#
# After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).
#
# Return the roots of the trees in the remaining forest.  You may return the result in any order.
#
#  
# Example 1:
#
#
#
#
# Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
# Output: [[1,2,null,4],[6],[7]]
#
#
#  
# Constraints:
#
#
# 	The number of nodes in the given tree is at most 1000.
# 	Each node has a distinct value between 1 and 1000.
# 	to_delete.length <= 1000
# 	to_delete contains distinct values between 1 and 1000.
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        ans = []
        def dfs(node):
            if not node:
                return node
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            if node.val not in to_delete:
                return node
            if node.left:
                ans.append(node.left)
            if node.right: 
                ans.append(node.right)
        root = dfs(root)
        if root:
            ans.append(root)
        return ans
        
            
            
        
        
