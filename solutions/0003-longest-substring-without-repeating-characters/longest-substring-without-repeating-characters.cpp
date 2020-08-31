// Given a string, find the length of the longest substring without repeating characters.
//
//
// Example 1:
//
//
// Input: "abcabcbb"
// Output: 3 
// Explanation: The answer is "abc", with the length of 3. 
//
//
//
// Example 2:
//
//
// Input: "bbbbb"
// Output: 1
// Explanation: The answer is "b", with the length of 1.
//
//
//
// Example 3:
//
//
// Input: "pwwkew"
// Output: 3
// Explanation: The answer is "wke", with the length of 3. 
//              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
//
//
//
//
//


#include <set>

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int l = s.length();
        int res = 0;
        for (int i = 0; i < l; i++) {
            std::set<char> temp;
            temp.insert(s[i]);
            for (int j = i + 1; j < l; j++){
                if (temp.find(s[j]) == temp.end()) temp.insert(s[j]);
                else break;
            }
            if (temp.size() > res) res = temp.size();
        }
        return res;
    }
};
