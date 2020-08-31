# -*- coding:utf-8 -*-


# In an array A of 0s and 1s, how many non-empty subarrays have sum S?
#
#  
#
# Example 1:
#
#
# Input: A = [1,0,1,0,1], S = 2
# Output: 4
# Explanation: 
# The 4 subarrays are bolded below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
#
#
#  
#
# Note:
#
#
# 	A.length <= 30000
# 	0 <= S <= A.length
# 	A[i] is either 0 or 1.
#


class Solution(object):
    def numSubarraysWithSum(self, A, S):
        res = total = 0
        dic = {0: 1}
        for x in A:
            total += x
            res += dic.get(total - S, 0)
            dic[total] = dic.get(total, 0) + 1
        
        return res
        
