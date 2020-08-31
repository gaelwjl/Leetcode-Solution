# Given a set of distinct integers, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
#
# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
#


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        toreturn = [[]]
        for i in range(len(nums)):
            a_ = []
            for j in range(len(toreturn)):
                a = toreturn[j]
                a_ = a[:]
                a_.append(nums[i])
                toreturn.append(a_)
        return toreturn
