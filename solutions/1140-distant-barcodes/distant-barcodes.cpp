// In a warehouse, there is a row of barcodes, where the i-th barcode is barcodes[i].
//
// Rearrange the barcodes so that no two adjacent barcodes are equal.  You may return any answer, and it is guaranteed an answer exists.
//
//  
//
// Example 1:
//
//
// Input: [1,1,1,2,2,2]
// Output: [2,1,2,1,2,1]
//
//
//
// Example 2:
//
//
// Input: [1,1,1,1,2,2,3,3]
// Output: [1,3,1,3,2,1,2,1]
//
//
//  
//
// Note:
//
//
// 	1 <= barcodes.length <= 10000
// 	1 <= barcodes[i] <= 10000
//
//
//
//  
//


using pii = pair<int, int>;
class Solution {
public:
    vector<int> rearrangeBarcodes(vector<int>& barcodes) {
        unordered_map<int, int> cnt;
        for (const int bar: barcodes){
            cnt[bar] ++;
        }
        set<pii> s;
        for (auto it = cnt.begin(); it != cnt.end(); it++) s.insert({it -> second, it -> first});
        // begin by the most common not the biggest value;
        // maintain a data structure which map from times to list of values in 
        vector<int> ans(barcodes.size());
        int ind = 0;
        for ( auto it = s.rbegin(); it != s.rend();++it) {
            for(int times = it -> first; times; times--){
                if (ind >= barcodes.size()){
                    ind = 1;
                }
                ans[ind] = it -> second;
                ind += 2;
            }
        }
        return ans;
    }
};
