// You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
//
// Example 1:
//
//
// Input: coins = [1, 2, 5], amount = 11
// Output: 3 
// Explanation: 11 = 5 + 5 + 1
//
// Example 2:
//
//
// Input: coins = [2], amount = 3
// Output: -1
//
//
// Note:
// You may assume that you have an infinite number of each kind of coin.
//


class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        sort(coins.rbegin(), coins.rend());
        int ans = INT_MAX;
        dfs(coins, 0, amount, 0, ans);
        return ans == INT_MAX ? -1 : ans;
    }
    void dfs(vector<int>& coins, int pos, int amount, int cnt, int& ans){
        if (amount == 0){
            ans = min(cnt, ans);
            return ;
        }
        if (pos == coins.size())
            return;
        int coin = coins[pos];
        for (int k = amount / coin; k >= 0 && cnt + k < ans; k--)
            dfs(coins, pos + 1, amount - coin * k, cnt + k, ans);
    }
};
