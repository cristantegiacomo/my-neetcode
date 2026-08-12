class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        squares = [ (x**2 + y**2, x, y) for x,y in points ]  
        res = []
        minHeap = squares
        heapq.heapify(minHeap)

        for _ in range(k):
            popp = heapq.heappop(minHeap)
            res.append( [popp[1], popp[2]] )
        
        return res