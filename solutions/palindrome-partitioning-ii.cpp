// Given a string s, partition s such that every substring of the partition is a palindrome.
//
// Return the minimum cuts needed for a palindrome partitioning of s.
//
//  
// Example 1:
//
//
// Input: s = "aab"
// Output: 1
// Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
//
//
// Example 2:
//
//
// Input: s = "a"
// Output: 0
//
//
// Example 3:
//
//
// Input: s = "ab"
// Output: 1
//
//
//  
// Constraints:
//
//
// 	1 <= s.length <= 2000
// 	s consists of lower-case English letters only.
//
//


class Solution {
public:
    const int p = 26; 
    const int mod = 1e9 + 7;
    vector<long long> rolling_hash(string& s){
        int n = s.size(); 
        vector<long long> prefix(n + 1);
        prefix[1] = s[0] - 'a'; 
        for (int i = 1; i < n; i++){
            prefix[i + 1] = (prefix[i]*p + (s[i] - 'a')) % mod;
        }
        return prefix;
    }
    int minCut(string s) {
        int n = s.size(); 
        auto prefix = rolling_hash(s);
        
        reverse(s.begin(), s.end());
        auto suffix = rolling_hash(s);
        reverse(suffix.begin(), suffix.end());
        // cout << suffix[n] << endl;
        
        reverse(s.begin(), s.end());
        vector<long long> power(n + 1);
        power[0] = 1;
        for (int i = 1; i <= n; i++)
            power[i] = (power[i - 1] * p) % mod;
        vector<int> memo(n, -1);
        function<int(int)> dfs = [&](int ind){
            // cout << ind << endl;
            // if s[i:ind] is a palin;
            // rolling_hash to know that in O(1)
            if (memo[ind] != -1) return memo[ind];
            int ans = ind;
            for (int i = 0; i <= ind; i++){
                // string index from i to ind (inclusive)
                long long hash_pre = (prefix[ind + 1] - (prefix[i] * power[ind - i + 1])%mod + mod)%mod; 
                long long hash_suff = (suffix[i] - (suffix[ind + 1] * power[ind - i + 1])%mod + mod)%mod;
                if (hash_pre == hash_suff){
                    // cout << s.substr(i + 1, ind - i) << endl;
                    if (i == 0) 
                        ans = 0;
                    else
                        ans = min(ans, dfs(i - 1) + 1);
                }
            }
            return memo[ind] = ans;
        };
        return dfs(n - 1);
    }
};
