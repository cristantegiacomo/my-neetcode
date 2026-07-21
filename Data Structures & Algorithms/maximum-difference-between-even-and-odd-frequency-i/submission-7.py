class Solution:
    def maxDifference(self, s: str) -> int:
        mp=collections.defaultdict(int)

        for c in s:
            mp[c]+=1
        ord=sorted(mp.values())
        l,r = 0, len(ord)-1
        while (ord[l]%2!=0 or ord[r]%2==0):
            if ord[l]%2!=0: l+=1
            if ord[r]%2==0: r-=1
        return ord[r]-ord[l]