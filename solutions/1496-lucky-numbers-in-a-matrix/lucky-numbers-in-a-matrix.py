# Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
#
# A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.
#
#  
# Example 1:
#
#
# Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
# Output: [15]
# Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column
#
#
# Example 2:
#
#
# Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
# Output: [12]
# Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
#
#
# Example 3:
#
#
# Input: matrix = [[7,8],[1,2]]
# Output: [7]
#
#
#  
# Constraints:
#
#
# 	m == mat.length
# 	n == mat[i].length
# 	1 <= n, m <= 50
# 	1 <= matrix[i][j] <= 10^5.
# 	All elements in the matrix are distinct.
#


class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        def isMax(array, ele):
            for a in array:
                if a > ele:
                    return False
            return True
        res = []
        n = len(matrix)
        for i in range(len(matrix)):
            min_j = 0
            min_v = matrix[i][0]
            #find the minimum of the row:
            for j in range(1, len(matrix[i])):
                if matrix[i][j] < min_v:
                    min_v = matrix[i][j]
                    min_j = j
            col = [matrix[i_][min_j] for i_ in range(n)]
   
            if isMax(col, min_v):
                res.append(min_v)
                
        return res
            
