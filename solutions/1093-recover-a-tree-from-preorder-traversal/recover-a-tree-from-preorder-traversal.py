# We run a preorder depth first search on the root of a binary tree.
#
# At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  (If the depth of a node is D, the depth of its immediate child is D+1.  The depth of the root node is 0.)
#
# If a node has only one child, that child is guaranteed to be the left child.
#
# Given the output S of this traversal, recover the tree and return its root.
#
#  
#
# Example 1:
#
#
#
#
# Input: "1-2--3--4-5--6--7"
# Output: [1,2,5,3,4,6,7]
#
#
#
# Example 2:
#
#
#
#
# Input: "1-2--3---4-5--6---7"
# Output: [1,2,5,3,null,6,null,4,null,7]
#
#
#
#  
#
#
# Example 3:
#
#
#
#
# Input: "1-401--349---90--88"
# Output: [1,401,null,349,88,90]
#
#
#
#  
#
# Note:
#
#
# 	The number of nodes in the original tree is between 1 and 1000.
# 	Each node will have a value between 1 and 10^9.
#
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        n = len(S)
        depth = 0
        tmp = ""
        stack = []
        i = 0
        while i < n:
            while i < n and S[i] == '-':
                depth += 1
                i += 1
            while i < n and S[i].isdigit():
                tmp += S[i]
                i += 1
            while len(stack) > depth:
                stack.pop()
            node = TreeNode(int(tmp))
            if stack and stack[-1].left == None:
                stack[-1].left = node
            elif stack:
                stack[-1].right = node
            tmp = ""
            depth = 0
            stack.append(node)
        return stack[0]
            
