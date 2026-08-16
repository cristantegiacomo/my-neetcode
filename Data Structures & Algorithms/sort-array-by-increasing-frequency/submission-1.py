class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        res = []

        minHeap = [ (freq, -n) for n, freq in counts.items() ]
        heapq.heapify(minHeap)

        while minHeap:
            freq, num = heapq.heappop(minHeap)
            for _ in range(freq):
                res.append(-num)

        return res