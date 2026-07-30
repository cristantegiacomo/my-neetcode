class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #if h < len(piles): return 0
        l, r = 1, max(piles)

        while l < r:
            m = l + ((r-l) // 2)
            if self.verify(m, piles, h):
                r = m
            else:
                l = m + 1
        return l
 # 1 2 3 4      h=9
    def verify(self, m: int, piles: List[int], h: int) -> bool:    
        for p in piles:
            if m >= p:
                h-=1
            else:
                if p % m != 0:
                    h -= ((p // m) + 1)
                else:
                    h -= (p // m)
        if h >= 0:
            return True
        else:
            return False
            