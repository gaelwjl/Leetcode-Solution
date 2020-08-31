// Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
//
// Example 1:
//
//
// Input: "babad"
// Output: "bab"
// Note: "aba" is also a valid answer.
//
//
// Example 2:
//
//
// Input: "cbbd"
// Output: "bb"
//
//


class Solution {
    public: 
    string longestPalindrome(string s) {
        int start = 0, maxLength = 0, n = s.length(), length = 0;
        for(int i = 0; i < n; ++i) {
            length = max(getOddLength(s, i, n), getEvenLength(s, i, n));
            if(length > maxLength) {
                start = i + 1 - (length+1)/2;
                maxLength = length;
            }
        }
        return s.substr(start, maxLength);
    }
    
    int getOddLength(string s, int i, int n) {
        int j = 1, comp = min(i+1, n-i);
        while(j < comp && s[i-j] == s[i+j]) ++j;
        return 2*(j-1)+1;
    }
    
    int getEvenLength(string s, int i, int n) {
        int j = 0; 
        int comp = min(i+1, n-1-i);
        while(j < comp && s[i-j] == s[i+j+1]) ++j;
        return 2*j;
    }
};
