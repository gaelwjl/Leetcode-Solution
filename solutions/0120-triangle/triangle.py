# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
#
# For example, given the following triangle
#
#
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
#
#
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
#
# Note:
#
# Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
#


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        mini_d = [triangle[0][0]]
        previous = [triangle[0][0]]
        
        for i in range(1, n):
            m = len(triangle[i])
            mini_d[0] = previous[0] + triangle[i][0]
            for j in range(1, m - 1):
                mini_d[j] = min(previous[j], previous[j - 1]) + triangle[i][j]
            mini_d.append(triangle[i][m - 1] + previous[m -2])
            previous = mini_d.copy()
     
        return min(mini_d)
