# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
# A sudoku solution must satisfy all of the following rules:
#
#
# 	Each of the digits 1-9 must occur exactly once in each row.
# 	Each of the digits 1-9 must occur exactly once in each column.
# 	Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
#
#
# The '.' character indicates empty cells.
#
#  
# Example 1:
#
#
# Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
# Explanation: The input board is shown above and the only valid solution is shown below:
#
#
#
#
#  
# Constraints:
#
#
# 	board.length == 9
# 	board[i].length == 9
# 	board[i][j] is a digit or '.'.
# 	It is guaranteed that the input board has only one solution.
#
#


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def rang(i):
            return i // 9
        def col(i):
            return i % 9
        def block(i):
            return (rang(i) // 3) * 3 + col(i) // 3
        def solve(i, board):
            if i >= 81: 
                return True
            r, c = rang(i), col(i)
            if board[r][c] != '.':
                for j in inconf[i]:
                    if board[rang(j)][col(j)] == board[r][c]:
                        return False
                return solve(i + 1, board)
            else:
                totry = [True for _ in range(10)]
                for j in inconf[i]:
                    tmp = board[rang(j)][col(j)]
                    if tmp != '.':
                        tmp = int(tmp)
                        totry[tmp] = False
                for n in range(1, 10):
                    if (totry[n]): 
                        board[r][c] = str(n)
                        if solve(i + 1, board):
                            return True
                        board[r][c] = "."
                return False
        # do some preprocessing to get all positions in conflict with indices from 0 to 80
        # backtracking: 
        #   if already contains a number: check if it is compatible with all other cells
        #   else get a number which isn't in conflit with existing numbers
        #   solve the backtracking function
        inconf = [[] for _ in range(81)]
        for i in range(81):
            for j in range(i + 1, 81):
                if rang(j) == rang(i) or col(j) == col(i) or block(i) == block(j):
                    inconf[i].append(j)
                    inconf[j].append(i)
        
        solve(0, board)
        
                            
