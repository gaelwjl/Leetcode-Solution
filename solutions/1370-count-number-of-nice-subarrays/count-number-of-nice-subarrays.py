# Given an array of integers nums and an integer k. A subarray is called nice if there are k odd numbers on it.
#
# Return the number of nice sub-arrays.
#
#  
# Example 1:
#
#
# Input: nums = [1,1,2,1,1], k = 3
# Output: 2
# Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
#
#
# Example 2:
#
#
# Input: nums = [2,4,6], k = 1
# Output: 0
# Explanation: There is no odd numbers in the array.
#
#
# Example 3:
#
#
# Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
# Output: 16
#
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 50000
# 	1 <= nums[i] <= 10^5
# 	1 <= k <= nums.length
#
#


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        n = len(nums)
        odds = {}
        i_ = 1
        for i in range(n):
            if nums[i] % 2 == 1:
                odds[i_] = odds.get(i_, 0)
                odds[i_] = i
                i_ += 1
        if k not in odds:
            return 0
    
        res = 0
        for i in range(1, i_):
            v = odds[i]
            if i != 1 and i + k - 1 not in odds:
                break
            elif i + k not in odds:
                n_r = n - odds[i + k - 1]
            else:
                n_r = odds[i + k] - odds[i + k - 1]
            
            if i == 1:
                n_l = v + 1
            else:
                n_l = v - odds[i - 1]
            #print((n_l, n_r))
            res += n_l * n_r
            
        return res
            
            
            
            
