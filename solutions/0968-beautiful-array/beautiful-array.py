# -*- coding:utf-8 -*-


# For some fixed N, an array A is beautiful if it is a permutation of the integers 1, 2, ..., N, such that:
#
# For every i < j, there is no k with i < k < j such that A[k] * 2 = A[i] + A[j].
#
# Given N, return any beautiful array A.  (It is guaranteed that one exists.)
#
#  
#
# Example 1:
#
#
# Input: 4
# Output: [2,1,4,3]
#
#
#
# Example 2:
#
#
# Input: 5
# Output: [3,1,2,5,4]
#
#  
#
#
# Note:
#
#
# 	1 <= N <= 1000
#
#
#
#  
#


class Solution(object):
    def beautifulArray(self, N):
        lst = [1]
        # l must contain all the numbers between 1 and N
        while len(lst) <= N:
            lst = [2*x - 1 for x in lst] + [2*x for x in lst]
        res = [x for x in lst if x <= N]
        return res
        
