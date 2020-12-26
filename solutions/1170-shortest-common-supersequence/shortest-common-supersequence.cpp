// Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences.  If multiple answers exist, you may return any of them.
//
// (A string S is a subsequence of string T if deleting some number of characters from T (possibly 0, and the characters are chosen anywhere from T) results in the string S.)
//
//  
//
// Example 1:
//
//
// Input: str1 = "abac", str2 = "cab"
// Output: "cabac"
// Explanation: 
// str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
// str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
// The answer provided is the shortest such string that satisfies these properties.
//
//
//  
//
// Note:
//
//
// 	1 <= str1.length, str2.length <= 1000
// 	str1 and str2 consist of lowercase English letters.
//
//


class Solution {
public:
    string shortestCommonSupersequence(string str1, string str2) {
        int n = str1.size(), m = str2.size(); 
        vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0)); 
        for (int i = 1; i <= n; i++){
            for (int j = 1; j <= m; j++){
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]); 
                if (str1[i - 1] == str2[j - 1]){
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                }
            }
        }

        string ans;
        function<void(int, int)> explore = [&](int i, int j){
            // cout << i << " " << j << endl;
            if (i == 0 && j == 0)
                return ; 
            if (i == 0){
                ans += str2[j - 1]; 
                explore(i, j - 1); 
                return ; 
            }
            if (j == 0){
                ans += str1[i - 1]; 
                explore(i - 1, j); 
                return ; 
            }
            if (dp[i][j] == dp[i - 1][j - 1] + 1 && str1[i - 1] == str2[j - 1]){
                ans += str1[i - 1];
                explore(i - 1, j - 1);
                return ;
            }else if (dp[i][j] == dp[i][j - 1] && dp[i][j - 1] > dp[i - 1][j]){
                ans += str2[j - 1];
                explore(i, j - 1); 
                return ; 
            }else{
                ans += str1[i - 1];
                explore(i - 1, j); 
            }
        }; 
        explore(n, m); 
        reverse(ans.begin(), ans.end()); 
        return ans; 
    }
};
