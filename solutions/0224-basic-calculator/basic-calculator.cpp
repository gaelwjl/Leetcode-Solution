// Implement a basic calculator to evaluate a simple expression string.
//
// The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces  .
//
// Example 1:
//
//
// Input: "1 + 1"
// Output: 2
//
//
// Example 2:
//
//
// Input: " 2-1 + 2 "
// Output: 3
//
// Example 3:
//
//
// Input: "(1+(4+5+2)-3)+(6+8)"
// Output: 23
// Note:
//
//
// 	You may assume that the given expression is always valid.
// 	Do not use the eval built-in library function.
//
//


class Solution {
    int i = 0;
public:
    int calculate(string s) {
        stack<long long> stk;
        long long sign = 1, tmp = 0;
        while (i < s.size()){
            if (isdigit(s[i])) {
                tmp = tmp * 10 + s[i] - '0';
                i++;
            }
            else if (s[i] == '('){
                i++;
                stk.push(sign * calculate(s));
            }
            else if (s[i] == ')'){
                i++;
                long long ans = sum(stk) + sign * tmp;
                sign = 1;
                tmp = 0;
                return ans;
            }
            else if (s[i] == '+' || s[i] == '-') {
                stk.push(sign * tmp);
                sign = s[i] == '+' ? 1 : -1;
                tmp = 0;
                i++;
            }
            else 
                i++;
        }
        return sum(stk) + sign*tmp;
    }
    int sum(stack<long long>& s){
        long long ans = 0;
        while (s.size()){
            ans += s.top();
            s.pop();
        }
        return ans;
    }
};
