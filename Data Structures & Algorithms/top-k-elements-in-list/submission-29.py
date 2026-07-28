class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr=[[] for _ in range((len(nums)+1))]
        counts=Counter(nums)    #1 --> 3
        res=[]

        for n in counts:
            arr[counts[n]].append(n)

        for i in range(len(nums),-1,-1):
            for j in range(len(arr[i])):
                res.append(arr[i][j])
                if len(res)==k: 
                    return res