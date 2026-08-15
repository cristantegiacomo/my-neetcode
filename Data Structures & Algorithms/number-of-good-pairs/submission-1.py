from math import factorial
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = Counter(nums)
        res = 0
        for _, freq in counts.items():
            if freq > 1:
                res += (factorial(freq) // (2 * factorial(freq-2)))
        return res