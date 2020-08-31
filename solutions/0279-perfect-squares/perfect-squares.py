# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
#
# Example 1:
#
#
# Input: n = 12
# Output: 3 
# Explanation: 12 = 4 + 4 + 4.
#
# Example 2:
#
#
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.


class Solution:
    @lru_cache(None)
    def numSquares(self, n: int) -> int:
        tmp = int(math.sqrt(n))
        if (tmp * tmp == n):
            return 1
        ans = n
        for i in range(tmp, 0, -1):
            if n - i*i >= 0:
                ans = min(ans, 1 + self.numSquares(n - i * i))            
        return ans
