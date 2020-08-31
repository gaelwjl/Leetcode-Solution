# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
#
# Example 1:
#
#
# Input: [[1,1],[2,2],[3,3]]
# Output: 3
# Explanation:
# ^
# |
# |        o
# |     o
# |  o  
# +------------->
# 0  1  2  3  4
#
#
# Example 2:
#
#
# Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4
# Explanation:
# ^
# |
# |  o
# |     o        o
# |        o
# |  o        o
# +------------------->
# 0  1  2  3  4  5  6
#
#
# NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
#


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        def coprime(x, y):
            if x == 0:
                return (0, 0)
            if y == 0:
                return (1, 0)
            if x < 0:
                x, y = -x, -y
            t = math.gcd(x, y)
            return (x // t, y // t)
        
        points = list([tuple(p) for p in points])
        n = len(points)
        if n < 3:
            return n
        max_cnt = 1
        for i in range(n):
            dup = 1
            lines = defaultdict(int) # record slop
            for j in range(i + 1, n):
                if points[j] == points[i]:
                    dup += 1
                    continue
                x1, y1 = points[i][0], points[i][1]
                x2, y2 = points[j][0], points[j][1]
                slope = coprime(x2 - x1, y2 - y1)
                lines[slope] += 1
            all_len = lines.values()
    
            if len(all_len):
                max_cnt = max(max(lines.values()) + dup, max_cnt)
            else:
                max_cnt = max(max_cnt, dup)
        return max_cnt
