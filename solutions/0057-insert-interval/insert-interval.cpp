// Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
//
// You may assume that the intervals were initially sorted according to their start times.
//
// Example 1:
//
//
// Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
// Output: [[1,5],[6,9]]
//
//
// Example 2:
//
//
// Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
// Output: [[1,2],[3,10],[12,16]]
// Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
//
// NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
//


class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        map<int, int> ranges;
        for (auto intv: intervals)
            ranges[intv[0]] = intv[1];
        auto it = ranges.lower_bound(newInterval[0]);
        if (it != ranges.begin() && (--it) -> second < newInterval[0]) ++it;
        int start = newInterval[0], end = newInterval[1];
        while (it != ranges.end() && it -> first <= newInterval[1]){
            start = min(start, it -> first);
            end = max(end, it -> second);
            it = ranges.erase(it);
        }
        ranges[start] = end;
        vector<vector<int>> ans;
        for (auto it : ranges)
            ans.push_back({it.first, it.second});
        
        return ans;
    }
};
