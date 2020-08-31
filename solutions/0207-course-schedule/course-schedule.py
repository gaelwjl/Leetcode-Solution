# There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.
#
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
#
#  
# Example 1:
#
#
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0. So it is possible.
#
#
# Example 2:
#
#
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0, and to take course 0 you should
#              also have finished course 1. So it is impossible.
#
#
#  
# Constraints:
#
#
# 	The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
# 	You may assume that there are no duplicate edges in the input prerequisites.
# 	1 <= numCourses <= 10^5
#
#


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = prerequisites
        n = numCourses
        r = [[] for _ in range(n)]
        for e in edges:
            r[e[0]].append(e[1])
        act = [0 for _ in range(n)]
        vis = [0 for _ in range(n)]
        self.bad = False
        def dfs(i):
            act[i] = 1
            vis[i] = 1
            for j in r[i]:
                if act[j]:
                    self.bad = True  
                if not vis[j]: 
                    dfs(j)
            act[i] = 0
        for i in range(n):
            if not vis[i]: 
                dfs(i)
        return not self.bad
