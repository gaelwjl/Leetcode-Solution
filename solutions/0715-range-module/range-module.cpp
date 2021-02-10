// A Range Module is a module that tracks ranges of numbers. Your task is to design and implement the following interfaces in an efficient manner.
//
// addRange(int left, int right) Adds the half-open interval [left, right), tracking every real number in that interval.  Adding an interval that partially overlaps with currently tracked numbers should add any numbers in the interval [left, right) that are not already tracked.
//
// queryRange(int left, int right) Returns true if and only if every real number in the interval [left, right)
//  is currently being tracked.
//
// removeRange(int left, int right) Stops tracking every real number currently being tracked in the interval [left, right).
//
// Example 1:
//
// addRange(10, 20): null
// removeRange(14, 16): null
// queryRange(10, 14): true (Every number in [10, 14) is being tracked)
// queryRange(13, 15): false (Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
// queryRange(16, 17): true (The number 16 in [16, 17) is still being tracked, despite the remove operation)
//
//
//
// Note:
// A half open interval [left, right) denotes all real numbers left <= x < right.
//
// 0 < left < right < 10^9 in all calls to addRange, queryRange, removeRange.
// The total number of calls to addRange in a single test case is at most 1000.
// The total number of calls to queryRange in a single test case is at most 5000.
// The total number of calls to removeRange in a single test case is at most 1000.
//


class RangeModule {
    vector<pair<int, int>> ranges_;
public:
    RangeModule() {}
    
    void addRange(int left, int right) {
        vector<pair<int, int>> new_ranges;
        int add = 0;
        for (auto& p: ranges_) {
            if (p.first > right && !add) {
                new_ranges.emplace_back(left, right);
                add = 1;
            }
            if (p.second < left || p.first > right){
                new_ranges.push_back(p);
            }
            else{
                left = min(left, p.first);
                right = max(right, p.second);
            }
        }
        if (!add) new_ranges.emplace_back(left, right);
        ranges_.swap(new_ranges);
        
    }
    
    bool queryRange(int left, int right) {
        int l = 0, r = ranges_.size() - 1;
        
        while (l <= r){
            int m = l + (r - l) / 2;
            if (ranges_[m].first > right){
                r = m - 1;
            }else if (ranges_[m].second < left){
                l = m + 1;
            }else{
                return ranges_[m].first <= left && ranges_[m].second >= right;
            }
        }
        return false;
    }
    
    void removeRange(int left, int right) {
        vector<pair<int, int>> new_ranges;
        for (auto& p: ranges_) {
            if (p.second < left || p.first > right){
                new_ranges.push_back(p);
            }
            else{
                if (p.first < left)
                    new_ranges.emplace_back(p.first, left);
                if (p.second > right) 
                    new_ranges.emplace_back(right, p.second);
            }
        }
        ranges_.swap(new_ranges);
        // for (auto p: ranges_) cout << p.first << " " << p.second << endl;
    }
};

/**
 * Your RangeModule object will be instantiated and called as such:
 * RangeModule* obj = new RangeModule();
 * obj->addRange(left,right);
 * bool param_2 = obj->queryRange(left,right);
 * obj->removeRange(left,right);
 */
