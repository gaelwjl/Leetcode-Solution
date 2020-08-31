// Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
//
// Note: You can only move either down or right at any point in time.
//
// Example:
//
//
// Input:
// [
//   [1,3,1],
//   [1,5,1],
//   [4,2,1]
// ]
// Output: 7
// Explanation: Because the path 1→3→1→1→1 minimizes the sum.
//
//


class Solution {
public:
    vector<vector<int>> grid;
    vector<vector<int>> dist;
    
    int n, m;
    
    void dfs(int i, int j){
        
        if (dist[i][j] != INT_MAX)
            return ;
        
        if (i + 1 < m){
            dfs(i + 1, j);
            dist[i][j] = min(dist[i][j], dist[i+1][j] + grid[i][j]);
        }
            
        if (j + 1 < n){
            dfs(i, j + 1);
            dist[i][j] = min(dist[i][j], dist[i][j + 1] + grid[i][j]);
        }
        
        if (i == m - 1 && j == n - 1){
            dist[i][j] = grid[i][j];
        }
    }
    
    int minPathSum(vector<vector<int>>& grid_) {
        grid = grid_;
        m = grid.size();
        if (m == 0) return 0;
        n = grid[0].size();
        for (int i = 0; i< m; i++){
            vector<int> temp(n, INT_MAX);
            dist.push_back(temp);
        }
        dfs(0, 0);
        // for (int i = 0; i< m; i++){
        //     for (int j = 0; j< n; j++)
        //         cout << dist[i][j] << " ";
        //     cout << endl;
        // }
        return dist[0][0];
    }
};
