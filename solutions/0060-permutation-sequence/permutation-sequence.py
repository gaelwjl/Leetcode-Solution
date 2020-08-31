# -*- coding:utf-8 -*-


# The set [1,2,3,...,n] contains a total of n! unique permutations.
#
# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
#
#
# 	"123"
# 	"132"
# 	"213"
# 	"231"
# 	"312"
# 	"321"
#
#
# Given n and k, return the kth permutation sequence.
#
# Note:
#
#
# 	Given n will be between 1 and 9 inclusive.
# 	Given k will be between 1 and n! inclusive.
#
#
# Example 1:
#
#
# Input: n = 3, k = 3
# Output: "213"
#
#
# Example 2:
#
#
# Input: n = 4, k = 9
# Output: "2314"
#
#


import math
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        A = list(range(1, n + 1))
        res = []
        okay = True
        while okay:
            n = len(A)
            temp = math.factorial(n - 1)
            for i in range(1, n + 1):
                if (k - i * temp) < 0:
                    k = k - (i - 1)*temp
                    res += [A[i - 1]]
                    A.remove(A[i - 1])
                    break
                elif k == i * temp:
                    res += [A[i - 1]]
                    A.remove(A[i - 1])
                    res += A[::-1]
                    okay = False
                    break
            
        res = [str(i) for i in res]
        toreturn =  ''.join(res)
        return toreturn
