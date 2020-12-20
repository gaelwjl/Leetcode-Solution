// Say you have an array for which the ith element is the price of a given stock on day i.
//
// Design an algorithm to find the maximum profit. You may complete at most two transactions.
//
// Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
//
//  
// Example 1:
//
//
// Input: prices = [3,3,5,0,0,3,1,4]
// Output: 6
// Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
// Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
//
// Example 2:
//
//
// Input: prices = [1,2,3,4,5]
// Output: 4
// Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
// Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
//
//
// Example 3:
//
//
// Input: prices = [7,6,4,3,1]
// Output: 0
// Explanation: In this case, no transaction is done, i.e. max profit = 0.
//
//
// Example 4:
//
//
// Input: prices = [1]
// Output: 0
//
//
//  
// Constraints:
//
//
// 	1 <= prices.length <= 105
// 	0 <= prices[i] <= 105
//
//


class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // optimize it to have constant space? 
        int n = prices.size(); 
        vector<vector<int>> max_sell(n, vector<int>(3, 0)), max_buy(n, vector<int>(3, 0));
        
        for (int j = 1; j < 3; j++){
            max_buy[0][j] = -prices[0];
            for (int i = 1; i < n; i++){
                max_sell[i][j] = max(max_buy[i - 1][j] + prices[i], max_sell[i - 1][j]);
                max_buy[i][j] = max(max_buy[i - 1][j], max_sell[i - 1][j - 1] - prices[i]);
            }
        }
        return max_sell[n - 1][2];
    }
};
