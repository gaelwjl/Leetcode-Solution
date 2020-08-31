# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
#  
# Example 1:
#
#
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
#
#
# Example 2:
#
#
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
#
#


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        if n >= 1:
            m = len(grid[0])
        else:
            return 0
        seen = [[0 for _ in range(m)] for _ in range(n)]
        
        def bfs(grid, i, j, n, m):
            seen[i][j] = 1
            if i + 1 < n and grid[i + 1][j] == '1' and seen[i + 1][j] == 0:
                bfs(grid, i + 1, j, n, m)
            if j + 1 < m and grid[i][j + 1] == '1' and seen[i][j + 1] == 0:
                bfs(grid, i, j + 1, n, m)
            if j - 1 >= 0 and grid[i][j - 1] == '1' and seen[i][j - 1] == 0:
                bfs(grid, i, j - 1, n, m)
            if i - 1 >= 0 and grid[i-1][j] == '1' and seen[i - 1][j] == 0:
                bfs(grid, i - 1, j, n, m)
            
        res = 0
        for i_iter in range(n):
            for j_iter in range(m):
                if grid[i_iter][j_iter] == '1' and seen[i_iter][j_iter] == 0:
                    bfs(grid, i_iter, j_iter, n, m)
                    res += 1

        return res
    
