# Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.
#
# Example 1:
#
#
#
# Input: 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 × 1 = 1.
#
#
# Example 2:
#
#
# Input: 10
# Output: 36
# Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
#
# Note: You may assume that n is not less than 2 and not larger than 58.
#
#


from functools import lru_cache
class Solution:
    def integerBreak(self, n: int) -> int:
        @lru_cache(None)
        def dp(n):
            if n <= 1:
                return 1
            toreturn = n
            for i in range(1, n // 2 + 1):
                toreturn = max(i*dp(n - i), toreturn)
            return toreturn
        return max(i*dp(n-i) for i in range(1, n // 2 + 1))
