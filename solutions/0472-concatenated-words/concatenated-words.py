# Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list of words.
# A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.
#
# Example:
#
# Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
#
# Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
#
# Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";  "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
#
#
#
# Note:
#
# The number of elements of the given array will not exceed 10,000 
# The length sum of elements in the given array will not exceed 600,000. 
# All the input string will only include lower case letters.
# The returned elements order does not matter. 
#
#


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        def helper(s, wordset):
            #check if s is segmented by wordset
            #dfs
            if s in wordset:
                return True
            for i in range(1, len(s)):
                if s[:i] in wordset and helper(s[i:], wordset):
                    return True
            return False
        res = []
        wordset = set(words)
        if len(words) <= 2:
            return []
        for s in words:
            wordset.remove(s)
            if len(s) == 0:
                continue
            if helper(s, wordset): res.append(s)
            wordset.add(s)
        return res
