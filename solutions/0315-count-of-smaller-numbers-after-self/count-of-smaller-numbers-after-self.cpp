// You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].
//
//  
// Example 1:
//
//
// Input: nums = [5,2,6,1]
// Output: [2,1,1,0]
// Explanation:
// To the right of 5 there are 2 smaller elements (2 and 1).
// To the right of 2 there is only 1 smaller element (1).
// To the right of 6 there is 1 smaller element (1).
// To the right of 1 there is 0 smaller element.
//
//
//  
// Constraints:
//
//
// 	0 <= nums.length <= 10^5
// 	-10^4 <= nums[i] <= 10^4
//
//


class FenwickTree {
private:
    vector<int> sums_;
public: 
    FenwickTree(int n): sums_(n, 0){}
    void upd(int i, int delta){
        while (i < sums_.size()){
            sums_[i] += delta;
            i += lowbit(i);
        }
    }
    int qry(int i) const{
        int sum = 0;
        while (i > 0){
            sum += sums_[i];
            i -= lowbit(i);
        }
        return sum;
    }
    static inline int lowbit(int x){
        return x & (-x);
    }
};

class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        int n = nums.size();
        FenwickTree tree(n + 1);

        unordered_map<int, int> ranks;
        set<int> sorted(nums.begin(), nums.end());
        int rank = 0;
        for (const int n : sorted)
            ranks[n] = ++rank;
        vector<int> ans;
        for (int i = n - 1; i >=0 ; i--){
            tree.upd(ranks[nums[i]], 1);
            ans.push_back(tree.qry(ranks[nums[i]] - 1));
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};
