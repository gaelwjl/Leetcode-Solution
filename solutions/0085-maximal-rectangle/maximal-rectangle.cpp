// Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
//
//  
// Example 1:
//
//
// Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
// Output: 6
// Explanation: The maximal rectangle is shown in the above picture.
//
//
// Example 2:
//
//
// Input: matrix = []
// Output: 0
//
//
// Example 3:
//
//
// Input: matrix = [["0"]]
// Output: 0
//
//
// Example 4:
//
//
// Input: matrix = [["1"]]
// Output: 1
//
//
// Example 5:
//
//
// Input: matrix = [["0","0"]]
// Output: 0
//
//
//  
// Constraints:
//
//
// 	rows == matrix.length
// 	cols == matrix.length
// 	0 <= row, cols <= 200
// 	matrix[i][j] is '0' or '1'.
//
//


class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        int n = matrix.size(); if (n == 0) return 0; int m = matrix[0].size();
        if (n == 0 || m == 0) return 0;
        vector<int> hist(m, 0);
        int ans = 0; 
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                if (matrix[i][j] == '1'){
                    hist[j] += 1;
                }
                else hist[j] = 0;
            }
            ans = max(ans, help(hist));
        }
        return ans;
    }
    int help(vector<int> heights) {
        vector<int> stk; 
        heights.push_back(0);
        int ans = 0; 
        for (int i = 0; i < heights.size(); i++){
            int last = i, origin = heights[i];
            while (stk.size() && heights[i] < heights[stk.back()]){
                ans = max(ans, (i - stk.back())*heights[stk.back()]);
                last = stk.back();
                stk.pop_back();
            }
            heights[last] = origin;
            stk.push_back(last);
        }
        return ans;
    }
};
