# Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
#
# Example:
#
#
# Input: 3
# Output:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]
#
#


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        dy = [1,  0,  -1, 0]
        dx = [0,  1,  0, -1]
        matrix = [[0 for _ in range(n)] for _ in range(n)]

        seen = [[False for _ in range(n)] for _ in range(n)]
        i = 1
        res = []
        i0 = 0
        x = 0
        y = 0
        while i <= n ** 2:
            #print(x, y, i)
            if seen[x][y] == False:
                matrix[x][y] = i
                seen[x][y] = True
                i += 1
            #compute next x and y
            tempx = x + dx[i0]
            tempy = y + dy[i0]
            if tempx < 0 or tempy < 0 or tempx == n or tempy == n or seen[tempx][tempy] == True:
                i0 = ((1 + i0) % 4)
            x += dx[i0]
            y += dy[i0]
        return matrix
