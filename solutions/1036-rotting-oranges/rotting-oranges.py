# In a given grid, each cell can have one of three values:
#
#
# 	the value 0 representing an empty cell;
# 	the value 1 representing a fresh orange;
# 	the value 2 representing a rotten orange.
#
#
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.
#
# Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.
#
#  
#
#
# Example 1:
#
#
#
#
# Input: [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
#
#
#
# Example 2:
#
#
# Input: [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
#
#
#
# Example 3:
#
#
# Input: [[0,2]]
# Output: 0
# Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
#
#
#  
#
# Note:
#
#
# 	1 <= grid.length <= 10
# 	1 <= grid[0].length <= 10
# 	grid[i][j] is only 0, 1, or 2.
#
#
#
#
#


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        tosee = deque([])
        n = len(grid)
        m = len(grid[0])
        tovis = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    tosee.append((i, j))
                elif grid[i][j] == 1:
                    tovis += 1
        if tovis == 0:
            return 0
        dirs = [1, 0, -1, 0, 1]
        res = 0
        while tosee:
            s = len(tosee)
            res += 1
            while s:
                s -= 1
                x, y = tosee.popleft()
                for i in range(4):
                    nx = x + dirs[i]
                    ny = y + dirs[i + 1]
                    if nx >= 0 and nx < n and ny >= 0 and ny < m:
                        if grid[nx][ny] == 1:
                            tosee.append((nx, ny))
                            grid[nx][ny] = 2
                            tovis -= 1
            if tovis == 0:
                return res
        return -1
            
