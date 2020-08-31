# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
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
# return its zigzag level order traversal as:
#
# [
#   [3],
#   [20,9],
#   [15,7]
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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        ans = []
        tovis = deque()
        tovis.append(root)
        sgn = 1
        while tovis:
            s = len(tovis)
            toappend = []
            while s:
                cur = tovis.popleft()
                toappend.append(cur.val)
                if cur.left:
                    tovis.append(cur.left)
                if cur.right:
                    tovis.append(cur.right)
                s -= 1
            if sgn == -1:
                toappend = toappend[::-1]
            ans.append(toappend)
            sgn *= -1
        return ans
