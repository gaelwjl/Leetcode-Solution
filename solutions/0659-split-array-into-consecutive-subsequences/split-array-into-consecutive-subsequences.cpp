// Given an array nums sorted in ascending order, return true if and only if you can split it into 1 or more subsequences such that each subsequence consists of consecutive integers and has length at least 3.
//
//  
//
// Example 1:
//
//
// Input: [1,2,3,3,4,5]
// Output: True
// Explanation:
// You can split them into two consecutive subsequences : 
// 1, 2, 3
// 3, 4, 5
//
//
//
// Example 2:
//
//
// Input: [1,2,3,3,4,4,5,5]
// Output: True
// Explanation:
// You can split them into two consecutive subsequences : 
// 1, 2, 3, 4, 5
// 3, 4, 5
//
//
//
// Example 3:
//
//
// Input: [1,2,3,4,4,5]
// Output: False
//
//
//  
//
// Constraints:
//
//
// 	1 <= nums.length <= 10000
//
//
//  
//


class Solution {
public:
    bool isPossible(vector<int>& nums) {
        unordered_map<int, priority_queue<int, vector<int>, greater<int> > > m;
        for (int i = 0; i < nums.size(); i++){
            auto it = m.find(nums[i] - 1);
            if (it == m.end()){
                m[nums[i]].push(1);
            }
            else {
                int top = it -> second.top();
                it -> second.pop();
                if (it -> second.size() == 0) m.erase(nums[i] - 1);
                top ++;
                m[nums[i]].push(top);
            }
        }
        for (auto it = m.begin(); it != m.end(); it++){
            // cout << it -> first << " "<<  it -> second.top() << endl;
            if (it -> second.top() < 3) return false;
        }
        return true;
    }
};
