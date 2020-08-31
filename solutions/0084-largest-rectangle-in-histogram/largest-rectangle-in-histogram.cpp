// Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
//
//  
//
//
// Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
//
//  
//
//
// The largest rectangle is shown in the shaded area, which has area = 10 unit.
//
//  
//
// Example:
//
//
// Input: [2,1,5,6,2,3]
// Output: 10
//
//


class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        heights.push_back(0);
        stack<vector<int>> s;
        int ans = 0, ind = 0;
        for (int ind = 0; ind < heights.size(); ind++){
            int l = ind, h = heights[ind];
            while (s.size() && h < s.top()[1]){
                auto top = s.top(); s.pop();
                l = top[0];
                int h_cur = top[1];
                ans = max(ans, (ind - l)*h_cur);
            }
            s.push({l, h});
        }
        return ans;
    }
};
