// Given a string s, you can convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.
//
//  
// Example 1:
// Input: s = "aacecaaa"
// Output: "aaacecaaa"
// Example 2:
// Input: s = "abcd"
// Output: "dcbabcd"
//
//  
// Constraints:
//
//
// 	0 <= s.length <= 5 * 104
// 	s consists of lowercase English letters only.
//
//


class Solution {
public:
    const int p = 26; 
    const int mod = 1e9 + 7;
    vector<long long> rolling_hash(string& s){
        int n = s.size(); 
        vector<long long> prefix(n + 2);
        prefix[1] = s[0] - 'a';
        for (int i = 1; i < n; i++){
            prefix[i + 1] = ((prefix[i]*p)%mod + mod + (s[i] - 'a')) % mod;
        }
        return prefix;
    }
    string shortestPalindrome(string s) {
        const int n = s.size(); 
        auto pref = rolling_hash(s);
        reverse(s.begin(), s.end()); 
        auto suffix = rolling_hash(s);
        reverse(suffix.begin(), suffix.end()); 
        reverse(s.begin(), s.end()); 
        int i; 
        vector<long long> factor(n + 1, 1);
        for (int i = 1; i <= n ; i++){
            factor[i] = (factor[i - 1]*p)%mod; 
        }
        for (i = n - 1; i >= 0; i--){
            // s[0:i] is palin 
            long long pref_hash = pref[i + 1], suff_hash = (suffix[1] - (suffix[i + 2]*factor[i + 1])%mod + mod) % mod; 
            if (pref_hash == suff_hash){
                // cout << s.substr(0, i + 1) << endl; 
                break;
            }
        }
        
        string toadd = s.substr(i + 1); 
        reverse(toadd.begin(), toadd.end());
        
        return toadd + s; 
    }
};

