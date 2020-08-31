# You should design a data structure that supports adding new words and finding if a string matches any previously added string.
#
# Implement the WordDictionary class:
#
#
# 	WordDictionary() Initializes the object.
# 	void addWord(word) adds word to the data structure, it can be matched later.
# 	bool search(word) returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
#
#
#  
# Example:
#
#
# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]
#
# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True
#
#
#  
# Constraints:
#
#
# 	1 <= word.length <= 500
# 	word in addWord consists lower-case English letters.
# 	word in search consist of  '.' or lower-case English letters.
# 	At most 50000 calls will be made to addWord and search .
#
#


class TrieNode():
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        it = self.data
        for c in word:
            if c not in it.children:
                it.children[c] = TrieNode()
            it = it.children[c]
        it.isWord = True
    
    def dfs(self, it, word, cur):
        if cur == len(word):
            if it.isWord:
                return True
            else:
                return False
        if word[cur] == '.':
            for k in it.children:
                if self.dfs(it.children[k], word, cur + 1):
                    return True
            return False
        elif word[cur] in it.children:
            return self.dfs(it.children[word[cur]], word, cur + 1)
        else:
            return False
    
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        it = self.data
        return self.dfs(it, word, 0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
