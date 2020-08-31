# Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.
#
# Example 1:
#
#
# Input:
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# Output: 3
# Explanation: 
# The repeated subarray with maximum length is [3, 2, 1].
#
#
#  
#
# Note:
#
#
# 	1 <= len(A), len(B) <= 1000
# 	0 <= A[i], B[i] < 100
#
#
#  
#


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        m = len(B)
        res = 0
        maxl = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0:
                    if B[j] == A[0]:
                        maxl[0][j] = 1
                    elif j >= 1:
                        maxl[0][j] = 0
                else:
                    if j == 0:
                        if B[0] == A[i]:
                            maxl[i][0] = 1
                        else:
                            maxl[i][0] = 0
                    else:
                        if A[i] == B[j]:
                            maxl[i][j] = maxl[i - 1][j - 1] + 1
                res = max(res, maxl[i][j])
 
        return res
                        
