// You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
//
// Design an algorithm to find the maximum profit. You may complete at most k transactions.
//
// Notice that you may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
//
//  
// Example 1:
//
//
// Input: k = 2, prices = [2,4,1]
// Output: 2
// Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
//
//
// Example 2:
//
//
// Input: k = 2, prices = [3,2,6,5,0,3]
// Output: 7
// Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
//
//
//  
// Constraints:
//
//
// 	0 <= k <= 100
// 	0 <= prices.length <= 1000
// 	0 <= prices[i] <= 1000
//
//


class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        // power of algorithm!!!
        int v, p = 0, n = prices.size();
        vector<vector<int>> stk;
        priority_queue<int> profits;
        while (p < n){
            for (v = p; v < n - 1 && prices[v] >= prices[v + 1]; v++);
            for (p = v + 1; p < n && prices[p - 1] <= prices[p]; p++);
            while (stk.size() && prices[v] <= prices[stk.back()[0]]){
                profits.push(prices[stk.back()[1] - 1] - prices[stk.back()[0]]);
                stk.pop_back();
            }
            while (stk.size() && prices[stk.back()[1] - 1] <= prices[p - 1]){
                profits.push(prices[stk.back()[1] - 1] - prices[v]);
                v = stk.back()[0];
                stk.pop_back();
            }
            stk.push_back({v, p});
        }
        for (auto& v: stk){
            profits.push(prices[v[1] - 1] - prices[v[0]]);
        }
        int ans = 0;
        for (int i = 0; i < k && profits.size(); i++){
            ans += profits.top();
            profits.pop();
        }
        return ans;
    }
};
