class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        bucket = [ [] for _ in range(len(nums)+1) ]
        res = []

        for n, freq in counts.items():
            bucket[freq].append(n)

        for i in range(1, len(bucket)):
            bucket[i].sort(reverse=True)
            for j in range(len(bucket[i])):
                for _ in range(i):
                    res.append(bucket[i][j])
        return res