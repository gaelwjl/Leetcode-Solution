# Given an array A of 0s and 1s, we may change up to K values from 0 to 1.
#
# Return the length of the longest (contiguous) subarray that contains only 1s. 
#
#  
#
#
# Example 1:
#
#
# Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
# Output: 6
# Explanation: 
# [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
#
#
# Example 2:
#
#
# Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
# Output: 10
# Explanation: 
# [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
#
#
#  
#
# Note:
#
#
# 	1 <= A.length <= 20000
# 	0 <= K <= A.length
# 	A[i] is 0 or 1 
#
#
#


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        ans = 0
        i, j = 0, 0
        cnt = A[0] == 0
        while i < len(A) and j < len(A):
            if cnt <= K:
                ans = max(ans, i - j + 1)
                i += 1
                if i < len(A) and A[i] == 0:
                    cnt += 1
            else:
                if A[j] == 0:
                    cnt -= 1
                j += 1
        return ans
