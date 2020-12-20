// You are given a 0-indexed integer array nums and an integer k.
//
// You are initially standing at index 0. In one move, you can jump at most k steps forward without going outside the boundaries of the array. That is, you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.
//
// You want to reach the last index of the array (index n - 1). Your score is the sum of all nums[j] for each index j you visited in the array.
//
// Return the maximum score you can get.
//
//  
// Example 1:
//
//
// Input: nums = [1,-1,-2,4,-7,3], k = 2
// Output: 7
// Explanation: You can choose your jumps forming the subsequence [1,-1,4,3] (underlined above). The sum is 7.
//
//
// Example 2:
//
//
// Input: nums = [10,-5,-2,4,0,3], k = 3
// Output: 17
// Explanation: You can choose your jumps forming the subsequence [10,4,3] (underlined above). The sum is 17.
//
//
// Example 3:
//
//
// Input: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
// Output: 0
//
//
//  
// Constraints:
//
//
// 	 1 <= nums.length, k <= 105
// 	-104 <= nums[i] <= 104
//
//



class Solution {
public:
    struct Tree {
    typedef int T;
    static constexpr T unit = INT_MIN;

    T f(T a, T b) { return max(a, b); } // (any associative fn)
    vector<T> s;
    int n;

    Tree(int n = 0, T def = unit) : s(2 * n, def), n(n) {}

    void update(int pos, T val) {
        for (s[pos += n] = val; pos /= 2;)
            s[pos] = f(s[pos * 2], s[pos * 2 + 1]);
    }

    T query(int b, int e) { // query [b, e)
        T ra = unit, rb = unit;
        for (b += n, e += n; b < e; b /= 2, e /= 2) {
            if (b % 2) ra = f(ra, s[b++]);
            if (e % 2) rb = f(s[--e], rb);
        }
        return f(ra, rb);
    }
};
    int maxResult(vector<int>& nums, int k) {
        int n = nums.size();
        Tree segt(n + 1, -INT_MAX/2);
        segt.update(n - 1, nums[n - 1]);
        for (int i = n - 1; i--; i >= 0){
            int tmp = segt.query(i + 1, min(n, i + k + 1)) + nums[i]; 
            // cout << tmp << endl;
            segt.update(i, tmp);
        }
        // cout << segt.query(1, 2) << endl; 
        return segt.query(0, 1);
    }
};
