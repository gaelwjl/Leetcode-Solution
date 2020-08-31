# Given a m * n matrix mat of integers, sort it diagonally in ascending order from the top-left to the bottom-right then return the sorted array.
#
#  
# Example 1:
#
#
# Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
# Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
#
#
#  
# Constraints:
#
#
# 	m == mat.length
# 	n == mat[i].length
# 	1 <= m, n <= 100
# 	1 <= mat[i][j] <= 100
#


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        diags = []
        for i in range(0, n):
            temp = []
            for j in range(0, min(n - i, m)):
                temp.append(mat[i + j][j])
            temp = sorted(temp)
            diags.append(temp)
        for j in range(1, m):
            temp = []
            for i in range(0, min(m - j, n)):
                temp.append(mat[i][i + j])
            temp = sorted(temp)
            diags.append(temp)
        count = 0
        for i in range(0, n):
            temp = 0
            for j in range(0, min(n - i, m)):
                mat[i + j][j] = diags[count][temp]
                temp += 1
            count += 1
        for j in range(1, m):
            temp = 0
            for i in range(0, min(m - j, n)):
                mat[i][i + j] = diags[count][temp]
                temp += 1
            count += 1
        return mat
