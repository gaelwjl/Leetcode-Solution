// Given a string s, return the longest palindromic substring in s.
//
//  
// Example 1:
//
//
// Input: s = "babad"
// Output: "bab"
// Note: "aba" is also a valid answer.
//
//
// Example 2:
//
//
// Input: s = "cbbd"
// Output: "bb"
//
//
// Example 3:
//
//
// Input: s = "a"
// Output: "a"
//
//
// Example 4:
//
//
// Input: s = "ac"
// Output: "a"
//
//
//  
// Constraints:
//
//
// 	1 <= s.length <= 1000
// 	s consist of only digits and English letters (lower-case and/or upper-case),
//


class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.size();
        string tor = "";
        vector<vector<int>> dp(n, vector<int>(n, 0)); 
        for (int l = 1; l <= n; l++){
            for (int i = 0; i + l - 1 < n; i++){
                int j = i + l - 1;
                if (i == j) {
                    dp[i][j] = 1;
                }else{
                    dp[i][j] = (s[i] == s[j] && (l == 2 || dp[i + 1][j - 1]))?1:0;
                }
                if (dp[i][j] && l > tor.size()){
                    tor = s.substr(i, l);
                }
            }
        }
        return tor;
    }
};

