# Given an array of 4 digits, return the largest 24 hour time that can be made.
#
# The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.
#
# Return the answer as a string of length 5.  If no valid time can be made, return an empty string.
#
#  
#
#
# Example 1:
#
#
# Input: [1,2,3,4]
# Output: "23:41"
#
#
#
# Example 2:
#
#
# Input: [5,5,5,5]
# Output: ""
#
#
#  
#
# Note:
#
#
# 	A.length == 4
# 	0 <= A[i] <= 9
#
#
#


from array import array
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        perms = itertools.permutations(A)
        argbest = []
        best = -1
        for p in perms:
            h = p[0]*10+p[1]
            if h > 23:
                continue
            m = p[2]*10+p[3]
            if m > 59:
                continue
            cur = h * 100 + m
            if cur > best:
                best = cur
                argbest = p
        if best < 0:
            return ''
        return str(argbest[0]) + str(argbest[1]) + ':' + str(argbest[2]) + str(argbest[3])
        
            
            
                
