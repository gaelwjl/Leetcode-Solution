# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
#
#
#
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
#
# Note: m and n will be at most 100.
#
# Example 1:
#
#
# Input:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# Output: 2
# Explanation:
# There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
#
#


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        number_paths = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if i == 0 and j == 0 and obstacleGrid[0][0] == 0:
                    number_paths[0][0] = 1
                elif i == 0 and obstacleGrid[0][j] == 0:
                    number_paths[0][j] = number_paths[0][j - 1]
                elif j == 0 and obstacleGrid[i][0] == 0:
                    number_paths[i][0] = number_paths[i - 1][0]
                elif obstacleGrid[i][j] == 0:
                    number_paths[i][j] = number_paths[i - 1][j] + number_paths[i][j - 1]
        return number_paths[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1]
