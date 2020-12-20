# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
#
#  
# Example 1:
#
#
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
#
#
# Example 2:
#
#
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 8
# 	-10 <= nums[i] <= 10
#
#


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        cn = Counter(nums)
        ans = []
        def backtrack(tmp, i):
            if i == len(nums):
                ans.append(tmp[:])
                return 
            for key in cn:
                if cn[key] > 0:
                    cn[key] -= 1
                    tmp.append(key)
                    backtrack(tmp, i + 1)
                    tmp.pop(-1)
                    cn[key] += 1
        tmp = []
        backtrack(tmp, 0)
        return ans
