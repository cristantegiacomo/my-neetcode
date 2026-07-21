class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        st=set()
        res=[]

        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            if i>0 and nums[i]==nums[i-1]: continue

            while l<r:
                sum=nums[l]+nums[r]
                if sum > -nums[i]:
                    r-=1
                elif sum < -nums[i]:
                    l+=1
                else:
                    #st.add((nums[i], nums[l], nums[r]))
                    res.append( [nums[i], nums[l], nums[r]] )
                    while l<r and nums[l]==nums[l+1]:
                     l+=1
                    while l<r and nums[r]==nums[r-1]:
                      r-=1
                    l+=1
                    r-=1

        #res=[list(t) for t in st]
        return res
# [-1, 0, 1, 2, -1, -4]
# [-4, -1, -1, 0, 1, 2, 5]

# [-4, -2, -2, -1, -1, 0, 1, 2, 2, 4, 5, 8] 
