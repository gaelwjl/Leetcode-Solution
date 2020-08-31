# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
#
# Example 1:
#
#
# Input:nums = [1,1,1], k = 2
# Output: 2
#
#
#  
# Constraints:
#
#
# 	The length of the array is in range [1, 20,000].
# 	The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
#
#


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        Ps = [0]
        record = {}
        for i in range(len(nums)):
            Ps.append(Ps[-1] + nums[i])

        res = 0
        for i in range(len(Ps)):
            if Ps[i] - k in record:
                res += record[Ps[i] - k]
            record[Ps[i]] = (record.get(Ps[i], 0) + 1)

        return res
