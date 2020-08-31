# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
#
#
#
# Given an integer n, return the number of distinct solutions to the n-queens puzzle.
#
# Example:
#
#
# Input: 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
# [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
#
#


class Solution:
    
    def totalNQueens(self, n: int) -> int:
        self.res = 0
        board = [['.' for _ in range(n)] for _ in range(n)]
        self.solve(board, 0)
        return self.res
    
    def solve(self, board, cur_col):
        n = len(board)
        if cur_col == n:
            self.res += 1
            return True
        for row in range(n):
            if self.isvalid(board, row, cur_col):
                board[row][cur_col] = 'Q'
                self.solve(board, cur_col + 1)
                board[row][cur_col] = '.'
        return False

    def isvalid(self, board, r, c):
        # we have already ensured only one Queen in each column
        # only need to check rows
        n = len(board)
        for j in range(n):
            if board[r][j] == 'Q':
                return False
        i, j = r, c
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
            
        i, j = r, c
        while i < n and j >= 0:
            if board[i][j] == 'Q':
                return False
            i += 1
            j -= 1
        return True

