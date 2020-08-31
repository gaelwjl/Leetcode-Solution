# In a 1 million by 1 million grid, the coordinates of each grid square are (x, y) with 0 <= x, y < 10^6.
#
# We start at the source square and want to reach the target square.  Each move, we can walk to a 4-directionally adjacent square in the grid that isn't in the given list of blocked squares.
#
# Return true if and only if it is possible to reach the target square through a sequence of moves.
#
#  
#
# Example 1:
#
#
# Input: blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]
# Output: false
# Explanation: 
# The target square is inaccessible starting from the source square, because we can't walk outside the grid.
#
#
# Example 2:
#
#
# Input: blocked = [], source = [0,0], target = [999999,999999]
# Output: true
# Explanation: 
# Because there are no blocked cells, it's possible to reach the target square.
#
#
#  
#
# Note:
#
#
# 	0 <= blocked.length <= 200
# 	blocked[i].length == 2
# 	0 <= blocked[i][j] < 10^6
# 	source.length == target.length == 2
# 	0 <= source[i][j], target[i][j] < 10^6
# 	source != target
#
#


class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        blocked = set([tuple(b) for b in blocked])
        dirs = [1, 0, -1, 0, 1]
        source = tuple(source)
        target = tuple(target)
        def bfs(source, target):
            seen = set([])
            tosee = [tuple(source)]
            while tosee:
                cur = tosee.pop(-1)
                if cur in seen:
                    continue
                seen.add(cur)
                if cur == target:
                    return True
                y, x = cur
                for i in range(4):
                    n_y, n_x = y + dirs[i], x + dirs[i + 1]
                    if n_y < 0 or n_x < 0 or n_y >= 1e6 or n_x >= 1e6:
                        continue
                    if (n_y, n_x) in seen or (n_y, n_x) in blocked:
                        continue
                    tosee.append((n_y, n_x))
                if len(tosee) >= 20000:
                    return True
            return False
        return bfs(source, target) and bfs(target, source)
