# Given an array arr of positive integers, consider all binary trees such that:
#
#
# 	Each node has either 0 or 2 children;
# 	The values of arr correspond to the values of each leaf in an in-order traversal of the tree.  (Recall that a node is a leaf if and only if it has 0 children.)
# 	The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree respectively.
#
#
# Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node.  It is guaranteed this sum fits into a 32-bit integer.
#
#  
# Example 1:
#
#
# Input: arr = [6,2,4]
# Output: 32
# Explanation:
# There are two possible trees.  The first has non-leaf node sum 36, and the second has non-leaf node sum 32.
#
#     24            24
#    /  \          /  \
#   12   4        6    8
#  /  \               / \
# 6    2             2   4
#
#
#  
# Constraints:
#
#
# 	2 <= arr.length <= 40
# 	1 <= arr[i] <= 15
# 	It is guaranteed that the answer fits into a 32-bit signed integer (ie. it is less than 2^31).
#


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        @lru_cache(None)
        def dfs(i, j):
            if i == j:
                return 0, arr[i]
            elif j == i + 1:
                return arr[i] * arr[i + 1], max(arr[i], arr[i + 1])
            ans = float('inf')
            ll = arr[i]
            for k in range(i, j):
                ll = max(ll, arr[k])
                ans = min(ans, dfs(i, k)[0] + dfs(k + 1, j)[0] +  dfs(i, k)[1] * dfs(k + 1, j)[1])
            return ans, max(ll, arr[j])
        return dfs(0, len(arr) - 1)[0]
