class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen=set()
        length=0
        
        for i in range(len(nums)):
            length=len(seen)
            seen.add(nums[i])
            if length==len(seen): 
                return nums[i]   