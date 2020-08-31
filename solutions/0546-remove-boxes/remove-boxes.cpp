// Given several boxes with different colors represented by different positive numbers.
// You may experience several rounds to remove boxes until there is no box left. Each time you can choose some continuous boxes with the same color (composed of k boxes, k >= 1), remove them and get k*k points.
// Find the maximum points you can get.
//
//  
// Example 1:
//
//
// Input: boxes = [1,3,2,2,2,3,4,3,1]
// Output: 23
// Explanation:
// [1, 3, 2, 2, 2, 3, 4, 3, 1] 
// ----> [1, 3, 3, 4, 3, 1] (3*3=9 points) 
// ----> [1, 3, 3, 3, 1] (1*1=1 points) 
// ----> [1, 1] (3*3=9 points) 
// ----> [] (2*2=4 points)
//
//
//  
// Constraints:
//
//
// 	1 <= boxes.length <= 100
// 	1 <= boxes[i] <= 100
//
//


class Solution {
    int dp[101][101][101];
    vector<int> arr;
    int _dfs(int i, int j, int k){
        if (i > j) return 0;
        if (dp[i][j][k] > 0)
            return dp[i][j][k];
        dp[i][j][k] = _dfs(i, j - 1, 0) + (k + 1) * (k + 1);
        for (int p = i; p < j; p++){
            if (arr[p] == arr[j]){
                dp[i][j][k] = max(_dfs(i, j, k), _dfs(i, p, k + 1) + _dfs(p + 1, j - 1, 0));
            }
        }
        return  dp[i][j][k];
    }
public:
    int removeBoxes(vector<int>& boxes) {
        arr = boxes;
        memset(dp, 0, sizeof(dp));
        int n = boxes.size();
        return _dfs(0, n - 1, 0);
    }
};
