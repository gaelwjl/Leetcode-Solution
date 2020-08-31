// There are n people and 40 types of hats labeled from 1 to 40.
//
// Given a list of list of integers hats, where hats[i] is a list of all hats preferred by the i-th person.
//
// Return the number of ways that the n people wear different hats to each other.
//
// Since the answer may be too large, return it modulo 10^9 + 7.
//
//  
// Example 1:
//
//
// Input: hats = [[3,4],[4,5],[5]]
// Output: 1
// Explanation: There is only one way to choose hats given the conditions. 
// First person choose hat 3, Second person choose hat 4 and last one hat 5.
//
// Example 2:
//
//
// Input: hats = [[3,5,1],[3,5]]
// Output: 4
// Explanation: There are 4 ways to choose hats
// (3,5), (5,3), (1,3) and (1,5)
//
//
// Example 3:
//
//
// Input: hats = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
// Output: 24
// Explanation: Each person can choose hats labeled from 1 to 4.
// Number of Permutations of (1,2,3,4) = 24.
//
//
// Example 4:
//
//
// Input: hats = [[1,2,3],[2,3,5,6],[1,3,7,9],[1,8,9],[2,5,7]]
// Output: 111
//
//
//  
// Constraints:
//
//
// 	n == hats.length
// 	1 <= n <= 10
// 	1 <= hats[i].length <= 40
// 	1 <= hats[i][j] <= 40
// 	hats[i] contains a list of unique integers.
//


class Solution {
public:
    int numberWays(vector<vector<int>>& hats) {
        int n = hats.size();
        int dp[41][1 << n];
        int MOD = 1e9 + 7;
        memset(dp, 0, sizeof(dp));
        vector<int> hatsToP[41];
        for (int i = 0; i < n; i++){
            for (int h : hats[i]){
                hatsToP[h].push_back(i);
            }
        }
        dp[0][0] = 1;
        for (int h = 1; h < 41; h++){
            for (int j = 0; j < (1 << n); j++){
                dp[h][j] = (dp[h - 1][j] + dp[h][j]) % MOD;
                for (int people : hatsToP[h]){
                    if (((1 << people) & j) == 0)
                        dp[h][j | (1 << people)] = (dp[h - 1][j] + dp[h][j | (1 << people)]) % MOD;
                }
            }
        }
        return dp[40][(1 << n) - 1];
    }
};
