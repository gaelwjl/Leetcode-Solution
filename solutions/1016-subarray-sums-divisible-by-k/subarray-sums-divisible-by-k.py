# Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.
#
#  
#
#
# Example 1:
#
#
# Input: A = [4,5,0,-2,-3,1], K = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by K = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
#
#
#  
#
# Note:
#
#
# 	1 <= A.length <= 30000
# 	-10000 <= A[i] <= 10000
# 	2 <= K <= 10000
#
#


class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        P_sum = [0 for _ in range(len(A) + 1)]
        P_sum[0] = 0
        for i in range(0, len(A)):
            P_sum[i + 1] = (A[i] + P_sum[i]) % K
        res = 0
        from collections import Counter
        c = Counter(P_sum)
        for k, v in c.items():
            res += v * (v - 1) // 2
        return res
