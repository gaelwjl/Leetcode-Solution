# You have d dice, and each die has f faces numbered 1, 2, ..., f.
#
# Return the number of possible ways (out of fd total ways) modulo 10^9 + 7 to roll the dice so the sum of the face up numbers equals target.
#
#  
# Example 1:
#
#
# Input: d = 1, f = 6, target = 3
# Output: 1
# Explanation: 
# You throw one die with 6 faces.  There is only one way to get a sum of 3.
#
#
# Example 2:
#
#
# Input: d = 2, f = 6, target = 7
# Output: 6
# Explanation: 
# You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
# 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
#
#
# Example 3:
#
#
# Input: d = 2, f = 5, target = 10
# Output: 1
# Explanation: 
# You throw two dice, each with 5 faces.  There is only one way to get a sum of 10: 5+5.
#
#
# Example 4:
#
#
# Input: d = 1, f = 2, target = 3
# Output: 0
# Explanation: 
# You throw one die with 2 faces.  There is no way to get a sum of 3.
#
#
# Example 5:
#
#
# Input: d = 30, f = 30, target = 500
# Output: 222616187
# Explanation: 
# The answer must be returned modulo 10^9 + 7.
#
#
#  
# Constraints:
#
#
# 	1 <= d, f <= 30
# 	1 <= target <= 1000
#


class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        const = int(1e9 + 7)
        t = target
        dp = [[0 for _ in range(t + 1)] for _ in range(d + 1)]
        for i in range(1, t + 1):
            if 1 <= i and i <= f:
                dp[1][i] = 1
        for i in range(2, d + 1):
            #compute dp[i][j]
            for j in range(1, t + 1):
                dp[i][j] = (dp[i][j - 1] + dp[i - 1][j - 1])%const
                if j - f - 1 >= 1:
                    dp[i][j] = (dp[i][j] - dp[i - 1][j - f - 1])%const     
        return dp[d][t]
