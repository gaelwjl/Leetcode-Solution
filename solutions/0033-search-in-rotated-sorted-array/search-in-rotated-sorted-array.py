# Given an integer array nums sorted in ascending order, and an integer target.
#
# Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#
# You should search for target in nums and if you found return its index, otherwise return -1.
#
#  
# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:
# Input: nums = [1], target = 0
# Output: -1
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 5000
# 	-10^4 <= nums[i] <= 10^4
# 	All values of nums are unique.
# 	nums is guranteed to be rotated at some pivot.
# 	-10^4 <= target <= 10^4
#
#


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        
        ls, rs = 0, len(nums) - 1
    
        while (ls < rs):
            mid = (ls + rs) // 2
            if (nums[mid] ==  target):
                return mid
            if (nums[ls] <= nums[mid]):
                if target >= nums[ls] and target < nums[mid]:
                    rs = mid - 1
                else:
                    ls = mid + 1
            else:
                if target > nums[mid] and target <= nums[rs]:
                    ls = mid + 1
                else:
                    rs = mid - 1
        if nums[ls] == target: 
            return ls
        return -1

