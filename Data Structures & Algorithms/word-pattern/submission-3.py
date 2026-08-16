class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        mp = {}
        words = s.split(" ")

        if len(words) != len(pattern):
            return False

        for i, p in enumerate(pattern):
            if p not in mp:
                mp[p] = words[i]
            if words[i] not in mp:
                mp[words[i]] = p

        for i, p in enumerate(pattern):
            if p != mp[words[i]] or words[i] != mp[p]:
                return False
        return True