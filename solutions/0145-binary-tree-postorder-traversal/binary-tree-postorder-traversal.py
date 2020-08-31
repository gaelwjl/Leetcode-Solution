# Given the root of a binary tree, return the postorder traversal of its nodes' values.
#
# Follow up: Recursive solution is trivial, could you do it iteratively?
#
#  
# Example 1:
#
#
# Input: root = [1,null,2,3]
# Output: [3,2,1]
#
#
# Example 2:
#
#
# Input: root = []
# Output: []
#
#
# Example 3:
#
#
# Input: root = [1]
# Output: [1]
#
#
# Example 4:
#
#
# Input: root = [1,2]
# Output: [2,1]
#
#
# Example 5:
#
#
# Input: root = [1,null,2]
# Output: [2,1]
#
#
#  
# Constraints:
#
#
# 	The number of the nodes in the tree is in the range [0, 100].
# 	-100 <= Node.val <= 100
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        tovis = [root]
        ans = []
        while tovis:
            cur = tovis.pop(-1)
            if cur == None:
                continue
            ans.append(cur.val)
            if cur.left:
                tovis.append(cur.left)
            if cur.right:
                tovis.append(cur.right)
        return ans[::-1]
