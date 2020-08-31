# There are N network nodes, labelled 1 to N.
#
# Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.
#
# Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.
#
#  
#
# Example 1:
#
#
#
#
# Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
# Output: 2
#
#
#  
#
# Note:
#
#
# 	N will be in the range [1, 100].
# 	K will be in the range [1, N].
# 	The length of times will be in the range [1, 6000].
# 	All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.
#
#


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, K: int) -> int:
        r = [[] for _ in range(n + 1)]
        w = [[] for _ in range(n + 1)]
        for e in times:
            r[e[0]].append(e[1])
            w[e[0]].append(e[2])
        # return the maximum distance from K
        h = []
        heappush(h, (0, K))
        max_d = 0
        dist = [-1 for _ in range(n + 1)]
        dist[K] = 0
        while len(h):
            d, node = heappop(h)
            d = -d
            for j in range(len(r[node])):
                next_node = r[node][j]
                weight = w[node][j]
                tmp = d + weight
                if dist[next_node] < 0 or dist[next_node] > tmp:
                    dist[next_node] = tmp
                    heappush(h, (-tmp, next_node))

        for i in range(1, n + 1):
            max_d = max(dist[i], max_d)
            if dist[i] < 0:
                return -1
        return max_d
