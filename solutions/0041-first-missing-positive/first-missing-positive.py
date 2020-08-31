# Given an unsorted integer array, find the smallest missing positive integer.
#
# Example 1:
#
#
# Input: [1,2,0]
# Output: 3
#
#
# Example 2:
#
#
# Input: [3,4,-1,1]
# Output: 2
#
#
# Example 3:
#
#
# Input: [7,8,9,11,12]
# Output: 1
#
#
# Follow up:
#
# Your algorithm should run in O(n) time and uses constant extra space.
#


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] < 0 or nums[i] > n:
                nums[i] = 0
        nums = [0] + nums
        for i in range(1, n + 1):
            j = nums[i]
            while i != j:
                tmp = nums[j]
                nums[j] = j
                i = j
                j = tmp
        for i in range(1, n + 1):
            if nums[i] != i:
                return i
        return n + 1
