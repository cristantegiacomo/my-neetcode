class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tot_prod=1
        count_zero=0
        output=[1] *len(nums)
        for i in range(len(nums)):
            if nums[i]!=0: tot_prod*=nums[i]
            else: count_zero+=1

        for i in range(len(nums)):
            if count_zero==0:
                output[i]=tot_prod//nums[i]
            elif count_zero==1:
                if nums[i]!=0: output[i]=0
                else: output[i]=tot_prod
            elif count_zero>=2:
                output[i]=0
                
        return output

