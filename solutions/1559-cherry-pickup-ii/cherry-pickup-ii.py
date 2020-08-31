# Given a rows x cols matrix grid representing a field of cherries. Each cell in grid represents the number of cherries that you can collect.
#
# You have two robots that can collect cherries for you, Robot #1 is located at the top-left corner (0,0) , and Robot #2 is located at the top-right corner (0, cols-1) of the grid.
#
# Return the maximum number of cherries collection using both robots  by following the rules below:
#
#
# 	From a cell (i,j), robots can move to cell (i+1, j-1) , (i+1, j) or (i+1, j+1).
# 	When any robot is passing through a cell, It picks it up all cherries, and the cell becomes an empty cell (0).
# 	When both robots stay on the same cell, only one of them takes the cherries.
# 	Both robots cannot move outside of the grid at any moment.
# 	Both robots should reach the bottom row in the grid.
#
#
#  
# Example 1:
#
#
#
#
# Input: grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
# Output: 24
# Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
# Cherries taken by Robot #1, (3 + 2 + 5 + 2) = 12.
# Cherries taken by Robot #2, (1 + 5 + 5 + 1) = 12.
# Total of cherries: 12 + 12 = 24.
#
#
# Example 2:
#
#
#
#
# Input: grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
# Output: 28
# Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
# Cherries taken by Robot #1, (1 + 9 + 5 + 2) = 17.
# Cherries taken by Robot #2, (1 + 3 + 4 + 3) = 11.
# Total of cherries: 17 + 11 = 28.
#
#
# Example 3:
#
#
# Input: grid = [[1,0,0,3],[0,0,0,3],[0,0,3,3],[9,0,3,3]]
# Output: 22
#
#
# Example 4:
#
#
# Input: grid = [[1,1],[1,1]]
# Output: 4
#
#
#  
# Constraints:
#
#
# 	rows == grid.length
# 	cols == grid[i].length
# 	2 <= rows, cols <= 70
# 	0 <= grid[i][j] <= 100 
#
#


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        @lru_cache(None)
        def dfs(i, p1, p2):
            if p1 >= p2:
                return -float('inf')
            if i == 0:
                if p1 != 0 or p2 != m - 1:
                    return -float('inf')
                else:
                    return grid[0][0] + grid[0][m - 1]
            ans = -float('inf')
            for np1 in range(max(p1 - 1, 0), min(p1 + 2, m)):
                for np2 in range(max(np1 + 1, max(p2 - 1, 0)), min(p2 + 2, m)):
                    if np1 == np2:
                        continue
                    if p1 != p2:
                        ans = max(ans, dfs(i - 1, np1, np2) + grid[i][p1] + grid[i][p2])
                    else:
                        ans = max(ans, dfs(i - 1, np1, np2) + grid[i][p1])
            return ans
        
        ans = -float('inf')
        for i in range(m):
            for j in range(i + 1, m):
                ans = max(ans, dfs(n - 1, i, j))
        return ans
