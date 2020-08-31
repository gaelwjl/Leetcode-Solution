# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1. 
#
#
# Example 1:
#
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
#
#
#
# Example 2:
#
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
#
#
#
# Note:
# The length of the given binary array will not exceed 50,000.
#


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cumsum = [0]
        for n in nums:
            if n == 0:
                n = -1
            cumsum.append(cumsum[-1] + n)
        max_len = 0
        record = {}
        for i, c in enumerate(cumsum):
            if c in record:
                max_len = max(max_len, i - record[c])
            else:
                record[c] = i
        return max_len
        
