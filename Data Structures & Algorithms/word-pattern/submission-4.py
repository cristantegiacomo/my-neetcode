class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")

        if len(words) != len(pattern):
            return False

        charToWord = {}
        wordToChar = {}

        for c, w in zip(pattern, words): 
            if ((c not in charToWord and w in wordToChar) or 
                (w not in wordToChar and c in charToWord)):
                return False
            charToWord[c] = w
            wordToChar[w] = c
        return True
