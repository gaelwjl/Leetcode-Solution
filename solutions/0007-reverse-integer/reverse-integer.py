# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
#
# Input: 123
# Output: 321
#
#
# Example 2:
#
#
# Input: -123
# Output: -321
#
#
# Example 3:
#
#
# Input: 120
# Output: 21
#
#
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
#


class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        if x == 0:
            return 0
        if s[0] != '-':
            res = ""
            ind = len(s) - 1
            while s[ind] == '0':
                ind -= 1
            while ind >= 0:
                res += s[ind]
                ind -= 1
            return int(res) if int(res) <= 2**31 - 1 else 0
        else:
            res = ""
            for i in range(len(s) - 1, 0,  -1):
                res += s[i]
            return - int(res) if - int(res) >= -2**31 else 0
