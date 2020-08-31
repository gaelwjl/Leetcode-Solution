# Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.
#
# Each person may dislike some other people, and they should not go into the same group. 
#
# Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.
#
# Return true if and only if it is possible to split everyone into two groups in this way.
#
#  
#
#
#
#
#
#
#
#
#
# Example 1:
#
#
# Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
# Output: true
# Explanation: group1 [1,4], group2 [2,3]
#
#
#
# Example 2:
#
#
# Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
# Output: false
#
#
#
# Example 3:
#
#
# Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
# Output: false
#
#
#
#
#
#  
# Constraints:
#
#
# 	1 <= N <= 2000
# 	0 <= dislikes.length <= 10000
# 	dislikes[i].length == 2
# 	1 <= dislikes[i][j] <= N
# 	dislikes[i][0] < dislikes[i][1]
# 	There does not exist i != j for which dislikes[i] == dislikes[j].
#


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        N += 1
        color = [0 for _ in range(N)]
        r = [[] for _ in range(N)]
        for l, r_ in dislikes:
            r[l].append(r_)
            r[r_].append(l)

        def dfs(node, col):
            color[node] = col
            for v in r[node]:
                if color[v] == col:
                    return False
                if color[v] == 0 and not dfs(v, -col):
                    return False
            return True

        for i in range(1, N):
            if color[i] == 0 and not dfs(i, 1):
                return False
        return True

