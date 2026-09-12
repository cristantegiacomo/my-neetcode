class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        counts = Counter(arr1)
        remaining = []
        res = []

        for c2 in arr2:
            for _ in range(counts[c2]):
                res.append(c2)
            del counts[c2]
        
        for c, freq in counts.items():
            for _ in range(freq):
                remaining.append(c)
        remaining.sort()

        return res + remaining