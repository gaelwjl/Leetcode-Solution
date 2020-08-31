# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
#
# Example:
#
#
# Input: 38
# Output: 2 
# Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
#              Since 2 has only one digit, return it.
#
#
# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?


class Solution:
    def addDigits(self, x: int) -> int:
        def digit_sum(x: int, b: int) -> int:
            total = 0
            while x > 0:
                total = total + (x % b)
                x = x // b
            return total
        seen = set()
        while x not in seen:
            seen.add(x)
            x = digit_sum(x, 10)
        return x
