// Given a 2D array of characters grid of size m x n, you need to find if there exists any cycle consisting of the same value in grid.
//
// A cycle is a path of length 4 or more in the grid that starts and ends at the same cell. From a given cell, you can move to one of the cells adjacent to it - in one of the four directions (up, down, left, or right), if it has the same value of the current cell.
//
// Also, you cannot move to the cell that you visited in your last move. For example, the cycle (1, 1) -> (1, 2) -> (1, 1) is invalid because from (1, 2) we visited (1, 1) which was the last visited cell.
//
// Return true if any cycle of the same value exists in grid, otherwise, return false.
//
//  
// Example 1:
//
//
//
//
// Input: grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
// Output: true
// Explanation: There are two valid cycles shown in different colors in the image below:
//
//
//
// Example 2:
//
//
//
//
// Input: grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
// Output: true
// Explanation: There is only one valid cycle highlighted in the image below:
//
//
//
// Example 3:
//
//
//
//
// Input: grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
// Output: false
//
//
//  
// Constraints:
//
//
// 	m == grid.length
// 	n == grid[i].length
// 	1 <= m <= 500
// 	1 <= n <= 500
// 	grid consists only of lowercase English letters.
//
//


class Solution {
public:
    bool containsCycle(vector<vector<char>>& grid) {
        int n = grid.size(), m = grid[0].size();
        vector<vector<int>> vis(n, vector<int>(m, 0)), act(n, vector<int>(m, 0));
        vector<int> DIRS{1, 0, -1, 0, 1}; 
        bool flag = false; 
        function<void(int, int)> dfs = [&](int cur, int prev=-1){
            int x = cur / m, y = cur%m;
            if (vis[x][y])
                return ;
            // cout << x << " " << y << " " << grid[x][y] << endl;
            vis[x][y] = 1; 
            act[x][y] = 1; 
            for (int d = 0; d < 4; d++){
                int nx = x + DIRS[d], ny = y + DIRS[d + 1]; 
                if (nx >= n || nx < 0 || ny >= m || ny < 0 || grid[nx][ny] != grid[x][y])
                    continue;
                if (act[nx][ny] && nx*m + ny != prev){
                    // cout << grid[nx][ny] << endl;
                    flag = true; 
                }
                dfs(nx*m + ny, cur);
            }
            act[x][y] = 0; 
        };
        for (int i = 0; i < n*m; i++)
            dfs(i, -1); 
        return flag; 
    }
};

