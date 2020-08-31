// Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
//
// Example 1:
//
//
// Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
// Output: true
//
//
// Example 2:
//
//
// Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
// Output: false
//
//


class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        int n1 = s1.size(), n2 = s2.size(), n3 = s3.size();
        bool dp[n1 + 1][n2 + 1];
        memset(dp, false, sizeof(dp));
        dp[0][0] = true;
        if (n1 + n2 != n3)
            return false;
        for(int i = 0; i<= n1; i++){
            for (int j = 0; j<= n2; j++){
                if (i >= 1) dp[i][j] |= (dp[i - 1][j] && s1[i - 1] == s3[i + j - 1]);
                if (j >= 1) dp[i][j] |= (dp[i][j - 1] && s2[j - 1] == s3[i + j - 1]);
            }
        }
        return dp[n1][n2];
    }
};
