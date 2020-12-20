// Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:
//
//
// 	Only one letter can be changed at a time
// 	Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
//
//
// Note:
//
//
// 	Return an empty list if there is no such transformation sequence.
// 	All words have the same length.
// 	All words contain only lowercase alphabetic characters.
// 	You may assume no duplicates in the word list.
// 	You may assume beginWord and endWord are non-empty and are not the same.
//
//
// Example 1:
//
//
// Input:
// beginWord = "hit",
// endWord = "cog",
// wordList = ["hot","dot","dog","lot","log","cog"]
//
// Output:
// [
//   ["hit","hot","dot","dog","cog"],
//   ["hit","hot","lot","log","cog"]
// ]
//
//
// Example 2:
//
//
// Input:
// beginWord = "hit"
// endWord = "cog"
// wordList = ["hot","dot","dog","lot","log"]
//
// Output: []
//
// Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
//
//
//
//
//


class Solution {
public:
    vector<vector<string>> findLadders(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> wordd, cur_s; 
        unordered_map<string, int> dist;
        // dist[beginWord] = 0;
        for (auto& w: wordList){
            wordd.insert(w); 
        }
        vector<vector<string>> ans; 
        vector<string> p{beginWord};
        
        auto bfs=[&](){
            deque<string> nxt_w{beginWord}; 
            int max_l = 0;
            
            while (nxt_w.size()){
                int s = nxt_w.size(); while (s--){
                    auto cur = nxt_w.front();
                    // cout << cur << endl;
                    nxt_w.pop_front(); 
                    if (dist.count(cur))
                        continue; 
                    dist[cur] = max_l + 1;
                    if (cur == endWord){
                        return max_l + 1;
                    }
                    for (int i = 0; i < cur.size(); i++){
                        int prev_c = cur[i];
                        for (int j = 0; j < 26; j++){
                            cur[i] = 'a' + j;
                            if (wordd.count(cur) && !dist.count(cur))
                                nxt_w.push_back(cur);
                        }
                        cur[i] = prev_c; 
                    }
                }
                max_l ++; 
            }
            return -1; 
        }; 
        auto max_l = bfs();
        // cout << max_l << endl;
        function<void(string&,vector<string>&, unordered_set<string>& )> dfs = [&](string& cur, vector<string>& path, unordered_set<string>& cur_s){
            if (path.size() > max_l) 
                return;
            if (cur == endWord){
                if (!ans.size()){
                    ans.push_back(path);
                }
                else if (ans[0].size() > path.size()){
                    ans.clear(); 
                    ans.push_back(path); 
                }
                else if (ans[0].size() == path.size()){
                    ans.push_back(path); 
                }
            }
            for (int i = 0; i < cur.size(); i++){
                auto prev_c = cur[i]; 
                int prev_d = dist[cur]; 
                for (int j = 0; j < 26; j++){
                    cur[i] = 'a' + j; 
                    if (wordd.count(cur) && !cur_s.count(cur)){
                        path.push_back(cur);
                        cur_s.insert(cur);
                        if (path.size() <= max_l && dist[cur] == prev_d + 1)
                            dfs(cur, path, cur_s);
                        cur_s.erase(cur);
                        path.pop_back();
                    }
                }
                cur[i] = prev_c; 
            }
        };
        dfs(beginWord, p, cur_s);
        return ans; 
    }
};
