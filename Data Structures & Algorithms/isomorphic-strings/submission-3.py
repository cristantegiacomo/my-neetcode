class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        map_st = {}
        map_ts = {}
        
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] not in map_st:
                map_st[s[i]] = t[i]
            if t[i] not in map_ts:
                map_ts[t[i]] = s[i]

            if map_st[s[i]] != t[i] or map_ts[t[i]] != s[i]:
                return False
        
        return True