// Given a string, your task is to count how many palindromic substrings in this string.
//
// The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.
//
// Example 1:
//
//
// Input: "abc"
// Output: 3
// Explanation: Three palindromic strings: "a", "b", "c".
//
//
//  
//
// Example 2:
//
//
// Input: "aaa"
// Output: 6
// Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
//
//
//  
//
// Note:
//
//
// 	The input string length won't exceed 1000.
//
//
//  


class Solution {
public:
    int countSubstrings(string s) {
        int n = s.size(), ans = 0; vector<vector<int>> dp(n, vector<int>(n));
        for (int i = 1; i <= n; i++){
            for (int st = 0, e = i - 1; e < n; st++, e++){
                if (i == 1 || (s[st] == s[e] && (i == 2 || dp[st + 1][e - 1]))){
                    dp[st][e] = 1;
                    ++ans;
                }
            }
        }
        return ans;
    }
};

