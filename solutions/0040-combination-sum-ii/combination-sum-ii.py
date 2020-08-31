# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
#
# Each number in candidates may only be used once in the combination.
#
# Note:
#
#
# 	All numbers (including target) will be positive integers.
# 	The solution set must not contain duplicate combinations.
#
#
# Example 1:
#
#
# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
#
#
# Example 2:
#
#
# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
#   [1,2,2],
#   [5]
# ]
#
#


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = self.solve(sorted(candidates), target)
        return res

    def solve(self, candidates, target):
        if target == 0:
            return [[]]
        if (len(candidates) == 0 and target != 0) or target < candidates[0]:
            return []
        else:
            res = []
            prev = 0
            for ind, c in enumerate(candidates):
                if prev == c:
                    continue
                right = self.solve(candidates[ind + 1:], target - c)
                for r in right:
                    res.append([c] + r)
                prev = c
            return res
