import random
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        euclidean = lambda x: x[0]**2 + x[1]**2

        def quickSelect(l, r):
            random_idx = random.randint(l, r)
            points[random_idx], points[r] = points[r], points[random_idx]
            
            p = l
            pivotDist = euclidean(points[r])

            for i in range(l, r):
                if euclidean(points[i]) <= pivotDist:
                    points[p], points[i] = points[i], points[p]
                    p += 1
            points[p], points[r] = points[r], points[p]


            if p > k-1:
                return quickSelect(l, p - 1)
            elif p < k-1:
                return quickSelect(p + 1, r)
            else:
                return points[:k]
        
        return quickSelect(0, len(points) - 1)