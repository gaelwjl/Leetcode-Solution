# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
#
#  
#
#
# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
#
#  
#
#
# The largest rectangle is shown in the shaded area, which has area = 10 unit.
#
#  
#
# Example:
#
#
# Input: [2,1,5,6,2,3]
# Output: 10
#
#


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        best = (0, 0, 0, 0)
        t = heights
        t.append(0)
        S = []
        for right in range(len(t)):
            x = t[right]
            left = right
            while len(S) > 0 and S[-1][1] >= x:
                left, height = S.pop()
                rect = (height * (right - left), left, height, right)
                if rect > best:
                    best = rect
            S.append((left, x))
        return best[0]
