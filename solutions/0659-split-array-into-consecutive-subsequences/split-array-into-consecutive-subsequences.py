# Given an array nums sorted in ascending order, return true if and only if you can split it into 1 or more subsequences such that each subsequence consists of consecutive integers and has length at least 3.
#
#  
#
# Example 1:
#
#
# Input: [1,2,3,3,4,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences : 
# 1, 2, 3
# 3, 4, 5
#
#
#
# Example 2:
#
#
# Input: [1,2,3,3,4,4,5,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences : 
# 1, 2, 3, 4, 5
# 3, 4, 5
#
#
#
# Example 3:
#
#
# Input: [1,2,3,4,4,5]
# Output: False
#
#
#  
#
# Constraints:
#
#
# 	1 <= nums.length <= 10000
#
#
#  
#


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        toput = Counter(nums)
        setted = defaultdict(int)
        for n in nums:
            if toput[n] == 0:
                continue
            toput[n] -= 1
            if setted[n - 1]:
                setted[n] += 1
                setted[n - 1] -= 1
            elif toput[n + 1] and toput[n + 2]:
                toput[n + 1] -= 1
                toput[n + 2] -= 1
                setted[n + 2] += 1
            else:
                return False
        return True
