// Implement a trie with insert, search, and startsWith methods.
//
// Example:
//
//
// Trie trie = new Trie();
//
// trie.insert("apple");
// trie.search("apple");   // returns true
// trie.search("app");     // returns false
// trie.startsWith("app"); // returns true
// trie.insert("app");   
// trie.search("app");     // returns true
//
//
// Note:
//
//
// 	You may assume that all inputs are consist of lowercase letters a-z.
// 	All inputs are guaranteed to be non-empty strings.
//
//


class Trie {
private:
    struct TrieNode{
        bool isword;
        vector<TrieNode*> children;
        TrieNode(): isword(false), children(26){};
    };
    
    TrieNode* _root;
    const TrieNode* _find(string p){
        auto* iter = _root;
        for (char c: p){
            if (iter -> children[c - 'a'] != nullptr)
                iter = iter -> children[c - 'a'];
            else
                return iter -> children[c - 'a'];
        }
        return iter;
    }
public:
    /** Initialize your data structure here. */
    Trie(): _root(new TrieNode){}
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        auto* iter = _root;
        for (char& c: word){
            if (iter -> children[c - 'a'] == nullptr)
                iter -> children[c - 'a'] = new TrieNode();
            iter = iter -> children[c - 'a'];
        }
        iter -> isword = true;
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        auto ans_node = _find(word);
        return ans_node != nullptr && ans_node -> isword;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        return _find(prefix) != nullptr;
    }
};
