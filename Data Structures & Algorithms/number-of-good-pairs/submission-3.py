class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        res = 0

        for n in nums:
            res += counts[n]
            counts[n] += 1
        return res
    
    # se hai [1,2,1,1] al primo 1 res += 0, al secondo 1 res+=1 al terzo 1 res += 2. Ad ogni duplicato aggiungi le combinazioni che ottieni con quel nuovo duplicato 