// Given an integer matrix, find the length of the longest increasing path.
//
// From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).
//
// Example 1:
//
//
// Input: nums = 
// [
//   [9,9,4],
//   [6,6,8],
//   [2,1,1]
// ] 
// Output: 4 
// Explanation: The longest increasing path is [1, 2, 6, 9].
//
//
// Example 2:
//
//
// Input: nums = 
// [
//   [3,4,5],
//   [3,2,6],
//   [2,2,1]
// ] 
// Output: 4 
// Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
//
//


class Solution {
public:
    int n, m, ans;
    vector<vector<int>> mat;
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        n = matrix.size();
        if (n == 0)
            return 0;
        m = matrix[0].size();
        mat = matrix;
        ans = 1;
        vector<vector<int>> memo(n, vector<int>(m, 0));
        for (int i = 0; i< n; i++){
            for (int j = 0; j < m; j++){
                dfs(i, j, memo);
            }
        }
        return ans;
    }
    
    int dfs(int x, int y, vector<vector<int>>& memo){
        if (memo[x][y])
            return memo[x][y];
        vector<int> dirs{1, 0, -1, 0, 1};
        memo[x][y] = 1;
        for (int i = 0; i < 4; i++){
            int vx = x + dirs[i], vy = y + dirs[i + 1];
            if (vx < 0 || vy < 0 || vx == n || vy == m)
                continue;
            if (mat[vx][vy] > mat[x][y]){
                memo[x][y] = max(dfs(vx, vy, memo) + 1, memo[x][y]);
            }
        }
        ans = max(ans, memo[x][y]);
        return memo[x][y];
    }
};
