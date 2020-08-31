# On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves. The rows and columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).
#
# A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.
#
#  
#
#
#
#  
#
# Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.
#
# The knight continues moving until it has made exactly K moves or has moved off the chessboard. Return the probability that the knight remains on the board after it has stopped moving.
#
#  
#
# Example:
#
#
# Input: 3, 2, 0, 0
# Output: 0.0625
# Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
# From each of those positions, there are also two moves that will keep the knight on the board.
# The total probability the knight stays on the board is 0.0625.
#
#
#  
#
# Note:
#
#
# 	N will be between 1 and 25.
# 	K will be between 0 and 100.
# 	The knight always initially starts on the board.
#
#


class Solution:
    @lru_cache(None)
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        if r >= N or r < 0 or c >= N or c < 0:
            return 0
        if K == 0:
            return 1
        dirs = [(2,1),(2,-1),(-2,1),(-2,-1), (1,2),(1,-2),(-1,2),(-1,-2)]
        ans = 0
        for tr, tc in dirs:
            ans += self.knightProbability(N, K - 1, r + tr, c + tc) / 8
        return ans
