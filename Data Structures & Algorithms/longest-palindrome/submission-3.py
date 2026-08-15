class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        foundOdd = 0
        tot = 0

        for freq in counts.values():
            val = freq - freq % 2
            if freq %2 != 0:
                foundOdd = 1
            tot += val

        return tot + foundOdd
