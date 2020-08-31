# Given an integer array nums and an integer k, return the maximum sum of a non-empty subsequence of that array such that for every two consecutive integers in the subsequence, nums[i] and nums[j], where i < j, the condition j - i <= k is satisfied.
#
# A subsequence of an array is obtained by deleting some number of elements (can be zero) from the array, leaving the remaining elements in their original order.
#
#  
# Example 1:
#
#
# Input: nums = [10,2,-10,5,20], k = 2
# Output: 37
# Explanation: The subsequence is [10, 2, 5, 20].
#
#
# Example 2:
#
#
# Input: nums = [-1,-2,-3], k = 1
# Output: -1
# Explanation: The subsequence must be non-empty, so we choose the largest number.
#
#
# Example 3:
#
#
# Input: nums = [10,-2,-10,-5,20], k = 2
# Output: 23
# Explanation: The subsequence is [10, -2, -5, 20].
#
#
#  
# Constraints:
#
#
# 	1 <= k <= nums.length <= 10^5
# 	-10^4 <= nums[i] <= 10^4
#
#


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        dq = deque()
        dq.append(nums[0])
        for i in range(1, len(nums)):
            dp[i] = nums[i] + max(dq[0], 0)
            dq.append(dp[i])
            
            while len(dq) > k or dq[-1] > dq[0]:
                dq.popleft()

        return max(dp)
            
