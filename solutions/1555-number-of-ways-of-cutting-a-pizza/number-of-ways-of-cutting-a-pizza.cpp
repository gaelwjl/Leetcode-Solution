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


const int mod = 1e9 + 7;
const int maxr = 51, maxc = 51;
class Solution {
public:
    int ways(vector<string>& pizza, int k) {
        row = pizza.size();
        col = pizza[0].size();
        memset(prefix, 0, sizeof(prefix));
        memset(dp, -1, sizeof(dp));
        for (int i = 1; i <= row; i++){
            for (int j = 1; j <= col; j++){
                prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + int(pizza[i - 1][j - 1] == 'A');
            }
        }
        int ans = search(1, 1, k - 1);
        return ans;
    }
private:
    int prefix[maxr][maxc];
    int row, col;
    int dp[maxr][maxc][11];
    int search(int x1, int y1, int k){
        if (dp[x1][y1][k] != -1){
            return dp[x1][y1][k];
        }
        if (k == 0)
            return 1;
        int allapples = prefix[row][col] + prefix[x1 - 1][y1 - 1] - prefix[x1 - 1][col] - prefix[row][y1 - 1];
        int ans = 0;
        for (int r = x1; r < row; r++){
            int ntocut = prefix[r][col] + prefix[x1 - 1][y1 - 1] - prefix[x1 - 1][col] - prefix[r][y1 - 1];
            if (ntocut < allapples && ntocut > 0){
                ans += search(r + 1, y1, k - 1);
                ans %= mod;
            }
        }
        for (int c = y1; c < col; c++){
            int ntocut = prefix[row][c] + prefix[x1 - 1][y1 - 1] - prefix[x1 - 1][c] - prefix[row][y1 - 1];
            if (ntocut < allapples && ntocut > 0){
                ans += search(x1, c + 1, k - 1);
                ans %= mod;
            }
        }
        dp[x1][y1][k] = ans;
        return ans;
    }

};
