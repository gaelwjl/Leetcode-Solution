# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
#
# You may return the answer in any order.
#
#  
# Example 1:
#
#
# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
#
#
# Example 2:
#
#
# Input: n = 1, k = 1
# Output: [[1]]
#
#
#  
# Constraints:
#
#
# 	1 <= n <= 20
# 	1 <= k <= n
#
#


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = []    
        self.combinefrom_i(n, 1, k, [])
        return self.res
        
    def combinefrom_i(self, n, i, k, temp):
        if k == 0:
            # print(temp)
            self.res.append(temp[:])
            return
        for iter_ in range(i, n + 1):
            temp.append(iter_ )
            self.combinefrom_i(n, iter_ + 1, k - 1, temp)
            temp.pop(-1)

