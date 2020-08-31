# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
#
# Example:
#
#
# Input:
# [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
# Output: 6
#
#


class Solution:
    def maxhisto(self, t):
        best = (float('-inf'), 0, 0, 0)
        t.append(float('-inf'))
        S = []
        for right in range(len(t)):
            x = t[right]
            left = right
            while len(S) > 0 and S[-1][1] >= x:
                left, height = S.pop()
                rect = (height * (right - left), left, height, right)
                if rect > best:
                    best = rect
            S.append((left, x))
        return best
    
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        if n == 0:
            return 0
        m = len(matrix[0])
        t = [0 for _ in range(m)]
        max_  = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    t[j] += 1
                else:
                    t[j] = 0
            surface = self.maxhisto(t)[0]
            if max_ < surface:
                max_ = surface
        return max_
