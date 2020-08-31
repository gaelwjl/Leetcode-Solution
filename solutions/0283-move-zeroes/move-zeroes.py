# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Example:
#
#
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
#
# Note:
#
#
# 	You must do this in-place without making a copy of the array.
# 	Minimize the total number of operations.
#


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.insert(0, 0)

        for i in range(1, len(nums)) :
            nums[i] = nums[i - 1] + nums[i]
            
        i, j = 0, 1
        while j < len(nums):
            if nums[j] != nums[j - 1]:
                nums[i] = nums[j] - nums[j - 1]
                i += 1
            j += 1
        for j in range(i, len(nums)):
            nums[j] = 0
        nums.pop(-1)
        
            
                
        
