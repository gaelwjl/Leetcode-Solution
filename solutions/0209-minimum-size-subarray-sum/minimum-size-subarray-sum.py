# Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.
#
# Example: 
#
#
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.
#
# Follow up:
#
# If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
#


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        j = 0
        sum_ = 0
        res = n + 2
        while True:
            while sum_ >= s:
                # print((i, j))
                # print(sum_)
                res = min(j - i, res)
                sum_ -= nums[i]
                i += 1
            if j == n:
                break
            sum_ += nums[j]
            j += 1
        if res > n:
            res = 0
        return res
