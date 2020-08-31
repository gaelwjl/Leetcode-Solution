# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
#
# Example:
#
#
# Input: 
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
#
# Output: 4
#


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        if n == 0:
            return 0
        m = len(matrix[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        max_ = 0
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    dp[0][0] = int(matrix[0][0])
                    
                elif i == 0:
                    dp[0][j] = int(matrix[0][j])
                    
                elif j == 0:
                    dp[i][0] = int(matrix[i][0])
                    
                elif int(matrix[i][j]) == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                
                if dp[i][j] > max_:
                    max_ = dp[i][j]
        return max_ * max_
