// The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
//
// Given an integer n, return the number of distinct solutions to the n-queens puzzle.
//
//  
// Example 1:
//
//
// Input: n = 4
// Output: 2
// Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
//
//
// Example 2:
//
//
// Input: n = 1
// Output: 1
//
//
//  
// Constraints:
//
//
// 	1 <= n <= 9
//
//


class Solution {
public:
    int n, ans;
    int totalNQueens(int n_) {
        n = n_;
        vector<string> s;
        for (int i = 0; i < n; i++){
            string tmp = "";
            for (int j = 0; j < n; j++){
                tmp += ".";
            }
            s.push_back(tmp);
        }
        solve(0, s);
        return ans;
    }
    bool check(int r, int c, vector<string>& s){
        for (int j = 0; j < n; j++){
            if (s[r][j] == 'Q') return false;
        }
        for (int i = 0; i < n; i++){
            if (s[i][c] == 'Q') return false;
        }
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                if ((i + j == r + c) || (i - j == r - c)){
                    if (s[i][j] == 'Q')
                        return false;
                }
            }
        }
        return true;
    }
    void solve(int r, vector<string>& s){
        if (r >= n) {
            ans += 1;
            return ;
        }
        // int r = row(i), c = col(i);
        for (int c = 0; c < n; c++){
            if (check(r, c, s)){
                s[r][c] = 'Q';
                solve(r + 1, s);
                s[r][c] = '.';
            }
        }
        return ;
    }
};
