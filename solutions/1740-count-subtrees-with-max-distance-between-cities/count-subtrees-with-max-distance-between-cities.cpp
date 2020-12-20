// There are n cities numbered from 1 to n. You are given an array edges of size n-1, where edges[i] = [ui, vi] represents a bidirectional edge between cities ui and vi. There exists a unique path between each pair of cities. In other words, the cities form a tree.
//
// A subtree is a subset of cities where every city is reachable from every other city in the subset, where the path between each pair passes through only the cities from the subset. Two subtrees are different if there is a city in one subtree that is not present in the other.
//
// For each d from 1 to n-1, find the number of subtrees in which the maximum distance between any two cities in the subtree is equal to d.
//
// Return an array of size n-1 where the dth element (1-indexed) is the number of subtrees in which the maximum distance between any two cities is equal to d.
//
// Notice that the distance between the two cities is the number of edges in the path between them.
//
//  
// Example 1:
//
//
//
//
// Input: n = 4, edges = [[1,2],[2,3],[2,4]]
// Output: [3,4,0]
// Explanation:
// The subtrees with subsets {1,2}, {2,3} and {2,4} have a max distance of 1.
// The subtrees with subsets {1,2,3}, {1,2,4}, {2,3,4} and {1,2,3,4} have a max distance of 2.
// No subtree has two nodes where the max distance between them is 3.
//
//
// Example 2:
//
//
// Input: n = 2, edges = [[1,2]]
// Output: [1]
//
//
// Example 3:
//
//
// Input: n = 3, edges = [[1,2],[2,3]]
// Output: [2,1]
//
//
//  
// Constraints:
//
//
// 	2 <= n <= 15
// 	edges.length == n-1
// 	edges[i].length == 2
// 	1 <= ui, vi <= n
// 	All pairs (ui, vi) are distinct.
//


class Solution {
public:
    vector<int> countSubgraphsForEachDiameter(int n, vector<vector<int>>& edges) {
        vector<vector<int>> graph(n); 
        for (auto& v: edges) {
            --v[0], --v[1]; 
            graph[v[0]].push_back(v[1]);
            graph[v[1]].push_back(v[0]); 
        }
        int dist = 0; 
        function<int(int, int, int, int&)> dfs = [&](int cur, int prev, int bitmask, int& cnt){
            vector<int> childs;
            for (int neib: graph[cur]){
                if (neib != prev && ((bitmask >> neib) & 1)){
                    cnt ++;
                    childs.push_back(dfs(neib, cur, bitmask, cnt));
                }
            }
            sort(childs.begin(), childs.end());
            if (childs.size() >= 2){
                dist = max(dist, childs.back() + childs[childs.size() - 2] + 2); 
                return childs.back() + 1;
            }else if (childs.size() == 1){
                dist = max(dist, childs.back() + 1); 
                return childs[0] + 1;
            }else{
                return 0;
            }
        }; 
        vector<int> ret(n - 1); 
        for (auto s = (1 << n) - 1; s; s--){
            int cnt_s = __builtin_popcount(s); 
            if (cnt_s <= 1)
                continue ;
            int i = 0; 
            for (; i < n; i++){
                if ((s >> i) & 1){
                    break; 
                }
            }
            int cnt = 1; dist = 0; 
            dfs(i, -1, s, cnt);
            if (cnt != cnt_s)
                continue;
            // cout << dist << endl;
            ret[dist - 1]++;
        }
        return ret;
    }
};
