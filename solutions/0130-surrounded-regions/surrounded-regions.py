# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
#
# Example:
#
#
# X X X X
# X O O X
# X X O X
# X O X X
#
#
# After running your function, the board should be:
#
#
# X X X X
# X X X X
# X X X X
# X O X X
#
#
# Explanation:
#
# Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
#


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dirs = [1, 0, -1, 0, 1]
        
        def dfs(i, j):
            if i < 0 or i > n - 1 or j < 0 or j > m - 1:
                return
            if vis[i][j]:
                return 
            if board[i][j] == 'X':
                return
            mark[i][j] = True
            vis[i][j] = True
            for it in range(4):
                dfs(i + dirs[it], j + dirs[it + 1])
            
        n = len(board)
        if n <= 2:
            return 
        m = len(board[0])
        if m <= 2:
            return 
        mark = [[0] * m  for _ in range(n)]
        vis = [[False] * m  for _ in range(n)]
        for i in range(n):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][m - 1] == 'O':
                dfs(i, m - 1)
                
        for j in range(m):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[n - 1][j] == 'O':
                dfs(n - 1, j)
        for i in range(n):
            for j in range(m):
                if not mark[i][j]:
                    board[i][j] = 'X'
        
