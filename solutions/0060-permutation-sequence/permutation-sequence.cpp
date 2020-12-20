// The set [1, 2, 3, ..., n] contains a total of n! unique permutations.
//
// By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
//
//
// 	"123"
// 	"132"
// 	"213"
// 	"231"
// 	"312"
// 	"321"
//
//
// Given n and k, return the kth permutation sequence.
//
//  
// Example 1:
// Input: n = 3, k = 3
// Output: "213"
// Example 2:
// Input: n = 4, k = 9
// Output: "2314"
// Example 3:
// Input: n = 3, k = 1
// Output: "123"
//
//  
// Constraints:
//
//
// 	1 <= n <= 9
// 	1 <= k <= n!
//
//


class Solution {
public:
    using ll = long long;
    vector<bool> used;
    int n;
    string getPermutation(int n_, int k) {
        vector<ll> fact{1};
        n = n_;
        for (int i = 1; i <= n; i++){
            fact.push_back(fact.back()*i);
        }
        used = vector<bool>(n + 1, false);
        return helper(n, k, fact);
    }
    int find_useful(int c){
        int cnt = 0;
        int i = 1;
        for (; i <= n; i++) {
            if (!used[i]) cnt += 1;
            if (cnt == c) break;
        }
        used[i] = true;
        return i;
    }
    string helper(int n, int k, vector<ll>& fact){
        if (n == 1) {
            return to_string(find_useful(1));
        }
        int first = (k - 1) / fact[n - 1] + 1;
        int i = 1;
        first = find_useful(first);
        int rest = (k - 1) % fact[n - 1];
        return to_string(first) + helper(n - 1, rest + 1, fact);
    }
};
