// Given a 2D board and a list of words from the dictionary, find all words in the board.
//
// Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
//
//  
//
// Example:
//
//
// Input: 
// board = [
//   ['o','a','a','n'],
//   ['e','t','a','e'],
//   ['i','h','k','r'],
//   ['i','f','l','v']
// ]
// words = ["oath","pea","eat","rain"]
//
// Output: ["eat","oath"]
//
//
//  
//
// Note:
//
//
// 	All inputs are consist of lowercase letters a-z.
// 	The values of words are distinct.
//
//


class TrieNode{
	public:
    vector<TrieNode*> children;
    string* word;
    TrieNode(): children(26), word(nullptr){}
    ~TrieNode(){
        for (auto n : children)
            delete n;
        //delete word;
    }
};

class Solution {
public:
	vector<string> ans;
	int n, m;
	vector<vector<char>> board;
    vector<string> findWords(vector<vector<char>>& board_, vector<string>& words) {
		board = board_;
        TrieNode root;
        for (auto& w: words){
            TrieNode* iter = &root;
            for (char c: w){
                auto& next = iter -> children[c - 'a'];
                if (!next)
                    next = new TrieNode();
                iter = next;
            }
			iter -> word = &w;
        }
		n = board.size(), m = board[0].size();
		for (int i = 0; i < n ; i++){
			for (int j = 0; j < m; j++){
				search(i, j, &root);
			}
		}
        sort(ans.begin(), ans.end());
        return ans;
    }
	void search(int i, int j, TrieNode* node){
		if (i < 0 || j < 0 || i == n || j == m || board[i][j] == '#')
			return ;
		char cur = board[i][j];
        auto& next = node -> children[cur - 'a'];
        if (!next)
            return ;
		if (next -> word){
			ans.push_back(*next -> word);
            next -> word = nullptr;
		}
        
		board[i][j] = '#';
		search(i + 1, j, next);
		search(i - 1, j, next);
		search(i, j + 1, next);
		search(i, j - 1, next);
		board[i][j] = cur;
	}
};
