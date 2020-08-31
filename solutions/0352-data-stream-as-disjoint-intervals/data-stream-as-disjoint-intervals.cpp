// Given a data stream input of non-negative integers a1, a2, ..., an, ..., summarize the numbers seen so far as a list of disjoint intervals.
//
// For example, suppose the integers from the data stream are 1, 3, 7, 2, 6, ..., then the summary will be:
//
//
// [1, 1]
// [1, 1], [3, 3]
// [1, 1], [3, 3], [7, 7]
// [1, 3], [7, 7]
// [1, 3], [6, 7]
//
//
//  
//
// Follow up:
//
// What if there are lots of merges and the number of disjoint intervals are small compared to the data stream's size?
//


class SummaryRanges {
private:
    map<int, int> ranges;
public:
    /** Initialize your data structure here. */
    SummaryRanges() {}
    
    void addNum(int val) {
        auto it = ranges.lower_bound(val);
        if (it != ranges.begin() && (--it) -> second < val - 1) it++;
        int start = val;
        int end = val;
        while (it != ranges.end() && it -> first <= val + 1){
            start = min(start, it -> first);
            end = max(end, it -> second);
            it = ranges.erase(it);
        }
        ranges[start] = end;
    }
    
    vector<vector<int>> getIntervals() {
        vector<vector<int>> ans;
        for (auto it : ranges){
            ans.push_back({it.first, it.second});
        }
        return ans;
    }
};

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * SummaryRanges* obj = new SummaryRanges();
 * obj->addNum(val);
 * vector<vector<int>> param_2 = obj->getIntervals();
 */
