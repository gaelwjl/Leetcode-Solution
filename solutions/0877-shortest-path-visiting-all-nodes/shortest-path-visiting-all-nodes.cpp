// An undirected, connected graph of N nodes (labeled 0, 1, 2, ..., N-1) is given as graph.
//
// graph.length = N, and j != i is in the list graph[i] exactly once, if and only if nodes i and j are connected.
//
// Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.
//
//  
//
//
//
//
// Example 1:
//
//
// Input: [[1,2,3],[0],[0],[0]]
// Output: 4
// Explanation: One possible path is [1,0,2,0,3]
//
// Example 2:
//
//
// Input: [[1],[0,2,4],[1,3,4],[2],[1,2]]
// Output: 4
// Explanation: One possible path is [0,1,4,2,3]
//
//
//  
//
// Note:
//
//
// 	1 <= graph.length <= 12
// 	0 <= graph[i].length < graph.length
//
//


using pii = pair<int, int>;
class Solution {
public:
    int shortestPathLength(vector<vector<int>>& graph) {
        int n = graph.size();
        deque<pii> q;
        for (int i = 0; i < n; i ++){
            q.push_back({i, 1 << i});
        }
        vector<vector<int>> visited(n, vector<int>(1 << n, 0));
        int steps = 0;
        while (!q.empty()){
            int s = q.size();
            while (s--){
                pii cur = q.front();
                q.pop_front();
                int node = cur.first, visited_state = cur.second;
                if (visited[node][visited_state]) 
                    continue;
                if (visited_state == (1 << n) - 1)
                    return steps;
                visited[node][visited_state] = 1;
                for (int j: graph[node]){
                    if ( ! visited[j][visited_state | 1 << j] ) q.push_back({j, visited_state | 1 << j});
                }
            }
            steps ++;
        }
        return -1;
    }
};
