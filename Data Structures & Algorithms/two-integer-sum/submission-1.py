class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp={}
        res=[]

        for i, n in enumerate(nums):
            mp[n]=i

        for i, n in enumerate(nums):
            diff=target-n
            if diff in mp and mp[diff]!=i:
                return [i, mp[diff]]
        return []
