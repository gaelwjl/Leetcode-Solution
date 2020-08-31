# Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.
#
#
# Example:
#
#
# Input: 2
# Output: 91 
# Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, 
#              excluding 11,22,33,44,55,66,77,88,99
#
#
#  
# Constraints:
#
#
# 	0 <= n <= 8
#
#


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        def cnt(n):
            if n == 1:
                return 10
            # if n >= 10:
            #     return cnt(9)
            if n >= 11:
                return cnt(10)
            ans = 81
            tmp = 8
            i = 0
            while i < n - 2:
                ans *= tmp
                i += 1
                tmp -= 1
            ans += cnt( n - 1)
            return ans
        return cnt(n)
