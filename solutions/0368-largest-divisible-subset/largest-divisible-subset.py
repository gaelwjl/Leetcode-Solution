# Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:
#
# Si % Sj = 0 or Sj % Si = 0.
#
# If there are multiple solutions, return any subset is fine.
#
# Example 1:
#
#
#
# Input: [1,2,3]
# Output: [1,2] (of course, [1,3] will also be ok)
#
#
#
# Example 2:
#
#
# Input: [1,2,4,8]
# Output: [1,2,4,8]
#
#
#


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        nums = sorted(nums)
        dp = [1 for _ in range(n)]
        prev = [i for i in range(n)]
        max_l = -float('inf')
        max_ind = 0
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        prev[i] = j
                        dp[i] = dp[j] + 1
            if dp[i] > max_l:
                max_ind = i
                max_l = dp[i]
        res = []
        while max_ind != prev[max_ind]:
            res.append(nums[max_ind])
            max_ind = prev[max_ind]
        res.append(nums[max_ind])
        return res[::-1]
                    
