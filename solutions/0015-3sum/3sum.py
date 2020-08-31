# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
#
# Example:
#
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#
#


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 3 pointeur solutions
        if len(nums) <=2:
            return []
        res = []
        nums = sorted(nums)
        N = len(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            # two sum questions to find the target value -nums[i]
            # nums[j] + nums[k] = target
            j = i + 1
            k = N - 1
            while j < k:
                if nums[j] + nums[k] < target:
                    j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j_prev = j
                    while j < k and nums[j] == nums[j_prev]:
                        j += 1

        return res
