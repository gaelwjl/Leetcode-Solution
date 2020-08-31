# -*- coding:utf-8 -*-


# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
#
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
#
# The replacement must be in-place and use only constant extra memory.
#
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
#
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
#


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        max0 = -1
        for i in range(0, len(nums) - 1):
            if nums[i] < nums[i + 1]:
                max0 = i
        if max0 == -1:
            nums.reverse()
        else:
            temp = nums[max0]
            #find minimum
            mini = nums[max0 + 1]
            index_min = max0 + 1
            for i in range(max0 + 1, len(nums)):
                if mini > nums[i] and nums[i] > temp:
                    mini = nums[i]
                    index_min = i
            nums[max0] = mini
            nums[index_min] = temp
            nums[max0 + 1:] = sorted(nums[max0 + 1:])
