// Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
//
// Example:
//
//
// Input: 
//
// 1 0 1 0 0
// 1 0 1 1 1
// 1 1 1 1 1
// 1 0 0 1 0
//
// Output: 4
//


class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        int n = matrix.size(), m = 0;
        if (n > 0)
            m = matrix[0].size();
        int dp[n + 1][m + 1];
        memset(dp, 0, sizeof(dp));
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (matrix[i - 1][j - 1] == '1')
                    dp[i][j] = min (dp[i - 1][j], min(dp[i - 1][j - 1],  dp[i][j - 1])) + 1;
                else
                    dp[i][j] = 0;
                //cout << dp[i][j] << endl;
            }
        }
        int ans = 0;
        for (int i = 0; i <= n; i++)
            ans = max(ans, *max_element(dp[i], dp[i] + m + 1));
        return ans * ans;
    }
};
