// Given a non-empty 2D matrix matrix and an integer k, find the max sum of a rectangle in the matrix such that its sum is no larger than k.
//
// Example:
//
//
// Input: matrix = [[1,0,1],[0,-2,3]], k = 2
// Output: 2 
// Explanation: Because the sum of rectangle [[0, 1], [-2, 3]] is 2,
//              and 2 is the max number no larger than k (k = 2).
//
// Note:
//
//
// 	The rectangle inside the matrix must have an area > 0.
// 	What if the number of rows is much larger than the number of columns?
//


class Solution {
public:
    int maxSumSubmatrix(vector<vector<int>>& matrix, int k) {
        int n = matrix.size(), m = matrix[0].size();
        int presum[n + 1][m + 1];
        memset(presum, 0, sizeof(presum));
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                presum[i + 1][j + 1] = presum[i][j + 1] + presum[i + 1][j] - presum[i][j] + matrix[i][j];
        int ans = -INT_MAX;
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= m; j++)
                for (int i_ = 0; i_ < i; i_++)
                    for (int j_ = 0; j_ < j; j_++){
                        int temp = presum[i][j] - presum[i][j_] - presum[i_][j] + presum[i_][j_];
                        if (temp <= k)
                            ans = max(ans, temp);   
                    }
                        
        return ans;
    }
};
