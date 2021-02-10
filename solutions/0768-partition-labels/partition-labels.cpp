// A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.
//
//  
//
// Example 1:
//
//
// Input: S = "ababcbacadefegdehijhklij"
// Output: [9,7,8]
// Explanation:
// The partition is "ababcbaca", "defegde", "hijhklij".
// This is a partition so that each letter appears in at most one part.
// A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
//
//
//  
//
// Note:
//
//
// 	S will have length in range [1, 500].
// 	S will consist of lowercase English letters ('a' to 'z') only.
//
//
//  
//


class Solution {
public:
    vector<int> partitionLabels(string S) {
        int last[26], cum = 0, l = 0, n = S.size();
        vector<int> ans;
        memset(last, -1, sizeof(last));
        for (int i = 0; i < S.size(); i++)
            last[S[i] - 'a'] = i;
        
        for (int i = 0; i < n; i++){
            if (i > l){
                ans.push_back(cum);
                cum = 1;
                l = last[S[i] - 'a'];
            }else{
                cum += 1;
                l = max(l, last[S[i] - 'a']);
            }
        }
        if (cum) ans.push_back(cum);
        return ans;
    }
};
