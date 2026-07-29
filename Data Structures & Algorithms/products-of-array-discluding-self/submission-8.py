class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=1
        count_zero=0
        res=[]
        for n in nums:
            if n!=0: prod*=n
            else: count_zero+=1

        for n in nums:
            if n==0:
                if count_zero==1: res.append(prod)
                elif count_zero>=2: res.append(0)
            else:
                if count_zero==0: res.append(int(prod/n))  
                if count_zero>=1: res.append(0)
        return res


        