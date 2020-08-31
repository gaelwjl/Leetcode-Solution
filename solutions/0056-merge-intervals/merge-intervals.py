# Given a collection of intervals, merge all overlapping intervals.
#
# Example 1:
#
#
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
#
#
# Example 2:
#
#
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
#
# NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
#
#  
# Constraints:
#
#
# 	intervals[i][0] <= intervals[i][1]
#
#


class Solution:
    def merge(self, intervals):
        intervals.sort(key = lambda x: x[0])
        res = []
        i = 0
        while i < len(intervals):
            left = intervals[i][0]
            right = intervals[i][1]
            j = i + 1
            while j < len(intervals):
                if intervals[j][0] > right:
                    break
                left = min(left, intervals[j][0])
                right = max(right, intervals[j][1])
                j += 1
            res.append([left, right])
            i = j
        return res
        
