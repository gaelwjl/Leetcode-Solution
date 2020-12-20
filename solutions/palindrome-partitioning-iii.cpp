// You are given a string s containing lowercase letters and an integer k. You need to :
//
//
// 	First, change some characters of s to other lowercase English letters.
// 	Then divide s into k non-empty disjoint substrings such that each substring is palindrome.
//
//
// Return the minimal number of characters that you need to change to divide the string.
//
//  
// Example 1:
//
//
// Input: s = "abc", k = 2
// Output: 1
// Explanation: You can split the string into "ab" and "c", and change 1 character in "ab" to make it palindrome.
//
//
// Example 2:
//
//
// Input: s = "aabbc", k = 3
// Output: 0
// Explanation: You can split the string into "aa", "bb" and "c", all of them are palindrome.
//
// Example 3:
//
//
// Input: s = "leetcode", k = 8
// Output: 0
//
//
//  
// Constraints:
//
//
// 	1 <= k <= s.length <= 100.
// 	s only contains lowercase English letters.
//


class Solution {
public:
    int palindromePartition(string s, int k) {
        int n = s.size(); 
        if (k >= n) 
            return 0; 
        vector<vector<int>> dp(n, vector<int>(n + 1, n)), f(n, vector<int>(n, 0)); 
        for (int d = 1; d <= n; d++){
            for (int i = 0; i + d - 1 < n; i++){
                if (d == 1){
                    f[i][i] = 0; 
                    continue; 
                }else if (d == 2){
                    f[i][i + 1] = (s[i] == s[i + 1])?0:1; 
                    continue; 
                }
                else{
                    f[i][i + d - 1] = (s[i] == s[i + d - 1])?f[i + 1][i + d - 2]:f[i + 1][i + d - 2] + 1; 
                    
                }
            }
        }
        for (int i = 0; i < n; i++){
            dp[i][1] = f[0][i];
        }
        for (int i = 0; i < n; i++){
            // dp[i][i + 1]
            for (int j = 1; j <= i + 1; j++){
                for (int l = 0; l < i; l++){
                    dp[i][j] = min(dp[i][j], dp[l][j - 1] + f[l + 1][i]); 
                }
            }
        }
        return dp[n - 1][k];
    }
};
