// Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.
//
// Note: The input string may contain letters other than the parentheses ( and ).
//
// Example 1:
//
//
// Input: "()())()"
// Output: ["()()()", "(())()"]
//
//
// Example 2:
//
//
// Input: "(a)())()"
// Output: ["(a)()()", "(a())()"]
//
//
// Example 3:
//
//
// Input: ")("
// Output: [""]
//


class Solution {
public:
    vector<string> ans;
    
    vector<string> removeInvalidParentheses(string s) {
        int l = 0, r = 0;
        for (const char c : s){
            l += (c == '(');
            if (l == 0) r += (c == ')');
            else l -= (c == ')');
        }
        dfs(l, r, s, 0);
        
        return ans;
    }
    
    void dfs(int l, int r, string tmp, int i){
        if (l == 0 && r == 0){
            if (isvalid(tmp)) ans.push_back(tmp);
            return ;
        }
        for (int j = i; j < tmp.size(); j++){
            if (j > i && tmp[j] == tmp[j - 1]) continue;
            if (tmp[j] == '(' && l > 0){
                string new_tmp = tmp;
                new_tmp.erase(j, 1);
                dfs(l - 1, r, new_tmp, j);
            }
            if (tmp[j] == ')' && r > 0){
                string new_tmp = tmp;
                new_tmp.erase(j, 1);
                dfs(l, r - 1, new_tmp, j);
            }
        }
    }
    
    bool isvalid(string s){
        int cnt = 0;
        for (const char c: s){
            if (c == '(') cnt += 1;
            else if (c == ')') cnt -= 1;
            if (cnt < 0) return false;
        }
        return cnt == 0;
    }
};
