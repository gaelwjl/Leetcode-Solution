// Given a string s, find the length of the longest substring without repeating characters.
//
//  
// Example 1:
//
//
// Input: s = "abcabcbb"
// Output: 3
// Explanation: The answer is "abc", with the length of 3.
//
//
// Example 2:
//
//
// Input: s = "bbbbb"
// Output: 1
// Explanation: The answer is "b", with the length of 1.
//
//
// Example 3:
//
//
// Input: s = "pwwkew"
// Output: 3
// Explanation: The answer is "wke", with the length of 3.
// Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
//
//
// Example 4:
//
//
// Input: s = ""
// Output: 0
//
//
//  
// Constraints:
//
//
// 	0 <= s.length <= 5 * 104
// 	s consists of English letters, digits, symbols and spaces.
//
//


class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.size(), j = 0, ans = 0;
        unordered_map<char, int> window;
        for (int i = 0; i < n; i++){
            window[s[i] - 'a'] ++;
            
            while (window[s[i] - 'a'] > 1) {
                // advance j to make it unique;
                window[s[j] - 'a'] --;
                j++;
            }
            ans = max(ans, i - j + 1); 
        }
        return ans;
    }
};

