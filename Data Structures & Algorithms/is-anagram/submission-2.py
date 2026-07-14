class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return False
        map_s={}
        map_t={}
        for c in s:
            if c not in map_s: map_s[c]=1
            else: map_s[c]+=1
        for c in t:
            if c not in map_t: map_t[c]=1
            else: map_t[c]+=1
        if map_s == map_t: return True
        else: return False
    
