// Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:
//
//
// 	'?' Matches any single character.
// 	'*' Matches any sequence of characters (including the empty sequence).
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
// Input: s = "aa", p = "*"
// Output: true
// Explanation: '*' matches any sequence.
//
//
// Example 3:
//
//
// Input: s = "cb", p = "?a"
// Output: false
// Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
//
//
// Example 4:
//
//
// Input: s = "adceb", p = "*a*b"
// Output: true
// Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
//
//
// Example 5:
//
//
// Input: s = "acdcb", p = "a*c?b"
// Output: false
//
//
//  
// Constraints:
//
//
// 	0 <= s.length, p.length <= 2000
// 	s contains only lowercase English letters.
// 	p contains only lowercase English letters, '?' or '*'.
//
//


class Solution {
public:
    string s, p;
    vector<vector<int>> memo; 
    bool isMatch(string s_, string p_) {
        s = s_; p = p_; 
        int n = s.size(), m = p.size(); 
        memo = vector<vector<int>> (n + 1, vector<int>(m + 1, -1));
        int ans = helper(s.size(), p.size());
        // for ()
        return ans;
    }
    bool helper(int i, int j){
        if (i == 0 && j == 0) return true;
        if (i > 0 && j == 0) return false;
        // i == 0 but j > 0
        if (i == 0 && j > 0){
            if (p[j - 1] != '*') return false;
            return helper(i, j - 1);
        }
        
        if (memo[i][j] != -1) 
            return memo[i][j];
        int ans = 0;
        if (s[i - 1] == p[j - 1] || p[j - 1] == '?') 
            ans = helper(i - 1, j - 1);
        else if (p[j - 1] == '*') 
            ans = helper(i - 1, j - 1) || helper(i - 1, j) || helper(i, j - 1);
        else ans = false;
        return memo[i][j] = ans;
    }
};
