// Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where: 
//
//
// 	'.' Matches any single character.​​​​
// 	'*' Matches zero or more of the preceding element.
//
//
// The matching should cover the entire input string (not partial).
//
//  
// Example 1:
//
//
// Input: s = "aa", p = "a"
// Output: false
// Explanation: "a" does not match the entire string "aa".
//
//
// Example 2:
//
//
// Input: s = "aa", p = "a*"
// Output: true
// Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
//
//
// Example 3:
//
//
// Input: s = "ab", p = ".*"
// Output: true
// Explanation: ".*" means "zero or more (*) of any character (.)".
//
//
// Example 4:
//
//
// Input: s = "aab", p = "c*a*b"
// Output: true
// Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
//
//
// Example 5:
//
//
// Input: s = "mississippi", p = "mis*is*p*."
// Output: false
//
//
//  
// Constraints:
//
//
// 	0 <= s.length <= 20
// 	0 <= p.length <= 30
// 	s contains only lowercase English letters.
// 	p contains only lowercase English letters, '.', and '*'.
// 	It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
//
//


class Solution {
public:
    bool isMatch(string s, string p) {
        int n = s.size(), m = p.size();
        vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));
        dp[n][m] = 1;
        for (int i = n; i >= 0; i--){
            for (int j = m - 1; j >= 0; j--){
                int match = i < n && (s[i] == p[j] || p[j] == '.');
                if (j + 1 < m && p[j + 1] == '*'){
                    dp[i][j] = dp[i][j + 2] || (match && dp[i + 1][j]);
                }
                else{
                    dp[i][j] = match && dp[i + 1][j + 1];
                }
            }
        }
        return dp[0][0];
    }
};
