#
# Given an unsorted array of integers, find the number of longest increasing subsequence.
#
#
# Example 1:
#
# Input: [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
#
#
#
# Example 2:
#
# Input: [2,2,2,2,2]
# Output: 5
# Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.
#
#
#
# Note:
# Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int.
#


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        maxl = [1 for _ in range(n)]
        cnt = [1 for _ in range(n)]
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if maxl[j] >= maxl[i]:
                        maxl[i] = 1 + maxl[j]
                        cnt[i] = cnt[j]
                    elif maxl[j] + 1 == maxl[i]:
                        cnt[i] += cnt[j]
        ans = 0
        maxl_ = max(maxl)
        for i in range(n):
            if maxl[i] == maxl_:
                ans += cnt[i]
                
        return ans
