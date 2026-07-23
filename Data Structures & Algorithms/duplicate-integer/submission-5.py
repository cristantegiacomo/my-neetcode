class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        length=0
        
        for i in range(len(nums)):
            length=len(seen)
            seen.add(nums[i])
            if length==len(seen): return True
        return False