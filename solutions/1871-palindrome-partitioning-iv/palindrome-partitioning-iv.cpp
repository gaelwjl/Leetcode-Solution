// Given a string s, return true if it is possible to split the string s into three non-empty palindromic substrings. Otherwise, return false.​​​​​
//
// A string is said to be palindrome if it the same string when reversed.
//
//  
// Example 1:
//
//
// Input: s = "abcbdd"
// Output: true
// Explanation: "abcbdd" = "a" + "bcb" + "dd", and all three substrings are palindromes.
//
//
// Example 2:
//
//
// Input: s = "bcbddxy"
// Output: false
// Explanation: s cannot be split into 3 palindromes.
//
//
//  
// Constraints:
//
//
// 	3 <= s.length <= 2000
// 	s​​​​​​ consists only of lowercase English letters.
//
//


class Solution {
public:
    bool checkPartitioning(string s) {
        // easy question use a dp[i][j] if s[i...j] is a palindrome 
        int n = s.size();
        vector<vector<int>> dp(n, vector<int>(n));
        for (int i = 1; i <= n; i++)
            for (int b = 0, e = i - 1; e < n; b++, e++)
                dp[b][e] = (i == 1 || s[b] == s[e] && (i == 2 || dp[b + 1][e - 1]))?1:0;
        
        for (int i = 1; i < n; i++){
            for (int j = i + 1; j < n; j++){
                if (dp[0][i - 1] && dp[i][j - 1] && dp[j][n - 1]) 
                    return true;
            }
        }
        return false;
    
    }
};

