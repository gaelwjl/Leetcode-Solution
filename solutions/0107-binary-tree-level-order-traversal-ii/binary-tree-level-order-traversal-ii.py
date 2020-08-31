# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
#
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
#
#
# return its bottom-up level order traversal as:
#
# [
#   [15,7],
#   [9,20],
#   [3]
# ]
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        tosee = deque()
        tosee.append(root)
        ans = []
        while tosee:
            s = len(tosee)
            level = []
            while s:
                cur = tosee.popleft()
                if cur.left:
                    tosee.append(cur.left)
                if cur.right:
                    tosee.append(cur.right)
                level.append(cur.val)
                s -= 1
            ans.append(level)
        return ans[::-1]
