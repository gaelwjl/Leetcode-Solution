# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
# A sudoku solution must satisfy all of the following rules:
#
#
# 	Each of the digits 1-9 must occur exactly once in each row.
# 	Each of the digits 1-9 must occur exactly once in each column.
# 	Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
#
#
# Empty cells are indicated by the character '.'.
#
#
# A sudoku puzzle...
#
#
# ...and its solution numbers marked in red.
#
# Note:
#
#
# 	The given board contain only digits 1-9 and the character '.'.
# 	You may assume that the given Sudoku puzzle will have a single unique solution.
# 	The given board size is always 9x9.
#
#


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def rang (indice):
            return indice//9
        
        def col(indice):
            return indice%9
        
        def block(indice):
            return (rang(indice) // 3)*3 + col(indice)//3
        m = [0 for _ in range(81)]
        inconflit = [[0 for _ in range(20)] for _ in range(81)]
        for i in range(81):
            count = 0;
            for j in range(81):
                if (j != i and (rang(j) == rang(i) or col(j) == col(i) or block(j) == block(i)) ):
                    inconflit[i][count] = j
                    count += 1
            if board[rang(i)][col(i)] != '.':
                m[i] = int(board[rang(i)][col(i)])
            else:
                m[i] = 0
        def solve(i, m):
            if i >= 81: return True;
            if (m[i] > 0):
                for j in range(20):
                    if (m[i] == m[inconflit[i][j]]):
                        return False;
                return solve(i + 1, m);
            used = [False for _ in range(10)];

            for j in range(20):
                used[m[inconflit[i][j]]] = True;
            for val in range(1, 10):
                if (used[val] != True):
                    m[i] = val;
                    if (solve(i + 1, m)):
                        return True;
                    m[i] = 0;
        
            return False;
        solve(0, m)
        # print(m)
        for i in range(81):
            board[rang(i)][col(i)] = str(m[i])
