# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
#
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
#
# Example:
#
#
# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
#
#


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        else:
            res = [[1]]
            for i in range(1, numRows):
                last = res[-1].copy()
                last.append(1)
                for j in range(1, len(last) - 1):
                    last[j] = res[-1][j - 1] + res[-1][j]
                res.append(last)
            return res
            
