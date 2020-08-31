# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.
#
# Note:
#
#
# 	The same word in the dictionary may be reused multiple times in the segmentation.
# 	You may assume the dictionary does not contain duplicate words.
#
#
# Example 1:
#
#
# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
#   "cats and dog",
#   "cat sand dog"
# ]
#
#
# Example 2:
#
#
# Input:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output:
# [
#   "pine apple pen apple",
#   "pineapple pen apple",
#   "pine applepen apple"
# ]
# Explanation: Note that you are allowed to reuse a dictionary word.
#
#
# Example 3:
#
#
# Input:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:
# []
#


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.memo = {}
        words = set(wordDict)
        return self.helper(s, words)
    
    def helper(self, s, words):
        if s in self.memo:
            return self.memo[s]
        break_s = []
        if s in words:
            break_s.append(s)
        for i in range(1, len(s)):
            if s[:i] in words:
                resteBreak = self.helper(s[i:], words)
                for r in resteBreak:
                    break_s.append(s[:i] + " " + r)
        self.memo[s] = break_s
        return self.memo[s]
        
