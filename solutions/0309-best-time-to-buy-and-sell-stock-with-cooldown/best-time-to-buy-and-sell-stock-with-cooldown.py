# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:
#
#
# 	You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
# 	After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
#
#
# Example:
#
#
# Input: [1,2,3,0,2]
# Output: 3 
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
#


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        B = [0 for _ in range(n)]
        S = [0 for _ in range(n)]
        for i in range(n):
            if i == 0:
                B[0] = -prices[0]
                continue
            if i == 1:
                B[1] = max(B[0], -prices[1])
            if i >= 2:
                B[i] = max(B[i - 1], S[i - 2] - prices[i])
            S[i] = max(prices[i] + B[i - 1], S[i - 1])
        print(B)
        print(S)
        return max(B[n - 1], S[n - 1])
