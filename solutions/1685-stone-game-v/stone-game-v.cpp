// There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.
//
// In each round of the game, Alice divides the row into two non-empty rows (i.e. left row and right row), then Bob calculates the value of each row which is the sum of the values of all the stones in this row. Bob throws away the row which has the maximum value, and Alice's score increases by the value of the remaining row. If the value of the two rows are equal, Bob lets Alice decide which row will be thrown away. The next round starts with the remaining row.
//
// The game ends when there is only one stone remaining. Alice's is initially zero.
//
// Return the maximum score that Alice can obtain.
//
//  
// Example 1:
//
//
// Input: stoneValue = [6,2,3,4,5,5]
// Output: 18
// Explanation: In the first round, Alice divides the row to [6,2,3], [4,5,5]. The left row has the value 11 and the right row has value 14. Bob throws away the right row and Alice's score is now 11.
// In the second round Alice divides the row to [6], [2,3]. This time Bob throws away the left row and Alice's score becomes 16 (11 + 5).
// The last round Alice has only one choice to divide the row which is [2], [3]. Bob throws away the right row and Alice's score is now 18 (16 + 2). The game ends because only one stone is remaining in the row.
//
//
// Example 2:
//
//
// Input: stoneValue = [7,7,7,7,7,7,7]
// Output: 28
//
//
// Example 3:
//
//
// Input: stoneValue = [4]
// Output: 0
//
//
//  
// Constraints:
//
//
// 	1 <= stoneValue.length <= 500
// 	1 <= stoneValue[i] <= 10^6
//
//


class Solution {
public:
    int stoneGameV(vector<int>& stoneValue) {
        vector<int> arr = stoneValue;
        int n=arr.size();
        vector<vector<int>> dp(n, vector<int>(n,0));
        function <int(int, int)> dfs = [&](int x, int y){
            if (x >= y) return 0;
            // if (y == x + 1) return min(arr[x], arr[x+1]);
            // cout << x << " " << y << endl;
            if (dp[x][y]) return dp[x][y];
            int ans = 0; 
            int s = 0;
            for (int m = x; m<=y; m++) s += arr[m];
            int cum = 0;
            for (int m=x; m<= y;m++){
                cum += arr[m];
                if (cum < s - cum) ans = max(ans, cum + dfs(x, m));
                else if (cum == s - cum) ans = max(ans, cum + max(dfs(x, m), dfs(m+1,y)));
                else ans = max(ans, s-cum+dfs(m+1, y));
            }
            dp[x][y]=ans;
            return ans;
        };
        return dfs(0, arr.size()-1);
    }
};
