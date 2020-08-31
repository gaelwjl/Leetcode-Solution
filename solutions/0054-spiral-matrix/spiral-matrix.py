# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
#
# Example 1:
#
#
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
#
#
# Example 2:
#
# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
#


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dy = [1,  0,  -1, 0]
        dx = [0,  1,  0, -1]
        if matrix == [[]] or matrix == []:
            return []
        n = len(matrix)
        m = len(matrix[0])
        seen = [[False for _ in range(m)] for _ in range(n)]
        i = 0
        res = []
        i0 = 0
        x = 0
        y = 0
        while i < n * m:
            #print(x, y, i)
            if seen[x][y] == False:
                res.append(matrix[x][y])
                seen[x][y] = True
                i += 1
            #compute next x and y
            tempx = x + dx[i0]
            tempy = y + dy[i0]
            if tempx < 0 or tempy < 0 or tempx == n or tempy == m or seen[tempx][tempy] == True:
                i0 = ((1 + i0) % 4)
            x += dx[i0]
            y  += dy[i0]
        return res
