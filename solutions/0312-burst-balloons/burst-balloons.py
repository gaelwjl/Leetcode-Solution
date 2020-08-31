# Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.
#
# Find the maximum coins you can collect by bursting the balloons wisely.
#
# Note:
#
#
# 	You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
# 	0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
#
#
# Example:
#
#
# Input: [3,1,5,8]
# Output: 167 
# Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
#              coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
#


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [1] + nums + [1]
        dp = [[0]*(n + 2) for _ in range(n + 2)]
        for i in range(1, n + 1):
            dp[i][i] = nums[i] * nums[i - 1] * nums[i + 1]
        for l in range(2, n + 1):
            i, j = 1, l
            while j <= n:
                for k in range(i, j + 1):
                    dp[i][j] = max(dp[i][j], dp[i][k - 1] + dp[k + 1][j] + nums[k]*nums[i - 1]*nums[j + 1])
                i += 1
                j += 1
        return dp[1][n]
            
