class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
# soluzione come la 2 del fattoriale ma semplificata: sapendo che k = 2 la formual diventa da n!/k!(n-k)! a n*(n-1)/2

        counts = Counter(nums)
        res = 0
        for freq in counts.values():
            res += freq * (freq-1) // 2
        return res