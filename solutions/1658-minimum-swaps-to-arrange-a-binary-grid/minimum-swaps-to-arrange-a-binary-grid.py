# Given an n x n binary grid, in one step you can choose two adjacent rows of the grid and swap them.
#
# A grid is said to be valid if all the cells above the main diagonal are zeros.
#
# Return the minimum number of steps needed to make the grid valid, or -1 if the grid cannot be valid.
#
# The main diagonal of a grid is the diagonal that starts at cell (1, 1) and ends at cell (n, n).
#
#  
# Example 1:
#
#
# Input: grid = [[0,0,1],[1,1,0],[1,0,0]]
# Output: 3
#
#
# Example 2:
#
#
# Input: grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
# Output: -1
# Explanation: All rows are similar, swaps have no effect on the grid.
#
#
# Example 3:
#
#
# Input: grid = [[1,0,0],[1,1,0],[1,1,1]]
# Output: 0
#
#
#  
# Constraints:
#
#
# 	n == grid.length
# 	n == grid[i].length
# 	1 <= n <= 200
# 	grid[i][j] is 0 or 1
#
#


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        arr = []
        n = len(grid)
        for i in range(n):
            cnt = 0
            for j in range(n):
                if grid[i][j] == 0:
                    cnt += 1
                else:
                    cnt = 0
            arr.append(cnt)
        ans = 0
        for i in range(n):
            target = n - 1 - i
            mark = False
            if arr[i] >= target:
                mark = True
            else:
                for j in range(i + 1, n):
                    if arr[j] >= target:
                        arr[i:j + 1] = arr[j:j+1] + arr[i:j]
                        ans += j - i
                        mark = True
                        break
            if not mark:
                return -1
        return ans
