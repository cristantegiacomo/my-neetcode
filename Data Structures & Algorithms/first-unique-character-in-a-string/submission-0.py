class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        counts = Counter(s)
        
        for c, freq in counts.items():
            if freq == 1:
                return s.index(c)
        return -1