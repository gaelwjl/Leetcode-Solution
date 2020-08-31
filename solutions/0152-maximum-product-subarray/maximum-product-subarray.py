# Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.
#
# Example 1:
#
#
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
#
#
# Example 2:
#
#
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
#


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_p = [0] * n
        max_n = [0] * n
        max_p[0] = nums[0]
        max_n[0] = nums[0]
        res = nums[0]
        for i in range(1, n):
            max_n[i] = min(nums[i] * max_n[i - 1], nums[i], max_p[i - 1] * nums[i])
            max_p[i] = max(nums[i] * max_p[i-1], nums[i], max_n[i - 1] * nums[i])
            if max_p[i] > res:
                res = max_p[i]
        # print(max_p)
        # print(max_n)
        return res
