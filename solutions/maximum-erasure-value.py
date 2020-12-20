# You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.
#
# Return the maximum score you can get by erasing exactly one subarray.
#
# An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).
#
#  
# Example 1:
#
#
# Input: nums = [4,2,4,5,6]
# Output: 17
# Explanation: The optimal subarray here is [2,4,5,6].
#
#
# Example 2:
#
#
# Input: nums = [5,2,1,2,5,2,1,2,5]
# Output: 8
# Explanation: The optimal subarray here is [5,2,1] or [1,2,5].
#
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 105
# 	1 <= nums[i] <= 104
#
#


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        ans = 0
        i, j = 0, 0
        
        prefix = [0]
        for v in nums:
            prefix.append(prefix[-1] + v)
        
        while i < len(nums):
            while i < len(nums):
                if cnt[nums[i]] >= 1:
                    break
                cnt[nums[i]] += 1
                i += 1
            if (i == len(nums)):
                ans = max(ans, prefix[-1] - prefix[j])
                break
            ans = max(ans, prefix[i] - prefix[j])
            while j < len(nums):
                cnt[nums[j]] -= 1
                j += 1
                if cnt[nums[i]] < 1:
                    break
        return ans 
            
