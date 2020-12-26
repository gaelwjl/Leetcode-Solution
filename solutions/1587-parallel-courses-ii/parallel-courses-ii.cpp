// Given the integer n representing the number of courses at some university labeled from 1 to n, and the array dependencies where dependencies[i] = [xi, yi]  represents a prerequisite relationship, that is, the course xi must be taken before the course yi.  Also, you are given the integer k.
//
// In one semester you can take at most k courses as long as you have taken all the prerequisites for the courses you are taking.
//
// Return the minimum number of semesters to take all courses. It is guaranteed that you can take all courses in some way.
//
//  
// Example 1:
//
//
//
//
// Input: n = 4, dependencies = [[2,1],[3,1],[1,4]], k = 2
// Output: 3 
// Explanation: The figure above represents the given graph. In this case we can take courses 2 and 3 in the first semester, then take course 1 in the second semester and finally take course 4 in the third semester.
//
//
// Example 2:
//
//
//
//
// Input: n = 5, dependencies = [[2,1],[3,1],[4,1],[1,5]], k = 2
// Output: 4 
// Explanation: The figure above represents the given graph. In this case one optimal way to take all courses is: take courses 2 and 3 in the first semester and take course 4 in the second semester, then take course 1 in the third semester and finally take course 5 in the fourth semester.
//
//
// Example 3:
//
//
// Input: n = 11, dependencies = [], k = 2
// Output: 6
//
//
//  
// Constraints:
//
//
// 	1 <= n <= 15
// 	1 <= k <= n
// 	0 <= dependencies.length <= n * (n-1) / 2
// 	dependencies[i].length == 2
// 	1 <= xi, yi <= n
// 	xi != yi
// 	All prerequisite relationships are distinct, that is, dependencies[i] != dependencies[j].
// 	The given graph is a directed acyclic graph.
//
//


class Solution {
public:
    int minNumberOfSemesters(int n, vector<vector<int>>& edges, int k) {
        vector<vector<int>> depend(n);
        for (auto& v: edges) {
            --v[0], --v[1];
            depend[v[1]].push_back(v[0]); 
        }
        
        deque<int> tosee{0};
        vector<int> vis(1 << n, 0); 
        int dist = 0; 
        
        while (tosee.size()){
            int sz = tosee.size(); 
            while(sz--){
                int cur_s = tosee.front();
                tosee.pop_front(); 
                if (vis[cur_s])
                    continue;
                vis[cur_s] = 1; 
                if (cur_s == ((1<< n) - 1))
                    return dist;
                // get all possible courses; 
                int can = 0; 
                for (int i = 0; i < n; i++){
                    if ((cur_s >> i)&1) 
                        continue; 
                    bool ok = true; 
                    for (auto dep: depend[i])
                        if (!((cur_s >> dep)&1))
                            ok = false; 
                    if (ok){
                        can = (can | (1 << i)); 
                    }   
                }
                
                // iterate all subsets of init_can;
                for (int s = can; s; s=can&(s - 1)){
                    if (__builtin_popcount(s) <= k){
                        tosee.push_back((cur_s|s));
                    }
                }
            }
            dist++; 
        }
        return dist;  
        
    }
};
