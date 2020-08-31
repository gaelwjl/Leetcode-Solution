# Given a collection of distinct integers, return all possible permutations.
#
# Example:
#
#
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
#
#


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]
        res = []
        begin = nums[0]
        for l in self.permute(nums[1:]):
            for i in range(len(l)):
                res.append(l[0:i] + [begin] + l[i:])
            res.append(l + [begin])
        return res
