// Given a rectangular pizza represented as a rows x cols matrix containing the following characters: 'A' (an apple) and '.' (empty cell) and given the integer k. You have to cut the pizza into k pieces using k-1 cuts. 
//
// For each cut you choose the direction: vertical or horizontal, then you choose a cut position at the cell boundary and cut the pizza into two pieces. If you cut the pizza vertically, give the left part of the pizza to a person. If you cut the pizza horizontally, give the upper part of the pizza to a person. Give the last piece of pizza to the last person.
//
// Return the number of ways of cutting the pizza such that each piece contains at least one apple. Since the answer can be a huge number, return this modulo 10^9 + 7.
//
//  
// Example 1:
//
//
//
//
// Input: pizza = ["A..","AAA","..."], k = 3
// Output: 3 
// Explanation: The figure above shows the three ways to cut the pizza. Note that pieces must contain at least one apple.
//
//
// Example 2:
//
//
// Input: pizza = ["A..","AA.","..."], k = 3
// Output: 1
//
//
// Example 3:
//
//
// Input: pizza = ["A..","A..","..."], k = 1
// Output: 1
//
//
//  
// Constraints:
//
//
// 	1 <= rows, cols <= 50
// 	rows == pizza.length
// 	cols == pizza[i].length
// 	1 <= k <= 10
// 	pizza consists of characters 'A' and '.' only.
//


class Solution {
public:
    int ways(vector<string>& pizza, int k) {
        int n = pizza.size(), m = pizza[0].size(), mod = 1e9 + 7;
        int dp[n + 1][m + 1][k + 1], prefix[n + 1][m + 1]; // stack allocation; at compile time;
        memset(dp, -1, sizeof(dp));
        memset(prefix, 0, sizeof(prefix)); 
        for (int i = 1; i <= n; i++){
            for (int j = 1; j <= m; j++)
                prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] + (pizza[i - 1][j - 1] == 'A') - prefix[i - 1][j - 1]; 
        }
        function<int(int, int, int)> dfs = [&](int i, int j, int k){
            if (k == 1) 
                return 1; 
            if (dp[i][j][k] != -1) return dp[i][j][k]; 
            int area = prefix[n][m] - prefix[i - 1][m] - prefix[n][j - 1] + prefix[i - 1][j - 1]; 
            
            // check row:
            int ans = 0, rightup = prefix[i - 1][m] - prefix[i - 1][j - 1]; 
            for (int r = i; r < n; r++){
                int cut = prefix[r][m] - prefix[r][j - 1] - rightup;
                if (cut > 0 && area - cut > 0) 
                    ans += dfs(r + 1, j, k - 1); 
                ans %= mod; 
            }
            // check col: 
            int leftlow = prefix[n][j - 1] - prefix[i - 1][j - 1]; 
            for (int c = j; c < m; c++){
                int cut = prefix[n][c] - prefix[i - 1][c] - leftlow; 
                if (cut > 0 && area - cut > 0)
                    ans += dfs(i, c + 1, k - 1); 
                ans %= mod; 
            }
            return dp[i][j][k] = ans; 
        };
        return dfs(1, 1, k);
    }
};
