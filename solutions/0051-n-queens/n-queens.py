# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
#
#
#
# Given an integer n, return all distinct solutions to the n-queens puzzle.
#
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
#
# Example:
#
#
# Input: 4
# Output: [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
#
#


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        self.solve(board, 0, res)
        return res
    
    def solve(self, board, cur_col, res):
        n = len(board)
        if cur_col == n:
            res.append(["".join(row_b) for row_b in board])
            return True
        for row in range(n):
            if self.isvalid(board, row, cur_col):
                board[row][cur_col] = 'Q'
                self.solve(board, cur_col + 1, res)
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

