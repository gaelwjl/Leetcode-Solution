// Given a weighted undirected connected graph with n vertices numbered from 0 to n-1, and an array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between nodes fromi and toi. A minimum spanning tree (MST) is a subset of the edges of the graph that connects all vertices without cycles and with the minimum possible total edge weight.
//
// Find all the critical and pseudo-critical edges in the minimum spanning tree (MST) of the given graph. An MST edge whose deletion from the graph would cause the MST weight to increase is called a critical edge. A pseudo-critical edge, on the other hand, is that which can appear in some MSTs but not all.
//
// Note that you can return the indices of the edges in any order.
//
//  
// Example 1:
//
//
//
//
// Input: n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
// Output: [[0,1],[2,3,4,5]]
// Explanation: The figure above describes the graph.
// The following figure shows all the possible MSTs:
//
// Notice that the two edges 0 and 1 appear in all MSTs, therefore they are critical edges, so we return them in the first list of the output.
// The edges 2, 3, 4, and 5 are only part of some MSTs, therefore they are considered pseudo-critical edges. We add them to the second list of the output.
//
//
// Example 2:
//
//
//
//
// Input: n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
// Output: [[],[0,1,2,3]]
// Explanation: We can observe that since all 4 edges have equal weight, choosing any 3 edges from the given 4 will yield an MST. Therefore all 4 edges are pseudo-critical.
//
//
//  
// Constraints:
//
//
// 	2 <= n <= 100
// 	1 <= edges.length <= min(200, n * (n - 1) / 2)
// 	edges[i].length == 3
// 	0 <= fromi < toi < n
// 	1 <= weighti <= 1000
// 	All pairs (fromi, toi) are distinct.
//
//


const int N = 100 + 10;
int f[N];
int find(int x){
    if (f[x] != f[f[x]]) f[x] = find(f[x]);
    return f[x];
}
class Solution {
public:
    vector<vector<int>> findCriticalAndPseudoCriticalEdges(int n, vector<vector<int>>& edges) {
        int m = edges.size();
        for (int i = 0; i < n; i++){
            f[i] = i;
        }
        for (int k = 0; k < m; k++){
            edges[k].push_back(k);
        }
        sort(edges.begin(), edges.end(), 
            [](const vector<int> x, const vector<int> y){
                return x[2] < y[2];
            });
        int best = 0;
        for (int k = 0; k < m; k++){
            int x = edges[k][0], y = edges[k][1];
            int rx = find(x), ry = find(y);
            if (rx != ry)
                best += edges[k][2];
            f[rx] = ry;
        }
        vector<int> retA, retB; 
        vector<bool> mark(m);
        for (int i = 0; i < m; i++){
            for (int i = 0; i < n; i++){
                f[i] = i;
            }
            int best_val = 0;
            for (int k = 0; k < m; k++){
                if (i == k) continue;
                int x = edges[k][0], y = edges[k][1];
                int rx = find(x), ry = find(y);
                if (rx != ry)
                    best_val += edges[k][2];
                f[rx] = ry;
            }
            if (best_val != best){
                retA.push_back(edges[i][3]);
                mark[i] = true;
            }
        }
        
        for (int i = 0; i < m; i++){
            if (mark[i]) continue;
            for (int i = 0; i < n; i++){
                f[i] = i;
            }
            int best_val = edges[i][2];
            int rxi = find(edges[i][0]), ryi = find(edges[i][1]);
            f[rxi] = ryi;
            for (int k = 0; k < m; k++){
                if (k == i) continue;
                int x = edges[k][0], y = edges[k][1];
                int rx = find(x), ry = find(y);
                if (rx != ry)
                    best_val += edges[k][2];
                f[rx] = ry;
            }
            if (best_val == best)
                retB.push_back(edges[i][3]);
        }
        
        return {retA, retB};
    }
};
