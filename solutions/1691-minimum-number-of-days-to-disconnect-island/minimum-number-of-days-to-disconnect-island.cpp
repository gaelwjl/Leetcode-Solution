// Given a 2D grid consisting of 1s (land) and 0s (water).  An island is a maximal 4-directionally (horizontal or vertical) connected group of 1s.
//
// The grid is said to be connected if we have exactly one island, otherwise is said disconnected.
//
// In one day, we are allowed to change any single land cell (1) into a water cell (0).
//
// Return the minimum number of days to disconnect the grid.
//
//  
// Example 1:
//
//
//
//
// Input: grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
// Output: 2
// Explanation: We need at least 2 days to get a disconnected grid.
// Change land grid[1][1] and grid[0][2] to water and get 2 disconnected island.
//
//
// Example 2:
//
//
// Input: grid = [[1,1]]
// Output: 2
// Explanation: Grid of full water is also disconnected ([[1,1]] -> [[0,0]]), 0 islands.
//
//
// Example 3:
//
//
// Input: grid = [[1,0,1,0]]
// Output: 0
//
//
// Example 4:
//
//
// Input: grid = [[1,1,0,1,1],
//                [1,1,1,1,1],
//                [1,1,0,1,1],
//                [1,1,0,1,1]]
// Output: 1
//
//
// Example 5:
//
//
// Input: grid = [[1,1,0,1,1],
//                [1,1,1,1,1],
//                [1,1,0,1,1],
//                [1,1,1,1,1]]
// Output: 2
//
//
//  
// Constraints:
//
//
// 	1 <= grid.length, grid[i].length <= 30
// 	grid[i][j] is 0 or 1.
//
//


using vi = vector<int>;
class Solution {
public:
    int n, m;
    vi dirs{1, 0, -1, 0, 1};
    int minDays(vector<vector<int>>& grid) {
        n = grid.size(); m = grid[0].size();
        int compo = getcompo(grid);
        // cout << compo << endl;
        if (compo > 1) return 0;
        else{
            for (int i = 0; i < n; i++){
                for (int j = 0; j < m; j++){
                    if (grid[i][j]){
                        grid[i][j] = 0;
                        int compo = getcompo(grid);
                        grid[i][j] = 1;
                        if (compo > 1) return 1;
                    }
                }
            }
        }
        return 2;
    }
    int getcompo(vector<vi>& grid){
        vector<vi> visited(n, vi(m, 0));
        int compo = 0;
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                if (!visited[i][j] && grid[i][j]) {
                    compo += 1;
                    dfs(i, j, grid, visited);
                }
            }
        }
        return compo;
    }
    void dfs(int x, int y, vector<vi>& grid, vector<vi>& visited){
        if (x < 0 || y < 0 || x >= n || y >= m || visited[x][y] || grid[x][y] == 0) return ;
        visited[x][y] = 1;
        for (int i = 0; i < 4; i++){
            dfs(x + dirs[i], y + dirs[i + 1], grid, visited);
        }
    }
    
};
