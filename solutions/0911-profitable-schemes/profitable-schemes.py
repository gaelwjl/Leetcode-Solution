# There is a group of G members, and a list of various crimes they could commit.
#
# The ith crime generates a profit[i] and requires group[i] members to participate in it.
#
# If a member participates in one crime, that member can't participate in another crime.
#
# Let's call a profitable scheme any subset of these crimes that generates at least P profit, and the total number of members participating in that subset of crimes is at most G.
#
# How many schemes can be chosen?  Since the answer may be very large, return it modulo 10^9 + 7.
#
#  
#
# Example 1:
#
#
# Input: G = 5, P = 3, group = [2,2], profit = [2,3]
# Output: 2
# Explanation: 
# To make a profit of at least 3, the group could either commit crimes 0 and 1, or just crime 1.
# In total, there are 2 schemes.
#
#
#
# Example 2:
#
#
# Input: G = 10, P = 5, group = [2,3,5], profit = [6,7,8]
# Output: 7
# Explanation: 
# To make a profit of at least 5, the group could commit any crimes, as long as they commit one.
# There are 7 possible schemes: (0), (1), (2), (0,1), (0,2), (1,2), and (0,1,2).
#
#
#  
#
#
# Note:
#
#
# 	1 <= G <= 100
# 	0 <= P <= 100
# 	1 <= group[i] <= 100
# 	0 <= profit[i] <= 100
# 	1 <= group.length = profit.length <= 100
#
#
#
#  
#
#


class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        mod = 10**9 + 7
        n = len(group)
        dp = [[0]*(P + 1) for _ in range(G + 1)]
        dp[0][0] = 1
        for i in range(n):
            dp2 = [row[:] for row in dp]
            for p in range(P + 1):
                p_n = min(P, p + profit[i])
                for g in range(G + 1 - group[i]):
                    g_n = g + group[i]
                    dp2[g_n][p_n] += dp[g][p]
                    dp2[g_n][p_n] %= mod
            dp = dp2
        return sum([x[P] for x in dp]) % mod
