# -*- coding:utf-8 -*-


# In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end, return True if and only if there exists a sequence of moves to transform one string to the other.
#
# Example:
#
#
# Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
# Output: True
# Explanation:
# We can transform start to end following these steps:
# RXXLRXRXL ->
# XRXLRXRXL ->
# XRLXRXRXL ->
# XRLXXRRXL ->
# XRLXXRRLX
#
#
#  
# Constraints:
#
#
# 	1 <= len(start) == len(end) <= 10000.
# 	Both start and end will only consist of characters in {'L', 'R', 'X'}.
#
#


class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        val = {'R': 1, 'X': 0, 'L': -1}
        count = 0
        for i in range(len(start)):
            temp = val[start[i]] - val[end[i]]
            count += temp
            print(count)
            if count < 0 or abs(temp) == 2: 
                return False
        return count == 0
