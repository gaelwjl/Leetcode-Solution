# Given a m * n grid, where each cell is either 0 (empty) or 1 (obstacle). In one step, you can move up, down, left or right from and to an empty cell.
#
# Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m-1, n-1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.
#
#  
# Example 1:
#
#
# Input: 
# grid = 
# [[0,0,0],
#  [1,1,0],
#  [0,0,0],
#  [0,1,1],
#  [0,0,0]], 
# k = 1
# Output: 6
# Explanation: 
# The shortest path without eliminating any obstacle is 10. 
# The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
#
#
#  
#
# Example 2:
#
#
# Input: 
# grid = 
# [[0,1,1],
#  [1,1,1],
#  [1,0,0]], 
# k = 1
# Output: -1
# Explanation: 
# We need to eliminate at least two obstacles to find such a walk.
#
#
#  
# Constraints:
#
#
# 	grid.length == m
# 	grid[0].length == n
# 	1 <= m, n <= 40
# 	1 <= k <= m*n
# 	grid[i][j] == 0 or 1
# 	grid[0][0] == grid[m-1][n-1] == 0
#
#


class Solution:
    def shortestPath(self, grid, k):
        n = len(grid)
        m = len(grid[0])
        seen = [[-1] * m for _ in range(n)]
        dir = [0, 1, 0, -1, 0]
        from collections import deque
        q = deque()
        q.append((0, 0, k))
        steps = 0

        seen[0][0] = k - grid[0][0]

        while len(q) > 0:
            size = len(q)
            # print(steps)
            while size > 0:
                size -= 1
                cur = q.popleft()
                # print(cur)
                if (cur[0], cur[1]) == (n - 1, m - 1):
                    return steps
                for i in range(len(dir) - 1):
                    x = cur[0] + dir[i]
                    y = cur[1] + dir[i + 1]
                    if x < 0 or y < 0 or x >= n or y >= m:
                        continue
                    obs = cur[2] - grid[x][y]
                    if obs <= seen[x][y] or obs < 0:
                        continue
                    seen[x][y] = obs
                    q.append((x, y, obs))
            steps += 1
        return -1
