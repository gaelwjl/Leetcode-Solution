# -*- coding:utf-8 -*-


# Given an array A of non-negative integers, the array is squareful if for every pair of adjacent elements, their sum is a perfect square.
#
# Return the number of permutations of A that are squareful.  Two permutations A1 and A2 differ if and only if there is some index i such that A1[i] != A2[i].
#
#  
#
# Example 1:
#
#
# Input: [1,17,8]
# Output: 2
# Explanation: 
# [1,8,17] and [17,8,1] are the valid permutations.
#
#
# Example 2:
#
#
# Input: [2,2,2]
# Output: 1
#
#
#  
#
# Note:
#
#
# 	1 <= A.length <= 12
# 	0 <= A[i] <= 1e9
#


from itertools import permutations
import math
class Solution(object):
    def numSquarefulPerms(self, A):
        c = collections.Counter(A)
        graphe = {x:[] for x in c}        
        def isSquareful(num):
            return (math.sqrt(num) == math.floor(math.sqrt(num)))
        def Edge(x, y):
            return (isSquareful(x+y))
        for x in graphe:
            for y in graphe:
                if Edge(x, y):
                    graphe[x].append(y)

        res = 0
        visited = len(A) - 1
        #find num of hamiltonian path in graphe by DFS
        #deep first searching
        #c is a Counter to store the time to visite this node
        def dfs(node, tovisit):
            c[node] -= 1
            if tovisit == 0:
                ans = 1
            else:
                ans = 0
                for y in graphe[node]:
                    if c[y] > 0:
                        ans = ans + dfs(y, tovisit - 1)
            c[node] +=1
            return ans
        
 
        res = sum(dfs(x, len(A) - 1) for x in c)
        
        return res






