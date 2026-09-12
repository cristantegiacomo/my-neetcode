class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        counts = Counter(arr1)
        res = []

        for c2 in arr2:
            res.extend([c2] * counts.pop(c2))
    # counts.pop(c2) returna counts[c2] e fa del counts[c2]

        for k in sorted(counts.keys()):
            res.extend([k] * counts.pop(k))
        
        return res