# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
# Example:
#
#
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
#
#
#  
# Constraints:
#
#
# 	board and word consists only of lowercase and uppercase English letters.
# 	1 <= board.length <= 200
# 	1 <= board[i].length <= 200
# 	1 <= word.length <= 10^3
#
#


class Solution:    
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        seen = [[0]*m for _ in range(n)]
        dirs = [1, 0, -1, 0, 1]
        
        def dfs(board, r, c, word, offset):
            if offset == len(word) or (offset == len(word) - 1 and board[r][c] == word[offset]):
                return True
            if (board[r][c] != word[offset]):
                return False
            for i in range(4):
                nr = r + dirs[i]
                nc = c + dirs[i + 1]
                if (nr < 0 or nc < 0 or nr >= n or nc >= m or seen[nr][nc]):
                    continue
                seen[nr][nc] = 1
                if dfs(board, nr, nc, word, offset + 1):
                    return True
                seen[nr][nc] = 0
            return False
        for i in range(n):
            for j in range(m):
                seen[i][j] = 1
                if dfs(board, i, j, word, 0):
                    return True
                seen[i][j] = 0 
        return False
            
