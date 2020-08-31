# Given an unsorted array of integers, find the length of longest increasing subsequence.
#
# Example:
#
#
# Input: [10,9,2,5,3,7,101,18]
# Output: 4 
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
#
# Note: 
#
#
# 	There may be more than one LIS combination, it is only necessary for you to return the length.
# 	Your algorithm should run in O(n2) complexity.
#
#
# Follow up: Could you improve it to O(n log n) time complexity?
#


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        #to record the number M[j]
        #since we don't need to revert to subsequence
        M = [float('inf') for _ in range(n + 1)]
        len_ = 0
        for x in nums:
            i = bisect.bisect_left(M, x)
            if i < 0:
                i = 0
            M[i] = x
            if (i == len_):
                len_ += 1
        return len_
