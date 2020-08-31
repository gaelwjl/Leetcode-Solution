# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
#
#  
# Example 1:
#
#
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#
#
#  
# Constraints:
#
#
# 	3 <= nums.length <= 10^3
# 	-10^3 <= nums[i] <= 10^3
# 	-10^4 <= target <= 10^4
#
#


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        nums = sorted(nums)
        res = 1e5
        for i in range(n - 2):
            if i>=1 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                tmp = nums[j] + nums[k] + nums[i]
                if abs(tmp - target) < abs(res - target):
                    res = tmp
                if tmp - target > 0:
                    k -= 1
                elif tmp - target < 0:
                    j += 1
                else:
                    return res
        return res
