// Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.
//
//  
// Example 1:
//
//
// Input: words = ["abcd","dcba","lls","s","sssll"]
// Output: [[0,1],[1,0],[3,2],[2,4]]
// Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
//
//
// Example 2:
//
//
// Input: words = ["bat","tab","cat"]
// Output: [[0,1],[1,0]]
// Explanation: The palindromes are ["battab","tabbat"]
//
//
// Example 3:
//
//
// Input: words = ["a",""]
// Output: [[0,1],[1,0]]
//
//
//  
// Constraints:
//
//
// 	1 <= words.length <= 5000
// 	0 <= words[i].length <= 300
// 	words[i] consists of lower-case English letters.
//
//


class Solution {
public:
    vector<vector<int>> palindromePairs(vector<string>& words) {
        unordered_map<string, int> dict; 
        for (int i = 0; i < words.size(); i++) 
            dict[words[i]] = i;
        auto is_palin = [](string& w, int left, int right){
            // if (!w.size())
            while (left < right){
                if (w[left++] != w[right--]){
                    return false; 
                }
            }
            return true;
        };
        vector<vector<int>> ans; 
        for (int i = 0; i < words.size(); i++){
            for (int j = 0; j <= words[i].size(); j++){
                // cout << j << endl;
                if (is_palin(words[i], j, words[i].size() - 1)){
                    auto p = words[i].substr(0, j);
                    // cout << p << endl; 
                    reverse(p.begin(), p.end());
                    if (dict.count(p) && dict[p] != i){
                        ans.push_back({i, dict[p]}); 
                    }
                }
                if (j > 0 && is_palin(words[i], 0, j - 1)){
                    auto p = words[i].substr(j);
                    // cout << p << endl;
                    reverse(p.begin(), p.end()); 
                    if (dict.count(p) && dict[p] != i){
                        ans.push_back({dict[p], i}); 
                    }
                }
            }
        }
        return ans; 
    }

};

