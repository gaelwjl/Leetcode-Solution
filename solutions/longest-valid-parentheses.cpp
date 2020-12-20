// Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
//
//  
// Example 1:
//
//
// Input: s = "(()"
// Output: 2
// Explanation: The longest valid parentheses substring is "()".
//
//
// Example 2:
//
//
// Input: s = ")()())"
// Output: 4
// Explanation: The longest valid parentheses substring is "()()".
//
//
// Example 3:
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
// 	0 <= s.length <= 3 * 104
// 	s[i] is '(', or ')'.
//
//


class Solution {
public:
    int longestValidParentheses(string s) {
        vector<int> stk{-1}; 
        int ans = 0;
        for (int i = 0; i<s.size();i++){
            if (s[i] == ')'){
                if (stk.back() != -1 && s[stk.back()] == '('){
                    stk.pop_back();
                    ans = max(ans, i - stk.back());
                }
                else{
                    stk.push_back(i);
                }
            }
            else{
                stk.push_back(i);
            }
        }
        return ans;
    }
};
