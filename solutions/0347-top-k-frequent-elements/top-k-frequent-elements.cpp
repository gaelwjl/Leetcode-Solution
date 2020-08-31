// Given a non-empty array of integers, return the k most frequent elements.
//
// Example 1:
//
//
// Input: nums = [1,1,1,2,2,3], k = 2
// Output: [1,2]
//
//
//
// Example 2:
//
//
// Input: nums = [1], k = 1
// Output: [1]
//
//
// Note: 
//
//
// 	You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
// 	Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
// 	It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
// 	You can return the answer in any order.
//
//


class Solution {
public:
    // struct mycomp{
    //     bool operator()(const pair<int, int>& a, const pair<int, int> & b){
    //         if (a.second != b.second)
    //             return a.second < b.second;
    //         else
    //             return a.first > b.first;
    //     }  
    // };
    vector<int> topKFrequent(vector<int>& nums, int k) {
        priority_queue<pair<int, int>> pq;
        map<int, int>  record;
        for (auto& n:nums){
            record[n]++;
        }
        for (auto& val:record){
            pq.push(make_pair(val.second, val.first));
        }
        vector<int> result;
        while (k--){
            result.push_back(pq.top().second);
            pq.pop();
        }
        return result;
    }
};
