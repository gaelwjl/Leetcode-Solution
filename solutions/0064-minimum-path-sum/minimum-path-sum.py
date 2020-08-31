# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
#
# Example:
#
#
# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.
#
#


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        partialMin = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    partialMin[0][0] = grid[0][0]
                elif i == 0:
                    partialMin[0][j] = partialMin[0][j - 1] + grid[0][j]
                elif j == 0:
                    partialMin[i][0] = partialMin[i - 1][0] + grid[i][0]
                else:
                    partialMin[i][j] = min(partialMin[i - 1][j] + grid[i][j], partialMin[i][j - 1] + grid[i][j])
        return partialMin[n - 1][m - 1]
