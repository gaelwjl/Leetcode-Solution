// There is a strange printer with the following two special requirements:
//
//
// 	On each turn, the printer will print a solid rectangular pattern of a single color on the grid. This will cover up the existing colors in the rectangle.
// 	Once the printer has used a color for the above operation, the same color cannot be used again.
//
//
// You are given a m x n matrix targetGrid, where targetGrid[row][col] is the color in the position (row, col) of the grid.
//
// Return true if it is possible to print the matrix targetGrid, otherwise, return false.
//
//  
// Example 1:
//
//
//
//
// Input: targetGrid = [[1,1,1,1],[1,2,2,1],[1,2,2,1],[1,1,1,1]]
// Output: true
//
//
// Example 2:
//
//
//
//
// Input: targetGrid = [[1,1,1,1],[1,1,3,3],[1,1,3,4],[5,5,1,4]]
// Output: true
//
//
// Example 3:
//
//
// Input: targetGrid = [[1,2,1],[2,1,2],[1,2,1]]
// Output: false
// Explanation: It is impossible to form targetGrid because it is not allowed to print the same color in different turns.
//
// Example 4:
//
//
// Input: targetGrid = [[1,1,1],[3,1,3]]
// Output: false
//
//
//  
// Constraints:
//
//
// 	m == targetGrid.length
// 	n == targetGrid[i].length
// 	1 <= m, n <= 60
// 	1 <= targetGrid[row][col] <= 60
//
//


class Solution {
public:

    bool isPrintable(vector<vector<int>>& targetGrid) {
        int n = targetGrid.size(), m = targetGrid[0].size(); 
        vector<array<int, 4>> pos(61, array<int, 4>{61, -1, 61, -1}); 
        for (int x = 0; x < n; x++){
            for (int y = 0; y < m; y++){
                pos[targetGrid[x][y]][0] = min(pos[targetGrid[x][y]][0], x); 
                pos[targetGrid[x][y]][1] = max(pos[targetGrid[x][y]][1], x); 
                pos[targetGrid[x][y]][2] = min(pos[targetGrid[x][y]][2], y); 
                pos[targetGrid[x][y]][3] = max(pos[targetGrid[x][y]][3], y);
            }
        }
        vector<vector<int>> graph(61); 
        for (int c = 1; c < 61; c++){
            if (pos[c][0] == 61) 
                continue; 
            vector<int> add(61, 0); 
            for (int x = pos[c][0]; x <= pos[c][1]; x++){
                for (int y = pos[c][2]; y <= pos[c][3]; y++){
                    if (c != targetGrid[x][y] && !add[targetGrid[x][y]]){
                        graph[c].push_back(targetGrid[x][y]);
                        add[targetGrid[x][y]] = 1; 
                    }
                }
            }
        }
        
        bool flag = true; 
        vector<int> vis(61, 0), act(61, 0);
        function<void(int)> dfs = [&](int cur){
            if (vis[cur]) 
                return; 
            vis[cur] = 1; 
            act[cur] = 1;
            for (auto v: graph[cur]){
                if (act[v]) 
                    flag = false; 
                dfs(v);
            }
            act[cur] = 0;
        };
        for (int i = 1; i < 61; i++)
            if (graph[i].size()){
                dfs(i);
            }
        return flag;
    }
};

