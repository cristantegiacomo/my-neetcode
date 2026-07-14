class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map={}
        res=[]
        for n in nums:
            if n not in map: map[n]=1
            else: map[n]+=1
        l=sorted(map.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            res.append(l[i][0])
        return res

        
