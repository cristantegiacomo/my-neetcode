class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")

        if len(words) != len(pattern):
            return False

        charToWord = {}
        wordToChar = {}

        for c, w in zip(pattern, words): 
            if c not in charToWord:
                charToWord[c] = w
            if w not in wordToChar:
                wordToChar[w] = c

        for c, w in zip(pattern, words): 
            if charToWord[c] != w or wordToChar[w] != c:
                return False
                
        return True
