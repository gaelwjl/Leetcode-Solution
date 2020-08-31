// Given a string s, partition s such that every substring of the partition is a palindrome
//
// Return the minimum cuts needed for a palindrome partitioning of s.
//
//  
// Example 1:
//
//
// Input: s = "aab"
// Output: 1
// Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
//
//
// Example 2:
//
//
// Input: s = "a"
// Output: 0
//
//
// Example 3:
//
//
// Input: s = "ab"
// Output: 1
//
//
//  
// Constraints:
//
//
// 	1 <= s.length <= 2000
// 	s consists of lower-case English letters only.
//
//


class Solution {
public:
    int minCut(string s) {
        int n = s.size();
        vector<vector<int>> isvalid(n, vector<int>(n, 1));
        for (int l = 2; l <= n; l++)
            for (int i = 0, j = l - 1; j < n; i++, j++)
                isvalid[i][j] = isvalid[i + 1][j - 1] && s[i] == s[j];
        
        vector<int> mincut(n + 1, n);
        mincut[0] = 0;
        for (int j = 1; j <= n; j++)
            if (isvalid[0][j - 1])
                mincut[j] = 0;
        for (int i = 1; i <= n; i++)
            for (int j = i; j <= n; j++)
                if (isvalid[i - 1][j - 1])
                    mincut[j] = min(mincut[j], mincut[i - 1] + 1);
        return mincut[n];
    }
};
