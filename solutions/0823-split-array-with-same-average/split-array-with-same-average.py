# In a given integer array A, we must move every element of A to either list B or list C. (B and C initially start empty.)
#
# Return true if and only if after such a move, it is possible that the average value of B is equal to the average value of C, and B and C are both non-empty.
#
#
# Example :
# Input: 
# [1,2,3,4,5,6,7,8]
# Output: true
# Explanation: We can split the array into [1,4,5,8] and [2,3,6,7], and both of them have the average of 4.5.
#
#
# Note:
#
#
# 	The length of A will be in the range [1, 30].
# 	A[i] will be in the range of [0, 10000].
#
#
#  
#


class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        n, s = len(A), sum(A)
        @lru_cache(None)
        def find(target, k, i):
            if k == 0: 
                return target == 0
            if target < 0 or k + i > n: 
                return False
            return find(target - A[i], k - 1, i + 1) or find(target, k, i + 1)
        return any(find(k*s//n, k, 0) for k in range(1, n // 2 + 1) if k*s % n == 0)

