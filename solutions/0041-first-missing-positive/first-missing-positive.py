# Given an unsorted integer array nums, find the smallest missing positive integer.
#
#  
# Example 1:
# Input: nums = [1,2,0]
# Output: 3
# Example 2:
# Input: nums = [3,4,-1,1]
# Output: 2
# Example 3:
# Input: nums = [7,8,9,11,12]
# Output: 1
#
#  
# Constraints:
#
#
# 	0 <= nums.length <= 300
# 	-231 <= nums[i] <= 231 - 1
#
#
#  
# Follow up: Could you implement an algorithm that runs in O(n) time and uses constant extra space?
#


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [0] + nums
        for i in range(1, n + 1):
            if nums[i] > n or nums[i] <= 0:
                nums[i] = 0
                continue
            if (i != nums[i]):
                ind = nums[i]
                while 1 <= ind <= n and nums[ind] != ind:
                    nxt_ind = nums[ind]
                    nums[ind] = ind
                    ind = nxt_ind

        for i in range(1, n + 1):
            if nums[i] != i:
                return i
        return n + 1

# [0,3,1,2]
# [3,4,-1,3]
# [7,8,9,11,12]
