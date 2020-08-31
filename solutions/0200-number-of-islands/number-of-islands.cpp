// Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
//
//  
// Example 1:
//
//
// Input: grid = [
//   ["1","1","1","1","0"],
//   ["1","1","0","1","0"],
//   ["1","1","0","0","0"],
//   ["0","0","0","0","0"]
// ]
// Output: 1
//
//
// Example 2:
//
//
// Input: grid = [
//   ["1","1","0","0","0"],
//   ["1","1","0","0","0"],
//   ["0","0","1","0","0"],
//   ["0","0","0","1","1"]
// ]
// Output: 3
//
//


class Solution {
public:
    
    vector<vector<char>> grid, seen;
    
    int n, m;
    
    void dfs(int i, int j){
        if (seen[i][j] == '1')
            return ;
        seen[i][j] = '1';
        if (i + 1 < n && grid[i + 1][j] =='1')
            dfs(i + 1, j);
        if (j + 1 < m && grid[i][j + 1] =='1')
            dfs(i, j + 1);
        if (i - 1 >= 0 && grid[i - 1][j] =='1')
            dfs(i - 1, j);
        if (j - 1 >= 0 && grid[i][j - 1] =='1')
            dfs(i , j - 1);
    }
    
    int numIslands(vector<vector<char>>& grid_) {
        grid = grid_;
        n = grid.size();
        if (n == 0)
            return 0;
        m = grid[0].size();
        for (int i = 0; i < n; i++){
            vector<char> temp(m, '0');
            seen.push_back(temp);
        }
        int res = 0;
        for (int i = 0; i < n; i++) 
            for (int j = 0; j < m; j++){
                if (grid[i][j] == '1' && seen[i][j] == '0'){
                    dfs(i, j);
                    res ++;
                }
            }
        return res;
    }
};
