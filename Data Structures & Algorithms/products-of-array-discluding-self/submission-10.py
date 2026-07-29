class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N=len(nums)
        pref=[1] * (N+1)
        suff=[1] * (N+1)
        res=[]

        for i in range(N):
            pref[i+1]=pref[i] * nums[i]

        for i in range(N-1,-1,-1):
            suff[i-1]=suff[i] * nums[i] # suff[-1]=suff[N]

        for i in range(N):
            res.append(pref[i]*suff[i])
        return res



