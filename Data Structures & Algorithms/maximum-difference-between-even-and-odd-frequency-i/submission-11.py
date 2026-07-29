class Solution:
    def maxDifference(self, s: str) -> int:
        counts=Counter(s)
        maxOdd=0
        minEven=float('inf')

        for freq in counts.values():
            if freq%2!=0:
                maxOdd=max(maxOdd, freq)
            else:
                minEven=min(minEven, freq)
        return maxOdd-int(minEven)