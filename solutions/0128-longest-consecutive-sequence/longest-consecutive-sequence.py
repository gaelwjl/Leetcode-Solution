# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
#
# Your algorithm should run in O(n) complexity.
#
# Example:
#
#
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
#
#


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        alln = set(nums)
        maxL = 0
        for n in alln:
            if n - 1 not in alln:
                curl = 1
                i = n + 1
                while i in alln:
                    i += 1
                    curl += 1
                maxL = max(maxL, curl)
        return maxL
