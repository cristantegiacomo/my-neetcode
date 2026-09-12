class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        counts = Counter(s)
        res = []

        for _ in range(counts["1"]-1):
            res.append("1")
        for _ in range(counts["0"]):
            res.append("0")
        res.append("1")

        return "".join(res)