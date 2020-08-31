// Given a string num representing the digits of a very large integer and an integer k.
//
// You are allowed to swap any two adjacent digits of the integer at most k times.
//
// Return the minimum integer you can obtain also as a string.
//
//  
// Example 1:
//
//
// Input: num = "4321", k = 4
// Output: "1342"
// Explanation: The steps to obtain the minimum integer from 4321 with 4 adjacent swaps are shown.
//
//
// Example 2:
//
//
// Input: num = "100", k = 1
// Output: "010"
// Explanation: It's ok for the output to have leading zeros, but the input is guaranteed not to have any leading zeros.
//
//
// Example 3:
//
//
// Input: num = "36789", k = 1000
// Output: "36789"
// Explanation: We can keep the number without any swaps.
//
//
// Example 4:
//
//
// Input: num = "22", k = 22
// Output: "22"
//
//
// Example 5:
//
//
// Input: num = "9438957234785635408", k = 23
// Output: "0345989723478563548"
//
//
//  
// Constraints:
//
//
// 	1 <= num.length <= 30000
// 	num contains digits only and doesn't have leading zeros.
// 	1 <= k <= 10^9
//
//


class FenwickTree{
    public:
    FenwickTree(int n): sums_(n + 1, 0){}

    void update(int i, int delta){
        i++;
        while (i < sums_.size()){
            sums_[i] += delta;
            i += lowbit(i);
        }
    }
    int qry(int i){
        i++;
        int sum = 0; 
        while (i > 0){
            sum += sums_[i];
            i -= lowbit(i);
        }
        return sum;
    }
    private:
    vector<int> sums_;
    static inline int lowbit(int x){
        return x & (-x);
    };
};


class Solution {
public:
    string minInteger(string num, int k) {
        const int n = num.size();
        FenwickTree ft(n);
        vector<queue<int>> pos(10);
        for (int i = 0; i < n; i++){
            pos[num[i] - '0'].push(i);
        }
        vector<int> used(n);
        string ans = "";
        while (k > 0 && ans.length() < n){
            for (int d = 0; d < 10; d++){
                if (pos[d].empty()) continue;
                int p = pos[d].front();
                int cost = p - ft.qry(p - 1);
                if (cost > k) continue;
                k -= cost;
                ft.update(p, 1);
                pos[d].pop();
                used[p] = 1;
                ans += num[p];
                break;
            }
        }
        for (int i = 0; i < n; i ++){
            if (!used[i]) ans += num[i];
        }
        return ans;
    }
};
