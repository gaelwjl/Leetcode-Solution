// Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.
//
// If possible, output any possible result.  If not possible, return the empty string.
//
// Example 1:
//
//
// Input: S = "aab"
// Output: "aba"
//
//
// Example 2:
//
//
// Input: S = "aaab"
// Output: ""
//
//
// Note:
//
//
// 	S will consist of lowercase letters and have length in range [1, 500].
//
//
//  
//


class Solution {
public:
	string reorganizeString(string S) {
		map<char, int> m; 
        set<pair<int, char>> r_m;
        string ans;
        for (char c: S){
            m[c]++;
            ans += " ";
        } 
        for (auto it: m)
            r_m.insert({it.second, it.first});
        
        int ind = 0;
        for (auto it = r_m.rbegin(); it != r_m.rend(); it++){
            int cnt = it -> first; 
            // if (it -> second == 'a') cout << it -> first;
            if (cnt > (ans.size() + 1) / 2)
                return "";
            while (cnt--) {
                if (ind >= S.size()){
                    ind = 1;
                }
                ans[ind] = it -> second;
                ind += 2;
            }
        }
		// string ans = "";
		// int i = 0, j = (S.size() + 1) / 2;
		// while (j < S.size()) {
		// 	// cout << ans;
		// 	if (i != j && S[i] == S[j])
		// 		return "";
		// 	ans += S[i]; ans += S[j];
		// 	i++; j++;
		// }
		// if (S[i] == S[0] && S[i] == S.back()) return "";
		// if (S.size()&1 && S[i] != S[0]) ans = S[i] + ans;
		// else ans = ans + S[i];
		// cout << ans << endl;
		return ans;
	}
};
