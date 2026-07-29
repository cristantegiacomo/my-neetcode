class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N=len(nums)
        pref=[1] * N
        suff=[1] * N
        res=[]

        for i in range(N-1):
            pref[i+1]=pref[i] * nums[i]

        for i in range(N-1,0,-1):
            suff[i-1]=suff[i] * nums[i] 

        for i in range(N):
            res.append(pref[i]*suff[i])
        return res



