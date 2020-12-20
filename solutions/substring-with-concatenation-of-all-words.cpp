// You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.
//
// You can return the answer in any order.
//
//  
// Example 1:
//
//
// Input: s = "barfoothefoobarman", words = ["foo","bar"]
// Output: [0,9]
// Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
// The output order does not matter, returning [9,0] is fine too.
//
//
// Example 2:
//
//
// Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
// Output: []
//
//
// Example 3:
//
//
// Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
// Output: [6,9,12]
//
//
//  
// Constraints:
//
//
// 	1 <= s.length <= 104
// 	s consists of lower-case English letters.
// 	1 <= words.length <= 5000
// 	1 <= words[i].length <= 30
// 	words[i] consists of lower-case English letters.
//
//


class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        unordered_map<string, int> ws;
        for (auto v: words){
            ws[v]++;
        }
        int len = words[0].size(), sl = len*words.size();
        vector<int> ans; 
        for (int i = 0; i + sl <= s.size(); i++){
            unordered_map<string, int> seen;
            bool flag = true;
            for (int cnt = 0; cnt < words.size(); cnt++){
                string tmp = s.substr(i + cnt*len, len); 
                auto it = ws.find(tmp); 
                if (it == ws.end()){
                    flag = false;
                }
                else{
                    seen[s.substr(i + cnt * len, len)]++;
                    if (seen[tmp] > ws[tmp]){
                        flag = false;
                    }
                }
            }
            if (flag)
                ans.push_back(i);
        }
        return ans;
    }
};
