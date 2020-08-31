# Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 
#
# Return the number of negative numbers in grid.
#
#  
# Example 1:
#
#
# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.
#
#
# Example 2:
#
#
# Input: grid = [[3,2],[1,0]]
# Output: 0
#
#
# Example 3:
#
#
# Input: grid = [[1,-1],[-1,-1]]
# Output: 3
#
#
# Example 4:
#
#
# Input: grid = [[-1]]
# Output: 1
#
#
#  
# Constraints:
#
#
# 	m == grid.length
# 	n == grid[i].length
# 	1 <= m, n <= 100
# 	-100 <= grid[i][j] <= 100
#


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        row, col = 0, len(grid[0]) - 1
        res = 0
        while row < len(grid) and col >= 0:
            while grid[row][col] >= 0:
                row += 1
                if row == len(grid):
                    return res
            while grid[row][col] < 0:
                col -= 1
                res += len(grid) - row 
                if col == -1:
                    return res
        return res
            