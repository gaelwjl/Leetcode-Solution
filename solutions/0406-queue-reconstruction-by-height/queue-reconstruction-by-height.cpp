// Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.
//
// Note:
// The number of people is less than 1,100.
//  
//
// Example
//
//
// Input:
// [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
//
// Output:
// [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
//
//
//  
//


class Solution {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        sort(people.begin(), people.end(), 
            [](vector<int>& ls, vector<int>& rs){
                if (ls[0] > rs[0]) return true;
                else if (ls[0] == rs[0] && ls[1] < rs[1]) return true;
                return false;
            });
        vector<vector<int>> ans;
        for (auto& p: people)
            ans.insert(ans.begin() + p[1], p);
        return ans;
    }
};