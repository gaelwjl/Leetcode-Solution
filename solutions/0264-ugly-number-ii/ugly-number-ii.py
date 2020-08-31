# Write a program to find the n-th ugly number.
#
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
#
# Example:
#
#
# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
#
# Note:  
#
#
# 	1 is typically treated as an ugly number.
# 	n does not exceed 1690.
#


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return n
        us = [[1] for _ in range(3)]
        ps = [2, 3, 5]
        def generate():
            min_ = float('inf')
            ind_ = 0
            for i, p in enumerate(ps):
                if min_ > p * us[i][0]:
                    min_ = p * us[i][0]
                    ind_ = i
            for i, p in enumerate(ps):
                if p*us[i][0] == min_:
                    us[i].pop(0)
            for i in range(3):
                us[i].append(min_)
            return min_
        n -= 1
        while n:
            res = generate()
            n -= 1
        return res

