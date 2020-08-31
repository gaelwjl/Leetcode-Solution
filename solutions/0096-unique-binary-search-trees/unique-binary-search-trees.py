# Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
#
# Example:
#
#
# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:
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
# 	1 <= n <= 19
#
#


class Solution:
    @lru_cache(None)
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 1
        if n <= 2:
            return n
        res = 0
        for k in range(n):
            res += self.numTrees(k) * self.numTrees(n - 1 - k)
        return res
