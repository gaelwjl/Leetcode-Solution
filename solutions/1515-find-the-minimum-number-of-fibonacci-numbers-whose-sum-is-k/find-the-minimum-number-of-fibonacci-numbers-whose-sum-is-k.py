# Given the number k, return the minimum number of Fibonacci numbers whose sum is equal to k, whether a Fibonacci number could be used multiple times.
#
# The Fibonacci numbers are defined as:
#
#
# 	F1 = 1
# 	F2 = 1
# 	Fn = Fn-1 + Fn-2 , for n > 2.
#
# It is guaranteed that for the given constraints we can always find such fibonacci numbers that sum k.
#  
# Example 1:
#
#
# Input: k = 7
# Output: 2 
# Explanation: The Fibonacci numbers are: 1, 1, 2, 3, 5, 8, 13, ... 
# For k = 7 we can use 2 + 5 = 7.
#
# Example 2:
#
#
# Input: k = 10
# Output: 2 
# Explanation: For k = 10 we can use 2 + 8 = 10.
#
#
# Example 3:
#
#
# Input: k = 19
# Output: 3 
# Explanation: For k = 19 we can use 1 + 5 + 13 = 19.
#
#
#  
# Constraints:
#
#
# 	1 <= k <= 10^9
#


class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fibons = [1, 1]
        for _ in range(100):
            fibons.append(fibons[-1] + fibons[-2])
        set_fibons = set(fibons)
        memo = {}
        def dfs(fibons, j):
            if j in memo:
                return memo[k]
            if j in set_fibons:
                memo[j] = 1
                return 1
            else:
                memo[j] = k
                for i in range(len(fibons) - 1, -1, -1):
                    if j - fibons[i] >= 1:
                        dfs(fibons, j - fibons[i])
                        memo[j] = min(memo[j], memo[j - fibons[i]] + 1)
                        break
                return memo[j]
        dfs(fibons, k)
        return memo[k]
