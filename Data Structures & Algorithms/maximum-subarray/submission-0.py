class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        cache = [None] * len(nums)    #cache[i] returna la somma max
        res = min(nums)

        def dfs(i): 
            if i >= len(nums):
                return 0

            if cache[i] is not None:
                return cache[i]

            cache[i] = nums[i] + max(0, dfs(i+1))
            return cache[i]


        for i in range(len(nums)):
            res = max(res, dfs(i)) 
        return res