// You are given four integers, m, n, introvertsCount, and extrovertsCount. You have an m x n grid, and there are two types of people: introverts and extroverts. There are introvertsCount introverts and extrovertsCount extroverts.
//
// You should decide how many people you want to live in the grid and assign each of them one grid cell. Note that you do not have to have all the people living in the grid.
//
// The happiness of each person is calculated as follows:
//
//
// 	Introverts start with 120 happiness and lose 30 happiness for each neighbor (introvert or extrovert).
// 	Extroverts start with 40 happiness and gain 20 happiness for each neighbor (introvert or extrovert).
//
//
// Neighbors live in the directly adjacent cells north, east, south, and west of a person's cell.
//
// The grid happiness is the sum of each person's happiness. Return the maximum possible grid happiness.
//
//  
// Example 1:
//
//
// Input: m = 2, n = 3, introvertsCount = 1, extrovertsCount = 2
// Output: 240
// Explanation: Assume the grid is 1-indexed with coordinates (row, column).
// We can put the introvert in cell (1,1) and put the extroverts in cells (1,3) and (2,3).
// - Introvert at (1,1) happiness: 120 (starting happiness) - (0 * 30) (0 neighbors) = 120
// - Extrovert at (1,3) happiness: 40 (starting happiness) + (1 * 20) (1 neighbor) = 60
// - Extrovert at (2,3) happiness: 40 (starting happiness) + (1 * 20) (1 neighbor) = 60
// The grid happiness is 120 + 60 + 60 = 240.
// The above figure shows the grid in this example with each person's happiness. The introvert stays in the light green cell while the extroverts live on the light purple cells.
//
//
// Example 2:
//
//
// Input: m = 3, n = 1, introvertsCount = 2, extrovertsCount = 1
// Output: 260
// Explanation: Place the two introverts in (1,1) and (3,1) and the extrovert at (2,1).
// - Introvert at (1,1) happiness: 120 (starting happiness) - (1 * 30) (1 neighbor) = 90
// - Extrovert at (2,1) happiness: 40 (starting happiness) + (2 * 20) (2 neighbors) = 80
// - Introvert at (3,1) happiness: 120 (starting happiness) - (1 * 30) (1 neighbor) = 90
// The grid happiness is 90 + 80 + 90 = 260.
//
//
// Example 3:
//
//
// Input: m = 2, n = 2, introvertsCount = 4, extrovertsCount = 0
// Output: 240
//
//
//  
// Constraints:
//
//
// 	1 <= m, n <= 5
// 	0 <= introvertsCount, extrovertsCount <= min(m * n, 6)
//
//


class Solution {
public:
    int m, n;
    int dp[25][7][7][64][64];
    int neibCost(int i, int j, int in_mask, int ex_mask, int d){
        int diff = 0, up = 1 << (n - 1);
        if (j > 0 && (in_mask&1)){
            diff += d - 30;
        }
        if (i > 0 && (in_mask&up)){
            diff += d - 30;
        }
        if (j > 0 && (ex_mask&1)){
            diff += d + 20;
        }
        if (i > 0 && (ex_mask&up)){
            diff += d + 20;
        }
        return diff;
    }
    int dfs(int p, int n_in, int n_ex, int in_mask, int ex_mask){
        int i = p / n, j = p%n;
        if (i >= m)
            return 0;
        // in_mask = in_mask & 63, ex_mask = ex_mask&63;
        if (dp[p][n_in][n_ex][in_mask][ex_mask] != -1)
            return dp[p][n_in][n_ex][in_mask][ex_mask];
        
        int nxt_in_mask = ((in_mask << 1)&63), nxt_ext_mask = ((ex_mask << 1)&63);
        int ans = dfs(p + 1, n_in, n_ex, nxt_in_mask, nxt_ext_mask); // nobody in this cell 
        // place intro
        if (n_in){
            int diff = 120 + neibCost(i, j, in_mask, ex_mask, -30);
            ans = max(ans, diff + dfs(p + 1, n_in - 1, n_ex, nxt_in_mask + 1, nxt_ext_mask));
        }
        if (n_ex){
            int diff = 40 + neibCost(i, j, in_mask, ex_mask, 20);
            ans = max(ans, diff + dfs(p + 1, n_in, n_ex - 1, nxt_in_mask, nxt_ext_mask + 1));
        }
        dp[p][n_in][n_ex][in_mask][ex_mask] = ans;
        return ans;
    }
    int getMaxGridHappiness(int m_, int n_, int IntroCnt, int ExtroCnt) {
        m = m_, n = n_;
        memset(dp, -1, sizeof(dp));
        return dfs(0, IntroCnt, ExtroCnt, 0, 0);
    }
};
