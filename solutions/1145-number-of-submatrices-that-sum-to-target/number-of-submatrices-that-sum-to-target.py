# Given a matrix, and a target, return the number of non-empty submatrices that sum to target.
#
# A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.
#
# Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.
#
#  
#
# Example 1:
#
#
# Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
# Output: 4
# Explanation: The four 1x1 submatrices that only contain 0.
#
#
#
# Example 2:
#
#
# Input: matrix = [[1,-1],[-1,1]], target = 0
# Output: 5
# Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.
#
#
#
#  
#
# Note:
#
#
# 	1 <= matrix.length <= 300
# 	1 <= matrix[0].length <= 300
# 	-1000 <= matrix[i] <= 1000
# 	-10^8 <= target <= 10^8
#
#
#  
# Constraints:
#
#
# 	1 <= matrix.length <= 100
# 	1 <= matrix[0].length <= 100
# 	-1000 <= matrix[i] <= 1000
# 	-10^8 <= target <= 10^8
#
#


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        #reduce the problem to the number of target sum in an array:
        n = len(matrix)
        m = len(matrix[0])
        partielSum = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                partielSum[i + 1][j + 1] += partielSum[i][j + 1] + matrix[i][j]
        res = 0
        for j in range(n):
            for i in range(j, n):
                #record the partiel values we have seen
                #values inclusive between j and i where j <= i
                seen = {0:1}
                tempSum = 0
                for k in range(m):
                    tempSum += partielSum[i + 1][k + 1] - partielSum[j][k + 1]
                    if tempSum - target in seen:
                        res += seen[tempSum - target]
                    if tempSum not in seen:
                        seen[tempSum] = 1
                    else:
                        seen[tempSum] += 1
        
        return res
        
